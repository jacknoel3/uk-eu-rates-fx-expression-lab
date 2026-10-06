"""Download small public samples for the Day 2 data feasibility audit.

The script deliberately uses only the Python standard library. Large BoE
archives are excluded by default; the latest yield-curve ZIP is enough to prove
programmatic access and inspect workbook structure.
"""

from __future__ import annotations

import argparse
import shutil
import ssl
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SAMPLES = {
    "ecb_eur_gbp_spot_sample.csv": (
        "https://data-api.ecb.europa.eu/service/data/EXR/"
        "D.GBP.EUR.SP00.A?startPeriod=2026-07-20&endPeriod=2026-07-24&format=csvdata"
    ),
    "boe_xudlers_spot_cross_check.csv": (
        "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp"
        "?csv.x=yes&Datefrom=20/Jul/2026&Dateto=24/Jul/2026&SeriesCodes=XUDLERS"
        "&UsingCodes=Y&CSVF=TN&VPD=Y&VFD=N"
    ),
    "boe_latest_yield_curve_data.zip": (
        "https://www.bankofengland.co.uk/-/media/boe/files/statistics/yield-curves/"
        "latest-yield-curve-data.zip"
    ),
    "bundesbank_german_2y_term_structure_sample.csv": (
        "https://api.statistiken.bundesbank.de/rest/data/BBSIS/"
        "D.I.ZAR.ZI.EUR.S1311.B.A604.R02XX.R.A.A._Z._Z.A"
        "?startPeriod=2026-07-20&endPeriod=2026-07-24&format=csv&lang=en"
    ),
    "bundesbank_german_10y_term_structure_sample.csv": (
        "https://api.statistiken.bundesbank.de/rest/data/BBSIS/"
        "D.I.ZAR.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A"
        "?startPeriod=2026-07-20&endPeriod=2026-07-24&format=csv&lang=en"
    ),
    "boe_mpc_voting.xlsx": (
        "https://www.bankofengland.co.uk/-/media/boe/files/"
        "monetary-policy-summary-and-minutes/mpcvoting.xlsx"
    ),
    "ecb_governing_council_calendar.html": (
        "https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html"
    ),
    "ukmpd.xlsx": (
        "https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2023/"
        "measuring-monetary-policy-in-the-uk-the-ukmpesd.xlsx"
    ),
    "eampd.xlsx": "https://www.ecb.europa.eu/pub/pdf/annex/Dataset_EA-MPD.xlsx",
    "cboe_vix_history.csv": "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",
}

LARGE_ARCHIVES = {
    "boe_ois_daily_archive.zip": (
        "https://www.bankofengland.co.uk/-/media/boe/files/statistics/yield-curves/"
        "oisddata.zip"
    ),
    "boe_glc_nominal_daily_archive.zip": (
        "https://www.bankofengland.co.uk/-/media/boe/files/statistics/yield-curves/"
        "glcnominalddata.zip"
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/raw/feasibility_samples") / date.today().isoformat(),
        help="Directory for downloaded public samples.",
    )
    parser.add_argument(
        "--include-large-archives",
        action="store_true",
        help="Also download the larger BoE daily OIS and nominal gilt archive ZIPs.",
    )
    parser.add_argument(
        "--insecure",
        action="store_true",
        help="Disable TLS certificate verification for managed networks with intercepting proxies.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Per-file download timeout in seconds.",
    )
    return parser.parse_args()


def download_one(url: str, destination: Path, insecure: bool, timeout: float) -> None:
    context = ssl._create_unverified_context() if insecure else None
    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0 Safari/537.36"
            ),
            "Connection": "close",
        },
    )
    with urlopen(request, context=context, timeout=timeout) as response:
        with destination.open("wb") as file:
            shutil.copyfileobj(response, file)


def download_samples(
    output_dir: Path, include_large_archives: bool, insecure: bool, timeout: float
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    samples = dict(SAMPLES)
    if include_large_archives:
        samples.update(LARGE_ARCHIVES)

    failures = []
    for filename, url in samples.items():
        destination = output_dir / filename
        print(f"Downloading {filename}", flush=True)
        try:
            download_one(url, destination, insecure, timeout)
        except (HTTPError, TimeoutError, URLError, OSError) as error:
            failures.append((filename, str(error)))
            print(f"  failed: {error}", flush=True)
            continue
        print(f"  wrote {destination} ({destination.stat().st_size} bytes)", flush=True)

    if failures:
        print("\nFailed downloads:", flush=True)
        for filename, error in failures:
            print(f"  {filename}: {error}", flush=True)
        raise SystemExit(1)


def main() -> None:
    args = parse_args()
    download_samples(args.output_dir, args.include_large_archives, args.insecure, args.timeout)


if __name__ == "__main__":
    main()

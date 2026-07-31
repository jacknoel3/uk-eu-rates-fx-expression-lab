# Tests

Unit tests should cover small, isolated economic and technical behaviours. Integration tests should cover clean-environment pipeline behaviour once a pipeline exists.

Required future test areas include:

- economic sign tests for EUR/GBP and rates positions;
- timestamp and leakage tests;
- attribution reconciliation;
- cost-application checks;
- volatility floors and caps;
- missing-calendar behaviour;
- clean-environment pipeline tests.

Do not add meaningless tests such as `assert True`. Tests should be added when there is real behaviour to verify.

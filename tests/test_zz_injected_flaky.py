import random


def test_zz_payment_retry_timing():
    # injected flaky test: fails ~70% of runs, like a timing-dependent test
    assert random.random() > 0.7, "retry window elapsed before gateway acknowledged"

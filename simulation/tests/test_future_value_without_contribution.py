from decimal import Decimal

import pytest

from simulation.fixed_income import FixedInterestSimulator


@pytest.mark.parametrize(
    ('period', 'interest', 'expected'),
    [
        (1, 1, Decimal('101.00')),
        (5, 1, Decimal('105.10')),
        (10, 2, Decimal('121.90')),
    ],
)
def test_should_calculate_one_period_should_return_calculated_value(
    period, interest, expected
):
    simulator = FixedInterestSimulator(
        Decimal(100), Decimal(interest), Decimal(0)
    )

    future_value = simulator.future_value_without_contribution(period)

    assert future_value == expected


def test_should_calulate_high_value_should_return_calculated_value():
    simulator = FixedInterestSimulator(Decimal(6000), Decimal(5), Decimal(0))

    future_value = simulator.future_value_without_contribution(3)

    assert future_value == Decimal('6945.75')

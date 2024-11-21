from decimal import Decimal

import pytest

from simulation.fixed_income import FixedInterestSimulator


@pytest.mark.parametrize(
    ('period', 'interest', 'expected'),
    [
        (5, 1, Decimal('510.10')),
        (10, 1, Decimal('1046.22')),
        (20, 2, Decimal('2429.74')),
        (120, 2, Decimal('48825.82')),
    ],
)
def test_calculate_with_contributions(period, interest, expected):
    simulator = FixedInterestSimulator(
        Decimal(0), Decimal(interest), Decimal('100.0')
    )

    future_value = simulator.future_value_with_contributions(period)

    assert future_value == expected


def test_calculate_one_period():
    simulator = FixedInterestSimulator(
        Decimal(0), Decimal(1), Decimal('100.0')
    )

    future_value = simulator.future_value_with_contributions(1)

    assert future_value == Decimal('100.00')

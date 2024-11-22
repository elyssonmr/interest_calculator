from decimal import Decimal

from simulation.fixed_income import FixedInterestSimulator


def test_simulate_without_contributions():
    simulator = FixedInterestSimulator(
        Decimal('1000.50'), Decimal(1), Decimal(0)
    )

    future_value = simulator.simulate(5)

    assert future_value == Decimal('1051.54')


def test_simulate_only_contributions():
    simulator = FixedInterestSimulator(
        Decimal(0), Decimal(1), Decimal('100.50')
    )

    future_value = simulator.simulate(5)

    assert future_value == Decimal('512.65')


def test_simulate_initial_amount_and_contributions():
    simulator = FixedInterestSimulator(
        Decimal('5987.65'), Decimal(5), Decimal('100.50')
    )

    future_value = simulator.simulate(5)

    assert future_value == Decimal('8197.26')

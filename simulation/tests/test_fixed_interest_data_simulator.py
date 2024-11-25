from decimal import Decimal

from simulation.fixed_income import FixedInterestDataSimulator


def test_simulate_should_simulate_one_month():
    simulator = FixedInterestDataSimulator(
        Decimal(1000), Decimal(1), Decimal(100)
    )

    simulator.simulate(1)

    assert simulator.monthly_data == [
        {
            'total_contribution': Decimal('1100.00'),
            'total_interest': Decimal('10.00'),
            'total_future_value': Decimal('1110.00'),
        }
    ]


def test_simulate_should_simulate_two_months():
    simulator = FixedInterestDataSimulator(
        Decimal(1000), Decimal(1), Decimal(100)
    )

    simulator.simulate(2)

    assert simulator.monthly_data == [
        {
            'total_contribution': Decimal('1100.00'),
            'total_interest': Decimal('10.00'),
            'total_future_value': Decimal('1110.00'),
        },
        {
            'total_contribution': Decimal('1200.00'),
            'total_interest': Decimal('21.10'),
            'total_future_value': Decimal('1221.10'),
        },
    ]


def test_simulate_should_simulate_three_months():
    simulator = FixedInterestDataSimulator(
        Decimal(1000), Decimal(1), Decimal(100)
    )

    simulator.simulate(3)

    assert simulator.monthly_data[-1] == {
        'total_contribution': Decimal('1300.00'),
        'total_interest': Decimal('33.31'),
        'total_future_value': Decimal('1333.31'),
    }


def test_simulate_should_simulate_ten_months():
    simulator = FixedInterestDataSimulator(
        Decimal(1000), Decimal(1), Decimal(100)
    )

    simulator.simulate(10)

    assert simulator.monthly_data[-1] == {
        'total_contribution': Decimal('2000.00'),
        'total_interest': Decimal('150.84'),
        'total_future_value': Decimal('2150.84'),
    }


def test_generate_csv_should_retrun_csv_file():
    simulator = FixedInterestDataSimulator(
        Decimal(1000), Decimal(1), Decimal(100)
    )

    csv_file = simulator.generate_csv(1)

    csv_file_data = csv_file.getvalue()

    assert 'month' in csv_file_data
    assert 'total_contribution' in csv_file_data
    assert '1100.00' in csv_file_data

from csv import DictWriter
from decimal import Decimal
from io import StringIO

TWOPLACES = Decimal('0.01')


class FixedInterestSimulator:
    def __init__(
        self,
        initial_amount: Decimal = Decimal(0.0),
        monthly_interest: Decimal = Decimal(0.0),
        monthly_contribution: Decimal = Decimal(0.0),
    ):
        self.initial_amount = initial_amount
        self.monthly_interest = monthly_interest
        self.monthly_contribution = monthly_contribution

    def simulate(self, period: int = 1) -> Decimal:
        return self.future_value_without_contribution(
            period
        ) + self.future_value_with_contributions(period)

    def future_value_without_contribution(self, period: int) -> Decimal:
        return (
            self.initial_amount
            * (1 + self.monthly_interest / Decimal(100)) ** Decimal(period)
        ).quantize(TWOPLACES)

    def future_value_with_contributions(self, period: int) -> Decimal:
        interest = self.monthly_interest / Decimal(100)
        return (
            self.monthly_contribution
            * ((1 + interest) ** Decimal(period) - 1)
            / interest
        ).quantize(TWOPLACES)


class FixedInterestDataSimulator:
    def __init__(
        self,
        initial_amount: Decimal = Decimal(0.0),
        monthly_interest: Decimal = Decimal(0.0),
        monthly_contribution: Decimal = Decimal(0.0),
    ):
        self.initial_amount = initial_amount
        self.monthly_interest = monthly_interest
        self.monthly_contribution = monthly_contribution
        self.monthly_data = []
        self.total_contribution = Decimal(0)
        self.total_interest = Decimal(0)
        self.total_future_value = Decimal(0)

    def simulate(self, period: int):
        interest = self.monthly_interest / Decimal(100)
        self.total_contribution = (
            self.initial_amount + self.monthly_contribution
        ).quantize(TWOPLACES)

        self.total_future_value = self.initial_amount + (
            self.initial_amount * (Decimal(1) * interest)
            + self.monthly_contribution
        ).quantize(TWOPLACES)

        self.total_interest = (
            self.total_future_value - self.total_contribution
        ).quantize(TWOPLACES)

        self.monthly_data.append({
            'total_contribution': self.total_contribution,
            'total_interest': self.total_interest,
            'total_future_value': self.total_future_value,
        })

        for _ in range(1, period):
            self.total_future_value += (
                self.total_future_value * (Decimal(1) * interest)
                + self.monthly_contribution
            ).quantize(TWOPLACES)

            self.total_contribution += self.monthly_contribution.quantize(
                TWOPLACES
            )

            self.total_interest = (
                self.total_future_value - self.total_contribution
            ).quantize(TWOPLACES)

            self.monthly_data.append({
                'total_contribution': self.total_contribution,
                'total_interest': self.total_interest,
                'total_future_value': self.total_future_value,
            })

    def generate_csv(self, period: int) -> StringIO:
        if self.monthly_data == []:
            self.simulate(period)

        csv_file = StringIO()
        fieldnames = [
            'month',
            'total_contribution',
            'total_interest',
            'total_future_value',
        ]
        writer = DictWriter(csv_file, fieldnames)
        writer.writeheader()

        for month, month_data in enumerate(self.monthly_data, 1):
            row_data = {'month': month}
            row_data.update(month_data)
            writer.writerow(row_data)

        return csv_file

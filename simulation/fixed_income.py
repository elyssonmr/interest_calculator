from decimal import Decimal

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

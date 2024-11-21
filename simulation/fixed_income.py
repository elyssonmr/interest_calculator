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

    def simulate(period: int = 1) -> Decimal:
        pass

    def future_value_without_contribution(self, period: int) -> Decimal:
        return (
            self.initial_amount
            * (1 + self.monthly_interest / Decimal(100)) ** Decimal(period)
        ).quantize(TWOPLACES)

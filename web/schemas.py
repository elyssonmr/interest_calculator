from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field, PositiveInt

Money = Annotated[
    Decimal,
    Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.00'),
        ge=Decimal('0.00'),
    ),
]

Interest = Annotated[
    Decimal,
    Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.01'),
        ge=Decimal('0.01'),
    ),
]


class SimulationRequest(BaseModel):
    initial_amount: Money
    monthly_interest: Interest
    monthly_contribution: Money
    periods: PositiveInt


class SimulationResponse(BaseModel):
    periods: PositiveInt
    future_value: Money


class PeriodInfo(BaseModel):
    month: PositiveInt
    total_contribution: Money
    total_interest: Money
    total_future_value: Money


class SimulationDataResponse(BaseModel):
    simulation: list[PeriodInfo]

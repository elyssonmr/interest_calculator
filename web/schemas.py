from decimal import Decimal

from pydantic import BaseModel, Field, PositiveInt


class SimulationRequest(BaseModel):
    initial_amount: Decimal = Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.00'),
        ge=Decimal('0.00'),
    )
    monthly_interest: Decimal = Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.01'),
        ge=Decimal('0.01'),
    )
    monthly_contribution: Decimal = Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.00'),
        ge=Decimal('0.00'),
    )
    periods: PositiveInt


class PeriodInfo(BaseModel):
    month: PositiveInt
    total_contribution: Decimal = Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.00'),
        ge=Decimal('0.00'),
    )
    total_interest: Decimal = Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.00'),
        ge=Decimal('0.00'),
    )
    total_future_value: Decimal = Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.00'),
        ge=Decimal('0.00'),
    )


class SimulationData(BaseModel):
    simulation: list[PeriodInfo]


class SimulationInfo(BaseModel):
    periods: PositiveInt
    future_value: Decimal = Field(
        max_digits=9,
        decimal_places=2,
        default=Decimal('0.00'),
        ge=Decimal('0.00'),
    )

from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter

from simulation import (
    FixedInterestDataSimulator,
    FixedInterestSimulator,
)
from web.schemas import (
    PeriodInfo,
    SimulationDataResponse,
    SimulationRequest,
    SimulationResponse,
)

router = APIRouter(prefix='', tags=['Simulation'])


@router.post('/simulate_future_value', response_model=SimulationResponse)
def simulate_future_value(simulation_data: SimulationRequest):
    simulation = FixedInterestSimulator(
        simulation_data.initial_amount,
        simulation_data.monthly_interest,
        simulation_data.monthly_contribution,
    )

    future_value = simulation.simulate(simulation_data.periods)

    return SimulationResponse(
        periods=simulation_data.periods, future_value=future_value
    )


@router.post(
    '/simulate_future_value_data', response_model=SimulationDataResponse
)
def simulate_future_value_data(simulation_data: SimulationRequest):
    simulation = FixedInterestDataSimulator(
        simulation_data.initial_amount,
        simulation_data.monthly_interest,
        simulation_data.monthly_contribution,
    )

    simulation.simulate(simulation_data.periods)
    future_value_data = []

    for period, data in enumerate(simulation.monthly_data, start=1):
        month_info = {'month': period}
        month_info.update(data)
        future_value_data.append(PeriodInfo.model_validate(month_info))

    return SimulationDataResponse(simulation=future_value_data)


@router.post(
    '/simulate_future_value_data_csv', response_class=StreamingResponse
)
def simulate_future_value_data_csv(simulation_data: SimulationRequest):
    simulation = FixedInterestDataSimulator(
        simulation_data.initial_amount,
        simulation_data.monthly_interest,
        simulation_data.monthly_contribution,
    )

    csv_file = simulation.generate_csv(simulation_data.periods)

    response = StreamingResponse(
        iter([csv_file.getvalue()]), media_type='text/csv'
    )

    response.headers['Content-Disposition'] = (
        'attachment; filename=simulation.csv'
    )

    return response

from http import HTTPStatus


def test_simulate_future_value(client):
    response = client.post(
        '/simulate_future_value',
        json={
            'initial_amount': 1000.00,
            'monthly_interest': 1,
            'monthly_contribution': 100.00,
            'periods': 10,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'periods': 10, 'future_value': '2150.84'}


def test_simulate_future_value_data(client):
    response = client.post(
        '/simulate_future_value_data',
        json={
            'initial_amount': 1000.00,
            'monthly_interest': 1,
            'monthly_contribution': 100.00,
            'periods': 2,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'simulation': [
            {
                'month': 1,
                'total_contribution': '1100.00',
                'total_future_value': '1110.00',
                'total_interest': '10.00',
            },
            {
                'month': 2,
                'total_contribution': '1200.00',
                'total_future_value': '1221.10',
                'total_interest': '21.10',
            },
        ]
    }


def test_simulate_future_value_data_csv(client):
    response = client.post(
        '/simulate_future_value_data_csv',
        json={
            'initial_amount': 1000.00,
            'monthly_interest': 1,
            'monthly_contribution': 100.00,
            'periods': 2,
        },
    )

    assert response.status_code == HTTPStatus.OK
    content = response.content.decode()
    assert '1100.00' in content
    assert '1221.10' in content
    assert '21.10' in content

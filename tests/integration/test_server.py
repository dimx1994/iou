import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.server import app


@pytest.fixture(scope='module')
def client():
    client = TestClient(app)
    yield client


def correct_request():
    return {
        'predicted': {'left': 4.5, 'top': 3.0, 'right': 11.5, 'bottom': 10.0},
        'ground_truth': {'left': 8.5, 'top': 7.0, 'right': 14.5, 'bottom': 13.0},
    }


def incorrect_values_in_request():
    return {
        'predicted': {'left': 5, 'top': 3, 'right': 4, 'bottom': 10},
        'ground_truth': {'left': 8, 'top': 7, 'right': 14, 'bottom': 13},
    }


def test_iou_correct(client):
    response = client.post('/intersection-over-union', json=correct_request())
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'iou': 0.118}


def test_iou_incorrect_values(client):
    response = client.post(
        '/intersection-over-union', json=incorrect_values_in_request()
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'predicted', 'right'],
                'msg': 'right should be greater than left',
                'type': 'value_error',
            }
        ]
    }


def test_iou_incorrect_request(client):
    response = client.post('/intersection-over-union', json={'a': 'b'})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'predicted'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
            {
                'loc': ['body', 'ground_truth'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
        ]
    }

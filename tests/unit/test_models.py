import pytest

from app.models import Box


def test_box_successful_creation():
    Box(left=4.1, right=4.2, top=3, bottom=10)


def test_box_unsuccessful_creation_left():
    with pytest.raises(ValueError):
        Box(left=1.1, right=1.0, top=3, bottom=10)


def test_box_unsuccessful_creation_bottom():
    with pytest.raises(ValueError):
        Box(left=1.0, right=1.1, top=3.1, bottom=2.9)

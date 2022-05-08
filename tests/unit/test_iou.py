import pytest

from app.iou import compute_iou
from app.models import Box


@pytest.mark.parametrize(
    'box1,box2,decimal_digits,expected',
    [
        (
            Box(left=4, right=11, top=3, bottom=10),
            Box(left=8, right=14, top=7, bottom=13),
            4,
            0.1184,
        ),
        (
            Box(left=4, right=11, top=3, bottom=10),
            Box(left=4, right=11, top=3, bottom=10),
            4,
            1.0,
        ),
        (
            Box(left=4, right=10, top=3, bottom=9),
            Box(left=4, right=7, top=3, bottom=9),
            4,
            0.5,
        ),
        (
            Box(left=4, right=11, top=3, bottom=10),
            Box(left=8, right=14, top=7, bottom=13),
            2,
            0.12,
        ),
        (
            Box(left=4, right=11, top=3, bottom=10),
            Box(left=20, right=21, top=3, bottom=10),
            2,
            0.0,
        ),
    ],
)
def test_compute_iou(box1, box2, decimal_digits, expected):
    assert compute_iou(box1, box2, decimal_digits) == expected

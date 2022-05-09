from pydantic import BaseModel, validator


class Box(BaseModel):
    left: float  # The X coordinate of the left side of the rectangle
    top: float  # The Y coordinate of the top of the rectangle
    right: float  # The X coordinate of the right side of the rectangle
    bottom: float  # The Y coordinate of the bottom of the rectangle

    @validator('right')
    def right_more_left(cls, v, values, **kwargs):  # pylint: disable=unused-argument
        if v < values['left']:
            raise ValueError('right should be greater than left')
        return v

    @validator('bottom')
    def bottom_more_top(cls, v, values, **kwargs):  # pylint: disable=unused-argument
        if v < values['top']:
            raise ValueError('bottom should be greater than top')
        return v


class IOUResponse(BaseModel):
    iou: float


class IOURequest(BaseModel):
    predicted: Box
    ground_truth: Box

    class Config:
        schema_extra = {
            'example': {
                'predicted': {'left': 4.5, 'top': 3.0, 'right': 11.5, 'bottom': 10.0},
                'ground_truth': {
                    'left': 8.5,
                    'top': 7.0,
                    'right': 14.5,
                    'bottom': 13.0,
                },
            }
        }

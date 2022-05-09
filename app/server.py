import logging

from fastapi import FastAPI

from app.iou import compute_iou
from app.models import IOURequest, IOUResponse
from app.settings import get_settings

logger = logging.getLogger(__name__)


app = FastAPI(docs_url='/')


@app.post('/intersection-over-union', response_model=IOUResponse)
def get_intersection_over_union(request: IOURequest):
    iou = compute_iou(
        request.predicted,
        request.ground_truth,
        decimal_digits=get_settings().decimal_digits,
    )
    logger.info(
        'Successfully calculated iou %s', iou
    )  # TODO: log full request if needed
    return IOUResponse(iou=iou)


if __name__ == '__main__':  # pragma: no cover
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)

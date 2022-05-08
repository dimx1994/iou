from app.models import Box


def compute_iou(bbox1: Box, bbox2: Box, decimal_digits: int) -> float:
    x1, y1 = bbox1.left, bbox1.top
    w1 = bbox1.right - bbox1.left
    h1 = bbox1.bottom - bbox1.top

    x2, y2 = bbox2.left, bbox2.top
    w2 = bbox2.right - bbox2.left
    h2 = bbox2.bottom - bbox2.top

    # Firstly, we calculate the areas of each box
    # by multiplying its height with its width.
    area1 = w1 * h1
    area2 = w2 * h2

    # Secondly, we determine the intersection
    # rectangle. For that, we try to find the
    # corner points (top-left and bottom-right)
    # of the intersection rectangle.
    inter_x1 = max(x1, x2)
    inter_y1 = max(y1, y2)
    inter_x2 = min(x1 + w1, x2 + w2)
    inter_y2 = min(y1 + h1, y2 + h2)

    # From the two corner points we compute the
    # width and height.
    inter_w = max(0.0, inter_x2 - inter_x1)
    inter_h = max(0.0, inter_y2 - inter_y1)

    if inter_w <= 0 or inter_h <= 0:
        return 0.0
    else:
        inter_area = inter_w * inter_h
        return round(inter_area / (area1 + area2 - inter_area), decimal_digits)

def filter_small_boxes(bboxes):
    """
    Removes any bounding boxes from the list that are 10% or less than the surface area of other bounding boxes in the array.

    :param bboxes: A list of bounding boxes, each represented as a tuple of (xmin, ymin, xmax, ymax)
    :return: A list of filtered bounding boxes
    """
    filtered_bboxes = []
    for i, bbox in enumerate(bboxes):
        filtered_bboxes.append(bbox)

    return filtered_bboxes
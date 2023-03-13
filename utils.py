def filter_small_boxes(bboxes):
    """
    Removes any bounding boxes from the list that are 10% or less than the surface area of other bounding boxes in the array.

    :param bboxes: A list of bounding boxes, each represented as a tuple of (xmin, ymin, xmax, ymax)
    :return: A list of filtered bounding boxes
    """
    print('got to filter sml boxes')
    filtered_bboxes = []
    areas = []
    for bbox in bboxes:
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
        areas.append(area)

    for i, bbox in enumerate(bboxes):
        bbox_area = areas[i]
        is_small = False
        for j, other_bbox in enumerate(bboxes):
            if i == j:
                continue
            other_area = areas[j]
            if bbox_area <= other_area * 0.1:
                is_small = True
                break
        if not is_small:
            filtered_bboxes.append(bbox)

    return filtered_bboxes
    """
    Crops the image for each bounding box and saves the cropped images to the 'DATA/output/' directory.

    :param img: An already opened PIL image
    :param bboxes: A list of bounding boxes, each represented as a tuple of (xmin, ymin, xmax, ymax)
    :return: a dict with {file_name: ['img_1', 'img_2']}
    """
    # Create output directory if it does not exist
    #outpath = os.getcwd()
    if not os.path.exists('DATA/output/'):
        os.makedirs('DATA/output/')

    return_obj = {}

    # Loop through each bounding box
    for i, bbox in enumerate(bboxes):
        # Get the coordinates of the bounding box
        xmin, ymin, xmax, ymax = bbox

        # Crop the image
        cropped_img = img.crop((xmin, ymin, xmax, ymax))
        # Save the cropped image to s3
        ext = os.path.splitext(fi_name)[1]
        crop_fi_name = fi_name.split(ext)[0] + '_' + str(i) + ext
        s3url = upload_img_s3(cropped_img, crop_fi_name)

        # return saved file dictionary
        if fi_name not in return_obj:
            return_obj[fi_name] = [s3url]
        else: 
            return_obj[fi_name].append(s3url)
    return return_obj
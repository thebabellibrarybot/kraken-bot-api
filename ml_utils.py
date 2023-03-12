from kraken import binarization
from PIL import Image
from kraken import pageseg
from utils import crop_and_s3ave, filter_small_boxes
import os

# might add custom model path to this so diff models can be selected
def segline_and_crop (img_path, fi_name = None, mime_type = None):

    """
    Uses default model weights to do line segmentation on medieval latin manuscripts
    :params: img_path to image user wants cropped
    :returns: dic with {img_path: ['img_1', 'img_2']}
    """
    print('got to segline and crop')
    if fi_name and mime_type != None:
        im = Image.open(img_path)
        bw_im = binarization.nlbin(im)
        seg = pageseg.segment(bw_im)
        comb_boxes = filter_small_boxes(seg['boxes'])
        files = crop_and_s3ave(im, comb_boxes, fi_name)

        return files
    
    else:
        fi_name = img_path.filename
        # load model and image
        im = Image.open(img_path)
        # binarize img and segment
        bw_im = binarization.nlbin(im)
        seg = pageseg.segment(bw_im)
        # filter small boxes and save
        comb_boxes = filter_small_boxes(seg['boxes'])
        files = crop_and_s3ave(im, comb_boxes, fi_name)

        return files
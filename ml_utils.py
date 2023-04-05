from kraken import binarization
from PIL import Image
from kraken import pageseg
from utils import filter_small_boxes
import os
import numpy as np
from skimage import morphology

def remove_connected_components(img, min_size=100):
    # Convert the image to a binary numpy array
    bin_img = np.array(img, dtype=np.bool)

    # Remove small connected components using skimage
    cleaned_img = morphology.remove_small_objects(bin_img, min_size=min_size)

    # Convert the cleaned image back to PIL Image format
    cleaned_img = Image.fromarray(np.uint8(cleaned_img * 255))

    return cleaned_img

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
        print(im, 'im')
        bw_im = binarization.nlbin(im)
        bw_im = remove_connected_components(bw_im)
        seg = pageseg.segment(bw_im)
        print(seg, 'seg')
        print(seg['boxes'], 'seg boxes')
        comb_boxes = filter_small_boxes(seg['boxes'])
        print(comb_boxes, 'comb boxes')
        return comb_boxes
    
    else:
        fi_name = img_path.filename
        print(fi_name, 'fi_name')
        # load model and image
        im = Image.open(img_path)
        print(im, 'im')
        # binarize img and segment
        bw_im = binarization.nlbin(im)
        seg = pageseg.segment(bw_im)
        print(seg, 'seg')
        print(seg['boxes'], 'seg')
        # filter small boxes and save
        comb_boxes = filter_small_boxes(seg['boxes'])
        print(comb_boxes, 'comb boxes')
        return comb_boxes
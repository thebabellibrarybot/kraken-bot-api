import boto3
import os
from io import BytesIO

s3 = boto3.client('s3')

def upload_img_s3(img, fi_name):
    """
    uploads req.file to s3
    :params: takes req.file
    :return: presigned s3 url
    """
    # Get the image file extension
    file_extension = (os.path.splitext(fi_name)[1]).strip('.').upper()
    if file_extension == 'JPG':
        file_extension = 'JPEG'
    
    # Create a binary stream of the image data using BytesIO
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format=file_extension)
    img_byte_arr.seek(0)

    # Upload the image file to S3 as an image file
    s3.upload_fileobj(
        Fileobj=img_byte_arr,
        Bucket='thisthatbukfornolaslines',
        Key=fi_name,
        ExtraArgs={'ACL': 'public-read', 'ContentType': 'image/' + file_extension}
    )
    #close buffer for memory leaks
    img_byte_arr.close()

    #return url and filename
    s3_url = f"https://thisthatbukfornolaslines.s3.amazonaws.com/{fi_name}"

    return {fi_name: s3_url}
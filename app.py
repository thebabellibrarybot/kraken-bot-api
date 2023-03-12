import json
from collections import defaultdict
from io import BytesIO
import requests
from ml_utils import segline_and_crop


def lambda_handler(event, context):

    print('ran')

    # return obj
    ret_obj = defaultdict(list)
    body = event['body']
    print(body, 'body')

    if 's3url' in body:
        req = body['s3url']

        if len(req) > 1:
            print(len(req))
            # get contents of the file from s3
            for fi in req:
                res = requests.get(fi)
                fi_content = res.content
                fi_obj = BytesIO(fi_content)
                fi_name = fi.split('.com/')[-1]
                mimetype = fi.split('.')[-1]
                i = segline_and_crop(fi_obj, fi_name, mimetype)
                ret_obj['files'].append(i)
        else:
            res = requests.get(req[0])
            fi_content = res.content
            fi_obj = BytesIO(fi_content)
            fi_name = req[0].split('.com/')[-1]
            mimetype = req[0].split('.')[-1]
            i = segline_and_crop(fi_obj, fi_name, mimetype)
            ret_obj['files'].append(i)

    else:
        err_msg = "Error: 's3url' list is empty"
        return {
            'statusCode': 400,
            'body': json.dumps(err_msg)
        }
    print(ret_obj, 'return obj')
    return {
        'statusCode': 200,
        'body': json.dumps({
        'files': ret_obj
        })
    }
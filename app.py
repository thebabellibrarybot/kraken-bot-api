import json
from collections import defaultdict

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
            for i in req:
                print(i, 'mult')
                ret_obj['files'].append(i)
        else:
            print(len(req))
            ret_obj['files'].append(req)

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

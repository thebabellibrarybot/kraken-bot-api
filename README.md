# seg_line_crop_lambda
kraken, FROM public.ecr.aws/lambda/python:3.8 

# Cropping lambda function

## params:
- takes an s3url at size 800px
- often will generate errs if the image has not already been cleanded (*** stills needs a cleanup function to account for this behavior)

## returns:
 - only returns bbox coords
 
## implimentation:
- used to display bbox coords in frontend without actually saving any alterations to user data
- coords and image url can be sent to lambda_function 'generate_html' which will return an array of s3urls to use in generating an interactive html form for making transcriptions

envoked via  https://fake:ituuukndmc.execute-api.us-east-1.amazonaws.com/prod

test = 
{
  "body": {
    "s3url": [
      "https://fake:zipzforlambda.s3.amazonaws.com/output.jpg"
    ]
  }
}

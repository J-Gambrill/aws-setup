# this shows how you would upload a file to your S3 bucket

import auth

def upload_file(object_key, filename):
    s3_resource, s3_bucket = auth()
    try:
        bucket = s3_resource.Bucket(s3_bucket)
        bucket.upload_file(f'../data/input/{filename}', object_key)
        return True
    except Exception as e:
        print('Error uploading file to S3: {str(e)}')
        return False
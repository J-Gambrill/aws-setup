# this shows how you would upload a file to your S3 bucket
# in this example we will use admission_cleaned_joined.csv

from auth import auth 

def upload_file(object_key, filename):
    s3_resource, s3_bucket = auth('config.ini')
    try:
        bucket = s3_resource.Bucket(s3_bucket)
        bucket.upload_file(f'{filename}', object_key) # please add a path before the file name if it is located elsewhere e.g. /data/admission/{filename}
        return True
    except Exception as e:
        print(f'Error uploading file to S3: {str(e)}')
        return False
    

upload_file('admissions_data_MV', 'admission_cleaned_joined.csv')
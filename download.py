from auth import auth

def download_file(object_key, new_file_name): #object_key what it is called in aws, new_file_name what you want it to be called
    s3_resource, s3_bucket = auth('config.ini')
    try:
        bucket = s3_resource.Bucket(s3_bucket)
        bucket.download_file(object_key, f'{new_file_name}') # as there is no file path it will download it to this current folder
        return True
    except Exception as e:
        print(f'Error uploading file to s3: {str(e)}')
        return False
    
download_file('admissions_data_MV', 'admission_cleaned_joined.csv')
import configparser, boto3

def auth(config_filename):
    config = configparser.ConfigParser()
    credentials = config.read(config_filename)

    service_name =  config.get('aws_s3', 'service_name')
    region_name = config.get('aws_s3', 'region_name')
    aws_access_key_id = config.get('aws_s3', 'aws_access_key_id')
    aws_secret_access_key = config.get('aws_s3', 'aws_secret_access_key')
    s3_bucket = config.get('aws_s3', 's3_bucket')

    s3_resource = boto3.resource(
        service_name=service_name,
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    return s3_resource, s3_bucket

test = auth('config.ini')
print(test[0])
print(test[1])
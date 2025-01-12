import boto3
import logging
from config.s3_config import BUCKET_NAME

# Set up logging
logging.basicConfig(filename='logs/performance_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def enable_transfer_acceleration(bucket_name):
    s3 = boto3.client('s3')

    try:
        # Enable transfer acceleration for the specified S3 bucket
        response = s3.put_bucket_accelerate_configuration(
            Bucket=bucket_name,
            AccelerateConfiguration={
                'Status': 'Enabled'
            }
        )
        logging.info(f"Successfully enabled Transfer Acceleration for {bucket_name}")
        return response
    except Exception as e:
        logging.error(f"Error enabling Transfer Acceleration: {e}")
        return None

if __name__ == "__main__":
    enable_transfer_acceleration(BUCKET_NAME)

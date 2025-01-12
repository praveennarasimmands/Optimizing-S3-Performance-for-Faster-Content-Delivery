import boto3
import logging

# Set up logging
logging.basicConfig(filename='logs/performance_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def monitor_performance():
    cloudwatch = boto3.client('cloudwatch')

    try:
        # Retrieve CloudWatch metrics for S3 and CloudFront
        s3_metrics = cloudwatch.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 's3_get_requests',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'AWS/S3',
                            'MetricName': 'AllRequests',
                            'Dimensions': [
                                {
                                    'Name': 'BucketName',
                                    'Value': 'your-bucket-name'
                                }
                            ]
                        },
                        'Period': 60,
                        'Stat': 'Sum',
                    },
                    'ReturnData': True
                }
            ]
        )
        logging.info(f"S3 performance metrics: {s3_metrics}")

        cloudfront = cloudwatch.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'cf_requests',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'AWS/CloudFront',
                            'MetricName': 'Requests',
                            'Dimensions': [
                                {
                                    'Name': 'DistributionId',
                                    'Value': 'your-distribution-id'
                                }
                            ]
                        },
                        'Period': 60,
                        'Stat': 'Sum',
                    },
                    'ReturnData': True
                }
            ]
        )
        logging.info(f"CloudFront performance metrics: {cloudfront}")
    except Exception as e:
        logging.error(f"Error monitoring performance: {e}")

if __name__ == "__main__":
    monitor_performance()

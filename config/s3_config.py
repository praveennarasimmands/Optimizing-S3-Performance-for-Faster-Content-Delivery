# Configuration file for S3 performance optimization project

# S3 Bucket Name
BUCKET_NAME = 'your-bucket-name'

# AWS Region where the S3 bucket is located
AWS_REGION = 'us-east-1'

# CloudFront Distribution ID (if configuring CloudFront)
CLOUDFRONT_DISTRIBUTION_ID = 'your-cloudfront-distribution-id'

# CloudWatch namespace for monitoring
CLOUDWATCH_NAMESPACE = 'AWS/S3'

# S3 Transfer Acceleration URL (this is constructed dynamically, typically doesn't need hardcoding)
TRANSFER_ACCELERATION_URL = f"http://{BUCKET_NAME}.s3-accelerate.amazonaws.com"

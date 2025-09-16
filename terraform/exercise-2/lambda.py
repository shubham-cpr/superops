import boto3
import json

tagging_client = boto3.client("resourcegroupstaggingapi")

def lambda_handler(event, context):
    print("Incoming event:", json.dumps(event, indent=2))

    detail = event.get("detail", {})
    user_arn = detail.get("userIdentity", {}).get("arn", "unknown")
    event_name = detail.get("eventName")
    region = event.get("region")
    account = event.get("account")
    service = detail.get("eventSource", "").split(".")[0]  # <-- FIX HERE

    resource_arns = []

    # --- EC2: RunInstances ---
    if event_name == "RunInstances":
        instances = detail.get("responseElements", {}).get("instancesSet", {}).get("items", [])
        for inst in instances:
            instance_id = inst["instanceId"]
            resource_arns.append(f"arn:aws:ec2:{region}:{account}:instance/{instance_id}")

    # --- S3: CreateBucket ---
    elif service == "s3" and "bucketName" in detail.get("requestParameters", {}):
        bucket_name = detail["requestParameters"]["bucketName"]
        s3 = boto3.client("s3")
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={
                "TagSet": [
                    {"Key": "CreatedBy", "Value": user_arn}
                ]
            }
        )
        print(f"Tagged S3 bucket {bucket_name} with CreatedBy={user_arn}")

    # --- RDS: CreateDBInstance ---
    elif event_name == "CreateDBInstance":
        db_id = detail.get("responseElements", {}).get("dBInstanceIdentifier")
        if db_id:
            resource_arns.append(f"arn:aws:rds:{region}:{account}:db:{db_id}")

    # --- EKS: CreateCluster ---
    elif event_name == "CreateCluster":
        cluster_name = detail.get("responseElements", {}).get("name")
        if cluster_name:
            resource_arns.append(f"arn:aws:eks:{region}:{account}:cluster/{cluster_name}")

    # --- ECR: CreateRepository ---
    elif event_name == "CreateRepository":
        repo_name = detail.get("responseElements", {}).get("repositoryName")
        if repo_name:
            resource_arns.append(f"arn:aws:ecr:{region}:{account}:repository/{repo_name}")

    # --- Add more services here as needed ---

    # Apply tagging if we found resources
    if resource_arns:
        try:
            tagging_client.tag_resources(
                ResourceARNList=resource_arns,
                Tags={"CreatedBy": user_arn}
            )
            print(f"Tagged {resource_arns} with CreatedBy={user_arn}")
        except Exception as e:
            print(f"Tagging failed: {str(e)}")
    else:
        print(f"No supported resources found for {event_name}")

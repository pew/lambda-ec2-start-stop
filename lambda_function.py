"""aws lambda function to start/stop instances"""
import boto3


def lambda_handler(event, context):
    """take instance-id and region from event, start or stop the instance"""
    client = boto3.client("ec2", region_name=event["region"])

    instance_id = event["instance_id"]
    get_status = client.describe_instances(InstanceIds=[instance_id])
    current_status = get_status["Reservations"][0]["Instances"][0]["State"]

    if current_status["Name"] == "running":
        response = client.stop_instances(InstanceIds=[instance_id])
    if current_status["Name"] == "stopped":
        response = client.start_instances(InstanceIds=[instance_id])

    return response

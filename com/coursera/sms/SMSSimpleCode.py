import boto3

client = boto3.client(
    "sns",
    aws_access_key_id="AKIAUBZBICXHUIHZSCIV",
    aws_secret_access_key="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",
    region_name="ap-south-1"
)

client.publish(
PhoneNumber="+919000017580",
Message="From Apparao"
)

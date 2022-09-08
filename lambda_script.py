import json
import boto3

def lambda_handler(event, context):

    print("MyEvent:")
    print(event)

    method = event['context']['http-method']

    
    if method == "POST":

        p_record = event['body-json']
        recordstring = json.dumps(p_record)

        client = boto3.client('kinesis')
        response = client.put_record(
            StreamName='OrderAPIData',
            Data= recordstring,
            PartitionKey='string'
        )

        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }
        
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }
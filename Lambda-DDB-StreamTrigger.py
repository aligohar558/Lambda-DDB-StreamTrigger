import json
import boto3

print('Loading function')

client=boto3.client('dynamodb')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        print(record['dynamodb'])
        #print(record['eventID'])
        #print(record['eventName'])
        #print("DynamoDB Record: " + json.dumps(record['dynamodb'], indent=2))
        
        if record['eventName'] == 'INSERT':
            response=client.put_item(TableName='Phase2',Item=record['dynamodb']['NewImage'])
        elif record['eventName'] == 'MODIFY':
            response=client.put_item(TableName='Phase2',Item=record['dynamodb']['NewImage'])
        elif record['eventName'] == 'REMOVE':
            response=client.delete_item(TableName='Phase2',Item=record['dynamodb']['NewImage'])
            
    return 'Successfully processed {} records.'.format(len(event['Records']))

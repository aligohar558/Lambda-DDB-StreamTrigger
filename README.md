# Lambda-DDB-StreamTrigger
A lambda function code, that will capture updates on the DynamoDB source table and copy to a new DynamoDB table. 

The source DynamoDB Table will have DynamoDB stream enabled.

The lambda function will have DynamoDB stream as the trigger. 

For more details about this see:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html

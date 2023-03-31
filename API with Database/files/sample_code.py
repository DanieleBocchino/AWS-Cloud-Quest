# AWS SDK for Python (Boto3) - https://aws.amazon.com/sdk-for-python/
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
import logging
import json

# AWS Lambda Function Logging in Python - https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html
logger = logging.getLogger()
logger.setLevel(logging.INFO)


session = boto3.Session()
# Boto3 - DynamoDB - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
dynamodb = session.resource("dynamodb")

###Lab Note: Change below to the new table name created for the DIY section.
table_name = "locations"

table = dynamodb.Table(table_name)

# DynamoDB create item in table logic
def create_item(item):
    try:
        ret = table.put_item(Item=item);
        logger.info({"operation": "create an item", "details": ret});
        
    except ClientError as err:
        print(err);
        logger.debug({"operation": "item creation", "details": err});
        

# DynamoDB update Item from table logic
def update_item(item, reserve):
    try:
        ret = table.update_item(
            Key={
                'id': item["id"]
            },
            UpdateExpression="set reserve = :ad",
            ExpressionAttributeValues={
                ':ad': reserve
            },
            ReturnValues="UPDATED_NEW"
        )
        logger.info({"operation": "update an item ", "details": ret});
        
    except ClientError as err:
        logger.debug({"operation": "item update", "details": err});

# DynamoDB get Item from table logic
def get_item(id):
    try:
        ret = table.get_item(
            Key={ 'id': id }
        )
        logger.info({"operation": "query an item ", "details": ret});
        # Return the Item - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.get_item
        return ret['Item'];
    except ClientError as err:
        logger.debug({"operation": "item query", "details": err});
    
    
# function to handle API Gateway Lambda proxy integration event and pass DIY validation
def api_gateway_handler(event):
    body = json.loads(event['body'])
    item = body['vehicle']
    item_id = item['id']
    
    create_item(item)
    update_item(item,"yes")
    
    ret = get_item(item_id)
    
    api_gateway_return = {
        'statusCode': '200',
        'body' : json.dumps(ret),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
    
    return api_gateway_return
    
# Function to handle Lambda Local Test
def local_test_handler(event):
    item = event['vehicle']  

    item_id = item['id']
    create_item(item)
    update_item(item,"yes")
        
    ret = get_item(item_id)
        
    # Uncomment the code above to print the return 
    # print("Return: " + json.dumps(ret, indent=2))
    
    return ret


def lambda_handler(event, context):
    ''''
      Example JSON in event when testing locally. 
      {
        "vehicle": {
          "id": "1",
          "available": "true",
          "type": "scooter"
        }
      }
    '''
    # Uncomment bellow line to inspect events at CloudWatch
    logger.info(event)


    # Function will first try to use the api-gateway-handler, if it fails it will default to trying the local test event.
    try:
        ret = api_gateway_handler(event)
    except:
        ret = local_test_handler(event)    

    return ret
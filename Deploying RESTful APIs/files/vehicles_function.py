import json
import logging

# AWS Lambda Function Logging in Python - https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    '''Demonstrates Amazon API Gateway Lambda proxy integration. You have full
    access to the request and response payload, including headers and
    status code.
    https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    '''
    logger.debug(event) # Mind logger.setLevel at line 6. Check Event printed at CloudWatch

    #/vehicles/{vehicleId}
    vehicles = [
        { "id": "1", "type": "bike", "available":"true"},
        { "id": "2", "type": "car", "available":"false"},
        { "id": "3", "type": "truck", "available": "true"}
    ]
    
    
    # Input Format https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    resource = event['resource']
    # Uncomment to print the event
    # print("Received event: " + json.dumps(event, indent=2))

    err = None
    # /vehicles List all vehicles
    response_body = {}
    if (resource == "/vehicles"):
        response_body = {
            "vehicles": vehicles
        }
    # /vehicles/vehicleId find vehicle by Id    
    elif (resource == "/vehicles/{id}"):
        vehicleId = event['pathParameters']['id']
        value = next((item for item in vehicles if item["id"] == str(vehicleId)), False)
        if( value == False ):
            err = "vehicle not found"
        else:
            response_body = {
                "vehicle": value
            }

        
    response =  response_payload(err, response_body)

    return response
  
  
    
'''
In Lambda proxy integration, API Gateway sends the entire request as input to a backend Lambda function. 
API Gateway then transforms the Lambda function output to a frontend HTTP response.
Output Format: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format
'''
def response_payload(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }
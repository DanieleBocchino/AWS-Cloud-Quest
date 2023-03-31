# Runtime: Python 3.8
# Please review the comments for each code block to help you understand the execution of this Lambda function.
# At the time you create a Lambda function, you specify a handler, 
# which is a function in your code, that AWS Lambda can invoke when the service executes your code.
# The Lambda handler is the first function that executes in your code.
# Python programming model - https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html
def lambda_handler(event, context):
    
    # context – AWS Lambda uses this parameter to provide runtime information to your handler.
    # event – AWS Lambda uses this parameter to pass in event data to the handler. This parameter is usually of the Python dict type.
    # AWS Lambda function Python handler - https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
    
    # When you invoke your Lambda function you can determine the content and structure of the event. 
    # When an AWS service invokes your function, the event structure varies by service.
    # 
    # In this lab, the lambda_handler "event" parameter has the following structure of name/value pairs:
    # {
    #     "emoji_type": number,
    #     "message": "string"
    # }
        
    # In a name-value pair you can extract the "value" of the pair using the "name" of the pair.   
    # Here the id value is extracted from the event Lambda parameter and passed to a variable called emoji_type.
    emoji_type = event["emoji_type"]
    # Here the message value is extracted from the event Lambda parameter and passed to a variable called message.
    message = event["message"]
    
    # The variables are printed here, which means the variable values will be displayed in CloudWatch logs and the Execution Results panel.
    print(emoji_type)
    print(message)
    
    # In Python, you can create a variable with no value using the Built-in constant None. This means the variable "custom_message" currently has no value.
    custom_message = None
    
    # In Python, we use the if-elif-else to create a conditional execution. https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
    # That is, if the value of emoji_type is equal to 0, we execute the statement inside its block
    if emoji_type == 0:
        # Only execute if id is equal to 1
        # The variable custom_message combines "Message for code 0:" string with the variable message
        custom_message = "Message for code 0: " + message

    elif emoji_type == 1:
        # The variable custom_message combines "Message for code 1:" string with the variable message
        custom_message = "Message for code 1: " + message

    else:
        # The variable custom_message combines "Message for all other codes:" string with the variable message
        custom_message = "Message for all other codes: " + message
        
    # Optionally, the handler can return a value. What happens to the returned value depends on the invocation type you use when invoking the Lambda function
    # In this lab we use synchronous execution, so we need to create a response for the lambda function.
    # We created a "response" variable that has a structure of name-value pairs using the id and custom_message created earlier.
    response = {
        # In this name-value pair, the literal value "message" will store the value of the variable custom_message.
        "message": message,
        # In this name-value pair, the literal value "id" will store the value of the variable id.
        "custom_message": custom_message,
    }
    
    # Finally, we return the values from response variable to the caller, which could be a test event or an AWS service performing a synchronous call.
    # The execution of the lambda function is finished.
    return response

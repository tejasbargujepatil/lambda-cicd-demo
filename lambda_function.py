import json

def lambda_handler(event, context):
    operation = event.get('operation', 'add')
    a = event.get('a', 0)
    b = event.get('b', 0)

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b if b != 0 else 'error: division by zero'
    else:
        result = 'unknown operation'

    return {
        'statusCode': 200,
        'body': json.dumps({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result,
            'version': 'v4.0'           # change this to prove CI/CD works
        })
    }


import json

def lambda_handler(event, context):
    # Parse input from the event
    try:
        num1 = event['num1']
        num2 = event['num2']
        result = num1 + num2
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f"Missing key: {e}"})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

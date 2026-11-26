import json
import base64


def _response(status_code, message):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': json.dumps({'message': message})
    }

def lambda_handler(event, context):
    if event is None:
        event = {}

    if event.get('requestContext', {}).get('http', {}).get('method') == 'OPTIONS' or event.get('httpMethod') == 'OPTIONS':
        return _response(200, 'OK')

    body = event.get('body')
    if isinstance(body, dict):
        data = body
    else:
        if not body:
            data = {}
        else:
            if event.get('isBase64Encoded'):
                try:
                    body = base64.b64decode(body).decode('utf-8')
                except (ValueError, UnicodeDecodeError):
                    return _response(400, 'Invalid base64 request body')
            try:
                data = json.loads(body)
            except (json.JSONDecodeError, TypeError):
                return _response(400, 'Invalid JSON request body')

    if not isinstance(data, dict):
        return _response(400, 'Request body must be a JSON object')

    name = data.get('name', 'Anonymous')
    email = data.get('email', 'No email')
    message = data.get('message', 'No message')

    print(f"Name: {name}, Email: {email}, Message: {message}")

    return _response(200, 'Thanks, message sent!')
# AWS Lambda Contact Form Handler

This Python Lambda function processes contact-form requests from API Gateway.

## Behavior

- Parses JSON, dictionary, and missing request bodies.
- Supports API Gateway REST and HTTP API event formats.
- Handles OPTIONS requests for CORS preflight.
- Returns clear `400` responses for invalid JSON or non-object bodies.
- Returns `200` for successful requests.

## Handler

The Lambda entry point is:

```python
lambda_handler(event, context)
```

## Example Request

```json
{
  "name": "Ada",
  "email": "ada@example.com",
  "message": "Hello"
}
```

## Deployment

Upload `lambda_function.py` to an AWS Lambda Python runtime, set the handler to
`lambda_function.lambda_handler`, and connect it to your API Gateway endpoint.

import json
import boto3
import traceback

sagemaker_runtime = boto3.client('sagemaker-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        if 'title' not in body or 'text' not in body:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'title' or 'text' in request body"})
            }

        text_input = f"{body['title']} {body['text']}"
        payload = {
            "instances": [text_input]
        }

        response = sagemaker_runtime.invoke_endpoint(
            EndpointName='check-news-4',
            ContentType='application/json',
            Body=json.dumps(payload)
        )

        result = json.loads(response['Body'].read().decode())
        prediction = result[0]

        label = prediction['label'][0].replace("__label__", "")
        prob = prediction['prob'][0]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "data": {
                    "label": f"{label}-news",
                    "prob": prob
                }
            })
        }

    except sagemaker_runtime.exceptions.ModelError as e:
        return {
            "statusCode": 502,
            "body": json.dumps({"error": "Model error", "details": str(e)})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Internal server error",
                "details": str(e),
                "trace": traceback.format_exc()
            })
        }

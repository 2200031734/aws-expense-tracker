import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Expenses')  # Make sure table name matches exactly

def lambda_handler(event, context):
    try:
        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event

        expense_id = body["expense_id"]

        table.delete_item(
            Key={
                "expense_id": expense_id
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Expense deleted successfully!")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }


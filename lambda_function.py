def lambda_handler(event, context):
    name = event["name"]
    message = f"Hello, {name}!"

    try:
        return {
            "statusCode": 200,
            "body": message
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": {"error": str(e)}
        }
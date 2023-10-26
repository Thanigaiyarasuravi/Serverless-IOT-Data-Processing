import json
def lambda_handler(event, context):
    try:
        # Extract IoT data from the event
        iot_data = json.loads(event['body'])
        # Perform data preprocessing (customize as needed)
        preprocessed_data = preprocess_data(iot_data)
        # Store the preprocessed data (e.g., in an S3 bucket)
        store_preprocessed_data(preprocessed_data)
        # Return a response if needed
        response = {
            "statusCode": 200,
            "body": "Data loaded and preprocessed successfully"
        }
        return response
    except Exception as e:
        # Handle errors and exceptions
        error_message = "Error processing IoT data: " + str(e)
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": error_message})
        }
        return response
def preprocess_data(iot_data):
    # Example preprocessing function
    # You can perform data cleaning, transformation, or feature extraction here
    # For simplicity, this example just returns the input data as-is
    return iot_data
def store_preprocessed_data(data):
    # Example function to store data (e.g., in an S3 bucket)
    # Replace with the actual code for storing data in your chosen storage service
    pass
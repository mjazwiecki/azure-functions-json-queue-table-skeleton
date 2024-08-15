import logging
import json
import random
import azure.functions as func

def main(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:
    """
    HTTP trigger function that generates random JSON data and writes it to an Azure Storage Queue.

    Args:
        req (func.HttpRequest): The HTTP request object.
        msg (func.Out[str]): The output binding to the Azure Storage Queue.

    Returns:
        func.HttpResponse: The HTTP response containing the generated JSON data.
    """
    logging.info('HTTP trigger function processed a request.')

    # Generate random JSON data
    data = {
        "id": random.randint(1, 1000),
        "name": "SampleName",
        "value": random.random()
    }

    # Convert to JSON string
    json_data = json.dumps(data)

    # Write to the queue
    msg.set(json_data)

    return func.HttpResponse(
        json_data,
        status_code=200,
        mimetype="application/json"
    )
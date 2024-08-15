import logging
import json
import azure.functions as func

def main(msg: func.QueueMessage, outputTable: func.Out[str]) -> None:
    """
    Queue trigger function that processes a message from an Azure Storage Queue 
    and writes a static entity to an Azure Table.

    Args:
        msg (func.QueueMessage): The message from the Azure Storage Queue.
        outputTable (func.Out[str]): The output binding to the Azure Table.

    Returns:
        None
    """
    logging.info('Queue trigger function processed a message.')
    
    data = json.loads(msg.get_body().decode('utf-8'))
    # Create a simple static entity for testing
    table_data = {
        "PartitionKey": "partition",
        "RowKey": str(data["id"]),
        "Name": data["name"],
        "Value": data["value"]
    }

    # Write the simple entity to the table
    outputTable.set(json.dumps(table_data))
    logging.info('Successfully written static test entity to the table.')

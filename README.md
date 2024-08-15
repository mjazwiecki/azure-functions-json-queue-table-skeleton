# Azure Functions App                                                     
                                                                            
This project contains two Azure Functions using the Python v1 programming model, both deployed in a single Function App.                              
                                                                            
## Functions                                                              
                                                                            
### 1. HTTP Trigger Function                                              
                                                                            
This function is triggered by an HTTP request and generates random JSON   
data, which is then written to an Azure Storage Queue.                      
                                                                            
- **Trigger**: HTTP                                                       
- **Output**: Azure Storage Queue

### 2. Queue Trigger Function

This function is triggered by messages added to an Azure Storage Queue and processes the messages.

- **Trigger**: Azure Storage Queue
- **Output**: None

## Local Development

The `local.settings.json` file contains the configuration settings for the  
Azure Functions. For local development, it uses the Azure Storage Emulator. 
For production, you should update the connection strings to point to your   
Azure Storage account.

## Contributing                                                             

If you would like to contribute to this project, please fork the repository 
and submit a pull request.                                                  

## License                                                                  

This project is licensed under the MIT License.
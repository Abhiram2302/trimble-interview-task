import requests
import json
import sys
from ExceptionHandler import ExceptionHandler

class Utils:
    # global method for getting response with retries
    def get_with_retry(url,request_params={}):
        # adding retry capability with incremental sleep time for 'get' function in case of connection issues
        retry_count = 0
        while retry_count < 3:
            try:
                response = requests.get(url, request_params)
                if response.status_code ==200:
                    return response.json()
                else:
                    # to handle http error codes
                    raise ExceptionHandler(response.text ,response.status_code)
                                        
            except requests.ConnectionError:
                # increment retry_count only when connection error occurs
                retry_count = retry_count + 1
                print("Connection failed -- trying to reconnect -- retry :" + str(retry_count))
            
                if retry_count == 3:
                    raise ExceptionHandler(f'ConnectionError : Unable to connect to {url} even after retries')
                else:
                    # incrementing sleep time for every retry by 5 sec
                    print("Sleeping for " + str(retry_count * 5 ) + 'sec')
                    time.sleep(3 * retry_count)    
                    
            except json.decoder.JSONDecodeError:
                # to handle json related issues
                raise ExceptionHandler("JSON Decode Error : " + response.text)
                break

import requests
import time

#This is the URL to switch on the LED.
#Please see the code explanation for more information
urlON="http://cloud.boltiot.com/remote/cf43bbd2-6af8-49e6-a9d4-f88092c71f1f / “digitalWrite?pin=0&state=HIGH” &deviceName=BOLT3462214"

#This is the URL to switch off the LED
#Please see code explanation for more information
urlOFF="http://cloud.boltiot.com/remote/cf43bbd2-6af8-49e6-a9d4-f88092c71f1f /“digitalWrite?pin=0&state=LOW”&deviceName=BOLT3462214"

#script runs continuously. Press CTRL+C to exit the loop and stop code.
while True:
    #Send request to switch on the LED
    r=requests.get(urlON)
    #Sleep for 5 seconds
    time.sleep(5)
    #Send request to switch off the LED
    r=requests.get(urlOFF)
    #Sleep for 5 seconds 
    time.sleep(5)

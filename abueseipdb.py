import csv
from pip._vendor import requests
import json


IP=[]              #list of all ip addresses that are stored in csv file

with open ('csv_file_path','r',newline='') as f:
    reader=csv.DictReader(f)
    for q in reader:
        IP.append(q['IP'])
key = 'your_API_KEY'
url = 'https://api.abuseipdb.com/api/v2/check'
headers = {
'Accept': 'application/json',
'Key': key}
Data=[]                    #to store proprties of all ip addresses as a list  
for e in IP:               #loop on all ip addresses and pass the next ip to #response 

    querystring = {'ipAddress': e,'maxAgeInDays': '90'}
    response = requests.request(method='GET', url=url, headers=headers, params=querystring) 
    json_Items = json.loads(response.text)
    json_Keys_Values = json_Items["data"]
    Data.append(json_Keys_Values)
with open("Output.csv","w", newline='') as d: 
    fieldnames = ['ipAddress','isPublic','ipVersion','isWhitelisted','abuseConfidenceScore','countryCode','usageType','isp','domain','hostnames','totalReports','numDistinctUsers','lastReportedAt']
    The_Writer = csv.DictWriter(d, fieldnames=fieldnames)            
    The_Writer.writeheader()
    for z in Data:
        The_Writer.writerow(z)      

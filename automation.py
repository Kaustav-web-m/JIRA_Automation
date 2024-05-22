import requests
import json

url = "https://kaustavm.atlassian.net/rest/api/3/issue"
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}  

payload = json.dumps(
    {
        "fields": {
            "project" :  
            {
                "key" : "WFDPF" # API key from project settings
            },
            "summary" : "DashRT Failure (wellsfargodashrtdashboard | PROD | UAT | r014nw6ar7 | POST | /wf/rendered-documents | us-west-2 | [10.79.15.250, 159.45.186.23, 172.17.2.202])",
            "description": {
            "content": [
                {  
                "content": [
                   {
                    "text": "Request Information\nApi ID: r014nw6ar7\nHttp Method: POST\nAPI Request: /wf/rendered-documents\nAWS Request ID: 11c10975-c8a9-41e9-9c07-7711013649e7\nRegion: us-west-2\nIP Address: [10.79.13.254, 159.45.186.23, 172.17.2.202]\nUser Agent: [Apache-HttpClient/4.5.14 (Java/11.0.22)]\nTrace ID: Root=1-66178420-2056fcfb63c36d2a760826fa\nX-CORRELATION-ID: e9f12077-9acf-4b72-8f76-552eb3066bbb",
                    "type": "text"
                   }   
                ],
            "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
            },
            "issuetype" : {
            "name" :  "[System] Incident"
            }
        }
    }
)

response = requests.post(url,headers=headers,data = payload,auth=("<Email>","<JIRA Auth Token>"))
print(response.text)


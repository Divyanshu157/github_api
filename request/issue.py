import requests
import json


import os
from dotenv import load_dotenv

load_dotenv()



token= os.getenv('token')
url ="https://api.github.com/repos/{}/{}/issues"

headers={
    "authorization":"Bearer {}".format(token)
}

data={
    "title":" Issues created with api",
    "body":"This all i want to ssay"
}
response = requests.post(url.format("divyanshu157","githubapidemo"),headers=headers,json=data)
output= json.loads(response.text)


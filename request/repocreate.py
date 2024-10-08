import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()



token= os.getenv('token')



url = "https://api.github.com/{}"

path="user/repos"


headers={
    "authorization" : "Bearer {}".format(token)
}

data = {
    "name" :"githubapidemo",
    "description":"Genetrating API"
}

response=requests.post(url.format(path) ,headers=headers,json=data)
output = json.loads(response.text)
# print(json.loads(response.text))



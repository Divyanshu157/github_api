import json
import requests

import os
from dotenv import load_dotenv

load_dotenv()



token= os.getenv('token')
url = "https://api.github.com/{}"

path="repos/divyanshu157/githubapidemo"


headers={
    "authorization" : "Bearer {}".format(token)
}
# data = {
#     "name" :"githubapidemo",
#     "description":"Genetrating API"
# }
response=requests.delete(url.format(path) ,headers=headers)
# output = json.loads(response.text)
# print(json.loads(response.text))

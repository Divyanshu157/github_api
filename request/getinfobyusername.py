
import requests

import json
username = "divyanshu157"

url = "https://api.github.com/users/{}".format(username)
respone = requests.get(url)


# # print(respone.text)
output = json.loads(respone.text)
# print(output['login'])

# response_img  =requests.get(output["avatar_url"])

# fp = open("{}.png".format(username) , "wb")
# fp.write(response_img.content)
# fp.close()




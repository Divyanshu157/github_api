import requests

response  =requests.get("https://in.bookmyshow.com/person/divyendu-sharma/23565/filmography")

fp = open("mypic.png" , "wb")
fp.write(response.content)
fp.close()
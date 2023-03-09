import requests
from bs4 import BeautifulSoup
import json








url =input("Please paste the video link:\n")
content = requests.get(url).text


soup = BeautifulSoup(content,"lxml")

slug = soup.find(name="link")["href"].replace("https://www.mlb.com/video/","")



all_script_label = soup.find_all(name ="script")

target = all_script_label[20].text.split("\n")[1].split("=")[1]


json_ob = json.loads(json.loads(target))


uu = '{\"idType\":\"SLUG\",\"ids\":\"'
rr = '\",\"languagePreference\":\"EN\"}'

new = uu+slug+rr

s =f'mediaPlayback({new})'

mediaplayback_id = json_ob["ROOT_QUERY"][s][0]["__ref"]

download_link = json_ob[mediaplayback_id]["feeds"][0]["playbacks"][0]["url"]

response = requests.get(download_link)

with open("xxx.mp4","wb") as f:
    f.write(response.content)
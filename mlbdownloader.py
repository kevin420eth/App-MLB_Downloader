import pyperclip
import requests
from bs4 import BeautifulSoup
import json


while True:
    url = input("Please Enter the url:\n")
    res = requests.get(url) 
    content = res.text

    soup =BeautifulSoup(content,"html.parser")

    #Copy the content of target website to target_website.html and make it look nice
    with open("target_website.html","w",encoding="utf-8") as f:
        f.write(soup.prettify())

    title = soup.find("title")
    match = soup.find("a",class_="GameMatchup__Label-sc-1d58ibd-0 ifOAxy")
    slug = soup.find(name="link")["href"].replace("https://www.mlb.com/video/","")

    #Split the elements in title with symbol "|"
    titlelist = title.text.split("|")
    video_title = titlelist[0]
    date = titlelist[1]
    file_date = date.replace("/","")

    #Create a new title for your Youtube videos and file name for your downloaded file
    new_title = f"[MLB] {video_title}| {match.text}{date}| MLB Postseason"
    file_name = f"[MLB] {video_title} {match.text}{file_date} MLB Postseason"

    #Copy the new title to clipboard
    pyperclip.copy(new_title)


    #below is to find the download link and download it
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

    #Download the target video to the desktop
    with open(f"C:/Users/Kevin/Desktop/{file_name}.mp4","wb") as f:
        f.write(response.content)

    print("\nDownload is completed!\n")
    print(f"The new title is 👇\n{new_title}\n")


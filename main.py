#!/usr/bin/python3
#Made by prine
import requests
import json
import os
import sys
import pyshorteners
from random import choice
# make a function to chekk the intetnet connection ...
def internet():
    try:
        res = requests.get("https://github.com/princekrvert")
        if res.status_code == 200:
            pass
        else:
            print("Something wrong happned!")
            banner()
    except:
        print("Please turn on internet connection")
    

# make a banner 
def banner():
    print("\033[35;1m")
    print('''  o8o                           o8o                  o8o           
 `"'                           `"'                  `"'           
oooo  ooo. .oo.   ooo. .oo.   oooo  ooo. .oo.      oooo  .oooo.   
`888  `888P"Y88b  `888P"Y88b  `888  `888P"Y88b     `888 `P  )88b  
 888   888   888   888   888   888   888   888      888  .oP"888  
 888   888   888   888   888   888   888   888      888 d8(  888  
o888o o888o o888o o888o o888o o888o o888o o888o     888 `Y888""8o 
                                                    888           
                                                .o. 88P           
                                                `Y888P             ''')
    print("\033[0;1m MADE BY PRINCE ")

# make a function to handle the user argument ..

def help():
    if len(sys.argv) == 1 or sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("\033[31;1m Uses : ")
        print("python3 main.py username")
    elif len(sys.argv) == 2 and sys.argv[1] != "-h":
        check_e(sys.argv[1])
    else:
        print("\033[32;1m Unknown arguments: ")
#Make a function to get the random useragent...
def userAgent():
    res = requests.get("https://gist.githubusercontent.com/haoliangyu/493a766d0e464e1e0d69/raw/fecf47d4fd0bf2e8f134b315acff12148513059c/userAgentList.json", timeout = 3)
    agent = choice(json.loads(res.text))
    return agent
#Make a function to get a working proxy
def getProxy():
    res = requests.get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true", timeout = 3)
    testProxy = { "https" : f"{res.text}",
            "http" : f"{res.text}"
            }
    
    return testProxy
    
#Create a function to make req
def userReq(username):
    session = requests.Session()
    session.headers = { "User-Agent" : userAgent(),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Alt-Used":"www.instagram.com",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host" : "www.instagram.com",
   "Sec-Fetch-Dest" : "document",
   "Sec-Fetch-Mode": "navigate",
   "Sec-Fetch-Site":"none",
   "Sec-Fetch-User":	"?1",
   "Sec-GPC" :	"1",
   "TE"	: "trailers",
   "Upgrade-Insecure-Requests":"1"
}
    session.proxies = getProxy()
    url = f"https://www.instagram.com/{username}/?__a=1"
    r = session.get(f"https://www.instagram.com/{username}/?__a=1", timeout = 10)
    try:
        data = json.loads(r.text)
        with open(f"data/{username}","w") as f:
            f.write(data)
        getInfo(data)
    
    except json.decoder.JSONDecodeError :
        print("\033[36;1m Server dected us try after some time ")
       


#Make a function to get th  e data
def getInfo(data):
    #Get the biography
    bio_data = data["graphql"]["user"]
    #Get the full name 
    print("\033[96;1m[~] Full Name: ")
    print("\033[35;1m ",end="")
    print(bio_data["full_name"])
    #Get profile pic url
    print("\033[96;1m[~] Profile pic: ")
    print("\033[35;1m ",end="")
    pic_url = bio_data["profile_pic_url_hd"]
    p= pyshorteners.Shortener()
    short_url=p.tinyurl.short(pic_url)
    print(short_url)
    #Connected facebook page 
    print("\033[96;1m[~] Facebook page: ")
    print("\033[35;1m ",end="")
    print(bio_data["connected_fb_page"])
    #Get the video url
    print("\033[96;1m[~] Video url: ")
    print("\033[35;1m ",end="")
    video_url = bio_data["edge_felix_video_timeline"]["edges"][0]["node"]["video_url"]
    short_url=p.tinyurl.short(video_url)
    print(short_url)
    #Get id
    print("\033[96;1m[~] Id : ")
    print("\033[35;1m ",end="")
    print(bio_data["edge_felix_video_timeline"]["edges"][0]["node"]["owner"]["id"])
    #Get info 
    #More info coming soon
    #Get the account info
    
    print("\033[96;1m[~] Pro account: ")
    print("\033[35;1m ",end="")
    print(bio_data["is_professional_account"])
    #Bisiness mail
    print("\033[96;1m[~] Mail : ")
    print("\033[35;1m ",end="")
    print(bio_data["business_email"])
    #Privet account info
    print("\033[96;1m[~] Private : ")
    print("\033[35;1m ",end="")
    print(bio_data["is_private"])

    print("\033[96;1m[~] Biography 🧐: ")
    print("\033[35;1m ",end="")
    print(bio_data["biography"])
    #Get the number of follower
    print("\033[96;1m[~] Follower 💟: ")
    print("\033[35;1m ",end="")
    print(bio_data["edge_follow"]["count"])
    #Get the following
    print("\033[96;1m[~] Following 🐥: ")
    print("\033[35;1m ",end="")
    print(bio_data["edge_followed_by"]["count"])
    #Get the external url
    print("\033[96;1m[~] Bio Url :")
    print("\033[35;1m",end="")
    print(bio_data["external_url"])
    sco_c = data["seo_category_infos"]
    print("\033[96;1m[~] Sco Info 👻: ")
    for cat in sco_c:
        print("\033[35;1m",end="")
        print(f"{cat[1]}")

def check_e(username):
    if os.path.exists(f"data/{username}.txt"):
        print("\033[33;1m An information with this username is already exists press y for continue or any key for new fetch")
        optn = input()
        if optn == "y" or optn == "Y":
            with open(f"data/{username}.txt","r") as r:
                data = json.load(r)
                getInfo(data)
        else:
            os.remove(f"data/{username}.txt")
            print("File deleted :> Fetching new info")
            #Call the fetch function..
            userReq(username)
    
    else:
        print("Getting info...")
        #cAll the fetch function..
        userReq("princekrvert")
if __name__ == "__main__":
    internet()
    banner()
    help()
    

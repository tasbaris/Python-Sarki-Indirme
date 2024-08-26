   
import requests
import json
import time
import sys
import os
import re

   
url = "https://yt-api.p.rapidapi.com/search"
arama = input("Aramak istediğiniz şarkı veya artist adını giriniz : ")
querystring = {"query":arama,"sort_by":"views","type":"video","geo":"TR","lang":"tr"}

headers = {
	"x-rapidapi-key": "98c1f187a7mshe068bc8a66da9a8p1e4e70jsn69d9436ad1ed",
	"x-rapidapi-host": "yt-api.p.rapidapi.com"
}
try:
   response = requests.request("GET", url, headers=headers, params=querystring)
except ConnectionError:
   print("İnternet bağlantınızı Kontrol edin.")
   exit(1)
except Exception:
   print("Hata lütfen daha sonra tekrar deneyiniz!")
sarkilar = json.loads(response.text)
idler = []
i=0
counter=1
song_c=0
while(i != len(sarkilar["data"])):
   if sarkilar["data"][i]["type"] == "video":
      print("["+str(counter)+"] ",sarkilar["data"][i]["title"])
      idler.append({
        "videoId": sarkilar["data"][i]["videoId"],
        "title": sarkilar["data"][i]["title"]
      })
      counter+=1
      song_c+=1
   i+=1
print(song_c," adet şarkı bulundu")
index = int(input("Şarkı seçiniz : "))

sarkiAdi =  idler[index-1]["title"]
print("Seçilen Şarkı : "+sarkiAdi)
sarkiAdi = re.sub(r'[\\/*?:"<>|]', "_", sarkiAdi) 
time.sleep(2)
print("indirme işlemi başladı ...")

url = "https://yt-api.p.rapidapi.com/dl"
querystring = {"id":idler[index-1]["videoId"]}
try:
   response = requests.request("GET", url, headers=headers, params=querystring)
   veri = json.loads(response.text)
   if veri["formats"][0]["audioQuality"] == "aAUDIO_QUALITY_MEDIUM":
      j=1
      while(j != len(veri["adaptiveFormats"])):
         if veri["adaptiveFormats"][j]["audioQuality"] == "AUDIO_QUALITY_MEDIUM":
            response = requests.get(veri["adaptiveFormats"][j]["url"])
            break
         j+=1
   else:
      response = requests.get(veri["formats"][0]["url"])
   if not os.path.exists("./Music"):
      os.mkdir("./Music")     
   file_path = os.path.join("Music", sarkiAdi + ".m4a")
   open(file_path,"wb").write(response.content)     
   print("İndirme işlemi tamamlandı!")  
except ConnectionError:
   print("İnternet bağlantınızı Kontrol edin.")
   exit(1)
except Exception:
   print("Hata lütfen daha sonra tekrar deneyiniz!\n", sys.exc_info())

time.sleep(5)

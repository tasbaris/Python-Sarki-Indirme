import requests
import json
import shutil
import time
   
url = "https://youtube-music1.p.rapidapi.com/v2/search"
arama = input("Aramak istediğiniz şarkı veya artist adını giriniz : ")
querystring = {"query":arama}

headers = {
	"X-RapidAPI-Key": "98c1f187a7mshe068bc8a66da9a8p1e4e70jsn69d9436ad1ed",
	"X-RapidAPI-Host": "youtube-music1.p.rapidapi.com"
}
try:
   response = requests.request("GET", url, headers=headers, params=querystring)
except ConnectionError:
   print("İnternet bağlantınızı Kontrol edin.")
   exit(1)
except Exception:
   print("Hata lütfen daha sonra tekrar deneyiniz!")
sarkilar = json.loads(response.text);
idler = []
i=0
while(i != len(sarkilar["result"]["songs"])):
   print("["+str(i)+"]",sarkilar["result"]["songs"][i]["name"])
   idler.append(sarkilar["result"]["songs"][i]["id"])
   i+=1
print(len(sarkilar["result"]["songs"]),"adet şarkı bulundu");
index = int(input("Şarkı seçiniz : "))

sarkiAdi =  sarkilar["result"]["songs"][index]["name"]
print("Seçilen Şarkı : "+sarkiAdi)
print("indirme işlemi başladı ...")

url = "https://youtube-music1.p.rapidapi.com/get_download_url"
querystring = {"id":idler[index],"ext":"mp3"}
try:
   response = requests.request("GET", url, headers=headers, params=querystring)
except ConnectionError:
   print("İnternet bağlantınızı Kontrol edin.")
   exit(1)
except Exception:
   print("Hata lütfen daha sonra tekrar deneyiniz!")
veri = json.loads(response.text);
response = requests.get(veri["result"]["download_url"])
open(sarkiAdi+".mp3","wb").write(response.content);
shutil.move(sarkiAdi+".mp3","C:/Users/Barış TAŞ/Desktop/Yedek/Müzikler")
print("İndirme işlemi tamamlandı!")  
time.sleep(2);

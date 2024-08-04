import requests
from bs4 import BeautifulSoup

class KriptoKazıyıcı:
    def __init__(self, url, basliklar=None):
        self.url = url
        self.basliklar = basliklar if basliklar else {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }
        self.soup = None

    def icerigi_getir(self):
        try:
            yanit = requests.get(self.url, headers=self.basliklar)
            yanit.raise_for_status()  
            self.soup = BeautifulSoup(yanit.content, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"{self.url} adresinden içerik getirilemedi: {e}")
            self.soup = None

    def kripto_basliklari_al(self):
        if self.soup:
            basliklar = self.soup.find_all("tbody", {"tbody-type-default"})
            return [baslik.text for baslik in basliklar]
        else:
            print("İçerik henüz yüklenmedi. Önce icerigi_getir() metodunu çağırın.")
            return []

    def kripto_basliklari_yazdir(self):
        basliklar = self.kripto_basliklari_al()
        for baslik in basliklar:
            print(baslik)


url = "https://finans.mynet.com/kripto-para/"
kaziyici = KriptoKazıyıcı(url)
kaziyici.icerigi_getir()
kaziyici.kripto_basliklari_yazdir()

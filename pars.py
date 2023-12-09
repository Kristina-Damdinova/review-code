import requests
from bs4 import BeautifulSoup
from db import DataAccessObject

class Parser:
    data_dresses = DataAccessObject()
    def GetDataDress(self, url, headers):
        req_dress = requests.get(url, headers)
        src_dress = req_dress.text
        soup_dress = BeautifulSoup(src_dress, "lxml")

        picture = soup_dress.find("img", class_="img-fluid img-gallery-mobile img-resize img-big popular-slide-img intrinsic-item").get("src")
        model = soup_dress.find("span", class_="d-md-none page-header mb-4 mt-3 mt-md-1 text-lowercase break-word")
        model = model.get_text(strip=True)
        price = soup_dress.find("div", class_="product-price static product-price-without-sale d-inline-block").text.strip()
        description = soup_dress.find("div", class_="subtext pt-3").find("p").text
        self.data_dresses.add_information(model, price, description, url, picture)
    def GetData(self, url):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'Accept-Language': 'ru',
        }

        req = requests.get(url, headers)

        src = req.text

        soup = BeautifulSoup(src, "lxml")
        dress_cards = soup.find_all("div", class_="col-6 col-sm-4 col-lg-3 mb-4")

        dress_urls = []

        # записываю url страничек с платьями
        for div in dress_cards:
            url ="https://vikisews.com" + div.find("a", class_ = "ml-0 position-relative fast-purchase").get("href")
            dress_urls.append(url)
        # иду по страничкам с платьями и считываю нужную инфу
        for url_dress in dress_urls:
            self.GetDataDress(url_dress, headers)

    def __init__(self):
        for i in range(1,4):# все страницы: range(1,45)
            self.GetData('https://vikisews.com/vykrojki/platja-i-sarafany/?page=' + str(i) +'&page_size=4&')
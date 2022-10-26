from bs4 import BeautifulSoup
import requests
import sendText.text


def getHtml(URL):
    data = requests.get(URL).content
    return data


def parseData(classname, URL):
    data = getHtml(URL)
    soup = BeautifulSoup(data, 'html.parser')
    results = soup.find(class_=classname).text
    return results


def checkStatus(classname, URL):
    results = parseData(classname, URL)
    if results.strip() != "SOLD OUT at Columbus Store":
        print("sold out")
        # sendText.text.sendText("BUY NOW!!!!!")
    else:
        print("Sold")
        # sendText.text.sendText("Still sold out :/")


checkStatus("inventory",
            "https://www.microcenter.com/product/621439/raspberry-pi-4-model-b---2gb-ddr4?storeid=141")

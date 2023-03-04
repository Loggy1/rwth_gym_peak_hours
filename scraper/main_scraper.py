import http.client
from globals import *


def scrape():
    # Get image from rwth
    # Image only available with referer
    conn = http.client.HTTPSConnection("buchung.hsz.rwth-aachen.de")
    payload = ''
    headers = {
    'authority': 'buchung.hsz.rwth-aachen.de',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Auslastung.html',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    conn.request("GET", "/cgi/studio.cgi?size=30", payload, headers)
    res = conn.getresponse()
    data = res.read()

    # Write bytes to file as an image
    with open(path + "/scraper" + "/images/my_file.png", "wb") as binary_file:
        binary_file.write(data)

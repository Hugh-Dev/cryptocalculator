# -*- coding:utf-8 -*-

"""
▌ ▌      ▌        ▐  ▌
▙▄▌▌ ▌▞▀▌▛▀▖▛▀▖▌ ▌▜▀ ▛▀▖▞▀▖▛▀▖▞▀▖▞▀▖▙▀▖
▌ ▌▌ ▌▚▄▌▌ ▌▙▄▘▚▄▌▐ ▖▌ ▌▌ ▌▌ ▌▛▀ ▛▀ ▌
▘ ▘▝▀▘▗▄▘▘ ▘▌  ▗▄▘ ▀ ▘ ▘▝▀ ▘ ▘▝▀▘▝▀▘▘   2017"""

from flask import Flask, request, render_template, url_for
from bs4 import BeautifulSoup
import requests

"""
Hughpythoneer
@author Hugo Ramírez
@copyright Hughpythoneer
@cto Hughpythoneer
@date 16-12-2017
@version 2.0.0
"""

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('template.index.html')
    else:
        return render_template('template.400.html')

# bitcoin coinzoeken
@app.route("/Bitcoin", methods=['GET', 'POST'])
def Bitcoin():
    if request.method == 'POST':
        btc = request.form['Bitcoin']
        url = "www.worldcoinindex.com"
        r  = requests.get("https://" +url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        class_btc_all = soup.find_all("tr", class_="bitcoin coinzoeken")
        for i, class_btc in enumerate(class_btc_all):
            value_btc = class_btc.find('span', {'class': 'span'}).getText()
            name_btc = class_btc.get('data-naam')
        search = ','
        replace = '.'
        f = value_btc.replace(search, replace)
        n = f.encode('utf-8')
        ibtc = float(btc)
        fbtc = float(n)
        coinresult = fbtc * ibtc
        return render_template('template.index.html', btc =  coinresult, name_btc = name_btc)

# ethereum coinzoeken
@app.route("/Ethereum", methods=['GET', 'POST'])
def Ethereum():
    if request.method == 'POST':
        eth = request.form['Ethereum']
        url = "www.worldcoinindex.com"
        r  = requests.get("https://" +url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        class_eth_all = soup.find_all("tr", class_="ethereum coinzoeken")
        for i, class_eth in enumerate(class_eth_all):
            value_eth = class_eth.find('span', {'class': 'span'}).getText()
            name_eth = class_eth.get('data-naam')
        search = ','
        replace = '.'
        f = value_eth.replace(search, replace)
        n = f.encode('utf-8')
        ieth = float(eth)
        feth = float(n)
        coinresult = feth * ieth
        return render_template('template.index.html', eth =  coinresult, name_eth = name_eth)

# dash coinzoeken
@app.route("/Dash", methods=['GET', 'POST'])
def Dash():
    if request.method == 'POST':
        dash = request.form['Dash']
        url = "www.worldcoinindex.com"
        r  = requests.get("https://" +url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        class_dash_all = soup.find_all("tr", class_="dash coinzoeken")
        for i, class_dash in enumerate(class_dash_all):
            value_dash = class_dash.find('span', {'class': 'span'}).getText()
            name_dash = class_dash.get('data-naam')
        search = ','
        replace = '.'
        f = value_dash.replace(search, replace)
        n = f.encode('utf-8')
        idash = float(dash)
        fdash = float(n)
        coinresult = fdash * idash
        return render_template('template.index.html', dash =  coinresult, name_dash = name_dash )

# zcash coinzoeken
@app.route("/zcash", methods=['GET', 'POST'])
def zcash():
    if request.method == 'POST':
        zcash = request.form['Zcash']
        url = "www.worldcoinindex.com"
        r  = requests.get("https://" +url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        class_zec_all = soup.find_all("tr", class_="zcash coinzoeken")
        for i, class_zec in enumerate(class_zec_all):
            value_zec = class_zec.find('span', {'class': 'span'}).getText()
            name_zec = class_zec.get('data-naam')
        search = ','
        replace = '.'
        f = value_zec.replace(search, replace)
        n = f.encode('utf-8')
        izcash = float(zcash)
        fzcash = float(n)
        coinresult = fzcash * izcash
        return render_template('template.index.html', zec = coinresult, name_zec = name_zec)

# monero coinzoeken
@app.route("/monero", methods=['POST'])
def monero():
    monero = request.form['monero']
    url = "www.worldcoinindex.com"
    r  = requests.get("https://" +url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    class_xmr_all = soup.find_all("tr", class_="monero coinzoeken")
    for i, class_xmr in enumerate(class_xmr_all):
        value_xmr = class_xmr.find('span', {'class': 'span'}).getText()
        name_xmr = class_xmr.get('data-naam')
    search = ','
    replace = '.'
    f = value_xmr.replace(search, replace)
    n = f.encode('utf-8')
    imonero = float(monero)
    fmonero = float(n)
    coinresult = fmonero * imonero
    return render_template('template.index.html', xmr =  coinresult, name_xmr = name_xmr)

#litecoin coinzoeken
@app.route("/litecoin", methods=['POST'])
def litecoin():
    litecoin = request.form['litecoin']
    url = "www.worldcoinindex.com"
    r  = requests.get("https://" +url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    class_ltc_all = soup.find_all("tr", class_="litecoin coinzoeken")
    for i, class_ltc in enumerate(class_ltc_all):
        value_ltc = class_ltc.find('span', {'class': 'span'}).getText()
        name_ltc = class_ltc.get('data-naam')
    search = ','
    replace = '.'
    f = value_ltc.replace(search, replace)
    n = f.encode('utf-8')
    ilitecoin = float(litecoin)
    flitecoin = float(n)
    coinresult = flitecoin * ilitecoin
    return render_template('template.index.html', ltc =  coinresult, name_ltc = name_ltc)

if __name__ == "__main__":
    app.run(port=5000, debug = True)

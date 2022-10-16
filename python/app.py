from flask import Flask, render_template, request, jsonify
import numpy as np
from joblib import load
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlparse
from nltk.sentiment.vader import SentimentIntensityAnalyzer


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    t = request.form['reviewOne']
    text1 = [t]

    t2 = request.form['reviewTwo']
    text2 = [t2]

    t3 = request.form['reviewThree']
    text3 = [t3]

    t4 = request.form['reviewFour']
    text4 = [t4]

    t5 = request.form['reviewFive']
    text5 = [t5]

    t6 = request.form['reviewSix']
    text6 = [t6]

    t7 = request.form['reviewSeven']
    text7 = [t7]

    t8 = request.form['reviewEight']
    text8 = [t8]

    t9 = request.form['reviewNine']
    text9 = [t9]

    t10 = request.form['reviewTen']
    text10 = [t10]

    pipeline = load("ModelSVMNew.joblib")

    pred1 = pipeline.predict(text1)
    pred2 = pipeline.predict(text2)
    pred3 = pipeline.predict(text3)
    pred4 = pipeline.predict(text4)
    pred5 = pipeline.predict(text5)
    pred6 = pipeline.predict(text6)
    pred7 = pipeline.predict(text7)
    pred8 = pipeline.predict(text8)
    pred9 = pipeline.predict(text9)
    pred10 = pipeline.predict(text10)

    sid = SentimentIntensityAnalyzer()
    sentiment1 = sid.polarity_scores(str(text1))
    sentiment2 = sid.polarity_scores(str(text2))
    sentiment3 = sid.polarity_scores(str(text3))
    sentiment4 = sid.polarity_scores(str(text4))
    sentiment5 = sid.polarity_scores(str(text5))
    sentiment6 = sid.polarity_scores(str(text6))
    sentiment7 = sid.polarity_scores(str(text7))
    sentiment8 = sid.polarity_scores(str(text8))
    sentiment9 = sid.polarity_scores(str(text9))
    sentiment10 = sid.polarity_scores(str(text10))

    listPredictions = [str(pred1), str(pred2), str(pred3), str(pred4),
                       str(pred5), str(pred6), str(pred7), str(pred8), str(pred9), str(pred10)]

    listR = [text1, text2, text3, text4, text5,
             text6, text7, text8, text9, text10]

    listsent = [sentiment1, sentiment2, sentiment3, sentiment4, sentiment5, sentiment6,
                sentiment7, sentiment8, sentiment9, sentiment10]

    return render_template('predictions.html', list=listPredictions, dic=listR, sent=listsent)


@app.route('/scrap', methods=['POST'])
def scrap():
    try:
        address = request.form['reviewfield']
        headers = {
            'authority': 'www.amazon.com',
            'method': 'GET',
            'path': '/OtterBox-Commuter-Case-iPhone-Packaging/dp/B07GBH6HRS/?_encoding=UTF8&pf_rd_p=ecfa29a9-8628-4653-941e-c73229e73558&pd_rd_wg=tc8JF&pf_rd_r=04NMBWM6P4R2GZ9ZH455&content-id=amzn1.sym.ecfa29a9-8628-4653-941e-c73229e73558&pd_rd_w=NfwV3&pd_rd_r=3dac34dc-fdbf-41e2-969b-35f97eb7d871',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'device-memory': '8',
            'downlink': '1.9',
            'dpr': '2',
            'ect': '4g',
            'referer': 'https://www.amazon.com/ref=navm_hdr_logo',
            'rtt': '250',
            'sec-ch-device-memory': '8',
            'sec-ch-dpr': '2',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-viewport-width': '1440',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
            'viewport-width': '1440'
        }

        html = requests.get(url=address, headers=headers)

        soup = BeautifulSoup(html.text, 'html.parser')

        output = soup.find_all(
            'span', {'class': 'review-text-sub-contents'})

        text1 = str(output[0].text)
        text2 = str(output[1].text)
        text3 = str(output[2].text)
        text4 = str(output[3].text)
        text5 = str(output[4].text)
        text6 = str(output[5].text)
        text7 = str(output[6].text)
        text8 = str(output[7].text)
        text9 = str(output[8].text)
        text10 = str(output[9].text)

        listReviews = [text1, text2, text3, text4,
                       text5, text6, text7, text8, text9, text10]

        return render_template('after.html', list=listReviews)
    except:
        return render_template('errorlog.html')


if __name__ == "__main__":
    app.run(port=3000, debug=True)

import sys
import requests
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from bs4 import BeautifulSoup
import urllib.request, urllib.error
import json

@respond_to('/help')
def help(message):
    message.reply('主要なニュース,流行りのゲーム,天気について答えることができるスクレイピングBotです')
    


@respond_to('主要|ニュース')
def news_reply(message):
    #yahooニュースをスクレイピング
    url = 'https://news.yahoo.co.jp/'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    #a要素を取得
    a_tag = soup.find_all('a',class_='sc-esjQYD kUrCjn')
    for title in a_tag:
        message.reply(title.text)
        message.send("ClickHere→"+title.get('href'))

@respond_to('流行り|ゲーム')
def game_reply(message):
    #Steamランキングをスクレイピング
    url  =  url = 'http://store.steampowered.com/search/?filter=topsellers&os=win'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    #span要素を取得
    span_tag = soup.select('.title')

    #ループをまわして配列にいれる
    for i in range(5):
        span_tag[i]
        #要素の文字列を取得
        span = span_tag[i].string
        messa = str(i+1) + '位' + span
        message.reply(messa)

def get_weather(city_number):
    url = "https://weather.tsukumijima.net/api/forecast/city/%s" % city_number
    # URLアクセスして情報を取得する
    response = requests.get(url)
    response.raise_for_status()
    # 取得したjsonデータを読み込む
    weather_data = json.loads(response.text)
    return(weather_data)

@respond_to('今日の天気は？')
def d_know(message):
    message.reply('位置情報がわからないから〇〇の天気は？みたいに地名を入れてね')
    message.send('ちなみに対応している地名は【東京,大阪,横浜,名古屋,札幌,神戸,京都,福岡,さいたま】だよ！')
@respond_to('東京の天気は？')
def tokyo_w(message):
    w = get_weather(130010)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

@respond_to('横浜の天気は？')
def yokohama_w(message):
    w = get_weather(140010)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

@respond_to('大阪の天気は？')
def osaka_w(message):
    w = get_weather(270000)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

@respond_to('名古屋の天気は？')
def nagoya_w(message):
    w = get_weather(230010)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

@respond_to('札幌の天気は？')
def sapporo_w(message):
    w = get_weather(16010)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

@respond_to('神戸の天気は？')
def kobe_w(message):
    w = get_weather(280010)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

@respond_to('京都の天気は？')
def kyoto_w(message):
    w = get_weather(260010)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

@respond_to('福岡の天気は？')
def hukuoka_w(message):
    w = get_weather(400010)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

@respond_to('さいたまの天気は？|埼玉の天気は？')
def saitama_w(message):
    w = get_weather(110010)
    t = w['forecasts'][0]
    message.reply(t['telop']+"だよ！")

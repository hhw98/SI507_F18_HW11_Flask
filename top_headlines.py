from flask import Flask, request,g, render_template
from secrets_example import *
import requests
import datetime

app = Flask(__name__)

@app.route("/")
def welcome():
    return '<h1>Welcome!</h1>'


@app.route('/user/<nm>')
def find_top_technology(nm):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + 'technology' + '.json'
    params={'api-key':api_key}
    story_list_json = requests.get(extendedurl, params).json()
    results = story_list_json['results']
    headlines = []
    #for r in results:
    for i in range(5):
        headlines.append(results[i]['title'])
    now = datetime.datetime.now()
    today12pm = now.replace(hour=12, minute=0, second=0, microsecond=0)
    today16pm = now.replace(hour=16, minute=0, second=0, microsecond=0)
    today20pm = now.replace(hour=20, minute=0, second=0, microsecond=0)
    if (now <= today12pm):
        gt = 'Good morning'
    elif (now <= today16pm):
        gt = 'Good afternoon'
    elif (now<=today20pm):
        gt = 'Good evening'
    else:
        gt = 'Good night'
    return render_template('user.html',greeting=gt, name=nm, my_list=headlines)

@app.route('/user/<nm>/<hd>')
def find_top_header(nm,hd):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + hd + '.json'
    params={'api-key':api_key}
    story_list_json = requests.get(extendedurl, params).json()
    results = story_list_json['results']
    headlines = []
    #for r in results:
    for i in range(5):
        #headlines.append(results[i]['title'])
        headlines.append(results[i]['title']+'('+results[i]['url']+')')
    return render_template('ec1.html',name=nm, header = hd, my_list=headlines)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY'
    response = requests.get(url)
    articles = response.json()['articles']
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run()

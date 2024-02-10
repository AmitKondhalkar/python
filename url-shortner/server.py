from flask import Flask, request, redirect
import random

app = Flask(__name__)

letters = 'asdasd12323vsdfer23esaaqs'
shortened_length = 8
url_mappings  = {}

@app.post('/shorten')
def create_new_short_url():
    global shortened_length
    long_url = request.json['url']
    short_url = '/s/'

    for i in range(shortened_length):
        short_url += random.choice(letters)

    if short_url not in url_mappings:
        url_mappings[short_url] = long_url
        return short_url
    else:
        return 'Oh no!'

@app.get('/s/<id>')
def redirect_to_url(id):
    long_url = url_mappings.get(f'/s/{id}')
    if long_url:
        return redirect(long_url)
    else:
        return 'Not Found!'

if __name__ == '__main__':
    app.run(debug=True)
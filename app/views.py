from index import app
from flask import render_template, request
from query import get_bands
from config import BASE_URL


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = 'Live From The Fort'
    bands = get_bands()
    landing = True

    social = {
        'title': "Live From The Fort",
        'subtitle': "",
        'img': "",
        'description': "",
        'twitter_text': "",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        social=social,
        bands=bands,
        landing=landing,
        page_url=page_url)


@app.route('/<bandname>')
def band_page(bandname):
    bands = get_bands()
    for band in bands:
        if bandname == band['slug']:
            bands.remove(band)
            bands.insert(0, band)

    page_url = BASE_URL + request.path
    page_title = 'Live From The Fort: ' + bands[0]['bandname']

    social = {
        'title': "Live From The Fort",
        'subtitle': "",
        'img': "",
        'description': "",
        'twitter_text': "",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        social=social,
        bands=bands,
        page_url=page_url)

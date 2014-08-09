from index import app
from flask import render_template, request
from query import get_bands
from config import BASE_URL

bands = get_bands()

project_social = {
    'url': BASE_URL,
    'title': "Live From The Fort",
    'subtitle': "",
    'img': bands[0]['coverphoto'],
    'description': "'Live From The Fort' is an online video music series by Vermont Public Radio. The intimate performances, recorded at VPR studios in Colchester's historic Fort Ethan Allen, provide an opportunity to discover and explore the rich and diverse contemporary music scene Vermont.",
    'twitter_text': "Intimate performances by Vermont's own music makers.",
    'twitter_hashtag': "LiveFromTheFort"
}


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = 'Live From The Fort'
    landing = True

    social = project_social

    return render_template('content.html',
        page_title=page_title,
        social=social,
        bands=bands,
        landing=landing,
        project_social=project_social,
        page_url=page_url)


@app.route('/<bandname>')
def band_page(bandname):
    for band in bands:
        if 'slug' in band and bandname == band['slug']:
            bands.remove(band)
            bands.insert(0, band)

    page_url = BASE_URL + request.path
    page_title = 'Live From The Fort: ' + bands[0]['bandname']

    social = {
        'title': page_title,
        'subtitle': "Recorded at VPR Studios",
        'img': bands[0]['coverphoto'],
        'description': "In this month's installment of 'Live From The Fort' " +
        bands[0]['bandname'] + ' performs at historic Fort Ethan Allen',
        'twitter_text': bands[0]['bandname'] + " performs at VPR Studios",
        'twitter_hashtag': "LiveFromTheFort"
    }

    return render_template('content.html',
        page_title=page_title,
        social=social,
        bands=bands,
        project_social=project_social,
        page_url=page_url)

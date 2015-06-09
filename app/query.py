#!/usr/bin/python
from sheet import get_google_sheet
from slugify import slugify

def get_bands():
    sheet = get_google_sheet()
    band_list = []
    for i, band in enumerate(sheet):
        if band['youtubelink']:
            band['youtubelink'] = '%sembed/%s?rel=0&start=0' % tuple(
                band['youtubelink'].rsplit('watch?v='))
            band['slug'] = slugify(band['bandname'])
            band['bandmembers'] = [member for member in band['bandmembers'].split(';')
                if member]
            for j, member in enumerate(band['bandmembers']):
                member_list = member.split(',')
                band['bandmembers'][j] = {'name': member_list[0],
                    'instrument': member_list[1]}
            band['setlist'] = band['setlist'].split(';')
            band_list.insert(0, band)
        else:
            band_list.append(band)

    return band_list

#!/usr/bin/python
from google_spreadsheet.api import SpreadsheetAPI
from config import GOOGLE_SPREADSHEET
from slugify import slugify


def list_sheets():
    """The API sheet_key is not the same as the key in the URL. This function
    just prints out all sheet keys"""
    api = SpreadsheetAPI(GOOGLE_SPREADSHEET['USER'],
        GOOGLE_SPREADSHEET['PASSWORD'],
        GOOGLE_SPREADSHEET['SOURCE'])
    spreadsheets = api.list_spreadsheets()
    for sheet in spreadsheets:
        print sheet

def get_google_sheet(sheet_key=False, sheet_id='od6'):
    """Uses python_google_spreadsheet API to interact with sheet"""
    api = SpreadsheetAPI(GOOGLE_SPREADSHEET['USER'],
        GOOGLE_SPREADSHEET['PASSWORD'],
        GOOGLE_SPREADSHEET['SOURCE'])
    sheet = api.get_worksheet(sheet_key, sheet_id)
    sheet_object = sheet.get_rows()

    return sheet_object


def get_bands():
    """Takes google sheet object, modifies some fields, puts newest first"""
    sheet = get_google_sheet(GOOGLE_SPREADSHEET['KEY'])
    band_list = []
    for i, band in enumerate(sheet):
        if band['youtubelink']:
	    print band['youtubelink']
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

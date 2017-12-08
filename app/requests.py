import urllib.request
import json
from .models import Sources

# Getting the API KEY
api_key = None

# Getting the news base url
base_url = None


def configure_request(app):
    global api_key
    api_key = app.config['NEWS_API_KEY']


def get_sources(category):
    """Function to retrieve news sources list from the News api"""

    get_sources_url = 'https://newsapi.org/v2/sources'.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

import urllib.request
import json
from .models import Sources, Articles

# Getting the API KEY
api_key = None

# Getting the news base url
base_url = None


def configure_request(app):
    global api_key
    api_key = app.config['NEWS_API_KEY']


def get_sources(source):
    """Function to retrieve news sources list from the News api"""

    get_sources_url = 'https://newsapi.org/v1/sources'.format(source, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    """Function that process the results list and transforms them into a list of objects
    Args: sources_list: A list of dictionaries that contains news sources details

    Returns:
    sources_results: a list of news sources objects"""

    sources_results = []
    for source_item in sources_list:
        source_id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Sources(source_id, name, description, url, category, language, country)
        sources_results.append(source_object)

    return sources_results


def get_articles(source):
    """Function to retrieve news sources list from the News api"""

    # get_articles_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(
    #     source_id, api_key)
    get_articles_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(source, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
    return articles_results


def process_articles_results(articles_list):
    """Function that process the results list and transforms them into a list of objects
    Args: articles_list: A list of dictionaries that contains news articles and links

    Returns:
    articles_results: a list of news articles objects"""

    articles_results = []
    for article_item in articles_list:
        source_id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')
        date = article_item.get('publishedAt')

        article_object = Articles(source_id, author, title, description, urlToImage, url, date)
        articles_results.append(article_object)
    return articles_results

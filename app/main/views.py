from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""
    title = 'Home- Welcome to the best News source page'
    # Getting the news sources
    news_sources = get_sources('sources')
    return render_template('index.html', title=title, sources=news_sources)


@main.route('/articles/<id>')
def source(id):
    """View for top story articles"""
    articles = get_articles('articles')
    id = get_articles(id)
    return render_template('articles.html', articles=articles)

from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles_general


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""
    title = 'Home- Welcome to the best News source page'
    # Getting the news sources
    news_sources = get_sources('sources')
    return render_template('index.html', title=title, sources=news_sources)


@main.route('/news/<category>')
def general(category):
    """View for top story articles"""
    general_articles = get_articles_general('articles')
    return render_template('general.html', articles=general_articles)

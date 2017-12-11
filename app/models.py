class Sources:
    """Sources class to define the news source object"""

    def __init__(self, source_id, name, description, url, category, language, country):
        self.source_id = source_id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Articles:
    """Articles class to define the articles object"""

    def __init__(self, source_id, author, title, description, urlToImage, url, date):

        self.source_id = source_id
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.date = date

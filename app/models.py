class Sources:
    """Sources class to define the news source object"""

    def __init__(self, name, description, link, category, country):
        self.name = name
        self.description = description
        self.link = 'Go to page' + link
        self.category = category
        self.country = country


# class Articles:

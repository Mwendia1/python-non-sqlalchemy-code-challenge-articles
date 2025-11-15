class Author:

    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name is not None:
            return
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) == 0:
            raise Exception("Name must not be empty")
        self._name = value

    def articles(self):
        from .article import Article
        return [a for a in Article.all if a.author == self]

    
    def magazines(self):
        return list({a.magazine for a in self.articles()})

   
    def add_article(self, magazine, title):
        from .article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if len(mags) == 0:
            return None
        return list({m.category for m in mags})

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Name length must be 2–16 chars")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value) == 0:
            raise Exception("Category cannot be empty")
        self._category = value

    def articles(self):
        from .article import Article
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if len(arts) == 0:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        authors = self.contributors()
        result = []
        for author in authors:
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                result.append(author)
        return result if result else None

    @classmethod
    def top_publisher(cls):
        from .article import Article
        if len(Article.all) == 0:
            return None
        return max(cls.all, key=lambda m: len(m.articles()))

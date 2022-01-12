class Book:
    def __init__(self, id, title, author, publication_date):
        self.id = id
        self.title = title
        self.author = author
        self.publication_date = publication_date

    def __str__(self):
        return "{} by {}, published at: {}".format(self.title, self.author, self.publication_date)

    
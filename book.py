class Book:
    def __init__(self, topic, title, author, publication_date):
        self.topic = topic
        self.title = title
        self.author = author
        self.publication_date = publication_date

    def get_title(self):
        return self.title

    def __str__(self):
        return "{}: {} by {}, published at: {}".format(self.topic, self.title, self.author, self.publication_date)

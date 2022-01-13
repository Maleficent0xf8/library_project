class Bookshelf:
    def __init__(self, topic):
        self.topic = topic
        self.shelf = dict()

    def insert_book(self, book):
        if not self.has_book(book.get_title()):
            self.shelf[self.generate_id(book.get_title())] = book

    def fetch_book(self, title):
        if self.has_book(title):
            return self.shelf[self.generate_id(title)]

    def delete_book(self, title):
        if self.has_book(title):
            self.shelf.pop(self.generate_id(title))

    def has_book(self, title):
        return self.generate_id(title) in self.shelf

    def generate_id(self, title):
        return "{}:{}".format(self.topic, title)

    def __str__(self):
        return "\n".join(self.shelf.keys())
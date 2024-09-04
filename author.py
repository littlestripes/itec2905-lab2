class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'


def main():
    tpynchon = Author('Thomas Pynchon')
    tpynchon.publish('The Crying of Lot 49')
    tpynchon.publish('Gravity\'s Rainbow')

    egoldman = Author('Emma Goldman')
    egoldman.publish('Living My Life')

    print(tpynchon)
    print(egoldman)


if __name__ == '__main__':
    main()

from random import randint

class Book:

    def __init__(self, name: str, genre: str, year: int, author: str, rating: float):
        self.name = name
        self.genre = genre
        self.year = year
        self.author = author
        self._rating = rating
        self.__ISBN = randint(100000000000000, 1000000000000000)

    def read(self):
        print(f"Someone is reading {self.name} of genre: {self.genre}")


class ComedyBook(Book):
    def __init__(self, name: str, genre: str, year: int, author: str, rating: float, comedy_genre: str):
        super().__init__(name, genre, year, author, rating)
        self.comedy_genre = comedy_genre

    def __str__(self):
        return f"name: {self.name}, genre: {self.genre}, year: {self.year}, author: {self.author}, rating: {self._rating}," \
               f" comedy_genre: {self.comedy_genre}"
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating: float):
        if 0 <= rating <= 10:
            self._rating = rating
        else:
            print("Invalid Rating Number")


buki = ComedyBook("jafara", 'kai kacoba', 2000, "gaurga", 4.6, "Jigarsona")
print(buki._rating)
buki.rating = 10
print(buki._rating)



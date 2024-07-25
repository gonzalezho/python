class Movie:
    def __init__(self, name: str, year: int) -> None:
        self.name = name
        self.year = year


if __name__ == "__main__":
    matrix = Movie("The Matrix", 2023)
    print(matrix.name)
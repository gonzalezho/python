from typing import List

# Link: https://www.geeksforgeeks.org/dunder-magic-methods-python/
# Link: https://mathspp.com/blog/pydonts/dunder-methods
class Garage:
    def __init__(self) -> None:
        self.cars: List[str] = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index: int) -> str:
        return self.cars[index]
    
    def __repr__(self) -> str:
        return f"<Garage {self.cars}>"
    
    def __str__(self) -> str:
        return f"Garage with {len(self)} cars"
    

if __name__ == "__main__":
    ford = Garage()
    ford.cars.append("Fiesta")
    ford.cars.append("Focus")
    print(ford)

    # g1 = Garage.__getitem__(ford, 1)
    # print(g1)

    # g2 = Garage.__repr__(ford)
    # print(g2)
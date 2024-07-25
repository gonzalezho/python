from typing import List

# Link: https://www.geeksforgeeks.org/dunder-magic-methods-python/
class Garage:
    def __init__(self) -> None:
        self.cars: List[str] = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index: int) -> str:
        return self.cars[index]
    

if __name__ == "__main__":
    ford = Garage()
    ford.cars.append("Fiesta")
    ford.cars.append("Focus")

    res = Garage.__getitem__(ford, 1)
    print(res)
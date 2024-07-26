from typing import List

class FixedFloat:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __repr__(self) -> str:
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, value1: float, value2: float) -> 'FixedFloat':
        return cls(value1 + value2)

    @staticmethod
    def is_positive(value: float) -> bool:
        return value > 0

class Euro(FixedFloat):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self) -> str:
        return f"<Euro {self.symbol}{self.amount:.2f}>"

    @classmethod
    def from_sum(cls, value1: float, value2: float) -> 'Euro':
        return cls(value1 + value2)

    @staticmethod
    def is_positive(value: float) -> bool:
        return value > 0

if __name__ == "__main__":
    n = FixedFloat(18.567)
    new_n = FixedFloat.from_sum(19.843, 0.789)
    print(n)              
    print(new_n)         

    e = Euro(15.23)
    new_e = Euro.from_sum(10.12, 5.67)
    print(e)              

    print(FixedFloat.is_positive(-5))  
    print(Euro.is_positive(10))        
    print(Euro.is_positive(-5))       

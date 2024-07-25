from typing import List

class Student:
    def __init__(self, name: str, grades: List[int]) -> None:
        self.name = name
        self.grades = grades

    def average(self) -> float:
        if not self.grades:  
            return 0.0
        return sum(self.grades) / len(self.grades)

if __name__ == "__main__":
    student_one = Student("Fido Dido", [70, 88, 90, 99])
    print(student_one.average()) 

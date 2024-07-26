from typing import List

class Student:
    def __init__(self, name: str, school: str) -> None:
        self.name = name
        self.school = school
        self.marks: List[int] = []

    def average(self) -> float:
        if not self.marks:  
            return 0.0
        return sum(self.marks) / len(self.marks)
    
    def __str__(self):
        return f"{self.name} from {self.school}"
    

class WorkingStudent(Student):
    def __init__(self, name: str, school: str, salary: float ) -> None:
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self) -> float:
        if self.salary <= 0:  
            return 0.0
        return self.salary * 37.5

if __name__ == "__main__":
    fido = WorkingStudent("Fido Dido", "MIT", 15.50)
    print(fido.salary)
    fido.marks.append(57)
    fido.marks.append(99)
    print(fido.average())
    print(fido.weekly_salary())

    fideo = WorkingStudent("Fideo", "Oxford", -1)
    print(fideo.weekly_salary())

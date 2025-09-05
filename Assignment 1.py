# Classe base
class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
    
    def info(self):
        return f"Subject: {self.name}, Teacher: {self.teacher}"

# Classe derivada (herança)
class Quimestre(Subject):
    def __init__(self, name, teacher, grade):
        super().__init__(name, teacher)
        self.grade = grade
    
    def set_grade(self, grade):
        self.grade = grade
    
    def status(self):
        if self.grade >= 10:
            return f"{self.name}: Passed ✅ (Grade: {self.grade})"
        else:
            return f"{self.name}: Failed ❌ (Grade: {self.grade})"

# Criando objetos
math = Quimestre("Mathematics", "Mr. John", 12)
physics = Quimestre("Physics", "Ms. Anna", 8)

print(math.info())     # Subject: Mathematics, Teacher: Mr. Boca
print(math.status())   # Mathematics: Passed ✅ (Grade: 12)

print(physics.info())  # Subject: Physics, Teacher: Ms. Claudia
print(physics.status())# Physics: Failed ❌ (Grade: 8)

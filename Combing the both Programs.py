# Base class
class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
    
    def info(self):
        return f"Subject: {self.name}, Teacher: {self.teacher}"
    
    def exam(self):
        return f"{self.name}: General exam 📝"

# Derived class with grades
class Quimestre(Subject):
    def __init__(self, name, teacher, grade):
        super().__init__(name, teacher)
        self.grade = grade
    
    def status(self):
        return f"{self.name}: {'Passed ✅' if self.grade >= 10 else 'Failed ❌'} (Grade: {self.grade})"

# Polymorphism: different subjects override exam()
class Math(Quimestre):
    def exam(self):
        return "Math Exam ➗: Solve equations and problems"

class Physics(Quimestre):
    def exam(self):
        return "Physics Exam ⚡: Perform experiments and calculations"

class English(Quimestre):
    def exam(self):
        return "English Exam 📖: Write essays and comprehension"

# Create objects
subjects = [
    Math("Mathematics", "Mr. Boca", 12),
    Physics("Physics", "Ms. Claudia", 8),
    English("English", "Mrs. Ilidio", 15)
]

# Demonstration
for subj in subjects:
    print(subj.info())
    print(subj.exam())   # Polymorphism in action
    print(subj.status())
    print("-" * 40)

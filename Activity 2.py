class Exam:
    def result(self):
        return "Result not available"

class MathExam(Exam):
    def result(self):
        return "Math Exam: Complex Calculations ➗"

class PhysicsExam(Exam):
    def result(self):
        return "Physics Exam: Experiments ⚡"

class EnglishExam(Exam):
    def result(self):
        return "English Exam: Essays 📖"

# Polimorfismo em ação
exams = [MathExam(), PhysicsExam(), EnglishExam()]

for e in exams:
    print(e.result())

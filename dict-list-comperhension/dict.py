from random import randint
names = ['Alex', 'Andrei', 'Mihai', 'Mihnea', 'Cosmin']
scores = {student:randint(0, 100) for student in names}
passed = {student:grade for (student, grade) in scores.items() if grade > 50}
print(passed)
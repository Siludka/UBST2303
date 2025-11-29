groupmates = [
    {
        "name": "Матвей",
        "surname": "Лебедев",
        "exams": ["Информатика", "ЭиПС", "Web"],
        "marks": [5, 3, 3]
    },
    {
        "name": "Маргарита",
        "surname": "Андреева",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Иван",
        "surname": "Гусев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Эдгар",
        "surname": "Князев",
        "exams": ["Информатика", "ЭиПС", "Web"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Станислав",
        "surname": "Мылин",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    }
]

try:
    min_avg = float(input("Введите минимальный средний балл для фильтрации: "))
except ValueError:
    print("Ошибка: введите число!")
    exit()

print(f"\nСтуденты со средним баллом выше {min_avg}:\n")
print("-" * 60)

found = False

for student in groupmates:
    avg_mark = sum(student["marks"]) / len(student["marks"])
    
    if avg_mark > min_avg:
        found = True
        print(f"Имя:          {student['name']}")
        print(f"Фамилия:      {student['surname']}")
        print(f"Экзамены:     {', '.join(student['exams'])}")
        print(f"Оценки:       {student['marks']}")
        print(f"Средний балл: {avg_mark:.2f}")
        print("-" * 60)

if not found:
    print("Таких студентов нет. Попробуйте уменьшить порог.")

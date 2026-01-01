students = [("Ali", ["fizika", "matematika"]), ("Laylo", ["ingliz tili"]), ("Jasur", ["matematika", "informatika"])]

fan = input("Fan: ")
soni = 0

for student in students:
    if fan in student[1]:
        soni += 1
        
print(soni)
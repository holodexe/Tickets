print("Введите кол-во билетов: \n")

ticket = input()
ticket = int(ticket)

age_list = []
sum = 0

print("Введите возраст каждого посетителя: \n")
for i in range(ticket):
    print(f"Посетитель номер {i + 1} \n")
    age = input()
    age = int(age)
    age_list.append(age)

for i in age_list:
    if i > 18 and i <= 25:
        sum += 990
    elif i > 25:
        sum += 1390

if ticket > 3:
    sum = sum * 0.9

print("")
print(sum)
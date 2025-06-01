1. 
text = 'Hello, Python World!'
print(text)

2.
a = int(input('first number: '))
b = int(input('second number: '))
print('сума:', a + b)
print('різниця:', a - b)
print('ділення:', a / b if b != 0  else 'ділення на нуль неможливо')
print('добуток:', a * b)

3.
str1 = "Happy"
str2 = " Birthday"
res = str1 + str2
print("отриманий рядок:", res)
print("довжина рядка:", len(res))

4. 
num = int(input("напишіть число: "))
if num % 2 ==0:
    print("парне")
else:
    print("непарне")

5. 
for i in range(1, 11):
    print(i)

6. 
num = int(input("напишіть число: "))
if num > 0:
    print("позитивний")
elif num < 0:
    print("негативний")
else:
    print("нуль")

7.
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

8. 
n = int(input("введіть n: " ))
total = 0
for i in range(1, n + 1):
    total += i
print("сума чисел від 1 до", n, "дорівнює", total)

9. 
for i in range (10, 0, -1):
    print(i)

10. 
for i in range(1, 11):
    if i == 5:
        continue 
    if i == 7:
        break
    print(i)

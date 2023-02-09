# Questão 7

soma = 0

a = int(input('Digite o começo do intervalo: '))
b = int(input('Digite o fim do intervalo: '))

while a <= b:
    if a % 2 != 0:
        soma += a
    a += 1

for i in range(a, b+1):
    if i % 2 != 0:
        soma += i

print(soma)

# Questão 8

c = []

a = int(input('Digite o começo do intervalo: '))
b = int(input('Digite o fim do intervalo: '))

while a <= b:
    c.append(round((((a - 32) * 5) / 9), 2))
    a += 1

for i in range(a, b+1):
    c.append(round((((i - 32) * 5) / 9), 2))

print(c)

# Questão 9

x = 0
s = -1
num1 = 1
num5 = 5
n = int(input('Digite o n:'))

while x < n-1:
    s += num1
    x += 1
    if x < n-1:
        s += num5
        x += 1

for i in range(1, n, 2):
    s += num1
    if i < n-1:
        s += num5


print(s)

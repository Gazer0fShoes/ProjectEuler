total = 0
i = 1
j = 2

while j <= 4000000:
    total += j
    newi = i + j + j
    j = newi + i + j
    i = newi

print(total)
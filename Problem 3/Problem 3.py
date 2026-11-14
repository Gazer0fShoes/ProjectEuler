n = 600851475143
x = 1
isprime = True

while x < n:
    candidate = n / x
    if candidate % 1 == 0 and candidate % 2 != 0: # if candidate is a whole number and odd
        y = 1
        while y < candidate / 2:
            if candidate % y == 0:
                isprime = False
                break
            else:
                y += 1
                isprime = True 
            if isprime == True:
                print(candidate)
                break   
        y = 1
    x += 1
            
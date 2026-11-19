def isPalindrome(n):
    if str(n) == "".join(reversed(str(n))):
        return True
    return False

firstFactor, secondFactor = 999, 999
count = 999*999
lowerLimit = 100*100

while count >= lowerLimit:
    if isPalindrome(count):
        pass # find if its factors can be two three digit numbers.
    count -= 1
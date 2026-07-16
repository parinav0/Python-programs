n = 55
g = int(input("Guess the number which lies in 1-100 = "))

while g != n:
    if g < n:
        g = int(input("Too low, try again: "))
    else:
        g = int(input("Too high, try again: "))

print("You got it!")

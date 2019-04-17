# Print 1-255
def PrintOneTwoFiftyFive():
    for x in range(0,256):
        print(x)

# Write a program that would print all the odd numbers from 1 to 1000
def PrintOdds():
    for x in range(1,1001):
        if x % 2 == 1:
            print(x)
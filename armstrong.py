#An Armstrong number of three digits is an integer such that the sum of the
#cubes of its digits is equal to the number itself. For example, 371 is an
#Armstrong number since 3**3 + 7**3 + 1**3 = 371.
#Write a program to find all Armstrong number in the range of 0 and 999.

armstronglijst = []
count = 0

def lancefunctie(number):
    armstronglijst.append(str(number))
    return armstronglijst

for number in range(0, 1000):
    string = str(number)
    
    if len(string) == 3:
        if int(string[0]) ** 3 + int(string[1]) ** 3 + int(string[2]) **3 == number:
            lancefunctie(number)
            count += 1
    
    elif len(string) == 2:
        if int(string[0]) ** 3 + int(string[1]) ** 3 == number:
            lancefunctie(number)
            count += 1

    elif len(string) == 1:
        if int(string[0]) ** 3 == number:
            lancefunctie(number)
            count += 1
        

print(armstronglijst)             
print("Er zijn in totaal " + str(count) + " armstrong nummers tussen 0 en 1000."

    

#Opgave 1

lijst = []

def div_by_ten(nums):
    
    for number in nums:
        if number % 10 == 0:
            lijst.append(number)
            
    return lijst

def count(nums):
    
    div_by_ten(nums)
    
    return len(lijst)


print(count([20, 25, 30, 35, 40]))

#Opgave 2

def add_greetings(names):
    groet = []
    for name in names:
        groet.append("Hello, " + name)
    return groet

print(add_greetings(["Owen", "Max", "Sophie"]))

#Opgave 3

def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Opgave 4

def odd_indices(lst):
    odd = []
    for number in range(1, len(lst), 2):
        odd.append(lst[number])
    return odd
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Opgave 5

def exponents(bases, powers):
    new = []
    for base in bases:
        for power in powers:
            new.append(base ** power)
    return new

print(exponents([2, 3, 4], [1, 2, 3]))

#Opgave 6

def larger_sum(lst1, lst2):
    if sum(lst1) >= sum(lst2):
        return lst1
    else:
        return lst2
    
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Opgave 7

def over_nine_thousand(lst):
    total = 0
    for number in lst:
        while total < 9000:
            total += number
            break
    return total
print(over_nine_thousand([800, 4500, 3460, 240, 457, 300, 120, 50]))

#Opgave 8

#Makkelijke manier

def max_num(nums):
    return max(nums)

#Moeilijke manier

def max_num(nums):
    maximum = nums[0]
    for number in nums:
        if number > maximum:
            maximum = number
    return maximum

print(max_num([50, -10, 0, 75, 20]))

#Opgave 9

def same_values(lst1, lst2):
    index = []
    for number in range(len(lst1)):
        if lst1[number] == lst2[number]:
            index.append(number)
    return index

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Opgave 10

def reversed_list(lst1, lst2):
    for number in range(len(lst1)):
        if lst1[number] == lst2[len(lst1) - 1 - number]:
            continue
        else:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

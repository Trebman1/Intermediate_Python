#Made by Tyler Rebman
#Int checker method https://stackoverflow.com/questions/37472361/how-do-i-check-if-a-string-is-a-negative-number-before-passing-it-through-int
def sumOfList(list1):
    sum = 0
    for x in list1:
        sum += x
    return sum

def intChecker(string1):
    try:
        x = int(string1)
        return True
    except ValueError:
        print("Enter a valid int")
        return False

list1 = []
i = 0
while i < 5:
    string1 = input("Enter int #" + str(i+1) + ": ")
    if intChecker(string1) == True:
        list1.append(int(string1))
        i += 1
total = sumOfList(list1)
print(total)
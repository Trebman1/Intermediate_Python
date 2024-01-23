#Made by Tyler Rebman
#Used w3Schools python dictionary methods
def countLetter(string1):
    list1 = []
    dict1 = {}
    string1 = string1.lower()
    for x in string1:
        if list1.count(x) == 0 and x != ' ':
            list1.append(x)
            count = 0
            for y in string1:
                if x == y:
                    count += 1
            dict1.setdefault(x, count)     
    print(dict1)

string1 = input("Enter a String\n")
countLetter(string1)

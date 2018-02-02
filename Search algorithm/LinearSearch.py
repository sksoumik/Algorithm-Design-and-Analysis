# Linear Search | Time Complexity: O(n)
numberList = [4, 2, 8, 9, 3, 7]
x = int(input("Enter the number to search"))
found = False
for i in range(len(numberList)):
    if numberList[i] == x:
        found = True
        print("%d found at position %d" % (x, i))
        break
if found == False:
    print("%d is not found in the list" % x)



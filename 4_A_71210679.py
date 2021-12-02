Data = int(input("Input : "))
a = 2
print("Output : ")
for Row in range(1, Data+1):


    for Column in range(1, 2*Data):
    
        if Row + Column == Data + 1 or Column - Row == Data-1:
            print("*", end= "")
    
        elif Row == Data and Column != a:
            print("*", end= "")
            a = a + 2
    
        else:
            print(end= " ")

    print()
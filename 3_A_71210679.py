Data = input("Input : ")
Column = 0
Row = 0

print("Output : ")
while Row < len(Data):
    print(Data[0:Row])
    Row += 1 
while Column < len(Data):
    print(Data[0:len(Data)-Column])
    Column += 1
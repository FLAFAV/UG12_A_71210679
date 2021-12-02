Num = input("Masukkan deret angka: ")
Split = Num.split(",")
x = 0
y = " "

for a in Split:
    if int(a) % 2 == 0:
        Number = 0 + int(a)
    else:
        Number = 0 - int(a)
    x = x + Number
print("Total: ",end="")

for a in Split:
    if int(a) % 2 == 0:
        z = ("+" + str(a))
    else:
        z = ("-" + str(a))
    y = y + z

if y[1] == "+":
    print(z[2:len(y)])
else:
    print(y)
print("Hasil perhitungan di atas ialah: ",x)

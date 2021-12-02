People = []
Num = []

while True:
    Name = input("Masukkan nama: ")
    if Name == "STOP":
        break 
    else:
        Seat = (input("Masukkan nomor kursi" + " " + Name + ": "))

    if Seat in Num:
        print("Mohon maaf, kursi tersebut telah terisi")
    else:
        People.append(Name)
        Num.append(Seat)


print("\nList kursi yang telah terisi:")

for a in range(len(Num)):
    print("Kursi nomor" + " " + Num[a] + " telah terisi oleh" + " " + People[a])
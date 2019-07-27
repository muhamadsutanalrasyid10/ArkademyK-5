n = int(input("Masukkan angka ganjil\n"))
print()
t1 = int(n/2)
t2 = int(n-1)

for i in range(n):
    for j in range(n):
        if(i == t1 or j == 0 or j == t2):
            print("*",end = "")
        else:
            print("=",end = "")
    print()
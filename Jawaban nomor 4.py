kata = input("Masukkan sebuah kata : \n")

panjangkata = len(kata)
i = 0
hurufvokal = 0

while i < panjangkata:
    if(kata[i] == "a" or kata[i] == "A" or kata[i] == "i" or kata[i] == "I" or kata[i] == "u" or kata[i] == "U" or kata[i] == "e" or kata[i] == "E" or kata[i] == "o" or kata[i] == "O" ):
        hurufvokal += 1
    i+=1

print("Jumlah huruf hidup / vokal :",hurufvokal )


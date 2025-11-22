chuoi = input ("nhap chuoi: ")
tong = 0
for c in chuoi:
    if c.isdigit(): 
        tong += int(c)
print("tong cac chu so la: ",tong)
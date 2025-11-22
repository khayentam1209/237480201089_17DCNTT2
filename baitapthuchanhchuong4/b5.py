chuoi = input ("nhap chuoi: ")
hoa =0
thuong =0
so =0

for c in chuoi:
    if c.isupper():     #kí tự in hoa
        hoa += 1
    elif c.islower():   #kí tự in thường
        thuong += 1
    elif c.isdigit():   #kí tự in số
        so += 1

print(" so ky tu in hoa", hoa)
print(" so ky tu in thuong", thuong)
print(" so ky tu in so", so)
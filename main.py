import diskon_formula_for_main
print('diskon member adalah {}%'.format(diskon_formula_for_main.diskon_member))
print('diskon libur adalah {}%'.format(diskon_formula_for_main.diskon_libur))

# #cara biasa
# total_belanja=int(input("berapa total belanjaan Anda?:Rp"))
# member=input("Apakah Anda member kami?(YA/TIDAK): ")
# libur= input("Apakah hari ini libur?(YA/TIDAK): ")

# a,b=0,0
# if member=="YA":
#     a=diskon_formula_for_main.hitung_diskon_member(total_belanja)
# else:
#     a=0

# if libur=="YA":
#     b=diskon_formula_for_main.hitung_diskon_libur(total_belanja)
# else:
#     b=0

#lebih efisien
total_belanja=int(input("berapa total belanjaan Anda?:Rp"))
member=bool(int(input("Apakah Anda member kami?(1/0): ")))
libur= bool(int(input("Apakah hari ini libur?(1/0): ")))

a,b=0,0    
if member:
    a=diskon_formula_for_main.hitung_diskon_member(total_belanja)

if libur:
    b= diskon_formula_for_main.hitung_diskon_libur(total_belanja)

total_diskon=a+b
bayar = total_belanja-total_diskon
print("Anda mendapat diskon sebesar Rp", total_diskon, sep='')
print("Jumlah yang harus anda bayar adalah sebesar Rp",bayar, sep='')
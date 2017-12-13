x = 58
y = 0

while y !=x:
	x = int(input("Tebak suatu angka (1-100)?"))
	if x < 58 :
		print("Coba lagi terlalu rendah")
	elif x == 58 :
		print("Selamat Anda Benar")
	else :
		print("Coba lagi, terlalu tyinggi")
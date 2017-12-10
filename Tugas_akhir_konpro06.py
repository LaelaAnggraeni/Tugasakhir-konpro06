def option():
	print("---------------------------------------------------------")
	print("|	1.Perkalian 					|")
	print("|	2.Calender		 		    	|")
	print("|	3.Menghitung Upah karyawan perminggu    	|")
	print("|	4.Keluar    					|")
	print("---------------------------------------------------------\n")
	pilihan = int(input("Masukkan pilihan anda: "))
	print("")
	return pilihan
	
pilihan = True
while(pilihan<4):
	pilihan = option()
	if(pilihan==1):
		print("---------------------------------------------------------")
		num = int(input("Masukkan angka perkalian: ")) 
		print("---------------------------------------------------------")
		print("Tabel perkalian")
		for i in range(1,11):  
			print(num,'x',i,'=',num*i)
		print("---------------------------------------------------------\n")
	elif(pilihan==2):
		print("---------------------------------------------------------")
		import calendar 
		yy = int(input("Masukkan Tahun: ")) 
		mm = int(input("Masukkan Bulan: "))  
		print("---------------------------------------------------------")
		print(calendar.month(yy,mm))
		print("---------------------------------------------------------\n")
	elif(pilihan==3):
		print("Menghitung upah kerja karyawan perminggu")
		print("")
		nama = str(input("Nama Anda: "))
		jkerja = int(input("Masukan Jam Kerja: "))
		upahperjam = int(input("Upah Per Jam: Rp."))
		if(jkerja<=35):
			upahtotal = jkerja*upahperjam
		else:
			upahtotal = jkerja*upahperjam+35*upahperjam
		print("Upah kerja dalkam 1 minggu: Rp.",upahtotal)
		print("---------------------------------------------------------")
		print("Karyawan",nama,"menerima upah perminggu: Rp.",upahtotal)
		print("---------------------------------------------------------\n")
		
		
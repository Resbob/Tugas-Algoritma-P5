#Nilai Mahasigmanya ini
budi = [80, 70, 75]
andi = [60, 65, 62]
siti = [90, 85, 88]

#Untuk menghitung rata rata nilai mahasigma
rata_budi = sum(budi) / len(budi)
rata_andi = sum(andi) / len(andi)
rata_siti = sum(siti) / len(siti)

#mencari mahasigma terpintar
nama_terpintar = "Budi"
nilai_tertinggi = rata_budi

if rata_andi > nilai_tertinggi:
    nama_terpintar = "Andi"
    nilai_tertinggi = rata_andi

if rata_siti > nilai_tertinggi:
    nama_terpintar = "Siti"
    nilai_tertinggi = rata_siti


#Mencari rata rata nilai mata kuliah
mk1 = (budi[0] + andi[0] + siti[0]) / 3
mk2 = (budi[1] + andi[1] + siti[1]) / 3
mk3 = (budi[2] + andi[2] + siti[2]) / 3

#mencari mata kuliah yang nilainya terendah
mk_terendah = "MK1"
nilai_terendah = mk1

if mk2 < nilai_terendah:
    mk_terendah = "MK2"
    nilai_terendah = mk2

if mk3 < nilai_terendah:
    mk_terendah = "MK3"
    nilai_terendah = mk3


#ini Outputnya lek
print("Mahasiswa Terpintar :", nama_terpintar, "(Nilai :", round(nilai_tertinggi, 2), ")")
print("Mata kuliah Nilai Terkecil :", mk_terendah, "(Nilai :", round(nilai_terendah, 2), ")")
#Program sistem nilai akademik
# input nama dan nilai mahasiswa
nama=input("masukan nama mahasiswa :")
nilai=float(input("Masukan nilai akhir :"))
# menentukan kategori nilai
if nilai >=85:
    kategori="A"
elif nilai >=70:
     kategori="B"
elif nilai >=55:
     kategori="C"
elif nilai >=40:
     kategori="D"
else:
     kategori="E"

# Output hasil
print("==== HASIL PENILAIAN ===" )
print("Nama Mahasiswa :",nama)
print("Nilai Akhir    :",nilai)                    
print("Kategori Nilai :",kategori)

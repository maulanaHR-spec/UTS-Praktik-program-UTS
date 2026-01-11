print("=== PROGRAM KASIR INDOMARKET ===")
# Input jumlah barang
jumlah_barang=int(input("masukan jumlah jenis barang yang dibeli :"))
total_belanja=0

# proses input barang
for i in range(1,jumlah_barang+1):
    print(f"\nBarang ke-{i}")
    nama_barang=input("Nama barang :")
    harga=float(input("Harga satuan (Rp):"))
    jumlah=int(input("Jumlah beli :"))

    subtotal=harga*jumlah
    total_belanja+=subtotal
    print(f"Subtotal{nama_barang}:Rp.{subtotal:,.0f}")
# Tampilan total awal
print("\n-------------------------------------")
print(f"Total belanja sebelum diskon: Rp.{total_belanja:,.0f}")
# Diskon berdasarkan total belanja
if total_belanja>100.000:
    diskon=0.1*total_belanja
    print("Anda mendapatkan diskon 10%!")
else:
    diskon=0
    print("Belanja kurang dari Rp.100.000, tidak  mendapatkan diskon.")
# hitung total akir
total_akhir=total_belanja-diskon
# output struk
print("\n======= STRUK PEMBAYARAN =======")
print(f"Total Belanja : Rp.{total_belanja:,.0f}")
print(f"Total Diskon : Rp.{diskon:,.0f}")
print(f"Total Bayar : Rp.{total_akhir:,.0f}")
print("===================================")
# perulangan while simulasi pembayaran
while True:
    bayar=float(input("Masukan jumlah uang yang dibayar : Rp"))
    if bayar<total_akhir:
        print("Uang Kurang !!! Silahkan masukan jumlah uang yang cukup.")
    else:
        kembalian=bayar-total_akhir 
        print(f"kembalian: Rp.{kembalian:,.0f} ")
        print("\nTerima kasih telah berbelanja di Indomarket")
        break

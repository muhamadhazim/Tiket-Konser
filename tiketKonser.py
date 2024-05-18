def name_to_number(name):
    return sum(ord(char) for char in name)

def generate_kode_tiket(nomor_transaksi, kategori, nama_pengguna, iterasi):
    return f'T{nomor_transaksi}CAT{kategori}B{name_to_number(nama_pengguna)}{iterasi}'

def beli_tiket(stok_tiket, daftar_kode_tiket, stok_per_kategori, nomor_transaksi, kode_bayar, line_kode):
    while True:
        print("\nPilih Kategori Tiket:")
        print("1. CAT 1 - $100")
        print("2. CAT 2 - $75")
        print("3. CAT 3 - $50")

        pilihan_kategori = int(input("Pilih kategori tiket (1-3): "))

        if pilihan_kategori not in range(1, 4):
            print("Pilihan kategori tidak valid.")
            return 0

        jumlah_tiket = int(input(f"Berapa tiket kategori CAT {pilihan_kategori} yang ingin dibeli? "))

        if jumlah_tiket > stok_per_kategori[pilihan_kategori - 1]:
            print(f"Maaf, stok tiket kategori CAT {pilihan_kategori} tidak mencukupi.")
        else:
            break

    nama_pengguna = input("Masukkan nama Anda: ")

    harga_per_kategori = [100, 75, 50]
    harga_tiket = jumlah_tiket * harga_per_kategori[pilihan_kategori - 1]
    stok_tiket -= jumlah_tiket
    stok_per_kategori[pilihan_kategori - 1] -= jumlah_tiket

    kode = nomor_transaksi + (sum(ord(char) for char in nama_pengguna))*456
    kode_bayar.append(kode)
    print(f"{kode} adalah kode bayar anda, silahkan masukkan di menu 3")

    for i in range(1, jumlah_tiket + 1):
        kode_tiket = generate_kode_tiket(nomor_transaksi, pilihan_kategori, nama_pengguna, i)
        daftar_kode_tiket.append((kode_tiket, nama_pengguna))
        abc = f"Berhasil membeli tiket CAT {pilihan_kategori} dengan kode: {kode_tiket} atas nama {nama_pengguna}"
        line_kode.append((kode, abc))

    print(f"Total harga: ${harga_tiket}")
    return harga_tiket, stok_tiket, daftar_kode_tiket, stok_per_kategori, nomor_transaksi + 1

def cek_stok_tiket(stok_tiket, stok_per_kategori):
    print(f"\nStok tiket saat ini:")
    print("Total Stok: ", stok_tiket, " tiket")
    for i, stok_kategori in enumerate(stok_per_kategori, start=1):
        print(f"CAT {i}: {stok_kategori} tiket")

def bayar_tiket(kodeBayar, line_kode, daftar_kode_tiket):
    valid = int(input("Masukkan Kode Bayar : "))
    if valid in kodeBayar:
        tiket_terkait = [item for kode, item in line_kode if kode == valid]
        for item in tiket_terkait:
            print(item)
        # kodeBayar.remove(valid)
        
    else:
        print("Kode Bayar tidak valid")

def tukar_tiket(daftar_kode_tiket, tiket_ditukar):
    kode_tiket = input("Masukkan kode tiket yang ingin ditukarkan: ")

    if kode_tiket in [kode for kode, _ in daftar_kode_tiket]:
        tiket = [(kode, nama) for kode, nama in daftar_kode_tiket if kode == kode_tiket][0]
        print(f"Tiket {kode_tiket} (CAT {kode_tiket[5]}) atas nama {tiket[1]} berhasil ditukarkan.")
        daftar_kode_tiket.remove(tiket)
        tiket_ditukar.append(tiket)
    else:
        print("Kode tiket tidak valid atau tiket sudah ditukarkan sebelumnya.")

def cek_tiket_ditukarkan(tiket_ditukar):
    if tiket_ditukar:
        print("\nDaftar Kode Tiket yang Sudah Ditukarkan:")
        for kode_tiket, nama_pengguna in tiket_ditukar:
            cat_kategori = kode_tiket[5]
            print(f"{kode_tiket} (CAT {cat_kategori}) atas nama {nama_pengguna}")
    else:
        print("Tidak ada tiket yang sudah ditukarkan.")

def urutkan_tiket_ditukarkan(tiket_ditukar):
    tiket_per_kategori = {'CAT 1': [], 'CAT 2': [], 'CAT 3': []}
    

    for kode_tiket, nama_pengguna in tiket_ditukar:
        cat_kategori = kode_tiket[5]
        tiket_per_kategori[f'CAT {cat_kategori}'].append((kode_tiket, nama_pengguna))
    
    for kategori, daftar_tiket in tiket_per_kategori.items():
        if daftar_tiket:
            print(f"\nTiket Ditukarkan untuk {kategori}:")
            for kode_tiket, nama_pengguna in daftar_tiket:
                print(f"{kode_tiket} atas nama {nama_pengguna}")
        else:
            print(f"\nTiket Ditukarkan untuk {kategori}:")
            print("TIDAK ADA TIKET DITUKARKAN")

stok_tiket = 100
stok_per_kategori = [30, 40, 30]
tiket_ditukar = []
daftar_kode_tiket = []
nomor_transaksi = 1
kode_bayar = []
line_kode = []

while True:
    print("\nMenu:")
    print("1. Beli Tiket Konser")
    print("2. Cek Stok Tiket")
    print("3. Bayar Kode Pembayaran & Print Kode Tiket")
    print("4. Tukarkan Tiket")
    print("5. Cek Tiket Ditukarkan")
    print("0. Keluar")

    pilihan = int(input("Pilih menu (0-5): "))

    if pilihan == 0:
        break
    elif pilihan == 1:
        hasil_beli, stok_tiket, daftar_kode_tiket, stok_per_kategori, nomor_transaksi = beli_tiket(stok_tiket, daftar_kode_tiket, stok_per_kategori, nomor_transaksi, kode_bayar, line_kode)
    elif pilihan == 2:
        cek_stok_tiket(stok_tiket, stok_per_kategori)
    elif pilihan == 3:
        bayar_tiket(kode_bayar, line_kode, daftar_kode_tiket)
    elif pilihan == 4:
        tukar_tiket(daftar_kode_tiket, tiket_ditukar)
    elif pilihan == 5:
        urutkan_tiket_ditukarkan(tiket_ditukar)
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")

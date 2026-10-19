def normalisasi_nama(nama):
    """Menghapus spasi berlebih dan merubah ke format Title Case."""
    kata = nama.strip().split()
    return " ".join(kata).title()

def buat_inisial(nama):
    """Mengambil huruf awal setiap kata dari nama yang sudah bersih."""
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    return "".join(k[0] for k in kata)

def normalisasi_kode(kode):
    """Menghapus spasi berlebih, UPPERCASE, dan mengganti spasi dengan hyphen (-)."""
    kata = kode.strip().upper().split()
    return "-".join(kata)

def main():
    print("=" * 40)
    print("      PROGRAM NORMALISASI DATA TEKS     ")
    print("=" * 40)
    
    nama_input = input("Nama       : ")
    kode_input = input("Kode kelas : ")
    
    nama_clean = normalisasi_nama(nama_input)
    kode_clean = normalisasi_kode(kode_input)
    inisial = buat_inisial(nama_input)
    jumlah_kata = len(nama_clean.split())
    
    print("\n" + "=" * 40)
    print("          HASIL NORMALISASI DATA        ")
    print("=" * 40)
    print(f"Nama bersih : {nama_clean}")
    print(f"Kode kelas  : {kode_clean}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")
    print("=" * 40)

if __name__ == "__main__":
    main()
import hashlib

# Fungsi untuk menghitung SHA-256 dari plaintext
def hash_sha256(plaintext):
    return hashlib.sha256(plaintext.encode()).hexdigest()

# Fungsi untuk membuat pasangan kunci RSA secara manual
def generate_rsa_keys():
    # Bilangan prima sederhana untuk simulasi RSA
    p = 61
    q = 53
    n = p * q  # Modulus (bagian dari kunci)
    phi = (p - 1) * (q - 1)  # Euler's Totient function

    # Pilih e yang relatif prima terhadap phi
    e = 17

    # Hitung d sebagai invers dari e modulo phi
    d = pow(e, -1, phi)

    return (e, n), (d, n)  # public_key, private_key

# Fungsi untuk enkripsi dengan private key (tanda tangan digital)
def encrypt_with_private_key(hash_text, private_key):
    d, n = private_key
    hash_int = int(hash_text, 16)  # Ubah hash heksadesimal ke integer
    cipher_int = pow(hash_int, d, n)  # Enkripsi hash menggunakan private key
    return cipher_int

# Fungsi untuk dekripsi dengan public key (untuk verifikasi tanda tangan)
def decrypt_with_public_key(cipher_text, public_key):
    e, n = public_key
    decrypted_int = pow(cipher_text, e, n)
    return decrypted_int

# Array untuk menyimpan surat valid
surat_valid = []

# Generate RSA keys (global untuk keperluan tanda tangan dan verifikasi)
public_key, private_key = generate_rsa_keys()

# Program utama dengan menu
while True:
    print("\nMenu:")
    print("1. Buat Surat")
    print("2. Validasi Surat")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        id_surat = input("Masukkan ID Surat: ")
        id_ketua = input("Masukkan ID Ketua: ")
        pesan = input("Masukkan Pesan Surat: ")

        plaintext = id_surat + "/" + id_ketua + "/" + pesan
        hash_text = hash_sha256(plaintext)
        cipher_text = encrypt_with_private_key(hash_text, private_key)

        # Simpan ke dalam array surat_valid
        surat_valid.append({
            "id_surat": id_surat,
            "id_ketua": id_ketua,
            "pesan": pesan,
            "hash": hash_text,
            "cipher": cipher_text
        })

        print("\nSurat berhasil dibuat dan disimpan!")
        # print(surat_valid)
        print(f"Hash SHA-256: {hash_text}")
        print(f"Tanda tangan digital (cipher): {cipher_text}")

    elif pilihan == "2":
        cipher_input = int(input("Masukkan tanda tangan digital (ciphertext): "))

        # Dekripsi ciphertext
        # decrypted_hash_int = decrypt_with_public_key(cipher_input, public_key)
        # decrypted_hash_hex = hex(decrypted_hash_int)[2:].zfill(64)  # ubah ke format hex

        # Cek apakah hash hasil dekripsi ada di surat_valid
        valid = False
        for surat in surat_valid:
            if surat["cipher"] == cipher_input:
                print("\nSurat valid!")
                print(f"ID Surat  : {surat['id_surat']}")
                print(f"ID Ketua  : {surat['id_ketua']}")
                print(f"Pesan     : {surat['pesan']}")
                valid = True
                break
            # if surat["cipher"] == decrypted_hash_hex and surat["cipher"] == cipher_input:
            #     print("\nSurat valid!")
            #     print(f"ID Surat  : {surat['id_surat']}")
            #     print(f"ID Ketua  : {surat['id_ketua']}")
            #     print(f"Pesan     : {surat['pesan']}")
            #     valid = True
            #     break

        if not valid:
            print("\nSurat tidak valid atau belum terdaftar.")

    elif pilihan == "3":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
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

# Fungsi untuk enkripsi dengan private key (tanda tangan)
def encrypt_with_private_key(hash_text, private_key):
    d, n = private_key
    hash_int = int(hash_text, 16)  # Ubah hash heksadesimal ke integer
    cipher_int = pow(hash_int, d, n)  # Enkripsi hash menggunakan private key
    return cipher_int

# Program utama
if __name__ == "__main__":
    # 1. Input dari user
    id_surat = input("Masukkan ID Surat: ")
    id_ketua = input("Masukkan ID Ketua: ")
    pesan = input("Masukkan Pesan Surat: ")

    # 2. Gabungkan input menjadi satu plaintext
    plaintext = id_surat + "/" + id_ketua + "/" + pesan

    # 3. Generate RSA keys
    public_key, private_key = generate_rsa_keys()

    # 4. Hash plaintext menggunakan SHA-256
    hash_text = hash_sha256(plaintext)
    print(f"\nHash SHA-256 dari plaintext:\n{hash_text}")

    # 5. Enkripsi hash menggunakan private key (membuat tanda tangan digital)
    cipher_text = encrypt_with_private_key(hash_text, private_key)
    print(f"\nCiphertext (tanda tangan digital):\n{cipher_text}")

stack = []

def tambah_buku(stack, nama_buku, nama_pengarang):
    buku_baru =[nama_buku, nama_pengarang]
    stack.append(buku_baru)
    print("f{buku_baru}berhasil ditambahkan ke dalam stack.")
    
def hapus_buku_terakir(stack):
    if len (stack)==0:
        print ("stack kosong, tidak ada buku yang dihapus.")
    else:
        buku_terakir=stack.pop()
        print("f{buku_terakir} berhasil dihapus dari stack")
        
def tampilkan_buku_teratas(stack):
    if len(stack)==0:
        print("stack kosong, tidak ada buku yang dapat ditampilkan")
    else:
        buku_teratas = stack[-1]
        print("f buku teratas di dalam stack adalah {buku_teratas}.")
        
while True:
    print("\ntumpukan buku saat ini: ",stack)
    print("menu:")
    print("1. tambah buku")
    print("2. hapus buku terakir")
    print("3. tampilkan buku teratas")
    print("4. keluar")
    
    pilihan = input("masukan pilihan anda (1/2/3/4/) : ")
    if pilihan=="1":
        nama_buku=input("masukan nama buku yang akan ditambahkan:")
        nama_pengarang=("masukan nama pengarang yang akan ditambahkan:")
        tambah_buku(stack, nama_buku, nama_pengarang)
    elif pilihan=="2":
        hapus_buku_terakir(stack)
    elif pilihan=="3":
        tampilkan_buku_teratas(stack)
    elif pilihan=="4":
        print("terimakasih telah menggunakan program ini.")
        break
    else:
        print("pilihan tidak valid. silahkan masukan pilihan yang benar.")
    
    


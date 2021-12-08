diskon_member=10
diskon_libur=5
max_diskon_libur=100000

def hitung_diskon_member(total_belanja):
    return diskon_member/100 * total_belanja

def hitung_diskon_libur(total_belanja):
    disc= diskon_libur/100 * total_belanja
    if disc>max_diskon_libur:
        disc=max_diskon_libur
    return disc
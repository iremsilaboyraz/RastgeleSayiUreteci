import time

class OzelUretec:
    def __init__(self, seed):
        # Başlangıçta tohumu nano saniye ile harmanlıyoruz (Tahmin edilemezlik)
        self.state = (seed ^ time.time_ns()) & ((1 << 48) - 1)
        self.magic = 0x5DEECE66D # Bu bizim gizli sosumuz

    def uret(self, alt_sinir, ust_sinir):
        # Collatz kuralı
        if self.state % 2 == 0:
            self.state //= 2
        else:
            self.state = 3 * self.state + 1
        
        # Bitleri birbirine katıyoruz
        self.state = (self.state ^ self.magic) & ((1 << 48) - 1)
        
        # Kullanıcının istediği aralığa oturtuyoruz
        return alt_sinir + (self.state % (ust_sinir - alt_sinir + 1))

# DENEME
test = OzelUretec(seed=123)
print("Senin İçin Üretilen Sayılar:")
for i in range(5):
    print(f"{i+1}. Sayı: {test.uret(1, 100)}")
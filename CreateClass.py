class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang
    def __str__(self):
        return f"Persegi panjang dengan panjang {self.panjang} cm dan lebar {self.lebar} cm"

# membuat object 
persegi = PersegiPanjang(3,5)

print("Keliling:", persegi.keliling(), "cm")
print("Luas:", persegi.luas(), "cm²")
print(persegi)
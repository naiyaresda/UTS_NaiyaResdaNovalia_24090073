def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i
        return hasil

# Contoh penggunaan
n = 5
print(f"Faktorial dari {n} adalah {faktorial(n)}")  # Output: 120

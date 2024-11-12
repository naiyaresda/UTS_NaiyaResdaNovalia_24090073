def hitung_elemen_sama(A, B):
    count = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            count += 1
    return count

# Contoh penggunaan
A = [1, 2, 3, 4, 5]
B = [1, 2, 0, 4, 8]
print(f"Jumlah elemen yang sama di posisi yang sama adalah {hitung_elemen_sama(A, B)}")  # Output: 3

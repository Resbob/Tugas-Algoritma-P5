while True:
    print("\nTugasP5 Operasi Matriks")
    print("1 = Penjumlahan")
    print("2 = Pengurangan")
    print("3 = Perkalian")
    print("0 = Exit")

    pilihan = int(input("Pilih menu : "))

    if pilihan == 0:
        print("Program selesai")
        break

    baris = int(input("Input baris : "))
    kolom = int(input("Input kolom : "))

    # Input matriks A
    print("\nMasukkan Matriks A")
    A = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(int(input(f"A[{i}][{j}] = ")))
        A.append(row)

    # Input matriks B
    print("\nMasukkan Matriks B")
    B = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(int(input(f"B[{i}][{j}] = ")))
        B.append(row)

    # Hasil matriks
    Hasil = []

    match pilihan:
        case 1:  # Penjumlahan
            for i in range(baris):
                row = []
                for j in range(kolom):
                    row.append(A[i][j] + B[i][j])
                Hasil.append(row)

        case 2:  # Pengurangan
            for i in range(baris):
                row = []
                for j in range(kolom):
                    row.append(A[i][j] - B[i][j])
                Hasil.append(row)

        case 3:  # Perkalian (sederhana)
            for i in range(baris):
                row = []
                for j in range(kolom):
                    total = 0
                    for k in range(kolom):
                        total += A[i][k] * B[k][j]
                    row.append(total)
                Hasil.append(row)

        case _:
            print("Pilihan tidak valid")
            continue

    # Output hasil
    print("\nHasil =")
    for i in range(baris):
        for j in range(kolom):
            print(Hasil[i][j], end=" ")
        print()
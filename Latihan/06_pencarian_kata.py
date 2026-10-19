teks = "Python untuk data. Python untuk pendidikan."
teks_lower = teks.lower()
kata = "python"

print("Apakah kata 'python' ada? :", kata in teks_lower)
print("Jumlah kemunculan kata    :", teks_lower.count(kata))
print("Posisi pertama kata (indeks):", teks_lower.find(kata))
# Info umum
df.info()

# Cek apakah ada data yang kosong
print("\nJumlah missing values:\n", df.isnull().sum())

# Statistik deskriptif
df.describe()

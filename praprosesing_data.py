import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Misalkan 'df' adalah DataFrame Anda yang sudah di-load sebelumnya
# Cek nama kolom yang ada di df
print("Nama Kolom dalam DataFrame:", df.columns)

# Hapus kolom ID dan ZIP Code jika ada (menggunakan 'errors="ignore"' untuk menghindari error jika kolom tidak ada)
df.drop(columns=['ID', 'ZIP Code'], inplace=True, errors='ignore')

# Pisahkan fitur (X) dan target (y)
X = df.drop(columns='Personal Loan')
y = df['Personal Loan']

# Normalisasi fitur numerik
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data 80% train dan 20% test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Cek ukuran data train dan test
print(f"Data latih (X_train) memiliki {X_train.shape[0]} sampel dan {X_train.shape[1]} fitur.")
print(f"Data uji (X_test) memiliki {X_test.shape[0]} sampel dan {X_test.shape[1]} fitur.")

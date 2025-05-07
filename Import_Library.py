# STEP 1: Upload File CSV ke Colab
from google.colab import files
uploaded = files.upload()

# Import library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import io

# STEP 2: Load Data (Diperbaiki agar fleksibel membaca file apapun)
filename = list(uploaded.keys())[0]  # ambil nama file yang di-upload
df = pd.read_csv(io.BytesIO(uploaded[filename]))  # baca file yang di-upload
print("Jumlah data awal:", df.shape)
df.head()

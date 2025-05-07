# Impor yang diperlukan
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Visualisasi pohon
plt.figure(figsize=(20, 10))
plot_tree(dt_model, 
          feature_names=df.drop('Personal Loan', axis=1).columns, 
          class_names=['No', 'Yes'], 
          filled=True)

plt.title("Decision Tree - Prediksi Personal Loan")
plt.savefig("decision_tree.jpg")
plt.show()

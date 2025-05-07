from sklearn.tree import DecisionTreeClassifier

# Buat model Decision Tree
dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)

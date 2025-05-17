import pandas as pd
import os

# Create data directory if not exists
os.makedirs("data", exist_ok=True)

# 1. Iris Dataset
iris_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(iris_url)
iris_df.head(100).to_csv("data/iris.csv", index=False)
print("✅ iris.csv downloaded")

# 2. Wine Dataset
wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_df = pd.read_csv(wine_url, sep=";")
wine_df.head(100).to_csv("data/wine.csv", index=False)
print("✅ wine.csv downloaded")

# 3. Titanic Dataset
titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(titanic_url)
titanic_df.head(100).to_csv("data/titanic.csv", index=False)
print("✅ titanic.csv downloaded")

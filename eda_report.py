import pandas as pd

print("✅ Step 1: Loading dataset...")
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print("✅ Step 2: Creating HTML...")
html = f"""
<html>
<head><title>Simple EDA Report</title></head>
<body>
<h2>Iris Dataset EDA</h2>
<p><strong>Shape:</strong> {df.shape}</p>
<h3>Columns:</h3>
<ul>{"".join(f"<li>{col}</li>" for col in df.columns)}</ul>
<h3>Summary Statistics:</h3>
{df.describe().to_html()}
<h3>First 5 Rows:</h3>
{df.head().to_html(index=False)}
</body>
</html>
"""

print("✅ Step 3: Saving report to docs/simple_eda_report.html...")
with open("docs/simple_eda_report.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Done! Report created successfully.")

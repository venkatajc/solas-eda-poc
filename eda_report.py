import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# === Input validation ===
if len(sys.argv) < 2:
    print("❌ Please provide a dataset name like: python eda_report.py iris")
    sys.exit(1)

dataset = sys.argv[1]  # e.g., iris
file_path = f"data/{dataset}.csv"

# === Check if dataset file exists ===
if not os.path.exists(file_path):
    print(f"❌ Dataset file not found: {file_path}")
    sys.exit(1)

# === Load data ===
df = pd.read_csv(file_path)

# === Generate plot ===
plot_path = f"docs/{dataset}_plot.png"
os.makedirs("docs", exist_ok=True)
df.hist(figsize=(10, 6))
plt.tight_layout()
plt.savefig(plot_path)
plt.close()

# === Generate HTML report ===
html_path = f"docs/{dataset}_report.html"
html = f"""
<html>
<head><title>{dataset} EDA Report</title></head>
<body>
<h2>Dataset: {dataset}</h2>
<p><strong>Shape:</strong> {df.shape}</p>
<h3>Summary Statistics</h3>
{df.describe().to_html()}
<h3>Auto-Generated Plot</h3>
<img src="{dataset}_plot.png" width="600">
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Report generated: {html_path}")
print(f"✅ Plot saved: {plot_path}")

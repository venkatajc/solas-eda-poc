from datetime import datetime
import os

# 👇 This will generate a timestamped file like iris_20250529_1545_report.html
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
safe_table_name = table_name.replace(".", "_")

os.makedirs("docs", exist_ok=True)

# Export report
df.solas.automate = True
report_file = f"{safe_table_name}_{timestamp}_report.html"
report_path = f"docs/{report_file}"
df.solas.export_to_html(report_path)

# Optional: track file info for index generation
with open("docs/_reports.txt", "a") as log:
    log.write(f"{report_file},{safe_table_name},{timestamp}\n")

from collections import defaultdict

index_file = "docs/index.html"
reports_by_table = defaultdict(list)

# Read log
with open("docs/_reports.txt") as f:
    for line in f:
        file, table, timestamp = line.strip().split(",")
        reports_by_table[table].append((file, timestamp))

# Sort and take latest 3
for t in reports_by_table:
    reports_by_table[t] = sorted(reports_by_table[t], key=lambda x: x[1], reverse=True)[:3]

# Build index HTML
html = """<!DOCTYPE html><html><head><title>Solas AI Reports</title>
<style>
body { font-family: Arial; padding: 20px; }
h2 { margin-top: 30px; }
ul { list-style-type: none; }
.timestamp { color: #999; font-size: 0.9em; margin-left: 10px; }
</style></head><body>
<h1>📊 Solas AI Report Index</h1>
"""

for table, reports in sorted(reports_by_table.items()):
    html += f"<h2>{table.replace('_', '.')}</h2><ul>\n"
    for file, ts in reports:
        ts_fmt = f"{ts[:4]}-{ts[4:6]}-{ts[6:8]} {ts[9:11]}:{ts[11:]}"
        html += f'<li><a href="{file}">{file}</a><span class="timestamp">({ts_fmt})</span></li>\n'
    html += "</ul>\n"

html += "</body></html>"

# Write index.html
with open(index_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Index page generated: {index_file}")

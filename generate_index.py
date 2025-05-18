import os
from datetime import datetime

docs_dir = "docs"
index_file = os.path.join(docs_dir, "index.html")

# Collect all report files
report_files = []
for file in os.listdir(docs_dir):
    if file.endswith("_report.html") and file != "index.html":
        file_path = os.path.join(docs_dir, file)
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        report_files.append((file, mod_time))

# Sort by latest modified
report_files.sort(key=lambda x: x[1], reverse=True)

# Build HTML
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Solas EDA Reports</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #336699; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        .timestamp { color: #999; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>📊 Solas EDA Reports</h1>
    <ul>
"""

for file, mod_time in report_files:
    display_name = file.replace("_report.html", "").capitalize()
    html += f'<li><a href="{file}">{display_name} Report</a> <span class="timestamp">({mod_time.strftime("%Y-%m-%d %H:%M:%S")})</span></li>\n'

html += """
    </ul>
</body>
</html>
"""

# Write to index.html
with open(index_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Index page generated: {index_file}")

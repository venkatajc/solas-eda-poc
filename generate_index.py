import os
from datetime import datetime

# Folder and output file
docs_dir = "docs"
index_file = os.path.join(docs_dir, "index.html")

# Step 1: Collect all report files
report_files = []
for file in os.listdir(docs_dir):
    if file.endswith("_report.html") and file != "index.html":
        file_path = os.path.join(docs_dir, file)
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        report_files.append((file, mod_time))

# Step 2: Sort by latest modified
report_files.sort(key=lambda x: x[1], reverse=True)

# Step 3: Build HTML
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Solas EDA Reports</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #336699; }
        input { padding: 5px; font-size: 16px; width: 300px; margin-bottom: 20px; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        .timestamp { color: #999; font-size: 0.9em; }
    </style>
    <script>
        function filterReports() {
            const input = document.getElementById("filterBox").value.toLowerCase();
            const items = document.querySelectorAll("#reportList li");
            items.forEach(li => {
                const text = li.textContent.toLowerCase();
                li.style.display = text.includes(input) ? "" : "none";
            });
        }
    </script>
</head>
<body>
    <h1>📊 Solas EDA Reports</h1>

    <input type="text" id="filterBox" placeholder="Enter table name to search..." onkeyup="filterReports()">

    <ul id="reportList">
"""

# Step 4: Add report entries
for file, mod_time in report_files:
    display_name = file.replace("_report.html", "").capitalize()
    html += f'<li><a href="{file}">{display_name} Report</a> <span class="timestamp">({mod_time.strftime("%Y-%m-%d %H:%M:%S")})</span></li>\n'

# Step 5: Close HTML
html += """
    </ul>
</body>
</html>
"""

# Step 6: Write to index.html
with open(index_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Index page generated: {index_file}")

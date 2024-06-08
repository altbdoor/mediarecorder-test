from datetime import datetime
import glob
import json

combined_data: list[dict] = []

for file_path in glob.glob("./dist/*/output.json"):
    with open(file_path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        combined_data.append(data)

if len(combined_data) == 0:
    raise Exception("no data")

# get the browser names
browser_names: list[str] = []
for entry in combined_data:
    browser_name = entry["_meta"]["browserName"]
    browser_version = entry["_meta"]["browserVersion"]

    browser_names.append(f"<td>{browser_name} {browser_version}</td>")

# get all the formats
row_keys: list[str] = [key for key in combined_data[0].keys() if key != "_meta"]
row_keys.sort()

# generate the table
html_rows = f'<tr><td></td>{"".join(browser_names)}</tr>\n'

for key in row_keys:
    html_rows += "<tr>"
    html_rows += f'<td align="right"><code>{key}</code></td>'

    for entry in combined_data:
        is_supported = entry.get(key)
        text = "Yes" if is_supported else "No"
        background_color = "#A5D6A7" if is_supported else "#EF9A9A"

        html_rows += f'<td bgcolor="{background_color}">{text}</td>'

    html_rows += "</tr>\n"

# write to html
with open("./dist/index.html", "w", encoding="utf-8") as fp:
    fp.write("<!DOCTYPE html>")
    fp.write('<html style="font-size: 16px;">')
    fp.write("<body>")

    today = datetime.today().isoformat()
    fp.write(f'<p>Updated on: <time datetime="{today}">{today}</time></p>')

    fp.write('<table border="1">')
    fp.write(html_rows)
    fp.write("</table>")
    fp.write("</body>")
    fp.write("</html>")

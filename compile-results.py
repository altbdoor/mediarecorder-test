from datetime import datetime
import glob
import json
import os


def main():
    combined_data: list[dict] = []

    for file_path in glob.glob("./dist/*/output.json"):
        with open(file_path, "r", encoding="utf-8") as fp:
            data = json.load(fp)

            json_path = os.path.normpath(file_path)
            json_path = json_path.split(os.sep)[1:]
            json_path = "/".join(json_path)

            data["_meta"]["jsonPath"] = json_path

            combined_data.append(data)

    if len(combined_data) == 0:
        raise Exception("no data")

    # get the browser names
    browser_names: list[str] = []
    for entry in combined_data:
        browser_name = entry["_meta"]["browserName"]
        browser_version = entry["_meta"]["browserVersion"]

        browser_names.append(
            "<td>"
            f'<a href="./{entry['_meta']['jsonPath']}">'
            f"{browser_name} {browser_version}"
            "</a>"
            "</td>"
        )

    # get all the formats
    row_keys: list[str] = [key for key in combined_data[0].keys() if key != "_meta"]
    row_keys.sort()

    # generate the table
    html_rows = f'<tr><td></td>{"".join(browser_names)}</tr>\n'

    for key in row_keys:
        html_rows += "<tr>"
        html_rows += f'<td align="right"><code>{key}</code></td>'

        for entry in combined_data:
            is_supported: bool = entry.get(key, False)
            text = "Yes" if is_supported else "No"
            background_color = "#A5D6A7" if is_supported else "#EF9A9A"

            html_rows += f'<td bgcolor="{background_color}">{text}</td>'

        html_rows += "</tr>\n"

    # write to html
    with open("./dist/index.html", "w", encoding="utf-8") as fp:
        today = datetime.today().isoformat()

        fp.write(
            "<!DOCTYPE html>"
            '<html style="font-size: 16px;">'
            "<body>"
            "<h1>MediaRecorder test</h1>"
            f'<p>GitHub repository: <a href="https://altbdoor.github.io/mediarecorder-test/">mediarecorder-test</a></p>'
            f'<p>Updated on: <time datetime="{today}">{today}</time></p>'
            '<table border="1">'
            f"{html_rows}"
            "</table>"
            "</body>"
            "</html>"
        )


if __name__ == "__main__":
    main()

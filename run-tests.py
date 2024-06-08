#!/usr/bin/env python

import base64
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def main():
    html_page = ""
    browser = os.environ.get("BROWSER")

    with open("./test.html", "r", encoding="utf-8") as fp:
        html_page = fp.read()
        html_page = base64.b64encode(html_page.encode("utf-8")).decode("utf-8")

    if browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    elif browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("unknown browser")

    browser_name = driver.capabilities["browserName"]
    browser_version = driver.capabilities["browserVersion"]

    driver.get("data:text/html;base64," + html_page)
    pre_element = driver.find_element(By.TAG_NAME, "pre")

    data = json.loads(pre_element.text)
    data["_meta"]["browserName"] = browser_name
    data["_meta"]["browserVersion"] = browser_version

    with open("./info.txt", "w", encoding="utf-8") as fp:
        fp.write(f"browser-name={browser_name}\n".lower())
        fp.write(f"browser-version={browser_version}\n".lower())

    with open("./output.json", "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=4)

    driver.quit()


if __name__ == "__main__":
    main()

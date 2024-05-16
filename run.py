#!/usr/bin/env python

import base64
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    html_page = ""
    browser = os.environ.get('BROWSER')

    with open("./test.html", "r", encoding="utf-8") as fp:
        html_page = fp.read()
        html_page = base64.b64encode(html_page.encode("utf-8")).decode("utf-8")

    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("unknown browser")

    browser_name = driver.capabilities["browserName"]
    browser_version = driver.capabilities["browserVersion"]

    driver.get("data:text/html;base64," + html_page)
    pre_element = driver.find_element(By.TAG_NAME, "pre")

    print(f"Browser: {browser_name}")
    print(f"Version: {browser_version}")
    print(pre_element.text)

    with open("./output.json", "w", encoding="utf-8") as fp:
        fp.write(pre_element.text)

    driver.quit()


if __name__ == "__main__":
    main()

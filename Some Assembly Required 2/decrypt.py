# first: get aD8SvhyVkb
# second: run server at localhost:8000


import chromedriver_binary
from selenium import webdriver
import string
import time
from tqdm.auto import tqdm

with open("aD8SvhyVkb", "rb") as fp:
    file_content = fp.read()
encoded_flag = file_content[821:]
file_content = file_content[:821] + b'\00' * len(encoded_flag)
decoded = ""
for i, f in tqdm(enumerate(encoded_flag)):
    file_content = file_content[:i + 821] + \
        chr(f).encode() + file_content[i + 822:]
    with open("aD8SvhyVkb", "wb") as fp:
        fp.write(file_content)
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000")
    for c in string.printable:
        driver.find_element_by_id("input").clear()
        driver.find_element_by_id("input").send_keys(decoded + c)
        driver.find_element_by_xpath("//button").click()
        time.sleep(1)
        if "Incorrect!" == driver.find_element_by_id("result").text.strip():
            continue
        else:
            decoded+=c
            driver.close()
            print(decoded)
            break

import requests
from bs4 import BeautifulSoup
import re
import shutil
import os

f = open('text.txt', 'w', encoding='utf-8')
domain = "https://www.mspaintadventures.ru/?s=4&p="
lower_bound = 219
upper_bound = 1892
for i in range(lower_bound, upper_bound+1):
    link = domain + str(i).zfill(6)
    response = requests.get(link).text
    text = BeautifulSoup(response,'lxml')
    raw_text = re.findall(r'</p><p>([\s\S]+?)</p>', str(text))
    print(raw_text)
    if raw_text:
        final_text = raw_text[0]
        print(final_text)
        f.write(str(final_text)+'\n')
        print(i)
f.close()
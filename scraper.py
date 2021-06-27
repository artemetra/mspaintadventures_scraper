import requests
from bs4 import BeautifulSoup
import re
import shutil
import os

f = open('text.txt', 'w')
domain = "https://www.mspaintadventures.ru/?s=4&p="
lower_bound = 219
upper_bound = 1892
for i in range(lower_bound, upper_bound+1):
    link = domain + str(i).zfill(6)
    response = requests.get(link).text
    text = BeautifulSoup(response,'lxml')
    raw_text = re.findall(r'</p><p>([\s\S]+?)</p>', str(text))
    print(str(raw_text))
    f.write(str(raw_text))
    print(i)
    f.close()
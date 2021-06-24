import requests
from bs4 import BeautifulSoup
import re
import shutil
import os


domain = "https://www.mspaintadventures.ru/?s=6&p="
lower_bound = 1901
upper_bound = 10029
flash = "&flash=1"
for i in range(lower_bound, upper_bound+1):
    link = domain + str(i).zfill(6) + flash
    response = requests.get(link).text

    gifs = BeautifulSoup(response, 'lxml').find_all('tr', class_='comic-images')
    result_link_raw = re.findall(r'(?<=src=\")(.+?)(?=\")|(?<=data=\")(.+?)(?=\")', str(gifs))
    for _result_link in result_link_raw:
        tmp1, tmp2 = _result_link
        result_link = tmp1 + tmp2
        result_image = requests.get(result_link, stream=True)
        filename = result_link[48:].replace("/",'')
        with open(filename, 'wb') as out_file:
            shutil.copyfileobj(result_image.raw, out_file)
        print("File \"{}\" saved!".format(filename))
        del result_image
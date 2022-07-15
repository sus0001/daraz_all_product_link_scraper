from playwright.sync_api import sync_playwright
from daraz_tools_oop import DarazIndivLinkScraper, DarazScraper, FlattenedLists, SplitDarazURL
import time
import winsound
import pandas as pd
import os
import shutil
import sys
import smtplib
import asynchat


start_time = time.time()

product_url = "https://www.daraz.com.np/auto-parts-spares/?spm=a2a0e.searchlistcategory.cate_12_5.4.d1654f4f5xaidm"

total_pages = 51
list_of_urls = SplitDarazURL(product_url).split(total_pages)
product_category = DarazScraper(product_url).category_name()

# print(f"Total pages | {total_pages}")

# Setting up the directory for downloaded databases:
folder_name = f"Daraz {product_category}" 
parent_dir = f"{os.getcwd()}"
path_dir = os.path.join(parent_dir, folder_name)

# Overwriting the direcoty if already existed
if os.path.exists(path_dir):
    shutil.rmtree(path_dir)
os.mkdir(path_dir)


all_daraz_product_links = FlattenedLists().flat([DarazScraper(url).all_product_links() for url in list_of_urls])
all_daraz_product_names = FlattenedLists().flat([DarazScraper(url).all_product_names() for url in list_of_urls])
all_daraz_product_prices = FlattenedLists().flat([DarazScraper(url).all_product_prices() for url in list_of_urls])


total_time = round(time.time()-start_time, 2)
time_in_secs = round(total_time)
time_in_mins = round(total_time/60)

d = {
    "Names": all_daraz_product_names,
    "Prices": all_daraz_product_prices,
    "Links": all_daraz_product_links
}

df = pd.DataFrame(d)

df.to_json(f"{os.getcwd()}//{folder_name}//Daraz {product_category} database.json", indent=4)
df.to_excel(f"{os.getcwd()}//{folder_name}//{product_category} database.xlsx", index=False)

print(f"{time_in_secs} seconds")
print(f"{time_in_mins} minutes.")
print(f"Saved | {folder_name}")



# Play the sound after the completion of Scraping process:
winsound.PlaySound('notification.mp3', winsound.SND_FILENAME)




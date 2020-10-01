from bs4 import BeautifulSoup
import requests
from datetime import datetime
from urllib.parse import urljoin
import sympy
import re 



base = 'https://wiki.project1999.com/'
url = "https://wiki.project1999.com/Magelo_Green:Ibol"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


mw = soup.find("div", {"class": "IventoryOuter"})
connie = mw.findAll('a')


inventory = []
for link in connie:
    if link.has_attr('href'):
        relative = link['href']
        item_name = urljoin(base, relative)
        inventory.append(item_name)

        
max_items = len(inventory)
print(max_items)
cycle_item_count = 0

def find_sum(str1):
    add_30day = sum(map(int,re.findall('\d+',str1)))
    avg = add_30day/2
    return avg

def get_item_name(slot_number):
    while slot_number <= max_items:
        print(slot_number)
        item_name = str(inventory[slot_number]).replace('https://wiki.project1999.com/', '')
        
        cycle_item_url = str(inventory[slot_number])
        r_itemurl = requests.get(cycle_item_url)
        soup_itemurl = BeautifulSoup(r_itemurl.text, 'html.parser')
       
        # mw-content-text is main item page you need to ask if had
        # related uqest
        # or item location displayed
        
        check_no_drop = soup_itemurl.find("div", {"class": "itemdata"})
        item_stats = check_no_drop.text.strip()
        # print(item_stats)
        related_quest = soup_itemurl.find("span", {"id": "Related_quests"})
        item_quest = related_quest.text.strip()
        
        print('')
        
        if 'DROP' in item_stats:
            print(item_quest)
            print(item_loc)
            slot_number += 1
            print(slot_number)
            print(item_name)
            get_item_name(slot_number)
        else:
            print(item_name)
            
        slot_number += 1

def get_item_price():
        price_div = soup_itemurl.find("div", {"class": "auctrackerbox"})
        price_blue = soup_itemurl.find("div", {"id": "auc_Blue"})
        price_tab_blue = price_blue.find("table", {"class": "eoTable3"})
        blue_item = price_tab_blue.find("td")

        price_green = soup_itemurl.find("div", {"id": "auc_Green"})
        price_tab_green = price_green.find("table", {"class": "eoTable3"})
        green_item = price_tab_green.find("td")

        bmoney = blue_item.get_text().replace('±', '+')
        gmoney = green_item.get_text().replace('±', '+')

        bmoney = find_sum(bmoney)
        gmoney = find_sum(gmoney)

        print(item_name)
        print("Blue 30-Day Average: " + str(bmoney), "Green 30-Day Average: " + str(gmoney))
        print('')
        
get_item_name(cycle_item_count)

#print(str(x2))
###########
# if no drop, say it's no drop or maybe questable?
# ... link quest if found one on the page...
# 
###########

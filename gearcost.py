from bs4 import BeautifulSoup
import requests
from datetime import date
from urllib.parse import urljoin
import sympy
import re 

now = str(date.today())

base = 'https://wiki.project1999.com/'
url = "https://wiki.project1999.com/Magelo_Green:Ibol"
#url = input("Your Magelo URL: ")
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
    if find_sum == 0:
        print('  None sold in the last 30 days')

print(" ")
print(" ")
print(" ")
print("== Calculated by gearcost on " + now + " ==")

def get_item_name(slot_number):
    while slot_number <= max_items:
        print('  ')
        # print(slot_number)
        item_name = str(inventory[slot_number]).replace('https://wiki.project1999.com/', '')
        item_name = item_name.replace('_', ' ')
        print(item_name)
        
        cycle_item_url = str(inventory[slot_number])
        r_itemurl = requests.get(cycle_item_url)
        soup_itemurl = BeautifulSoup(r_itemurl.text, 'html.parser')

        def get_item_price():
            if soup_itemurl.find("div", {"id": "auc_Blue"}) != None or soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                price_div = soup_itemurl.find("div", {"class": "auctrackerbox"})
                if soup_itemurl.find("div", {"id": "auc_Blue"}) != None and soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                    price_blue = soup_itemurl.find("div", {"id": "auc_Blue"})
                    price_tab_blue = price_blue.find("table", {"class": "eoTable3"})
                    blue_item = price_tab_blue.find("td")
                    bmoney = blue_item.get_text().replace('±', '+')
                    bmoney = find_sum(bmoney)
                    print("  Blue 30-Day Average: " + str(bmoney))  
                    price_green = soup_itemurl.find("div", {"id": "auc_Green"})
                    price_tab_green = price_green.find("table", {"class": "eoTable3"})
                    green_item = price_tab_green.find("td")
                    gmoney = green_item.get_text().replace('±', '+')
                    gmoney = find_sum(gmoney)
                    print("  Green 30-Day Average: " + str(gmoney))
                if soup_itemurl.find("div", {"id": "auc_Blue"}) != None and soup_itemurl.find("div", {"id": "auc_Green"}) == None:
                    print('  Prices found for Blue, but,')
                    print('  No prices found for Green.')
                    price_blue = soup_itemurl.find("div", {"id": "auc_Blue"})
                    price_tab_blue = price_blue.find("table", {"class": "eoTable3"})
                    blue_item = price_tab_blue.find("td")
                    bmoney = blue_item.get_text().replace('±', '+')
                    bmoney = find_sum(bmoney)
                    print("  Blue 30-Day Average: " + str(bmoney))  
                if soup_itemurl.find("div", {"id": "auc_Blue"}) == None and soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                    print('  Prices found for Green, but,')
                    print('  No prices found for Blue.')
                    price_green = soup_itemurl.find("div", {"id": "auc_Green"})
                    price_tab_green = price_green.find("table", {"class": "eoTable3"})
                    green_item = price_tab_green.find("td")
                    gmoney = green_item.get_text().replace('±', '+')
                    gmoney = find_sum(gmoney)
                    print("  Green 30-Day Average: "+ str(gmoney))    
                    
                    
                    
            else:
                print('No Prices Found')

        # mw-content-text is main item page you need to ask if had
        # related uqest
        # or item location displayed
        
        item_page = soup_itemurl.find("div", {"id": "mw-content-text"})
        item__page = item_page.text.strip()
        
        check_no_drop = soup_itemurl.find("div", {"class": "itemdata"})
        item_stats = check_no_drop.text.strip()
        # print(item_stats)
        
        # quest
        related_quest = soup_itemurl.find("span", {"id": "Related_quests"})
        related_quest__header = related_quest.text.strip()
        #drops from
        drops_from = soup_itemurl.find("span", {"id": "Drops_From"})
        drops_from__header = related_quest.text.strip()
        #Player_crafted
        
        player_crafted = soup_itemurl.find("span", {"id": "Player_crafted"})
        player_crafted__header = player_crafted.text.strip()
        
        collect_links = item_page.findAll("a", {"class": 'mw-redirect'})
        collection_list = []
        
        for link in collect_links:
            if link['href']:
                relative = link['href']
                collection_list.append(urljoin(base, relative))
                # print(collection_list)
                
        if 'DROP' in item_stats:
            print('  ' + 'NO DROP')
            # print('Find this items Quest or Location')
#            if 'Quests' in item__page:
#                print(related_quest__header,collection_list)
#                slot_number += 1
#            if 'Drops From' in item__page:
#                print(drops_from__header,collection_list)
#                slot_number += 1
#            if 'Player Crafted' in item__page:
#                print(player_crafted__header,collection_list)
#                slot_number += 1
                
            slot_number += 1
            # print(item_name)
            get_item_name(slot_number)
        else:
            get_item_price()
            
        if slot_number == max_items:
            break
        else:
            slot_number += 1

try:
    get_item_name(cycle_item_count)
except IndexError: 
    pass


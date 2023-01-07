from bs4 import BeautifulSoup
import requests
from datetime import date
from urllib.parse import urljoin
from sympy import *
import re 

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

import urllib3
http = urllib3.PoolManager()

###################################################
now = str(date.today())

base = 'https://wiki.project1999.com/'
url = "https://wiki.project1999.com/Magelo_Green:Ibol"
# url = input("Your Magelo URL: ")
if 'Blue' in url:
    charname = url.replace('https://wiki.project1999.com/Magelo_Blue:', '')
elif 'Green' in url:
    charname = url.replace('https://wiki.project1999.com/Magelo_Green:', '')
elif 'Red' in url:
    print('We need a new red server! Gearcost doesnt calc red prices, yet.')
    
###################################################

# Create an SSL context with unverified certificate checks
context = urllib3.util.ssl_.create_urllib3_context()

# Use the SSL context to make an HTTPS request
r = http.request('GET', url, ssl_context=context)

###################################################
#r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
###################################################


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

inventory_txt = open('inventory.txt', 'w+')

############ Find Sum
def find_sum(str1):
    add_30day = sum(map(int,re.findall('\d+',str1)))
    avg = add_30day/2
    return avg
    if find_sum == 0:
        print('  None sold in the last 30 days')
############

print(" ")
print(" ")
gearcost__header = "== Calculated by gearcost on " + now + " ==\n"
print(gearcost__header)
inventory_txt.write(str(gearcost__header))

def thegearcost():

    ####################################
    # Todo:
    # calculate how many no drop items there are....
    # calculate the prices for blue
    # calculate the prices for green
    ####################################
    # Ibol's Inventory Value:
    # --------------------------
    # Blue: 500p
    # Green: 800p
    # x5 NO DROP items
    # --------------------------
    ####################################
    markdown_newline = '  '
    global char_header
    global gc_blue
    global gc_green
    global no_drop_tally
    char_header = "\n" + charname+"`s Inventory Value\n--------------------------  "
    print(char_header)
    inventory_txt.write(char_header)

    #global blue__gearcost $$
    #print(blue__gearcost)
    gc_blue = find_sum(str(blue__gearcost))
    print('Blue: ' + str(gc_blue), markdown_newline)
    inventory_txt.write('\nBlue: ' + str(gc_blue) + '  ')

    #global green__gearcost $$
    #print(green__gearcost)
    gc_green = find_sum(str(green__gearcost))
    print('Green: ' + str(gc_blue), markdown_newline)
    inventory_txt.write('\nGreen: ' + str(gc_green) + '  ')

    # no drop talley $$ no_drop_tally + NO DROP items
    no_drop_tally = len(no___drop)
    printed_nd_talley_terminal = "x" + str(no_drop_tally) + " NO DROP items\n--------------------------  "
    printed_nd_talley = "\nx" + str(no_drop_tally) + " NO DROP items\n--------------------------  "
    print(printed_nd_talley_terminal)
    inventory_txt.write(str(printed_nd_talley))

####################### wiki 
def wikicode():
    wiki_code = open('wikicode.txt', 'w+')
    blank_section_header = '==  =='
    newline = '\n'

    gearcost_code = str(blank_section_header) + str(newline) + '{| ' + str(newline) + '|- ' + str(newline) + '! scope="col" style="width: 222px; text-align: left;" | ' + str(charname) + '`s Inventory' + str(newline) + '! scope="col" style="text-align: left;" | Value ' + str(newline) + '|- ' + str(newline) + '| Blue || ' + str(gc_blue) + str(newline) + '|- ' + str(newline) + '| Green || ' + str(gc_green) + str(newline) + '|- ' + str(newline) + '| NO DROP || ' + str(no_drop_tally) + str(newline) + '|} '
    
    wiki_code.write(str(gearcost_code))
    print('...Done!')

def ask_wikicode():
    print(" ")
    code_answer = input('Would you like a nice table-code for the wiki? [yes] / [no] ')
    if code_answer == 'yes':
        print('Creating wikicode.txt...')
        wikicode()
    elif code_answer == 'no':
        print('See ya!')

####################### wiki 

no___drop = []
blue__gearcost = []
green__gearcost = []

def get_item_name(slot_number):
    #    global blue__gearcost
    #    global green__gearcost
    #    global no___drop
    #    global no_drop_tally
        
    while slot_number <= max_items:
        if slot_number == max_items:
            thegearcost()
            ask_wikicode()
            
        print(' ')
        inventory_txt.write('\n')
        
        item_name = str(inventory[slot_number]).replace('https://wiki.project1999.com/', '')
        item_name = item_name.replace('_', ' ')
        print(item_name)
        inventory_txt.write(str(item_name)+'\n')
        
        cycle_item_url = str(inventory[slot_number])
        r_itemurl = requests.get(cycle_item_url)
        soup_itemurl = BeautifulSoup(r_itemurl.text, 'html.parser')

        def get_item_price():
            global blue_nerd
            global green_nerd
            

            def green_nerd():
                green__report_terminal = '  Green 30-Day Average: ' + str(gmoney)
                green__report = '  Green 30-Day Average: ' + str(gmoney) + '\n'
                print(green__report_terminal)
                inventory_txt.write(green__report)
                green__gearcost.append(green__report)
                    
            def blue_nerd():
                blue__report_terminal = '  Blue 30-Day Average: ' + str(bmoney)
                blue__report = '  Blue 30-Day Average: ' + str(bmoney) + '\n'
                print(blue__report_terminal)
                inventory_txt.write(blue__report)
                blue__gearcost.append(blue__report)
                
            if soup_itemurl.find("div", {"id": "auc_Blue"}) != None or soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                price_div = soup_itemurl.find("div", {"class": "auctrackerbox"})
                if soup_itemurl.find("div", {"id": "auc_Blue"}) != None and soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                    price_blue = soup_itemurl.find("div", {"id": "auc_Blue"})
                    price_tab_blue = price_blue.find("table", {"class": "eoTable3"})
                    blue_item = price_tab_blue.find("td")
                    bmoney = blue_item.get_text().replace('±', '+')
                    bmoney = find_sum(bmoney)
                    
                    blue_nerd()
                    
                    price_green = soup_itemurl.find("div", {"id": "auc_Green"})
                    price_tab_green = price_green.find("table", {"class": "eoTable3"})
                    green_item = price_tab_green.find("td")
                    gmoney = green_item.get_text().replace('±', '+')
                    gmoney = find_sum(gmoney)
                    
                    green_nerd()
                    
                if soup_itemurl.find("div", {"id": "auc_Blue"}) != None and soup_itemurl.find("div", {"id": "auc_Green"}) == None:
                    blue_no_green_prices = '  Prices found for Blue, but, No prices found for Green.'
                    print(blue_no_green_prices)
                    inventory_txt.write(blue_no_green_prices)

                    price_blue = soup_itemurl.find("div", {"id": "auc_Blue"})
                    price_tab_blue = price_blue.find("table", {"class": "eoTable3"})
                    blue_item = price_tab_blue.find("td")
                    bmoney = blue_item.get_text().replace('±', '+')
                    bmoney = find_sum(bmoney)
                    
                    blue_nerd()
                    
                if soup_itemurl.find("div", {"id": "auc_Blue"}) == None and soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                    green_no_blue_prices = '  Prices found for Green, but, No prices found for Blue.'
                    print(green_no_blue_prices)
                    
                    price_green = soup_itemurl.find("div", {"id": "auc_Green"})
                    price_tab_green = price_green.find("table", {"class": "eoTable3"})
                    green_item = price_tab_green.find("td")
                    gmoney = green_item.get_text().replace('±', '+')
                    gmoney = find_sum(gmoney)
                    
                    green_nerd()
                    
                    inventory_txt.write(green_no_blue_prices)
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
            no___drop.append('nodrop')
            print('  ' + 'NO DROP')
            inventory_txt.write('  NO DROP'+'\n')  
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


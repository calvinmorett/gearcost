# def gcscrape(url):
#     # code to set up initial scraping process

#     # create a while loop to continue scraping until there are no more items in inventory
#     while inventory:
#         for item in inventory:
#             # code to scrape individual item page

#             # remove item from inventory list after it has been scraped
#             inventory.remove(item)

#         # code to scrape next page of inventory, if there is one
#         # update the inventory list with the items on the next page



from bs4 import BeautifulSoup
import requests
from datetime import date
from urllib.parse import urljoin
from sympy import *
import re

# to fix ssl issues, install them using pip
# pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user pip-system-certs'

"""
    Calculates the average cost of a list of inventory items, from a Character's Magelo URL.
    
    variable definitions:
        now (string) = capture the current date of the initial webscraping
        base (string) = the url of the base of the website, this is useful when doing a join later into the file, can call this back, for repeatable patterns w/in the URL.
        url = the profile that contains the inventory of items that will be averaged, and calculated. Total cost, and per item a 30-day average.
              intended to be used as an 'input' for a user to easily paste a URL and get results.
        
        r = makes a request to the wiki profile page
        soup = takes the request and parses the html document
        mw = find the div where the class matches, then use `connie`
        connie = will find, all the links contained within `mw`
        
        inventory (list, array) = empty list, that eventually is appended to. `connie` collects all links, then per link, appends them to this list. 
        max_items = the number of links contained within the inventory array/list. cycle_item_count uses this # to break the webscraping.
        cycle_item_count = serves as a counter, to break the script so it doesn't run infinitely. after running through the code, it will add a 1 to the count/counter.
                           it is the number of items we've gone through within the inventory. It starts on 0, and if it hits the `max_items` number, it will stop/break the code.
                     
        inventory_txt = this will open a text file for us to export each output to.
                
    Returns:
        @BUG - https://github.com/calvinmorett/gearcost/issues/5
        find_sum: returns a 30 day average, or 0 if there is none sold within that time period. it does not work as intended when running the script 1/10/22. 
        y: ...
    
"""
now = str(date.today())

base = 'http://wiki.project1999.com/'
url = "http://wiki.project1999.com/Magelo_Green:Ibol"
# url = input("Your Magelo URL: ")

if 'Blue' in url:
    charname = url.replace('http://wiki.project1999.com/Magelo_Blue:', '')
elif 'Green' in url:
    charname = url.replace('http://wiki.project1999.com/Magelo_Green:', '')
elif 'Red' in url:
    print('Red is dead.')

# code to set up initial scraping process  
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

inventory = []
mw = soup.find("div", {"class": "IventoryOuter"})
connie = mw.findAll('a')

#   the actual html a:link within the inventory on the page is coded like ...
#             <a href="/Chipped_Bone_Bracelet">
#             This is why it's important to `urljoin` the base w/ this link
#             `/Chipped` turns into `https://www.x.com/Chipped`
for link in connie:
    if link.has_attr('href'):
        relative = link['href']
        item_name = urljoin(base, relative)
        inventory.append(item_name)

max_items = len(inventory)
print('items = ',max_items)
cycle_item_count = 0

inventory_txt = open('inventory.txt', 'w+')

# @BUG - Not working as intended. 30d average online displays 42, script displays 22. Not actually taking the 30d average, taking an all time average.
def find_sum(str1):
    add_30day = sum(map(int,re.findall('\d+',str1)))
    avg = add_30day/2
    if find_sum == 0:
        print('None sold in the last 30 days')
            
    return avg

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

            ### commenting out wikicode
####################### wiki 
# def wikicode():
#     wiki_code = open('wikicode.txt', 'w+')
#     blank_section_header = '==  =='
#     newline = '\n'

#     gearcost_code = str(blank_section_header) + str(newline) + '{| ' + str(newline) + '|- ' + str(newline) + '! scope="col" style="width: 222px; text-align: left;" | ' + str(charname) + '`s Inventory' + str(newline) + '! scope="col" style="text-align: left;" | Value ' + str(newline) + '|- ' + str(newline) + '| Blue || ' + str(gc_blue) + str(newline) + '|- ' + str(newline) + '| Green || ' + str(gc_green) + str(newline) + '|- ' + str(newline) + '| NO DROP || ' + str(no_drop_tally) + str(newline) + '|} '
    
#     wiki_code.write(str(gearcost_code))
#     print('...Done!')

# def ask_wikicode():
#     print(" ")
#     code_answer = input('Would you like a nice table-code for the wiki? [yes] / [no] ')
#     if code_answer == 'yes':
#         print('Creating wikicode.txt...')
#         wikicode()
#     elif code_answer == 'no':
#         print('See ya!')

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
            ### commenting out wikicode
            # ask_wikicode()
            
        print(' ')
        inventory_txt.write('\n')
        
        item_name = str(inventory[slot_number]).replace('http://wiki.project1999.com/', '')
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


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
        find_sum: returns a 30 day average, or 0 if there is none sold within that time period. it does not work as intended when running the script 1/10/22. 
        y: ...
"""
###############################################################################
"""
    Changelog
        1/10/22 - Removing wiki outputs.
                - Changing order of functions below where it's blue vs green, the `Blue` server should be first.
                - Adding reminders to places where terminal/cli gets an output/print, where I can add `yields`, that can be used on the flask-frontend.
                - Adding reminders to remove `text` related items, for frontend (# can remove any txt related items, for frontend code)
    Issues
        1/10/22 - 30d average calculated, is not a 30d average.
        https://github.com/calvinmorett/gearcost/issues/5      

"""

now = str(date.today())

base = 'http://wiki.project1999.com/'
# url = "http://wiki.project1999.com/Magelo_Green:Ibol"
url = input("Your Magelo URL: ")

if 'Blue' in url:
    charname = url.replace('http://wiki.project1999.com/Magelo_Blue:', '')
elif 'Green' in url:
    charname = url.replace('http://wiki.project1999.com/Magelo_Green:', '')
elif 'Red' in url:
    print('Red is dead.')
    # yield here...

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
print('items = ',max_items) # yield here...
cycle_item_count = 0

# can remove any txt related items, for frontend code
inventory_txt = open('inventory.txt', 'w+')

def find_sum(str1):
    add_30day = sum(map(int,re.findall('\d+',str1)))
    ## debug print
    #print(add_30day,'debug')
    if add_30day == 0:
        print('None sold in the last 30 days')
    return add_30day

print(" ")
print(" ")
gearcost__header = "== Calculated by gearcost on " + now + " ==\n"
print(gearcost__header)
inventory_txt.write(str(gearcost__header))

def thegearcost():
    ###############################################################################
    # Ibol's Inventory Value:
    # --------------------------
    # Blue: 500p
    # Green: 800p
    # x5 NO DROP items
    # --------------------------
    ###############################################################################
    markdown_newline = '  '
    global char_header
    global gc_blue
    global gc_green
    global no_drop_tally
    char_header = "\n" + charname+"`s Inventory Value\n--------------------------  "
    print(char_header)
    # yield here...
    inventory_txt.write(char_header) # can remove any txt related items, for frontend code

    # print for debugging:
    #print(blue__gearcost)
    gc_blue = find_sum(str(blue__gearcost))
    print('Blue: ' + str(gc_blue), markdown_newline)
    # yield here...
    inventory_txt.write('\nBlue: ' + str(gc_blue) + '  ') # can remove any txt related items, for frontend code
    
    # print for debugging:
    #print(green__gearcost)
    gc_green = find_sum(str(green__gearcost))
    print('Green: ' + str(gc_green), markdown_newline)
    # yield here...
    inventory_txt.write('\nGreen: ' + str(gc_green) + '  ') # can remove any txt related items, for frontend code

    # counts the number of NO DROP
    no_drop_tally = len(no___drop)
    printed_nd_talley_terminal = "x" + str(no_drop_tally) + " NO DROP items\n--------------------------  "
    printed_nd_talley = "\nx" + str(no_drop_tally) + " NO DROP items\n--------------------------  "
    print(printed_nd_talley_terminal)
    # yield here...
    inventory_txt.write(str(printed_nd_talley)) # can remove any txt related items, for frontend code
   

###############################################################################
# commenting out wikicode - 1/10/22
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
###############################################################################

no___drop = []
blue__gearcost = []
green__gearcost = []

def get_item_name(slot_number):     
    while slot_number <= max_items:
        if slot_number == max_items:
            # run the function until the inventory doesn't contain anymore items
            thegearcost()
            ###############################################################################
            # commenting out wikicode - 1/10/22
            # ask_wikicode()
            
        print(' ')
        # yield here...
        inventory_txt.write('\n') # can remove any txt related items, for frontend code
        
        item_name = str(inventory[slot_number]).replace('http://wiki.project1999.com/', '')
        item_name = item_name.replace('_', ' ')
        print(item_name)
        inventory_txt.write(str(item_name)+'\n') # can remove any txt related items, for frontend code
        
        cycle_item_url = str(inventory[slot_number])
        r_itemurl = requests.get(cycle_item_url)
        soup_itemurl = BeautifulSoup(r_itemurl.text, 'html.parser')

        def get_item_price():
            # these global functions handle the outputs you will see within the terminal and txt file
            global blue_nerd
            global green_nerd        
                    
            def blue_nerd():
                # intended for output within CLI terminal
                blue__report_terminal = '  Blue 30-Day Average: ' + str(bmoney)
                print(blue__report_terminal)  
                # yield here...
                              
                # intended for output within a text file
                blue__report = '  Blue 30-Day Average: ' + str(bmoney) + '\n' # can remove any txt related items, for frontend code
                inventory_txt.write(blue__report) # can remove any txt related items, for frontend code 
                blue__gearcost.append(blue__report) # can remove any txt related items, for frontend code
            
            def green_nerd():
                # intended for output within CLI terminal
                green__report_terminal = '  Green 30-Day Average: ' + str(gmoney)
                print(green__report_terminal)
                # yield here...
                
                # intended for output within a text file
                green__report = '  Green 30-Day Average: ' + str(gmoney) + '\n' # can remove any txt related items, for frontend code
                inventory_txt.write(green__report) # can remove any txt related items, for frontend code
                green__gearcost.append(green__report) # can remove any txt related items, for frontend code
                
            if soup_itemurl.find("div", {"id": "auc_Blue"}) != None or soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                price_div = soup_itemurl.find("div", {"class": "auctrackerbox"})
                if soup_itemurl.find("div", {"id": "auc_Blue"}) != None and soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                    price_blue = soup_itemurl.find("div", {"id": "auc_Blue"})
                    price_tab_blue = price_blue.find("table", {"class": "eoTable3"})
                    blue_item = price_tab_blue.find("td")                   
                    blue_item = blue_item.get_text().replace('±', '+')    
                    blue_item = blue_item.split("+")[0]
                    ## debug print
                    #print(blue_item, 'debug............')
                    bmoney = find_sum(blue_item)
                    
                    # these global functions handle the outputs you will see within the terminal and txt file
                    blue_nerd()
                    
                    price_green = soup_itemurl.find("div", {"id": "auc_Green"})
                    price_tab_green = price_green.find("table", {"class": "eoTable3"})
                    green_item = price_tab_green.find("td")
                    green_item = green_item.get_text().replace('±', '+')  
                    green_item = green_item.split("+")[0]
                    ## debug print
                    #print(green_item, 'debug............')
                    gmoney = find_sum(green_item)

                    # these global functions handle the outputs you will see within the terminal and txt file
                    green_nerd()
                    
                if soup_itemurl.find("div", {"id": "auc_Blue"}) != None and soup_itemurl.find("div", {"id": "auc_Green"}) == None:
                    blue_no_green_prices = '  Prices found for Blue, but, No prices found for Green.'
                    print(blue_no_green_prices)
                    # yield here...
                    inventory_txt.write(blue_no_green_prices) # can remove any txt related items, for frontend code

                    price_blue = soup_itemurl.find("div", {"id": "auc_Blue"})
                    price_tab_blue = price_blue.find("table", {"class": "eoTable3"})
                    blue_item = price_tab_blue.find("td")
                    bmoney = blue_item.get_text().replace('±', '+')
                    bmoney = find_sum(bmoney)
                    
                    # these global functions handle the outputs you will see within the terminal and txt file
                    blue_nerd()
                    
                if soup_itemurl.find("div", {"id": "auc_Blue"}) == None and soup_itemurl.find("div", {"id": "auc_Green"}) != None:
                    green_no_blue_prices = '  Prices found for Green, but, No prices found for Blue.'
                    print(green_no_blue_prices)
                    # yield here...
                    
                    price_green = soup_itemurl.find("div", {"id": "auc_Green"})
                    price_tab_green = price_green.find("table", {"class": "eoTable3"})
                    green_item = price_tab_green.find("td")
                    gmoney = green_item.get_text().replace('±', '+')
                    gmoney = find_sum(gmoney)
                    
                    # these global functions handle the outputs you will see within the terminal and txt file
                    green_nerd()
                    
                    inventory_txt.write(green_no_blue_prices) # can remove any txt related items, for frontend code
            else:
                print('No Prices Found')
                # yield here...

###############################################################################
# Future Features
        # # mw-content-text is main item page you need to ask if had
        # # related quest
        # # or item location displayed
        
        # item_page = soup_itemurl.find("div", {"id": "mw-content-text"})
        # item__page = item_page.text.strip(    

        
        # # quest
        # related_quest = soup_itemurl.find("span", {"id": "Related_quests"})
        # related_quest__header = related_quest.text.strip()
        
        # #drops from
        # drops_from = soup_itemurl.find("span", {"id": "Drops_From"})
        # drops_from__header = related_quest.text.strip()
        
        # #Player_crafted
        # player_crafted = soup_itemurl.find("span", {"id": "Player_crafted"})
        # player_crafted__header = player_crafted.text.strip()
        
        # collect_links = item_page.findAll("a", {"class": 'mw-redirect'})
        # collection_list = []
        
        # for link in collect_links:
        #     if link['href']:
        #         relative = link['href']
        #         collection_list.append(urljoin(base, relative))
        #         # print(collection_list)
###############################################################################

        check_no_drop = soup_itemurl.find("div", {"class": "itemdata"})
        item_stats = check_no_drop.text.strip()
        # debug print
        # print(item_stats)
        
        if 'DROP' in item_stats:
            no___drop.append('nodrop')
            print('  ' + 'NO DROP')
            # yield here...
            inventory_txt.write('  NO DROP'+'\n') # can remove any txt related items, for frontend code


###############################################################################
# Future Features
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
###############################################################################  

            slot_number += 1
            # debug print
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
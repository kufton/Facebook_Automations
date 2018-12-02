from os import system
import pyautogui
import time

# IMPORTANT: This Program only works on a Windiws Computer with Screen Size of 1920px * 1080px.
# In Chrome: 100% Zoom on Windows Chrome with Bookmarks Bar turned off and no downloads bar



first_list_of_days = [7,10,14,30,60,90,180,365]
full_list_of_days = [3,7,10,14,30,60,90,180,365]
list_of_days = [3,7,10,14,30,60,90,180]

def open_audiences():
	'''This function opens up the Business Manager drop down menu then brings you to the Audiences page.'''
	pyautogui.click(83,119) , time.sleep(.4) # Open Dropdown Menu
	pyautogui.click(1039,253) # Click on Audiences
	print("Please remove any of Facebooks messages altering the GUI then press enter")
	system('pause')

def define_client():
	client = str(input('Which client is this?: '))
	pyautogui.click(674,396) , time.sleep(.4) # Opens the Page selector to enter the correct client
	pyautogui.click(642,462) , time.sleep(.4) # Page selector search bar
	pyautogui.typewrite(client) , time.sleep(.4) # Enters correct client name to pull to the top of the list
	pyautogui.click(620,574) , time.sleep(.4) # Selects the top page result

def create_custom():
	'''This function opens up the "Custom Audience" creation menu from the audience creation page'''
	pyautogui.click(463,272) , time.sleep(.4) # Create Audience buttton
	pyautogui.click(474,317) # Custom Audience button
	time.sleep(1) # Wait for page to load

# Custom Audience Menu Functions

def engagement():
	'''Clicks on the "Engagement" button inside the "Custom Audience" creation menu.'''
	pyautogui.click(914,775) , time.sleep(.4)

def website_traffic():
	'''Clicks on the "Website Traffic" button inside the "Custom Audience" creation menu.'''
	pyautogui.click(710,470)
	time.sleep(.4)


# For Engagement Facebook Page Audiences

def fb_page():
	pyautogui.click(914,775) # Facebook Page button
	time.sleep(.4) # Wait for page to load


def fb_page_PE_days(days):
	pyautogui.doubleClick(1047,459) , time.sleep(.4) # Selects the number of days
	pyautogui.typewrite(str(days)) , time.sleep(.4) # Enters 3 as the number of days
	pyautogui.click(761,598) , time.sleep(.4) # Audience name field
	pyautogui.typewrite(f'PE - {days} Days') , time.sleep(.4)

def fb_page_PPE_days(days):
	pyautogui.doubleClick(1047,459) , time.sleep(.4) # Selects the number of days
	pyautogui.typewrite(str(days)) , time.sleep(.4) # Enters 3 as the number of days
	pyautogui.click(761,598) , time.sleep(.4) # Audience name field
	pyautogui.typewrite(f'PPE - {days} Days') , time.sleep(.4)

def fb_page_ppe():
	pyautogui.click(649,457) , time.sleep(.4) # Clicks on "Everyone who engaged with your Page"
	pyautogui.click(686,598) , time.sleep(.4) # Clicks on "People who engaged with any post or ad"

def fb_page_complete():
	pyautogui.click(1260,699) , time.sleep(.4) # Creates Audience
	pyautogui.click(1300,770) , time.sleep(.4) # Done

# For Website Traffic Audiences

def vc():
	pyautogui.click(670, 450) , time.sleep(.4)
	pyautogui.typewrite("ViewContent") , time.sleep(.4)
	pyautogui.click(670, 570) , time.sleep(.4)

def atc():
	pyautogui.click(670, 450) , time.sleep(.4)
	pyautogui.typewrite("AddToCart") , time.sleep(.4)
	pyautogui.click(670, 570) , time.sleep(.4)

def ic():
	pyautogui.click(670, 450) , time.sleep(.4)
	pyautogui.typewrite("InitiateCheckout") , time.sleep(.4)
	pyautogui.click(670, 570) , time.sleep(.4)

def pur():
	pyautogui.click(670, 450) , time.sleep(.4)
	pyautogui.typewrite("Purchase") , time.sleep(.4)
	pyautogui.click(670, 570) , time.sleep(.4)

def vc_days(days):
	pyautogui.doubleClick(860,450) , time.sleep(.4) # Selects the number of days
	pyautogui.typewrite(str(days)) , time.sleep(.4) # Enters 3 as the number of days
	pyautogui.click(770,650) , time.sleep(.4) # Audience name field
	pyautogui.typewrite(f'VC - {days} Days') , time.sleep(.4)


def atc_days(days):
	pyautogui.doubleClick(860,450) , time.sleep(.4) # Selects the number of days
	pyautogui.typewrite(str(days)) , time.sleep(.4) # Enters 3 as the number of days
	pyautogui.click(770,650) , time.sleep(.4) # Audience name field
	pyautogui.typewrite(f'ATC - {days} Days') , time.sleep(.4)


def ic_days(days):
	pyautogui.doubleClick(890,450) , time.sleep(.4) # Selects the number of days
	pyautogui.typewrite(str(days)) , time.sleep(.4) # Enters 3 as the number of days
	pyautogui.click(770,650) , time.sleep(.4) # Audience name field
	pyautogui.typewrite(f'IC - {days} Days') , time.sleep(.4)


def pur_days(days):
	pyautogui.doubleClick(850,450) , time.sleep(.4) # Selects the number of days
	pyautogui.typewrite(str(days)) , time.sleep(.4) # Enters 3 as the number of days
	pyautogui.click(770,650) , time.sleep(.4) # Audience name field
	pyautogui.typewrite(f'PUR - {days} Days') , time.sleep(.4)

def website_traffic_complete():
	pyautogui.click(1250,750) , time.sleep(.4)
	pyautogui.click(1250,800) , time.sleep(.4)
	time.sleep(.4)




# Audience Creators

def first_audience(days):
	create_custom()
	engagement()
	fb_page()
	define_client()
	fb_page_PE_days(days)
	fb_page_complete()

def create_pe_audience(days):
	create_custom()
	engagement()
	fb_page()
	fb_page_PE_days(days)
	fb_page_complete()

def create_ppe_audience(days):
	create_custom()
	engagement()
	fb_page()
	fb_page_ppe()
	fb_page_PPE_days(days)
	fb_page_complete()

def create_vc_audience(days):
	create_custom()
	website_traffic()
	vc()
	vc_days(days)
	website_traffic_complete()

def create_atc_audience(days):
	create_custom()
	website_traffic()
	atc()
	atc_days(days)
	website_traffic_complete()

def create_ic_audience(days):
	create_custom()
	website_traffic()
	ic()
	ic_days(days)
	website_traffic_complete()

def create_pur_audience(days):
	create_custom()
	website_traffic()
	pur()
	pur_days(days)
	website_traffic_complete()

# Audience Stack Creators

def create_pe_stack():
	for days in first_list_of_days:
		create_pe_audience(days)

def create_ppe_stack():
	for days in full_list_of_days:
		create_ppe_audience(days)

def create_vc_stack():
	for days in list_of_days:
		create_vc_audience(days)

def create_atc_stack():
	for days in list_of_days:
		create_atc_audience(days)

def create_ic_stack():
	for days in list_of_days:
		create_ic_audience(days)

def create_pur_stack():
	for days in list_of_days:
		create_pur_audience(days)


# Full Audience Stack

def audienceStack():
	first_audience(3)
	create_pe_stack()
	create_ppe_stack()
	create_vc_stack()
	create_atc_stack()
	create_ic_stack()
	create_pur_stack()


# Run

audienceStack()
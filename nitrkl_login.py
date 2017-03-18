#https://selenium-python.readthedocs.io/navigating.html
# We can switch between windows, alerts and can also add cookies.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get('https://mail.nitrkl.ac.in/')

#print(driver.current_url)          #to get the url of the current page
page_src=driver.page_source         #returns the page source of the current page
#print(page_src)

#assert "Python" in driver.title
#assert "No results found." not in driver.page_source

#element = driver.find_element_by_id("passwd-id")

##  ***  To clear the already set text from the brwoser input box *** ##
#username_box = driver.find_element_by_name("username")
#username_box.clear()

username = driver.find_element_by_name('username')
username.send_keys('114cs0089')

password = driver.find_element_by_name('password')
password.send_keys('i_have_to_enter_my_password_here')
password.submit()

# Assume the button has the ID "submit" :)
#driver.find_element_by_id("submit").click()

#element.get_attribute("value")

# To move forward and backward in driver window
#driver.forward()
#driver.back()

time.sleep(5) 
driver.quit()

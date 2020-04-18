from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username = input("Enter Username: ")
password = input("Enter Password: ")

driver = webdriver.Chrome() # may have to add path of webdriver in as parameter
driver.get("https://www.instagram.com/")
driver.implicitly_wait(10)

usernameBox= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
usernameBox.send_keys(username) # inputs username 
driver.implicitly_wait(10)

passwordBox = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
passwordBox.send_keys(password) #inputs password 
loginButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
loginButton.click() # clicks login button

driver.implicitly_wait(10)

prompt= driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
prompt.click() # clicks 'not now' (the first prompt that appears when signing in)







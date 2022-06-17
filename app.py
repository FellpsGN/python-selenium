from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(executable_path=r'\python-selenium\edge\msedgedriver.exe') #Seria o caminho até o executável do edge
driver.get("https://www.facebook.com/")

driver.find_element_by_name("email").send_keys("seuemail@email.com")
sleep(2)
driver.find_element_by_name("pass").send_keys("*******")
sleep(2)
driver.find_element_by_name("pass").send_keys(Keys.RETURN)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

driver.get("https://discord.com/login")
driver.find_element_by_name("email").send_keys("seuemail@email.com")

sleep(2)

driver.find_element_by_name("password").send_keys("*******")
driver.find_element_by_name("password").send_keys(Keys.RETURN)

sleep(20)



# driver.find_element_by_name("password").send_keys("testetesteteste")
# driver.find_element_by_name("password").send_keys(Keys.RETURN)

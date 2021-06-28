from selenium import webdriver
chrome_driver_path ="D:\\New folder\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name=driver.find_element_by_name("fName")
first_name.send_keys("vasavi")
last_name=driver.find_element_by_name("LName")
last_name.send_keys("s")
email=driver.find_element_by_name("email")
email.send_keys("vasavi@gmail.com")

submit=driver.find_element_by_css_selector("form button")
submit.click()
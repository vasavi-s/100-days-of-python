from selenium import webdriver
chrome_driver_path ="D:\\New folder\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.in/IFB-Fully-Automatic-Diva-Aqua-SX/dp/B071G3B81W/ref=lp_22489506031_1_5")
price=driver.find_element_by_id("priceblock_ourprice ")
print(price.text)

#driver.close()
driver.quit()
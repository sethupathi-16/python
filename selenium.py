from  selenium import webdriver
chrome_path ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.chrome(chrome_path)
driver.get("https://www.flipkart.com/mobile-phones-store")
driver.find_element_by_xpath("""//*[@id="container"]/div/""").click()
posts = driver.find-elements_by_class_name("class=_1fQZEK")
for post in posts:
    print(post.text)
  

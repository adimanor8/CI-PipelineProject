from selenium import webdriver
driver=webdriver.Chrome(executable_path='/Users/Owner2-pc/Downloads/chromedriver_win32/chromedriver.exe')

def h1():
    c1=driver.get("http://192.168.99.100:5000")
    l1=driver.find_element_by_xpath('//*[contains(text(),"Hello")]')
    print(l1.text)

h1()
# 控制 css
from selenium import webdriver

fp = webdriver.FirefoxProfile()
fp.set_preference('permissions.default.image', 2)
fp.set_preference("permissions.default.stylesheet", 2)
fp.set_preference("javascript.enabled", False)
driver = webdriver.Firefox(firefox_profile=fp, executable_path=r'C:\Users\严涛\Desktop\geckodriver.exe')
# 把上述地址改成你电脑中geckodriver.exe程序的地址
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

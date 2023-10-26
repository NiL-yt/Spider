from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\严涛\Desktop\geckodriver.exe")
driver.implicitly_wait(20)  # 隐性等待，最长等20秒
# 把上述地址改成你电脑中geckodriver.exe程序的地址
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(5)

for i in range(1, 11):
    print(f"----------开始爬取第{i}页的评论........ ----------")
    """
    switch_to.frame()用于解析iframe,用于实现点击效果
    """
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[title="라이브리 - 댓글영역"]'))
    """
    1.元素后加 [] -> []内包含的是元素拥有的属性，非值
    2.元素后加 . -> .后跟着的是元素的类名（class） 
    """
    bt = driver.find_element_by_css_selector('button[data-page="%d"]' % i)
    bt.click()
    time.sleep(5)

    driver.switch_to.default_content()
    driver.implicitly_wait(30)

    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[title="라이브리 - 댓글영역"]'))
    comment_list = driver.find_elements_by_css_selector('div.reply-wrapper')
    for comment in comment_list:
        name = comment.find_element_by_css_selector('li.writer-name').text
        times = comment.find_element_by_css_selector('div.reply-history-time').text
        content = comment.find_element_by_css_selector('div.reply-content').text
        print(f'网友{name} 于{times} 说：{content}', '\n')

    time.sleep(5)
    driver.switch_to.default_content()
    driver.implicitly_wait(30)

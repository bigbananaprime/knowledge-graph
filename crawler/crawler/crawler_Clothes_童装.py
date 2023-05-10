from selenium import webdriver  # 第三方库selenium
import time
import csv
import requests
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

# f = open('jd女装.csv', mode='a', encoding='utf-8', newline='')
# csv_writer = csv.DictWriter(f, fieldnames=[
#     '商品',
#     '价格',
#     '店铺',
#     '详情页',
#     '品牌',
#     '详情',
# ])
# csv_writer.writeheader()

# 打开浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.get('https://www.jd.com')
# 定位关键字+输入关键字
driver.find_element_by_css_selector("#key").send_keys('童装')
# # 定位搜索按钮+点击搜索
driver.find_element_by_css_selector(
    "#search > div > div.form > button > i").click()
# 等待网页加载(time <= 10s)
driver.implicitly_wait(10)

# 下滑浏览器


def drop_down():
    for x in range(1, 12, 2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


def get_shop_info():
    f = open('童装.csv', mode='a', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=[
        '商品',
        '价格',
        '店铺',
        '详情页',
        '品牌',
        '详情',
    ])
    csv_writer.writeheader()
    # 等待网页加载(time <= 10s)
    driver.implicitly_wait(10)
    # 获取商品数据
    drop_down()
    list = driver.find_elements_by_css_selector(".goods-list-v2 .gl-item")
    # print(list)
    for li in list:
        try:
            title = li.find_element_by_css_selector(
                '.p-name-type-2').text.replace('\n', '')  # 商品名称
            price = li.find_element_by_css_selector(
                '.p-price i').text.replace('\n', '')   # 价格
            shop_name = li.find_element_by_css_selector(
                '.p-shop a').text.replace('\n', '')   # 店铺名字
            href = li.find_element_by_css_selector(
                '.p-name a').get_attribute('href')  # 详情页
            # 打开标签页

            time.sleep(2)

            li.find_element_by_css_selector('.p-name a').click()

            # 切换到标签页
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(10)
            # 获取标签页数据
            div_list = driver.find_elements_by_xpath(
                '//*[@id="detail"]/div[2]/div[1]/div[1]')
            for div in div_list:
                pinpai = div.find_element_by_xpath(
                    '//*[@id="parameter-brand"]/li').text.replace('\n', '')
                xiangqing = div.find_element_by_xpath(
                    '//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]').text.replace('\n', '')
                # print(pinpai)
                # print(xiangqing)
            # print(driver_list)
            time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            dif = {
                '商品': title,
                '价格': price,
                '店铺': shop_name,
                '详情页': href,
                '品牌': pinpai,
                '详情': xiangqing,
            }
            csv_writer.writerow(dif)
            print(title, price, shop_name, href, pinpai, xiangqing)
        except:
            continue
        f.close


for page in range(1, 151):
    print(f'正在采集第{page}页的数据内容')
    get_shop_info()
    driver.find_element_by_css_selector('.pn-next').click()

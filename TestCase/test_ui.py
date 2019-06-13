#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from time import sleep

from selenium import webdriver


class Test_ui():
    def test_demo(self):
        driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.implicitly_wait(8)  # 设置隐式时间等待
        sleep(3)
        driver.quit()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from Common.Baseui import baseUI


class Test_mall():

    def test_login(self,driver):
        #使用baseUI
        base=baseUI(driver)
        #打开登录页面
        driver.get("http://192.168.60.132/#/login")
        #输入用户名
        base.send_keys("输入用户名",'''//input[@name="username"]''','admin')
        #输入密码
        base.send_keys("输入密码",'''//input[@name="password"]''','123456')
        #点击登录
        base.click("点击登录","""(//span[contains(text(),'登录')])[1]""")
        assert '首页' in driver.page_source
        sleep(3)
    def test_fahuo(self,driver):
        # 使用baseUI
        base = baseUI(driver)
        #点击订单 //span[@slot="title" and contains(text(),'订单')]
        base.click("点击订单",'''//span[@slot="title" and contains(text(),'订单')]''')
        #点击订单列表 //span[contains(text(),'订单列表')]
        base.click("点击订单列表",'''//span[contains(text(),'订单列表')]''')
        #点击订单状态 //label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态",'''//label[contains(text(),'订单状态：')]/following-sibling::div//input''')
        #点击待发货 //span[contains(text(),'待发货')]
        base.click("点击待发货",'''//span[contains(text(),'待发货')]''')
        #点击查询搜索 //span[contains(text(),'查询搜索')]
        base.click("点击查询搜索",'''//span[contains(text(),'查询搜索')]''')
        #点击第一笔订单的订单发货 //tbody/tr[1]/td[10]//span[contains(text(),'订单发货')]
        base.click("点击第一笔订单的订单发货",'''//tbody/tr[1]/td[10]//span[contains(text(),'订单发货')]''')
        assert "发货列表" in driver.page_source
        #点击物流公司
        #选择圆通快递
        #输入物流单号
        #点击确定
        #点击确定
        #获取提示文本
        #断言

        sleep(3)
        pass

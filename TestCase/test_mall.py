#! /usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest



class Test_mall():

    @pytest.mark.fahuo
    def test_fahuo(self,base):
        base.driver.get("http://192.168.60.132/#/oms/order")
        #点击订单状态 //label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态",'''//label[contains(text(),'订单状态：')]/following-sibling::div//input''')
        #点击待发货 //span[contains(text(),'待发货')]
        base.click("点击待发货",'''//span[contains(text(),'待发货')]''')
        #点击查询搜索 //span[contains(text(),'查询搜索')]
        base.click("点击查询搜索",'''//span[contains(text(),'查询搜索')]''')
        #点击第一笔订单的订单发货 //tbody/tr[1]/td[10]//span[contains(text(),'订单发货')]
        base.click("点击第一笔订单的订单发货",'''//tbody/tr[1]/td[10]//span[contains(text(),'订单发货')]''')
        assert "发货列表" in base.driver.page_source
        #点击物流公司 //tbody/tr[1]/td[6]//input
        base.click("点击物流公司",'''//tbody/tr[1]/td[6]//input''')
        #选择圆通快递//span[contains(text(),'圆通')]
        base.click("选择圆通快递",'''//span[contains(text(),'圆通')]''')
        #输入物流单号//tbody/tr[1]/td[7]//input
        base.send_keys("输入物流单号","//tbody/tr[1]/td[7]//input","8912831293")
        #点击确定//span[contains(text(),'确定')]
        base.click("点击确定","//span[contains(text(),'确定')]")
        #点击确定//div[@role="dialog"]//span[contains(text(),'确定')]
        base.click("点击确定",'''//div[@role="dialog"]//span[contains(text(),'确定')]''')
        #获取提示文本//div[@role="alert"]//p
        text = base.get_text("获取提示文本",'''//div[@role="alert"]//p''')
        #断言
        assert "发货成功" in text

        sleep(3)
        pass

    @pytest.mark.tuihuo
    def test_tuihuo(self,base):
        base.driver.get("http://192.168.60.132/#/oms/returnApply")
        #点击处理状态//label[contains(text(),"处理状态：")]/following-sibling::div//input
        base.click("点击处理状态",'''//label[contains(text(),"处理状态：")]/following-sibling::div//input''')
        #点击待处理//span[contains(text(),"待处理")]
        base.click("点击待处理",'''//span[contains(text(),"待处理")]''')
        #点击查询搜索//span[contains(text(),"查询搜索")]
        base.click("点击查询搜索",'''//span[contains(text(),"查询搜索")]''')
        #点击第一笔订单的查看详情//tbody/tr[1]/td[8]//span[contains(text(),'查看详情')]
        base.click('点击第一笔订单的查看详情','''//tbody/tr[1]/td[8]//span[contains(text(),'查看详情')]''')
        #滚动窗口
        base.scroll_screen("滚动窗口")
        #获取订单金额//div[contains(text(),'订单金额')]/following-sibling::div
        money = base.get_text("获取订单金额", '''//div[contains(text(),'订单金额')]/following-sibling::div''')
        money=money[1:]
        #输入退款金额//div[contains(text(),'确认退款金额')]/following-sibling::div//input
        base.send_keys("输入退款金额",'''//div[contains(text(),'确认退款金额')]/following-sibling::div//input''',str(money))
        #点击确认收货//span[contains(text(),'确认退货')]
        base.click("点击确认收货",'''//span[contains(text(),'确认退货')]''')
        #点击确定//span[contains(text(),'确定')]
        base.click('点击确定','''//span[contains(text(),'确定')]''')
        #获取操作提示文本//div[@role="alert"]//p
        actual = base.get_text("获取操作提示文本",'''//div[@role="alert"]//p''')
        #断言
        assert '操作成功' in actual


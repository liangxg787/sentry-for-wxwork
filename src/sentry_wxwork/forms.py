# -*- coding: UTF-8 -*-
"""
@Time : 2022/1/20 2:34 PM
@Author : xiaoguangliang
@File : forms.py
@Project : sentry-for-wxwork
"""
from django import forms


class WxWorkOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='WxWork robot access_token'
    )

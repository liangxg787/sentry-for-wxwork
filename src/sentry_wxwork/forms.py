# coding: utf-8

from django import forms


class WxWorkOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='WxWork robot access_token'
    )

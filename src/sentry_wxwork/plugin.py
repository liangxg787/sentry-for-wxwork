# -*- coding: UTF-8 -*-
"""
@Time : 2022/1/20 2:34 PM
@Author : xiaoguangliang
@File : plugins.py
@Project : sentry-for-wxwork
"""

import json

import requests
from sentry.plugins.bases.notify import NotificationPlugin

import sentry_wxwork
from .forms import WxWorkOptionsForm

WxWork_API = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={token}"


class WxWorkPlugin(NotificationPlugin):
    """
    继承sentry的消息插件，构建基于企微群机器人的报警插件
    Sentry plugin to send error counts to wxwork.
    """
    author = 'Ngenie'
    author_url = 'https://github.com/liangxg787/sentry-for-wxwork'
    version = sentry_wxwork.VERSION
    description = 'Send error counts to wxwork.'
    resource_links = [
        ('Source', 'https://github.com/liangxg787/sentry-for-wxwork'),
        ('Bug Tracker', 'https://github.com/liangxg787/sentry-for-wxwork/issues'),
        ('README', 'https://github.com/liangxg787/sentry-for-wxwork/tree/main#readme'),
    ]

    slug = 'WxWork'
    title = 'WxWork'
    conf_key = slug
    conf_title = title
    project_conf_form = WxWorkOptionsForm

    def is_configured(self, project):
        """
        校验token
        @param project:
        @return:
        """
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        """
        给用户发消息
        @param group:
        @param event:
        @param args:
        @param kwargs:
        @return:
        """
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        post请求企微群机器人
        @param group:
        @param event:
        @param args:
        @param kwargs:
        @return:
        """
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        access_token = self.get_option('access_token', group.project)
        send_url = WxWork_API.format(token=access_token)
        title = u'【%s】的项目异常' % event.project.slug

        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": u"## {title} \n\n > {message} \n\n [详细信息]({url})".format(
                    title=title,
                    message=event.title or event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.event_id), )
            }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )


if __name__ == "__main__":
    pass

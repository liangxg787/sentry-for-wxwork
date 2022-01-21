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

        result = self.get_option('access_token', group.project)
        # 支持在企微群聊机器人的key值后面添加，指定该项目的负责人，方便在群聊中@该负责人，格式为{key}_{name}
        results = result.split('_')
        name = ''
        if len(results) == 1:
            # 如果没有按照格式要求配置key，或者只配置了key没有配置名字，则默认配置的只有key
            access_token = results[0]
        else:
            access_token, name = results
        send_url = WxWork_API.format(token=access_token)
        title = u'【%s】的项目异常' % event.project.slug

        if name:
            data = {
                "msgtype": "text",
                "text": {
                    "content": f"@{name}",
                }
            }
            self.post_request(send_url, data)

        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": u"## {title} \n\n > {message} \n\n [详细信息]({url})".format(
                    title=title,
                    message=event.title or event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.event_id), )
            }
        }
        self.post_request(send_url, data)

    @staticmethod
    def post_request(send_url, data):
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )


if __name__ == "__main__":
    pass

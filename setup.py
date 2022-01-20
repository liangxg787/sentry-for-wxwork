# -*- coding: UTF-8 -*-
"""
@Time : 2022/1/20 2:34 PM
@Author : xiaoguangliang
@File : setup.py
@Project : sentry-for-wxwork
"""
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sentry-for-wxwork",
    version='1.0.0',
    author='Ngenie',
    author_email='hplxg@hotmail.com',
    url='https://github.com/liangxg787/sentry-for-wxwork',
    description='A Sentry extension which send errors stats to WxWork',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry wxwork',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_wxwork = sentry_wxwork.plugin:WxWorkPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)

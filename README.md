# Sentry-for-WxWork
# 1 项目介绍
本项目是模仿[sentry-10-dingding](https://github.com/FeSeason/sentry-10-dingding.git)，专为企业微信群聊机器人写的报警消息插件。
如果你想使用钉钉的机器人作为sentry报警的工具，可以去使用[sentry-10-dingding](https://github.com/FeSeason/sentry-10-dingding.git)
# 2 使用方法
## 2.1 安装
可以修改sentry项目中requirement.txt文件，增加sentry-for-wxwork
```
# requirement.txt

sentry-for-wxwork
```
然后使用以下docker命令重新部署即可
```bazaar
# 目前，对于self-hosted版本的开源sentry来说，需要先运行
./install.sh

# 然后在运行
docker-compose up -d 
```
如果是你的sentry服务已经部署好了，依然需要重新运行上面两个命令，才能重新安装好新的插件

## 2.2 使用
### 2.2.1 先在整个sentry的Settings里面找到WxWork，如下图所示
![找到Wxwork](images/Wxwork.png)
### 2.2.2 然后在可以在你所建的项目的Settings中找到 Legacy integrations, 在里面把WxWork打开
![找到Legacy_ntegrations](images/Legacy_ntegrations.png)
### 2.2.3 然后刷新一下，可以在你所建的项目中，看到WxWork，接着配置上你的token即可，如下图所示。
注意，这里的token，即为你在配置企微群机器人得到的url中的key的值。
![找到token](images/token.png)

# 3 FAQ
如果您在使用过程中，有任何问题，可以给我提交issue



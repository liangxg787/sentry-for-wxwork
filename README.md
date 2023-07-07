<h1 align="center">Sentry-for-WxWork</h1>
<div align="center">

This project is a plugin designed specifically for enterprise WeChat group chat robots, mimicking <a href="https://github.com/FeSeason/sentry-10-dingding.git">sentry-10-dingding</a> for <a href="https://github.com/getsentry/sentry">sentry</a>, 
for writing alarm messages. If you want to use a DingTalk robot as a tool for sentry alarms, you can use sentry-10-dingding.

Languages： English | [中文](README_CN.md)
</div>


# 1 Installation
You can modify the requirement.txt file in the Sentry project and add "sentry-for-wxwork."
```
# requirement.txt

sentry-for-wxwork
```
Then you can redeploy using the following Docker command.
```
# Currently, for the self-hosted open-source version of Sentry, it is necessary to run the following command first.
./install.sh

# And then run the following command.
docker-compose up -d 
```
If your Sentry service is already deployed, you still need to run the above two commands again in order to reinstall the new plugin.

# 2 Usage
## 2.1 First, find "WxWork" in the Settings of the entire Sentry, as shown in the following image.
![To Wxwork](images/Wxwork.png)
## 2.2 Then, you can find "Legacy integrations" in the Settings of the project you created, and enable WxWork inside it.
![To Legacy_ntegrations](images/Legacy_ntegrations.png)
## 2.3 Then refresh the page, and you will be able to see WxWork in the project you created. Proceed to configure your token, as shown in the following image.
Note that the token mentioned here refers to the value of the key in the URL you obtained while configuring the WeChat Work group chat robot.
The new version supports adding the name of the project owner, making it convenient to mention (@) the relevant responsible person in the group chat. After the key value of the WeChat Work group chat robot, you can add the specified project owner by following the format: {key}_{name}. This allows you to mention the project owner in the group chat.
![find token](images/token.png)

# 3 FAQ
If you encounter any issues during your usage, you can submit an issue to me.



## 微博热搜历史记录

微博热搜历史记录，互联网人的记忆

后端运行于Linux服务器，每5分钟抓取一次微博热搜榜
通过crontab定时执行脚本，半小时commit一次，每小时向Github push一次

Python Script 根据(weibo_Hot_Search项目)[https://github.com/Writeup001/weibo_Hot_Search]修改，感谢Writeup大佬的项目支持

## 运行环境安装与配置
### Python脚本运行环境
- 安装 Python 3.0 +
Debian/Ubuntu用户使用apt安装
```
apt install python3 python3-pip
```
- 安装Python依赖包: requests lxml
```
pip install requests

pip install
```
完成Python运行环境安装(国内pip换源访问问题请搜索'pip换源'解决)
## 运行
### Linux用户
给予Python脚本运行权限，可直接执行
```
chmod +x WeiBoHot_history.py
./WeiBoHot_history.py
```
若无法运行，尝试
```
python WeiBoHot_history.py
```
或
```
python3 WeiBoHot_history.py
```
### 自动化git脚本配置
WeiBoHot_history.py & Auto-git.sh & Auto-push.sh均用crontab执 行

给予执行权限
```
chmod +x ./*
```
配置Crontab
```
# Weibo Hot script begin
*/5 * * * * cd $YOUR_PATH/WeiBoHot_history;python3 ./WeiBoHot_history.py
*/30 * * * * sh $YOUR_PATH/WeiBoHot_history/Auto-git.sh YOUR_PATH/WeiBoHot_history
0 * * * * sh $YOUR_PATH/WeiBoHot_history/Auto-push.sh $YOUR_PATH/WeiBoHot_history
#Weibo Hot script end
```
## 数据来源
新浪微博公开热搜榜单: https://s.weibo.com/top/summary/

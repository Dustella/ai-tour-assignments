# 夸夸！！！

## 基于话题相似度的夸夸机器人

项目地址 https://github.com/Dustella/kuakua/

原作者[@Hualong_Zhang](https://github.com/xiaopangxia)

我(特菈 Dustella)修复了模块的若干问题，优化目录结构，去除了基于 chatterbot 的部分，提供了一个 flask 后端。

语料来自豆瓣表扬小组，详见https://github.com/xiaopangxia/kuakua_corpus

相似度采用 TF-IDF、LSI、LDA 等，搜索 top4 相似话题的回复，从中随机返回表扬语句，效果还不错。

![](https://raw.githubusercontent.com/xiaopangxia/kuakua_robot/master/image/kukua_2.PNG)

## 食用方法

将 sim_kuakua 移动到项目文件夹，在你的项目内使用

```Python
from sim_kuakua import kuakuaChat
```

### 直接在项目中调用

```Python
input="" #输入语句
bot=kuakuaChat()
answerList=bot.answer_question(input)
```

会返回一个回答的 List

### 启动服务器

```Python
bot=kuakuaChat()
bot.start_server()
```

这样会在 5000 端口启动一个服务器。

请求 /getKuakua ,附加 payload sentence={输入}

样例：

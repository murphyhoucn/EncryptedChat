# EncryptedChat

描述： 腾讯QQ聊天消息加密

[murphyhoucn/EncryptedChat](https://github.com/murphyhoucn/EncryptedChat)

[博客地址：QQ聊天框消息加密](https://cosmicdusty.cc/post/QQ%E8%81%8A%E5%A4%A9%E6%A1%86%E6%B6%88%E6%81%AF%E5%8A%A0%E5%AF%86)

[视频演示："加密对话"EncryptedChat](https://www.bilibili.com/video/BV1KT4y1S7kF?spm_id_from=333.999.0.0)

# 使用

使用 git 将仓库代码 clone 到本地或者下载打包好的 .zip 仓库文件。

``` bash
git clone https://github.com/murphyhoucn/EncryptedChat.git
```

文件目录结构

``` bash
D:\Develop_GitHub\MurphyHouCN\EncryptedChat
├─.gitignore
├─Encrypt.py
├─EncryptChat.exe
├─FilesStructure.md
├─GUI.py
├─ICON.ico
├─LICENSE
├─README.md
├─.git
```

如果只是使用该软件的话，可以直接在`命令行`运行或者双击`EncryptChat.exe`

``` bash
# 例如
D:\Develop_GitHub\MurphyHouCN\EncryptedChat>EncryptChat.exe
```

如果是更改程序代码的话，程序算法可在`Encrypt.py`中修改，GUI界面在`GUI.py`中修改

修改完成后，通过`PyInstaller`打包生成新的`.exe`文件，供自己或他人使用。

``` bash
pyinstaller -F- w -i ICON.ico Encrypt.py
```

# 学习

`EncryptChat.exe`的使用方法有演示视频：[视频演示："加密对话"EncryptedChat](https://www.bilibili.com/video/BV1KT4y1S7kF?spm_id_from=333.999.0.0)

`Encrypt.py`使用的算法在博客中有介绍：[博客地址：QQ聊天框消息加密](https://cosmicdusty.cc/post/QQ%E8%81%8A%E5%A4%A9%E6%A1%86%E6%B6%88%E6%81%AF%E5%8A%A0%E5%AF%86)

# 交流

如果有什么问题/想法可以通过以下方式，提出您的问题/想法：

1. 在GitHub仓库中提出一个Issues
2. 通过邮件联系到我：[Murphy](mailto:Murphy0928Hou@outlook.com)
3. 在博文最下面的评论区留下您的问题/想法




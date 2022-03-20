import sys
from PyQt5 import QtWidgets
from GUI import Ui_Form

import win32gui
import win32con
import win32clipboard as w
import  time

import base64
from Crypto.Cipher import AES

'''
采用AES对称加密算法
'''

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):

    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)

    # 获取窗口所输入的信息的函数
    def pushButton1_click(self):

        # 获取Windows界面输入的消息
        name=self.lineEdit_1.text()
        key=self.lineEdit_2.text()
        msg=self.lineEdit_3.text()

        # 对消息进行加密
        msg_encrypt=encrypt_oracle(key,msg)

        self.textEditi.setPlainText("加密信息如下：\n"+\
            "昵称:" + name +'\n'+\
            "密钥:" + key +'\n'+\
            "明文:" + msg +'\n'+\
            "暗文:" + msg_encrypt +'\n')
        start(name,msg_encrypt)

    def pushButton2_click(self):

        key=self.lineEdit_2.text()

        get_msg_encrypt=getText()
        # print(get_msg_encrypt)
        msg_decrypt=decrypt_oralce(key,get_msg_encrypt)

        self.textEdito.setPlainText("解密信息如下：\n"+\
            "暗文:" + get_msg_encrypt +'\n'+\
            "明文:" + msg_decrypt +'\n')


# 输出相关函数
def start(name,msg_encrypt):


    # =====将消息复制到剪切板中=====

    w.OpenClipboard() #打开剪切板
    w.EmptyClipboard() #清空剪切板
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg_encrypt)  #将msg_encrypt设置给剪切板
    w.CloseClipboard() #关闭剪切板

    handle = win32gui.FindWindow(None, name) # 根据对方昵称获取窗口句柄
    win32gui.SendMessage(handle, 770, 0, 0) # 将剪切板内容填充消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0) # 按下回车发送消息


# 加密相关函数
# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

# 加密相关函数
# 加密方法
def encrypt_oracle(key0,msg):
    # 秘钥
    key = key0

    mystr=msg
    text = base64.b64encode(mystr.encode('utf-8')).decode('ascii')
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(text))
    # 用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    # print(encrypted_text) 测试打印加密数据
    return encrypted_text



# 解密
def decrypt_oralce(key0,msg):
    # 秘钥
    key = key0
    # 密文
    text=msg
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))

    # bytes解密
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8') # 执行解密密并转码返回str
    decrypted_text = base64.b64decode(decrypted_text.encode('utf-8')).decode('utf-8')
    # print(decrypted_text)

    return decrypted_text


def getText():  # 读取剪切板  
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d.decode('utf-8')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    
    # 窗口的打开和关闭
    my_pyqt_form.show()
    sys.exit(app.exec_())
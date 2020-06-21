# 普通二维码
# from MyQR import myqr
# myqr.run(words='https://me.csdn.net/github_35856054')
# # 带图片的艺术二维码
# from MyQR import myqr
# myqr.run(words='https://hao.360.com/',
#          picture='qrcode.png',
#          save_name='qr1.png',
#          colorized=True)
# 动态二维码
from MyQR import myqr
myqr.run(words='https://hao.360.com/',#网址
         picture='qakki.gif',#图片路径
         save_name='qr4.gif',#保存格式，要和选择图片格式一致
         colorized=True)

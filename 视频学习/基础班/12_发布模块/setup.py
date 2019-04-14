from distutils.core import setup

setup(name="hm_message",
      version="1.0",
      description="itheima`s 发送和接受消息模块",
      long_description="完整的发送和接受消息模块",
      author="itheima",
      author_email="itheima@itheima.com",
      url="www.itheima.com",
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/ch21.2.2.py

import cocos


# 自定义HelloWorld层类
class HelloWorld(cocos.layer.Layer):

    def __init__(self):
        super(HelloWorld, self).__init__()
        # 创建标签
        label = cocos.text.Label('Hello, World!',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')

        # 获得窗口的宽度和高度
        width, height = cocos.director.director.get_window_size()
        # 设置标签的位置
        label.position = width // 2, height // 2

        # 添加标签到HelloWorld层
        self.add(label)


if __name__ == "__main__":
    # 初始化导演，设置窗口的高、宽、标题
    cocos.director.director.init(width=640, height=480, caption="Hello World")

    # 创建HelloWorld层实例
    hello_layer = HelloWorld()

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = cocos.scene.Scene(hello_layer)

    # 开始启动main_scene场景
    cocos.director.director.run(main_scene)

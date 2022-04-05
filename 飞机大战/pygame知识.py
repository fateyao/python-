# 自己定义的文件名不要和模块名重名!!!
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pygame==1.9.6

# pygame使用
# 1.游戏的初始化和退出
# 要使用pygame提供的所有功能之前,需要调用init方法
# 在游戏结束之前需要调用quit方法
# import pygame
# pygame.init()
# print('游戏的代码')
# pygame.quit()

# 2.游戏中的坐标系
# x轴水平方向向右,逐渐增加
# y轴垂直方向向下,逐渐增加
# 在游戏中,所有可见的元素都是以矩形区域来描述位置的,要描述一个矩形区域有四个元素
# (x, y)起始点的横纵坐标
# (width, height)矩形的宽度和高度
# pygame提供给了一个类pygame.Rect(x, y, width, height)
# import pygame
# rect = pygame.Rect(100, 50, 120, 125)
# print('矩形的原点:({},{})'.format(rect.x, rect.y))
# print('矩形的尺寸:({},{})'.format(rect.width, rect.height))

# 3.创建游戏的主窗口
# pygame提供了一个模块pygame.display用于创建,管理游戏窗口
# 初始化游戏窗口:pygame.display.set_mode()
# 刷新屏幕内容显示:pygame.display.update()

# set_mode(resolution=(), flags=0, depth=0)
# 参数
# resolution指定屏幕的宽和高,默认创建的窗口大小和屏幕一致
# flags参数指定屏幕的附加选项,例如是否全屏等等,默认不需要传递
# depth参数表示颜色的位数,默认自动匹配
# 返回值
# 游戏的屏幕,游戏的元素都需要被绘制到游戏的屏幕上
# 注意:必须使用变量记录set_mode方法的返回结果

# import pygame
# import time
# pygame.init()
# # 创建游戏窗口 480*700
# screen = pygame.display.set_mode((480, 700))
# time.sleep(10)
# pygame.quit()

# 4.图像的绘制
# 在游戏中,能够看到的游戏元素大多都是图像
# 图像文件初始是保存在磁盘上的,如果需要使用则需要加载
# 要在屏幕上看到图像内容,需要三个步骤
# (1).使用pygame.image.load()加载图像数据
# (2).使用游戏屏幕对象,调用blit方法将图像绘制到指定位置
# (3)调用pygame.display.update()方法更新整个屏幕的显示
# import pygame
# pygame.init()
#
# # 创建游戏窗口
# screen = pygame.display.set_mode((480, 700))
#
# # 绘制背景图像
# # 1.加载图像数据
# bg = pygame.image.load('./images/background.png')
# # 2.绘制图像
# screen.blit(bg, (0, 0))
#
# # 绘制飞机图像
# plane = pygame.image.load('./images/me1.png')
# screen.blit(plane, (150, 150))
# # 3.更新屏幕显示
# pygame.display.update()
# while True:
#     pass

# 5.update()


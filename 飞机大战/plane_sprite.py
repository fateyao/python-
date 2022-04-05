# 精灵模块
# 飞机向上移动的效果:将背景图向下移动
import pygame
import random
# 敌机出现事件
ENEMY_EVENT = pygame.USEREVENT
# 发射子弹事件
FIRE = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    # 飞机大战的游戏精灵
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


# 背景精灵
class Background(GameSprite):

    def update(self):
        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕,如果移出屏幕,将图像设置到屏幕上方
        if self.rect.y >= 700:
            self.rect.y = -self.rect.height


# 敌机精灵
# 游戏启动后,每隔一秒会出现一架敌机
# 每架敌机向屏幕下方飞行,飞行速度各不相同
# 每架敌机出现的水平位置也不同
# 当敌机从屏幕下方飞出,不会回到屏幕中
# 在pygame中可以使用pygame.time.set_timer()来添加定时器
# set_timer()可以创建一个事件
# 第一个参数:事件代号(需要基于常量pygame.USEREVNET来指定)
# USEREVNET是一个整数,再增加的事件可以使用USEREVNET+1
# 第二个参数:事件触发间隔的毫秒值

# pygame定时器套路:
# 定义定时器常量
# 在初始化方法中,调用set_timer()方法
# 在游戏循环中,监听定时器事件

class Enemy(GameSprite):
    def __init__(self):
        super().__init__('./images/enemy1.png')
        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 指定敌机的初始随机位置
        self.rect.x = random.randint(0, 480-self.rect.width)

    def update(self):
        super().update()
        # 判断是否飞出屏幕,如果是,需要从精灵组删除敌机
        if self.rect.y >= 700:
            print('飞出屏幕,需要从精灵组删除')
            # kill()方法可以将精灵从所在的精灵组中移出,精灵就会自动销毁
            self.kill()


# 设计英雄飞机和子弹类
# 英雄需求
# 游戏启动后, 英雄飞机出现在水平中间位置,距离底部30
# 英雄飞机每隔0.5秒发射一次子弹,每次连发三颗子弹
# 英雄飞机不会移动,需要通过左右方向键,控制英雄飞机在水平方向上移动
# 子弹需求
# 子弹从英雄飞机的正上方发射沿直线向上飞机
# 飞出屏幕后,需要从精灵组中删除

# 捕获按键控制飞机的左右移动
# 首先通过pygame.key.get_pressed()返回所有按键元组
# 通过键盘常量,判断元组中某个键是否被按下,如果按下,对应数值为1
# 如:if keypressed[pygame.K_LEFT]:  # 判断向左的按键是否被按下

class Hero(GameSprite):
    # 调用父类方法,设置图片和速度
    def __init__(self):
        super().__init__('./images/me1.png', 0)
        # 设置英雄的初始位置
        self.rect.y = 700 - self.rect.height - 30
        self.rect.x = 240 - self.rect.width // 2
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 480 - self.rect.width:
            self.rect.x = 480 - self.rect.width

    def fire(self):
        print('发射子弹')
        for i in range(3):
            # 创建子弹精灵
            bullet = Bullet()
            # 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 将精灵添加到精灵组
            self.bullets.add(bullet)



class Bullet(GameSprite):
    def __init__(self):
        # 调用父类方法,设置子弹图片,设置初始速度
        super().__init__('./images/bullet1.png', -2)

    def update(self):
        # 调用父类的方法,让子弹沿着垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

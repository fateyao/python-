# 游戏初始化
# 设置游戏窗口
# 创建游戏时钟
# 创建精灵和精灵组

# 游戏循环
# 设置刷新帧率
# 事件监听
# 碰撞检测
# 更新/绘制精灵组
# 更新屏幕显示
import pygame
from plane_sprite import *
class PlaneGame:
    def __init__(self):
        print('游戏初始化')
        # 设置游戏窗口
        self.screen = pygame.display.set_mode((480, 700))
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法创建精灵和精灵组
        self.__create_sprite()
        # 设定一个定时器,每隔1000毫秒产生一个ENEMY_EVENT事件
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        # 设定一定时器,每隔500毫秒,发射一次子弹
        pygame.time.set_timer(FIRE, 500)

    # 创建精灵和精灵组
    def __create_sprite(self):
        # 创建背景精灵和精灵组
        bg1 = Background('./images/background.png')
        bg2 = Background('./images/background.png')
        bg2.rect.y = - bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print('游戏开始')
        while True:
            pass
            # 设置刷新帧率
            self.clock.tick(60)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprite()
            # 更新屏幕显示
            pygame.display.update()

    # 事件监听
    def __event_handler(self):
        # 获取按键
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif keypressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        else:
            self.hero.speed = 0

        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == ENEMY_EVENT:
                print('敌机出场')
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == FIRE:
                self.hero.fire()

    # 碰撞检测
    # 子弹撞毁敌机
    # 敌机撞毁英雄飞机
    # groupcollide(group1, group2, dokill1, dokill2, collided=None)用法
    # group1和group2代表这两个检测的精灵组
    # 如果将dokill设置为True,则发生碰撞的精灵将被自动移除
    # collided参数用来计算碰撞的回调函数,如果没有指定,则每个精灵必须有一个rect属性
    # 不发生碰撞返回空字典,发生碰撞返回有值字典(组1为键,组2为值)
    def __check_collide(self):
        # 子弹和敌机相撞(都会消失)
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 英雄飞机和敌机相撞(游戏结束)
        rect = pygame.sprite.groupcollide(self.enemy_group, self.hero_group, True, True)
        if len(rect):
            pygame.quit()

    # 更新/绘制精灵组
    def __update_sprite(self):
        # 更新绘制背景精灵组
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 更新绘制敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 更新绘制英雄精灵组
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 子弹
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
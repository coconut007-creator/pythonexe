import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
def run_game():
    #初始化游戏，创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_length))
    pygame.display.set_caption("Alien Invasion")
    #设置背景颜色
    bg_color = (230, 230, 230)
    ship = Ship(ai_settings, screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        #每次循环重新绘制屏幕
        #让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship)

run_game()
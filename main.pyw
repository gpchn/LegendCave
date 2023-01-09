#!/usr/bin/env python3
# coding: utf-8


def main():
    # 导入第三方库
    import pygame
    import pygame.locals
    from sys import exit

    # 硬件初始化
    pygame.init()
    # 获取屏幕信息
    info = pygame.display.Info()
    # 全屏分辨率
    fullscreen = (info.current_w, info.current_h)
    # 1/4 全屏分辨率
    halfscreen = (info.current_w / 2, info.current_h / 2)
    # 现在是否是全屏
    fullscreen_now = False

    # 设置主屏窗口
    screen = pygame.display.set_mode(halfscreen)
    # 设置窗口标题
    pygame.display.set_caption("Legend Cave")
    # 导入字体类型
    f = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 30)

    # 主循环
    while True:
        # 生成文本信息，后面参数分别是：字体是否平滑，前景、背景色
        text = f.render("按 F11 切换全屏，ESC 或右上角“X”退出", True, (255, 255, 255), (0, 0, 0))
        # 获得 rect 区域坐标
        textRect = text.get_rect()
        # 设置坐标
        textRect.center = (300, 30)
        # 绘制到主屏幕
        screen.blit(text, textRect)

        # 监听事件
        for event in pygame.event.get():
            # 是否点了关闭按钮
            if event.type == pygame.QUIT:
                # 退出
                pygame.quit()
                exit()

            # 是否按下按键
            if event.type == pygame.locals.KEYDOWN:
                # 是否按下 ESC
                if event.key == pygame.locals.K_ESCAPE:
                    # 退出
                    pygame.quit()
                    exit()
                # 是否按下 F11
                if event.key == pygame.locals.K_F11:
                    # 现在是否是全屏
                    if fullscreen_now:
                        # 设置成 1/4 全屏
                        screen = pygame.display.set_mode(halfscreen)
                        fullscreen_now = False
                    # 现在不是全屏
                    else:
                        # 设置成全屏
                        screen = pygame.display.set_mode(fullscreen, pygame.locals.FULLSCREEN)
                        fullscreen_now = True
        
        # 刷新屏幕
        pygame.display.flip()


if __name__ == "__main__":
    main()

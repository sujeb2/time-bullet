import pygame, sys
from tkinter import messagebox

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (97, 97, 97)

# bool
isMainGameScene = False
isMainMenuScene = True

def quitGame():
    print("Exiting..")
    pygame.quit()
    sys.exit() # to make sure that game is closed.

# Image
print("Reading Images..")
try:
    img_backgroundLoop = pygame.image.load('./src/img/background/game_default_background.png')
    img_backgroundLoop = pygame.transform.scale(img_backgroundLoop,(1280, 720))
    img_gameLogo = pygame.image.load('./src/img/gameicon_placeholder.png')
    csrImg_Crosshair = pygame.image.load('./src/img/cursor/default-crosshair.png')
    print("Loaded.")
except Exception as e:
    messagebox.showerror(title='Error occurred', message=e)
    print("Error occurred while loading Images.")
    print("Is file even exists?")
    print(e)
    quitGame()

# 재설정
print("Initallizing..")
try:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    dt = 0
    display = pygame.display
    csrImg_rect = csrImg_Crosshair.get_rect()
    pygame.mouse.set_visible(False)
    print("Initallized.")
except Exception as e:
    messagebox.showerror(title='Error occurred', message=e)
    print("Error occurred while initallizing game.")
    print("May occurrs because of weird pygame bug lol")
    print(e)

# SFX / OST
print("Loading Sounds..")
try:
    # sfx
    sfx_HandgunFire1 = pygame.mixer.music.load('./src/sound/sfx/handgun/handgun_fire1.wav')
    sfx_HandgunNoAmmo = pygame.mixer.music.load('./src/sound/sfx/handgun/handgun_noammo.wav')
    sfx_HandgunReload = pygame.mixer.music.load('./src/sound/sfx/handgun/handgun_reload.wav')

    # ost
    ost_MainMenuAmbientLoop = pygame.mixer.music.load('./src/sound/ost/background_ambient1.wav')
    ost_MainMenuAmbientLoop = pygame.mixer.music.set_volume(45)
    print("Loaded.")
except Exception as e:
    messagebox.showerror(title='Error occurred', message=e)
    print("Error occurred while loading Sound.")
    print("Is file even exists?")
    print(e)
    quitGame()

# 폰트및 타이틀 재설정
print("Resetting Font/Title..")
try:
    display.set_caption('spsroEngine Scene Replayer')
    display.set_icon(img_gameLogo)

    # Font
    defaultFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 30)
    defaultCopyrightFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 20)

    print("Loaded.")
except Exception as e:
    messagebox.showerror(title='Error occurred', message=e)
    print("Error occurred while reseting font/title.")
    print("May occurrs because of weird pygame bug lol")
    print(e)
finally:
    if display.get_caption == '':
        display.set_caption('Caption not set.')

# 텍스트
print("Resetting text object..")
text_MainLogoTitle = defaultFont.render('게임이름을여기에입력', True, WHITE)
text_MainStartGame = defaultFont.render('START', False, WHITE)
text_MainLoadGame = defaultFont.render('LOAD', False, WHITE)
text_MainSetting = defaultFont.render('SETTING', False, WHITE)
text_MainExit = defaultFont.render('EXIT', False, WHITE)
text_copyrightTeamName = defaultCopyrightFont.render('SONGRO STUDIO_', True, GRAY)

# 메인
print("Replaying MainMenuScene..")
try:
    pygame.mixer.Sound.play(ost_MainMenuAmbientLoop, loops=-1)

    while isMainMenuScene:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isMainMenuScene = False
                isMainGameScene = False

        # render text
        screen.blit(text_MainLogoTitle, [200, 300])
        screen.blit(text_MainStartGame, [200, 342])
        screen.blit(text_MainLoadGame, [200, 372])
        screen.blit(text_MainSetting, [200, 402])
        screen.blit(text_MainExit, [200, 432])
        screen.blit(text_copyrightTeamName, [200, 465])

        pygame.display.flip()

        pygame.display.update()
        dt = clock.tick(300) / 700
except Exception as e:
    messagebox.showerror(title='Error occurred', message=e)
    print("Error occurred while replaying mainmenu scene.")
    print(e)

pygame.quit()
import pygame, sys
from tkinter import messagebox

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (97, 97, 97)

# bool
isMainGameScene = False
isMainMenuScene = True

# int
MaxHandgunBullet = 255
MaxMachineGunBullet = 255
MaxHandgunLoadBullet = 18
MaxMachinegunLoadBullet = 75

# str
str_MaxHandgunBullet = str(MaxHandgunBullet)
str_MaxMachineGunBullet = str(MaxMachineGunBullet)
str_MaxHandgunLoadBullet = str(MaxHandgunLoadBullet)
str_MaxMachinegunLoadBullet = str(MaxMachinegunLoadBullet)

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

    icn_bulletFull = pygame.image.load('./src/img/icon/indiv_icon/Bullet.png')
    icn_bulletFull = pygame.transform.scale(icn_bulletFull, (32, 32))
    icn_bulletEmpty = pygame.image.load('./src/img/icon/indiv_icon/BulletEmpty.png')
    icn_bulletEmpty = pygame.transform.scale(icn_bulletEmpty, (32, 32))
    icn_GunSelect_handGun = pygame.image.load('./src/img/icon/indiv_icon/Handgun.png')
    icn_GunSelect_handGun = pygame.transform.scale(icn_GunSelect_handGun, (32, 32))
    icn_GunSelect_machineGun = pygame.image.load('./src/img/icon/indiv_icon/Machinegun.png')
    icn_GunSelect_machineGun = pygame.transform.scale(icn_GunSelect_machineGun, (32, 32))
    
    hud_HealthFull = pygame.image.load('./src/img/hud/Health1.png')
    hud_HealthFull = pygame.transform.scale(hud_HealthFull, (32, 32))
    hud_HealthHalf = pygame.image.load('./src/img/hud/Health1Half.png')
    hud_HealthHalf = pygame.transform.scale(hud_HealthHalf, (32, 32))
    hud_HealthEmpty = pygame.image.load('./src/img/hud/HealthEmpty.png')
    hud_HealthEmpty = pygame.transform.scale(hud_HealthEmpty, (32, 32))
    
    hudBackground_weaponSelect = pygame.image.load('./src/img/hud/weapon_select.png')

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
    sfx_Handgun = ['./src/sound/sfx/handgun/handgun_fire1.wav', './src/sound/sfx/handgun/handgun_noammo.wav', './src/sound/sfx/handgun/handgun_reload.wav']
    sfx_smg = ['./src/sound/sfx/smg/smg_startloop.wav', './src/sound/sfx/smg/smg_loop.wav', './src/sound/sfx/smg/smg_endloop.wav', './src/sound/sfx/smg/smg_noammo.wav', './src/sound/sfx/smg/smg_realod.wav']
    sfx_Click = ['']

    # ost
    ost_MainMenu = './src/sound/ost/background_ambient1.wav'

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
    defaultBulletFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 24)

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

hud_bulletLeft = defaultBulletFont.render(str_MaxHandgunLoadBullet, False, WHITE)
hud_bulletMax = defaultBulletFont.render(str_MaxHandgunBullet, False, WHITE)

# 메인
print("Replaying MainMenuScene..")
try:
    #pygame.mixer.music.load(ost_MainMenu)
    #pygame.mixer.music.set_volume(45)
    #pygame.mixer.Sound.play()

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

        # render hud
        screen.blit(hud_HealthFull, [30, 20])
        screen.blit(hud_HealthFull, [65, 20])
        screen.blit(hud_HealthFull, [100, 20])
        screen.blit(icn_GunSelect_handGun, [30, 60])
        screen.blit(hud_bulletLeft, [66, 60])
        screen.blit(hud_bulletMax, [100, 60])

        pygame.display.flip()

        pygame.display.update()
        dt = clock.tick(300) / 700
except Exception as e:
    messagebox.showerror(title='Error occurred', message=e)
    print("Error occurred while replaying mainmenu scene.")
    print(e)

pygame.quit()
import pygame, sys, math, GameSetting, os, traceback

from pygame import *
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
CurrentHandgunBulletLeft = 18
CurrentMachinegunBulletLeft = 75

# str
str_MaxHandgunBullet = str(MaxHandgunBullet)
str_MaxMachineGunBullet = str(MaxMachineGunBullet)
str_MaxHandgunLoadBullet = str(MaxHandgunLoadBullet)
str_MaxMachinegunLoadBullet = str(MaxMachinegunLoadBullet)
str_CurrntHandgunBulletLeft = str(CurrentHandgunBulletLeft)
str_CurrentMachinegunBulletLeft = str(CurrentMachinegunBulletLeft)
str_SceneName = ''

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

    tile_mapDefaultBackground = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png')
    print("Loaded.")
except:
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print("Error occurred while loading Images.")
    print("Is file even exists?")
    quitGame()

# 재설정
print("Initallizing..")
try:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    dt = 0
    display = pygame.display
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    tile_mapDefaultBackground = pygame.transform.scale(pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png').convert(), [1280, 720])

    print("Initallized.")
except:
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print("Error occurred while initallizing game.")
    print("May occurrs because of weird pygame bug lol")

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
except:
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print("Error occurred while loading Sound.")
    print("Is file even exists?") # over 100!
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
except:
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print("Error occurred while reseting font/title.")
    print("May occurrs because of weird pygame bug lol")
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

hud_bulletLeft = defaultBulletFont.render(str_CurrntHandgunBulletLeft, False, WHITE)
hud_bulletMax = defaultBulletFont.render(str_MaxHandgunBullet, False, WHITE)
hud_bulletSlash = defaultBulletFont.render('/', True, WHITE)

class Player(pygame.sprite.Sprite): # main player class
    def __init__(self):
        super().__init__()
        print('Loading Player Sprite..')
        try:
            self.playerPos = pygame.math.Vector2(GameSetting.PLAYER_START_X, GameSetting.PLAYER_START_Y)
            self.playerSprite = pygame.transform.rotozoom(pygame.image.load('.\\src\\img\\animations\\entity\\player\\placeholder\\indiv_animation\\player_handgun_frame1.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
            self.basePlayerImage = self.playerSprite
            self.PlayerHitBoxRect = self.basePlayerImage.get_rect(center = self.playerPos)
            self.rect = self.PlayerHitBoxRect.copy()
            self.playerSpeed = GameSetting.PLAYER_SPEED
            self.playerDefaultDashSpeed = GameSetting.PLAYER_DASH_SPEED
            self.playerShoot = False
            self.shootCooldown = 0
            self.currentHandgunLeft = CurrentHandgunBulletLeft
            self.currentMachinegunLeft = CurrentMachinegunBulletLeft
            print("Loaded.")
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while loading Player Sprite.")
            print("Is file even exists?")
            quitGame()

    def playerRotation(self): # player rotation
        try:
            self.mouseCord = pygame.mouse.get_pos()
            self.x_change_mouse_player = (self.mouseCord[0] - self.PlayerHitBoxRect.centerx)
            self.y_change_mouse_player = (self.mouseCord[1] - self.PlayerHitBoxRect.centery)
            self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
            self.playerSprite = pygame.transform.rotate(self.basePlayerImage, -self.angle)
            self.rect = self.playerSprite.get_rect(center = self.PlayerHitBoxRect.center)
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while rotating player.")
            print(traceback.format_exc())
            quitGame()


    def userInput(self): # player movement
        try:
            self.velo_x = 0
            self.velo_y = 0

            userInputKey = pygame.key.get_pressed()

            if userInputKey[pygame.K_d]:
                self.velo_x = self.playerSpeed
            if userInputKey[pygame.K_a]:
                self.velo_x = -self.playerSpeed
            if userInputKey[pygame.K_w]:
                self.velo_y = -self.playerSpeed
            if userInputKey[pygame.K_s]:
                self.velo_y = self.playerSpeed

            if self.velo_x != 0 and self.velo_y != 0:
                self.velo_x /= math.sqrt(2)
                self.velo_y /= math.sqrt(2)

            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.playerShoot = True
                self.isPlayerShooting()
            else:
                self.playerShoot = False
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while checking user input.")
            print(traceback.format_exc())
            quitGame()

    def playerMove(self): # actual movement
        try:
            self.playerPos += pygame.math.Vector2(self.velo_x, self.velo_y)
            self.PlayerHitBoxRect.center = self.playerPos
            self.rect.center = self.PlayerHitBoxRect.center
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while moving player.")
            print(traceback.format_exc())
            quitGame()

    def isPlayerShooting(self):
        try:
            if self.shootCooldown == 0:
                self.shootCooldown = GameSetting.PLAYER_SHOOT_COOLDOWN
                spawnBulletPos = self.playerPos
                self.bullet = Bullet(spawnBulletPos[0], spawnBulletPos[1], self.angle)
                bulletSpriteGroup.add(self.bullet)
                defaultSpritesGroup.add(self.bullet)
            else:
                pass
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while checking player is shooting.")
            print(traceback.format_exc())
            quitGame()

    def playerUpdate(self): # player update
        try:
            self.userInput()
            self.playerMove()
            self.playerRotation()

            if self.shootCooldown > 0:
                self.shootCooldown -= 1
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while updating player.")
            print(traceback.format_exc())
            quitGame()

class Bullet(pygame.sprite.Sprite): # Bullet object
    def __init__(self, x, y, angle):
        super().__init__()
        print("Initallizing..")
        try:
            self.bulletImg = pygame.image.load('.\\src\\img\\animations\\object\\bullet\\BulletProjectile.png').convert_alpha()
            self.bulletImg = pygame.transform.rotozoom(self.bulletImg, 0, GameSetting.BULLET_VIEW_SIZE)
            self.rect = self.bulletImg.get_rect()
            self.rect.center = (x, y)
            self.bulletX = x
            self.bulletY = y
            self.angle = angle
            self.bulletSpeed = GameSetting.BULLET_SHOOT_SPEED
            self.velo_x = math.cos(self.angle * (2*math.pi/360)) * self.bulletSpeed
            self.velo_y = math.sin(self.angle * (2*math.pi/360)) * self.bulletSpeed
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while initallizing bullet object.")
            print(traceback.format_exc())
            quitGame()

    def bulletMovement(self):
        try:
            self.bulletX += self.velo_x
            self.bulletY += self.velo_y

            self.rect.x = int(self.bulletX)
            self.rect.y = int(self.bulletY)
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while moving bullet.")
            print(traceback.format_exc())
            quitGame()

    def bulletUpdate(self):
        try:
            self.bulletMovement()
        except:
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
            print("Error occurred while updating bullet object.")
            print(traceback.format_exc())
            quitGame()

player = Player()

defaultSpritesGroup = pygame.sprite.Group()
bulletSpriteGroup = pygame.sprite.Group()

defaultSpritesGroup.add(player)

# 메인
print(f"Replaying {str_SceneName}..")
try:
    while isMainMenuScene: # replay scene
        inputKey = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isMainMenuScene = False
                isMainGameScene = False
                pygame.quit()
                exit()

        screen.blit(tile_mapDefaultBackground, [0, 0])

        # render text
        #screen.blit(text_MainLogoTitle, [200, 300])
        #screen.blit(text_MainStartGame, [200, 342])
        #screen.blit(text_MainLoadGame, [200, 372])
        #screen.blit(text_MainSetting, [200, 402])
        #screen.blit(text_MainExit, [200, 432])
        #screen.blit(text_copyrightTeamName, [200, 465])

        # render hud
        screen.blit(hud_HealthFull, [30, 20])
        screen.blit(hud_HealthFull, [65, 20])
        screen.blit(hud_HealthFull, [100, 20]) # over 200!
        screen.blit(icn_GunSelect_handGun, [30, 60])
        screen.blit(hud_bulletLeft, [66, 60])
        screen.blit(hud_bulletMax, [108, 60])
        screen.blit(hud_bulletSlash, [95, 60])

        # render player
        defaultSpritesGroup.draw(screen)
        #defaultSpritesGroup.update()

        if GameSetting.SHOW_PLAYERHITBOX == True:
            pygame.draw.rect(screen, 'red', player.PlayerHitBoxRect, width=2)
            pygame.draw.rect(screen, 'yellow', player.rect, width=2)
        else:
            pass
        
        if GameSetting.SHOW_CURRENTFPS == True:
            pygame.display.set_caption(f"{clock.get_fps()}")
        else:
            pass

        pygame.display.flip()
        pygame.display.update()
        dt = clock.tick(60)
except:
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print("Error occurred while replaying scene.")
    print(traceback.format_exc())
    quitGame()

pygame.quit()
# default imports
import pygame, sys, math, GameSetting, traceback, json, jsonschema
from tkinter import messagebox
from pytmx.util_pygame import load_pygame
from videoplayer import Video
from pygame.locals import *
from MapSetting import *
from Level import LevelManager
from LevelData import *
from ButtonManager import Button

print('INFO: Loading..')

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (97, 97, 97)
DARK_GRAY = (23, 23, 23)

# bool
isMainGameScene = False
isMainMenuScene = True
isMainMenuToDemo = False

# int
MaxHandgunBullet = 255
MaxMachineGunBullet = 255
MaxHandgunLoadBullet = 18
MaxMachinegunLoadBullet = 75
LoadedHandgunBullet = 18
LoadedMachineBullet = 75

# str
str_MaxHandgunBullet = str(MaxHandgunBullet)
str_MaxMachineGunBullet = str(MaxMachineGunBullet)
str_MaxHandgunLoadBullet = str(MaxHandgunLoadBullet)
str_MaxMachinegunLoadBullet = str(MaxMachinegunLoadBullet)
str_SceneName = ''

data = {
    'mxHandgunBullet': MaxHandgunBullet,
    'crtHandgunBullet': LoadedHandgunBullet,
    'crtScene': str_SceneName,
    'playerX': 0,
    'playerY': 0
}

flags = GameSetting.SCREEN_FLAGS

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def validateJson(jsonData): # validate save file
    try:
        jsonschema.validate(instance=jsonData, schema=data)
    except jsonschema.ErrorTree.errors:
        print(f"{bcolors.FAIL}ERROR: Failed to validate player save data, is File even exists?\nTraceBack: {traceback.format_exc()}{bcolors.ENDC}")
        return False
    return True

print("INFO: Reading save file..")
try:
    with open('.\\src\\save\\0\\playerSaveData.json', 'r+', encoding='utf-8') as svFile:
        data = json.load(svFile)
        print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")
except:
    print(f"{bcolors.FAIL}ERROR: Error occurred while loading 'save/0/playeSaveData.json' file.")
    print(f"ERROR: This might happen when player changed some data.{bcolors.ENDC}")
    print(f'{bcolors.WARNING}WARN: Returning Traceback:\n{traceback.format_exc()}{bcolors.ENDC}')
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    pygame.quit()
    sys.exit()

print("INFO: Checking save file requirements..")
try:
    with open('.\\src\\save\\0\\playerSaveData.json', 'r') as pSv:
        mainData = str(json.load(pSv))
        isFileVaild = validateJson(mainData)

        if isFileVaild:
            print(f"{bcolors.OKCYAN}SUCCESS: playerSaveData is vaild.{bcolors.ENDC}")
        else:
            print(f"{bcolors.WARNING}WARN: playerSaveData isn't vaild as default state.{bcolors.ENDC}")
except FileNotFoundError:
    print(f"{bcolors.FAIL}ERROR: Failed to read playerSaveData, is File even exists?\nTraceback: {traceback.format_exc()}{bcolors.ENDC}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    pygame.quit()
    sys.exit()

def quitGame():
    print("INFO: Exiting..")
    pygame.quit()

# Image
print("INFO: Reading Images..")
try:
    img_backgroundLoop = pygame.image.load('./src/img/background/game_default_background.png')
    img_backgroundLoop = pygame.transform.scale(img_backgroundLoop,(GameSetting.WIDTH, GameSetting.HEIGHT))
    img_gameFavicon = pygame.image.load('./src/img/gameicon_placeholder.png')
    img_gameLogo = pygame.image.load('./src/img/gamelogo.png')
    img_gameLogo = pygame.transform.scale(img_gameLogo, (200, 100))

    icn_bulletFull = pygame.image.load('./src/img/icon/indiv_icon/Bullet.png')
    icn_bulletFull = pygame.transform.scale(icn_bulletFull, (32, 32))
    icn_bulletEmpty = pygame.image.load('./src/img/icon/indiv_icon/BulletEmpty.png')
    icn_bulletEmpty = pygame.transform.scale(icn_bulletEmpty, (32, 32))
    icn_GunSelect_handGun = pygame.image.load('./src/img/icon/indiv_icon/Handgun.png')
    icn_GunSelect_handGun = pygame.transform.scale(icn_GunSelect_handGun, (32, 32))
    icn_GunSelect_machineGun = pygame.image.load('./src/img/icon/indiv_icon/Machinegun.png')
    icn_GunSelect_machineGun = pygame.transform.scale(icn_GunSelect_machineGun, (32, 32))
    
    hud_HealthFull = pygame.image.load('./src/img/hud/hud_health1.png')
    hud_HealthFull = pygame.transform.scale(hud_HealthFull, (32, 32))
    hud_HealthHalf = pygame.image.load('./src/img/hud/hud_health_half.png')
    hud_HealthHalf = pygame.transform.scale(hud_HealthHalf, (32, 32))
    hud_HealthEmpty = pygame.image.load('./src/img/hud/hud_health_empty.png')
    hud_HealthEmpty = pygame.transform.scale(hud_HealthEmpty, (32, 32))
    hud_radiation = pygame.image.load('./src/img/hud/hud_radiation.png')
    hud_radiation = pygame.transform.scale(hud_radiation, (32, 32))
    hudBackground_weaponSelect = pygame.image.load('./src/img/hud/weapon_select.png')

    btn_Start = pygame.image.load('./src/img/button/menu/start_btn.png')
    btn_Load = pygame.image.load('./src/img/button/menu/load_btn.png')
    btn_Setting = pygame.image.load('./src/img/button/menu/setting_btn.png')
    btn_Exit = pygame.image.load('./src/img/button/menu/exit_btn.png')

    csrImg_Crosshair = pygame.image.load('./src/img/cursor/default-crosshair.png')

    tile_mapDefaultBackground = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png')
    mainMenu_backgruond = pygame.image.load('.\\src\\img\\background\\menu_background.png')
    print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")
except:
    print(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print(f"{bcolors.FAIL}ERROR: Error occurred while loading Images.")
    print(f"ERROR: Is file even exists?{bcolors.ENDC}")
    quitGame()

# game init
print("INFO: Initallizing..")
try:
    pygame.init()
    screen = pygame.display.set_mode((GameSetting.WIDTH, GameSetting.HEIGHT), flags)
    clock = pygame.time.Clock()
    dt = 0
    display = pygame.display
    running = True
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    tile_mapDefaultBackground = pygame.transform.scale(pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png').convert(), [1280, 720])
    level = LevelManager(mp_tutorial, screen)
    #print(f'INFO: GameSetting: {GameSetting.PLAYER_START_X},\n{GameSetting.PLAYER_START_Y},\n{GameSetting.PLAYER_VIEW_SIZE},\n{GameSetting.PLAYER_SPEED},\n{GameSetting.BULLET_COOLDOWN},\n{GameSetting.BULLET_LIFETIME},\n{GameSetting.BULLET_SPEED},\n{GameSetting.BULLET_VIEWSIZE},\n{GameSetting.SHOW_CURRENTFPS}')
    
    if GameSetting.SHOW_PLAYERMANA_CONSOLE == True and GameSetting.SHOW_CURRENTFPS == True:
        print(f'{bcolors.WARNING}WARNING: Too many debug updates! it may slow down performance.{bcolors.ENDC}')
    else:
        pass

    print(f"{bcolors.OKGREEN}SUCCESS: Initallized.{bcolors.ENDC}")
except:
    print(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print(f"{bcolors.FAIL}ERROR: Error occurred while initallizing game.")
    print(f"ERROR: May occurrs because of weird pygame bug lol{bcolors.ENDC}")

# SFX / OST
print("INFO: Loading Sounds..")
try:
    # sfx
    sfx_Handgun = ['./src/sound/sfx/handgun/handgun_fire1.wav', './src/sound/sfx/handgun/handgun_noammo.wav', './src/sound/sfx/handgun/handgun_reload.wav']
    sfx_smg = ['./src/sound/sfx/smg/smg_startloop.wav', './src/sound/sfx/smg/smg_loop.wav', './src/sound/sfx/smg/smg_endloop.wav', './src/sound/sfx/smg/smg_noammo.wav', './src/sound/sfx/smg/smg_realod.wav']
    sfx_Click = ['']

    # ost
    ost_MainMenu = pygame.mixer.music.load('./src/sound/ost/background_ambient1.wav')
    ost_MainMenu = pygame.mixer.music.set_volume(GameSetting.MUSIC_VOL)
    print(f'INFO: Volume set to {GameSetting.MUSIC_VOL}%')
    if isMainMenuScene == True and isMainGameScene == False:
        #pygame.mixer.music.play(-1)
        pass
    elif isMainGameScene == True and isMainMenuScene == False:
        pass

    print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")
except:
    print(f"{traceback.format_exc()}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print(f"{bcolors.FAIL}ERROR: Error occurred while loading Sound.")
    print(f"ERROR: Is file even exists?{bcolors.ENDC}") # over 100!
    quitGame()

print("INFO: Reading Video..")
try:
    start_std = Video('.\\src\\mp4\\std_start.mp4')
    start_std.set_size((GameSetting.WIDTH, GameSetting.HEIGHT))
    print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")
except FileNotFoundError:
    print(f'{bcolors.FAIL}ERROR: Failed to load video file, is File even exist?\nReturning Traceback: {traceback.format_exc()}{bcolors.ENDC}')
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    quitGame()

# font setup
print("INFO: Resetting Font/Title..")
try:
    display.set_caption(f'TIME / BULLET - {GameSetting.VER}')
    display.set_icon(img_gameFavicon)

    # Font
    defaultFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 30)
    defaultCopyrightFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 20)
    defaultBulletFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 24)
    mainTitleFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 25)
    subTitleFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 15)

    print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")
except:
    print(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print(f"{bcolors.FAIL}ERROR: Error occurred while reseting font/title.")
    print(f"ERROR: May occurrs because of weird pygame bug lol{bcolors.ENDC}")
finally: 
    if display.get_caption == '':
        display.set_caption('Caption not set.')

# font reset
print("INFO: Resetting text object..")
text_MainLogoTitle = defaultFont.render('TIME \ BULLET', True, WHITE)
text_copyrightTeamName = defaultCopyrightFont.render('MADEBY. SONGRO STUDIO_', True, GRAY)
text_autoSave = defaultFont.render('자동 저장중..', False, DARK_GRAY)
text_version = mainTitleFont.render(f'v {GameSetting.VER}', True, WHITE)

hud_bulletLeft = defaultBulletFont.render(str_MaxHandgunLoadBullet, False, WHITE)
hud_bulletMax = defaultBulletFont.render(str_MaxHandgunBullet, False, WHITE)
hud_bulletSlash = defaultBulletFont.render('/', False, WHITE)

debug_showFps = defaultFont.render('', False, WHITE)

def checkFps():
    if clock.get_fps() > GameSetting.DEBUG_FPSWARNING_VALUE:
        pass
    else:
        print(f"{bcolors.WARNING}WARNING: FPS is lower than {GameSetting.DEBUG_FPSWARNING_VALUE}fps!")
        print(f"WARNING: This may cause 'unplayable' for certain players.{bcolors.ENDC}")
        #killPlayer()

def autoSave():
    print("INFO: AutoSaving..")
    Saving = 5
    try:
        with open('.\\src\\save\\0\\playerSaveData.json', 'w+') as svFile:
            json.dump(data, svFile)
            print(f"{bcolors.OKGREEN}SUCCESS: Saved.{bcolors.ENDC}")
        
        while Saving > 0:
            screen.blit(text_autoSave, [30, 650])
            Saving -= 1

        if Saving == 0:
            Saving = 5
    except:
        print(f"{bcolors.FAIL}ERROR: Failed to save file to {svFile}.\nERROR: Is file even exist?")
        print(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")

class Player(pygame.sprite.Sprite): # player
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(GameSetting.PLAYER_START_X, GameSetting.PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame1.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.base_player_image = self.image
        self.playerShootFrame = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame2.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.speed = GameSetting.PLAYER_SPEED
        self.playerDashSpeed = GameSetting.PLAYER_DASH_SPEED
        self.shoot = False
        self.isDashing = False
        self.shoot_cooldown = 0
        self.gunBarrelOffset = pygame.math.Vector2(GameSetting.GUN_OFFSET_X, GameSetting.GUN_OFFSET_Y)
        self.playerMana = 100       
        self.playerManaCooldown = GameSetting.PLAYERMANA_COOLDOWN
        self.playerVignette = pygame.image.load('./src/img/player_deco/vignette.png').convert_alpha()

    def player_rotation(self):
        self.mouse_coords = pygame.mouse.get_pos()
        self.x_change_mouse_player = (self.mouse_coords[0] - self.hitbox_rect.centerx)
        self.y_change_mouse_player = (self.mouse_coords[1] - self.hitbox_rect.centery)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        rotated_image = pygame.transform.rotate(self.base_player_image, -self.angle)

        # Create a new surface with per-pixel alpha to smooth the rotated image
        self.image = pygame.Surface(rotated_image.get_size(), pygame.SRCALPHA)
        self.image.blit(rotated_image, (0, 0))

        self.rect = self.image.get_rect(center=self.hitbox_rect.center)
       
    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
            self.playerVignette.blit(screen, self.pos)
        if keys[pygame.K_s]:
            self.velocity_y = self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed

        if self.velocity_x != 0 and self.velocity_y != 0: # moving diagonally
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)

        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.shoot = True
            self.is_shooting()
        else:
            self.shoot = False

        if keys[pygame.K_SPACE]:
            self.isDashing = True
            self.dash()
        else:
            self.isDashing = False
    
        # to-do: fix player y velocity value multiply while pressing player speed change key
        if self.playerMana < 0:
            print('INFO: ReAdding Mana..')
            self.playerMana = 100
        else:
            if keys[pygame.K_f] and keys[pygame.K_d]:
                self.velocity_x = self.speed/GameSetting.SLOWSPEED_X
                self.playerMana -= GameSetting.PLAYERMANA_REMOVE_VAL
            elif keys[pygame.K_f] and keys[pygame.K_a]:
                self.velocity_x = self.speed/GameSetting.SLOWSPEED_X
                self.playerMana -= GameSetting.PLAYERMANA_REMOVE_VAL
        # 이거 버그 수정하기
            elif keys[pygame.K_f] and keys[pygame.K_w]:
                self.velocity_y = self.speed/GameSetting.SLOWSPEED_Y
                self.playerMana -= GameSetting.PLAYERMANA_REMOVE_VAL
            elif keys[pygame.K_f] and keys[pygame.K_s]:
                self.velocity_y = self.speed/GameSetting.SLOWSPEED_Y
                self.playerMana -= GameSetting.PLAYERMANA_REMOVE_VAL

        if GameSetting.SHOW_PLAYERMANA_CONSOLE == True:
            print(self.playerMana)
        else:
            pass

    def is_shooting(self): 
        if self.shoot_cooldown == 0:
            self.base_player_image = self.playerShootFrame
            self.shoot_cooldown = GameSetting.BULLET_COOLDOWN
            spawnBulletPos = self.pos + self.gunBarrelOffset.rotate(self.angle)
            self.bullet = Bullet(spawnBulletPos[0], spawnBulletPos[1], self.angle)
            bulletGroup.add(self.bullet)
            allSpritesGroup.add(self.bullet)
            self.bulletLeft = MaxHandgunLoadBullet
            self.bulletLeft -= 1
            self.base_player_image = self.image

    def dash(self):
        #if self.isl
        self.speed = GameSetting.PLAYER_DASH_SPEED

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center

    def update(self):
        self.user_input()
        self.move()
        self.player_rotation()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load('./src/img/animations/object/bullet/BulletProjectile.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, GameSetting.BULLET_VIEWSIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = GameSetting.BULLET_SPEED
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
        self.bullet_lifetime = GameSetting.BULLET_LIFETIME
        self.spawn_time = pygame.time.get_ticks() # gets the specific time that the bullet was created

    def bullet_movement(self):  
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
            self.kill() 

    def update(self):
        self.bullet_movement()

player = Player()
allSpritesGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()

btnStart = Button(30, 560, btn_Start, 1)
btnLoad = Button(30, 590, btn_Load, 1)
btnSetting = Button(30, 620, btn_Setting, 1)
btnExit = Button(30, 650, btn_Exit, 1)

allSpritesGroup.add(player)

# main
if GameSetting.RUN_GAME_BEFORE_MENU:
    isMainGameScene = True
    isMainMenuScene = False
else:
    isMainGameScene = False
    isMainMenuScene = True

while running:
    try:
        while isMainGameScene: # replay scene
            inputKey = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("INFO: Saving..")
                    try:
                        with open('.\\src\\save\\0\\playerSaveData.json', 'w+') as svFile:
                            json.dump(data, svFile)
                        svFile.close()
                        print(f"{bcolors.OKGREEN}SUCCESS: Saved.{bcolors.ENDC}")
                    except:
                        print(f"{bcolors.FAIL}ERROR: Fai5led to save file to {svFile}.\nERROR: Is file even exist?")
                        print(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")

                    isMainMenuScene = False
                    isMainGameScene = False
                    isMainMenuToDemo = False
            
            screen.blit(img_backgroundLoop, [0, 0])

            screen.blit(hud_HealthFull, [30, 20])
            screen.blit(hud_HealthFull, [65, 20])
            screen.blit(hud_HealthFull, [100, 20])
            screen.blit(icn_GunSelect_handGun, [30, 60])
            screen.blit(hud_bulletLeft, [66, 60])
            screen.blit(hud_bulletMax, [108, 60])
            screen.blit(hud_bulletSlash, [95, 60])

            # render player
            allSpritesGroup.draw(screen)
            allSpritesGroup.update()
            
            if GameSetting.SHOW_CURRENTFPS == True:
                pygame.display.set_caption(f"FPS: {clock.get_fps()}")
            else:
                pass

            #checkFps()
            
            level.run()

            pygame.display.update()
            dt = clock.tick(GameSetting.DEF_FPS)

        while isMainMenuScene:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("INFO: Saving..")
                    try:
                        with open('.\\src\\save\\0\\playerSaveData.json', 'w+') as svFile:
                            json.dump(data, svFile)
                        svFile.close()
                        print(f"{bcolors.OKGREEN}SUCCESS: Saved.{bcolors.ENDC}")
                    except:
                        print(f"{bcolors.FAIL}ERROR: Failed to save file to {svFile}.\nERROR: Is file even exist?")
                        print(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")

                    isMainMenuScene = False
                    isMainGameScene = False
                    isMainMenuToDemo = False

            if GameSetting.SHOW_CURRENTFPS == True:
                pygame.display.set_caption(f"FPS: {clock.get_fps()}")
            else:
                pass

            screen.blit(mainMenu_backgruond, [0, 0])
            screen.blit(text_version, [32, 53])

            screen.blit(text_MainLogoTitle, [30, 20])
            screen.blit(text_copyrightTeamName, [985, 650])

            if btnStart.drawBtn(screen):
                print('INFO: Pressed Start.')
            
            if btnLoad.drawBtn(screen):
                isMainGameScene = True
                isMainMenuScene = False
                isMainMenuToDemo = False
                
                with open('./src/save/0/playerSaveData.json', 'r+') as pSv:
                    data = json.load(pSv)
                    print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")

            btnSetting.drawBtn(screen)

            if btnExit.drawBtn(screen):
                print("INFO: Saving..")
                try:
                    with open('.\\src\\save\\0\\playerSaveData.json', 'w+') as svFile:
                        json.dump(data, svFile)
                        svFile.close()
                        print(f"{bcolors.OKGREEN}SUCCESS: Saved.{bcolors.ENDC}")
                except:
                    print(f"{bcolors.FAIL}ERROR: Failed to save file to {svFile}.\nERROR: Is file even exist?")
                    print(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")

                isMainMenuScene = False
                isMainGameScene = False
                isMainMenuToDemo = False

            #checkFps()

            pygame.display.update()
            dt = clock.tick(GameSetting.DEF_FPS)
        
        while isMainMenuToDemo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("INFO: Saving..")
                    try:
                        with open('.\\src\\save\\0\\playerSaveData.json', 'w+') as svFile:
                            json.dump(data, svFile)
                        svFile.close()
                        print(f"{bcolors.OKGREEN}SUCCESS: Saved.{bcolors.ENDC}")
                    except:
                        print(f"{bcolors.FAIL}ERROR: Failed to save file to {svFile}.\nERROR: Is file even exist?")
                        print(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")

                    isMainMenuScene = False
                    isMainGameScene = False
                    isMainMenuToDemo = False

            if GameSetting.SHOW_CURRENTFPS == True:
                pygame.display.set_caption(f"FPS: {clock.get_fps()}")
            else:
                pass

            pygame.display.update()
            dt = clock.tick(GameSetting.DEF_FPS)
            
    except:
        print(f"{traceback.format_exc}")
        messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
        print(f"{bcolors.FAIL}ERROR: `Error occurred while replaying scene.")
        print(f'{traceback.format_exc()}{bcolors.ENDC}')
        quitGame()
pygame.quit()

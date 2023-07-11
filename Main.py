import pygame, sys, math, GameSetting, time, traceback, os, LevelData, json, jsonschema
from tkinter import messagebox
from pytmx.util_pygame import load_pygame
from LevelSetting import *
from Level import Level

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
    with open('.\\src\\save\\0\\playerSaveData.json', 'r') as svFile:
        data = json.load(svFile)
    print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")
except:
    print(f"{bcolors.FAIL}ERROR: Error occurred while loading 'save/0/playeSaveData.json' file.")
    print(f"This might happen when player changed some data.{bcolors.ENDC}")
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
    sys.exit() # to make sure that game is closed.

# Image
print("INFO: Reading Images..")
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
    screen = pygame.display.set_mode((GameSetting.WIDTH, GameSetting.HEIGHT))
    clock = pygame.time.Clock()
    level = Level(LevelData.mp_tutorial, screen)
    dt = 0
    display = pygame.display
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    tile_mapDefaultBackground = pygame.transform.scale(pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png').convert(), [1280, 720])
    print(f'INFO: GameSetting: {GameSetting.PLAYER_START_X},\n{GameSetting.PLAYER_START_Y},\n{GameSetting.PLAYER_VIEW_SIZE},\n{GameSetting.PLAYER_SPEED},\n{GameSetting.BULLET_COOLDOWN},\n{GameSetting.BULLET_LIFETIME},\n{GameSetting.BULLET_SPEED},\n{GameSetting.BULLET_VIEWSIZE},\n{GameSetting.SHOW_CURRENTFPS}')
    
    if GameSetting.SHOW_PLAYERMANA_CONSOLE == True and GameSetting.SHOW_CURRENTFPS == True and GameSetting.SHOW_CURRENTFPS_TOSCREEN == True:
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
    ost_MainMenu = './src/sound/ost/background_ambient1.wav'

    print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")
except:
    print(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print(f"{bcolors.FAIL}ERROR: Error occurred while loading Sound.")
    print(f"ERROR: Is file even exists?{bcolors.ENDC}") # over 100!
    quitGame()

# font setup
print("INFO: Resetting Font/Title..")
try:
    display.set_caption('spsroEngine Scene Replayer')
    display.set_icon(img_gameLogo)

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
text_MainLogoTitle = defaultFont.render('TIME AND\nBULLET', True, WHITE)
text_MainStartGame = defaultFont.render('START', True, WHITE)
text_MainLoadGame = defaultFont.render('LOAD', True, WHITE)
text_MainSetting = defaultFont.render('SETTING', True, WHITE)
text_MainExit = defaultFont.render('EXIT', True, WHITE)
text_copyrightTeamName = defaultCopyrightFont.render('SONGRO STUDIO_', True, GRAY)

hud_bulletLeft = defaultBulletFont.render(str_MaxHandgunLoadBullet, False, WHITE)
hud_bulletMax = defaultBulletFont.render(str_MaxHandgunBullet, False, WHITE)
hud_bulletSlash = defaultBulletFont.render('/', False, WHITE)

debug_showFps = defaultFont.render(str(clock.get_fps()), False, WHITE)

def checkFps():
    if clock.get_fps() > GameSetting.DEBUG_FPSWARNING_VALUE:
        pass
    else:
        print(f"{bcolors.WARNING}WARNING: FPS is lower than {GameSetting.DEBUG_FPSWARNING_VALUE}fps!")
        print(f"WARNING: This may cause 'unplayable' for certain players.{bcolors.ENDC}")
        killPlayer()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(GameSetting.PLAYER_START_X, GameSetting.PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame1.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.base_player_image = self.image
        self.playerShootFrame = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame2.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.speed = GameSetting.PLAYER_SPEED
        self.shoot = False
        self.isDashing = False
        self.shoot_cooldown = 0
        self.gunBarrelOffset = pygame.math.Vector2(GameSetting.GUN_OFFSET_X, GameSetting.GUN_OFFSET_Y)
        self.playerMana = 100       
        self.playerManaCooldown = GameSetting.PLAYERMANA_COOLDOWN

    def player_rotation(self):
        self.mouse_coords = pygame.mouse.get_pos()
        self.x_change_mouse_player = (self.mouse_coords[0] - self.hitbox_rect.centerx)
        self.y_change_mouse_player = (self.mouse_coords[1] - self.hitbox_rect.centery)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        self.image = pygame.transform.rotate(self.base_player_image, -self.angle)
        self.rect = self.image.get_rect(center = self.hitbox_rect.center)
       
    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
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
        # lee go wae duam
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
            time.sleep(1)
            self.base_player_image = self.image

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

allSpritesGroup.add(player)

def killPlayer():
    print("INFO: Removing Sprites from group..")
    try:
        allSpritesGroup.remove(player)
        print(f'{bcolors.OKGREEN}SUCCESS: Removed.{bcolors.ENDC}')
    except:
        print(f"{bcolors.FAIL}Failed to remove sprite 'player' from 'allSpritesGroup'!")
        print(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")
    print("INFO: Adding player to 'allSpritesGroup'..")
    try:
        allSpritesGroup.add(player)
        print(f'{bcolors.OKGREEN}SUCCESS: Added.{bcolors.ENDC}')
    except:
        print(f"{bcolors.FAIL}ERROR: Failed to add sprite 'player' to 'allSpritesGroup'!")
        print(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")


# main
print(f"INFO: Replaying {str_SceneName}..")
try:
    while isMainMenuScene: # replay scene
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
                    print(f"{bcolors.FAIL}ERROR: Failed to save file to {svFile}.\nERROR: Is file even exist?")
                    print(f"Traceback: {traceback.print_exc}{bcolors.ENDC}")

                isMainMenuScene = False
                isMainGameScene = False

        level.run()
            
        #screen.blit(img_backgroundLoop, [0, 0])

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

        if GameSetting.SHOW_CURRENTFPS_TOSCREEN == True:
            screen.blit(debug_showFps, [0, 0])
        else:
            pass

        checkFps()

        pygame.display.update()
        dt = clock.tick(GameSetting.DEF_FPS)
except:
    print(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print(f"{bcolors.FAIL}ERROR: `Error occurred while replaying scene.")
    print(f'{traceback.format_exc()}{bcolors.ENDC}')
    quitGame()

pygame.quit()

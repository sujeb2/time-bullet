# default imports
import pygame, sys, math, GameSetting, traceback, json, jsonschema, random
from tkinter import messagebox
from videoplayer import Video
from pygame.locals import *
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
    print('INFO: Writting default save file...')
    with open('./src/save/0/playerSaveData.json', 'w') as writeSvFile:
        writeSvFile.write('{"mxHandgunBullet": 255, "crtHandgunBullet": 20000, "crtScene": "", "playerX": 0, "playerY": 0}')

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
    #print(f'INFO: GameSetting: {GameSetting.PLAYER_START_X},\n{GameSetting.PLAYER_START_Y},\n{GameSetting.PLAYER_VIEW_SIZE},\n{GameSetting.PLAYER_SPEED},\n{GameSetting.BULLET_COOLDOWN},\n{GameSetting.BULLET_LIFETIME},\n{GameSetting.BULLET_SPEED},\n{GameSetting.BULLET_VIEWSIZE},\n{GameSetting.SHOW_CURRENTFPS}')
    
    if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
        if GameSetting.SHOW_PLAYERMANA_CONSOLE == True and GameSetting.SHOW_CURRENTFPS == True:
            print(f'{bcolors.WARNING}WARNING: Too many debug updates! it may slow down performance.{bcolors.ENDC}')
        else:
            pass
    else:
        pass

    print(f"{bcolors.OKGREEN}SUCCESS: Initallized.{bcolors.ENDC}")
except:
    print(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print(f"{bcolors.FAIL}ERROR: Error occurred while initallizing game.")
    print(f"ERROR: May occurrs because of weird pygame bug lol{bcolors.ENDC}")

# Image
print("INFO: Reading Images..")
try:
    img_backgroundLoop = pygame.image.load('./src/img/background/game_default_background.png').convert_alpha()
    img_backgroundLoop = pygame.transform.scale(img_backgroundLoop,(GameSetting.WIDTH, GameSetting.HEIGHT))
    img_gameFavicon = pygame.image.load('./src/img/gameicon_placeholder.png').convert_alpha()
    img_gameLogo = pygame.image.load('./src/img/gamelogo.png').convert_alpha()
    img_gameLogo = pygame.transform.scale(img_gameLogo, (200, 100))

    icn_GunSelect_handGun = pygame.image.load('./src/img/icon/indiv_icon/Handgun.png').convert_alpha()
    icn_GunSelect_handGun = pygame.transform.scale(icn_GunSelect_handGun, (32, 32))
    icn_GunSelect_machineGun = pygame.image.load('./src/img/icon/indiv_icon/Machinegun.png').convert_alpha()
    icn_GunSelect_machineGun = pygame.transform.scale(icn_GunSelect_machineGun, (32, 32))
    
    hud_HealthFull = pygame.image.load('./src/img/hud/hud_health1.png').convert_alpha()
    hud_HealthFull = pygame.transform.scale(hud_HealthFull, (32, 32))
    hud_HealthHalf = pygame.image.load('./src/img/hud/hud_health_half.png').convert_alpha()
    hud_HealthHalf = pygame.transform.scale(hud_HealthHalf, (32, 32))
    hud_HealthEmpty = pygame.image.load('./src/img/hud/hud_health_empty.png').convert_alpha()
    hud_HealthEmpty = pygame.transform.scale(hud_HealthEmpty, (32, 32))
    hud_radiation = pygame.image.load('./src/img/hud/hud_radiation.png').convert_alpha()
    hud_radiation = pygame.transform.scale(hud_radiation, (32, 32))
    hudBackground_weaponSelect = pygame.image.load('./src/img/hud/weapon_select.png').convert_alpha()

    btn_Start = pygame.image.load('./src/img/button/menu/start_btn.png').convert_alpha()
    btn_Load = pygame.image.load('./src/img/button/menu/load_btn.png').convert_alpha()
    btn_Setting = pygame.image.load('./src/img/button/menu/setting_btn.png').convert_alpha()
    btn_Copyright = pygame.image.load('./src/img/button/menu/copyright_btn.png').convert_alpha()
    btn_Exit = pygame.image.load('./src/img/button/menu/exit_btn.png').convert_alpha()

    csrImg_Crosshair = pygame.image.load('./src/img/cursor/default-crosshair.png').convert_alpha()

    tile_mapDefaultBackground = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png').convert_alpha()
    mainMenu_backgruond = pygame.image.load('.\\src\\img\\background\\menu_background.png').convert_alpha()

    map_devTest = pygame.image.load('./src/maps/png/dev_test.png').convert_alpha()
    print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")
except:
    print(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print(f"{bcolors.FAIL}ERROR: Error occurred while loading Images.")
    print(f"ERROR: Is file even exists?{bcolors.ENDC}")
    quitGame()

# SFX / OST
print("INFO: Loading Sounds..")
try:
    # sfx
    sfx_handgunFire = pygame.mixer.Sound("./src/sound/sfx/handgun/handgun_fire.wav")
    sfx_handgunNoAmmo = pygame.mixer.Sound("./src/sound/sfx/handgun/handgun_noammo.wav")
    sfx_handgunReload = pygame.mixer.Sound("./src/sound/sfx/handgun/handgun_reload.wav")
    sfx_playerHurt = pygame.mixer.Sound("./src/sound/sfx/player/hurt.wav")
    sfx_playerDash = pygame.mixer.Sound("./src/sound/sfx/player/dash.wav")
    sfx_playerRadiation = pygame.mixer.Sound('./src/sound/sfx/player/radiation.wav')

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
if list(GameSetting.MOTD) == '':
    text_mainMenuMotd = defaultCopyrightFont.render('지정되지 않은 메세지 입니다.', True, WHITE)
else:
    text_mainMenuMotd = defaultCopyrightFont.render(random.choice(list(GameSetting.MOTD)), True, WHITE)
text_autoSave = defaultFont.render('자동 저장중..', False, DARK_GRAY)
text_version = mainTitleFont.render(f'v {GameSetting.VER}', True, WHITE)

hud_bulletLeft = defaultBulletFont.render(str_MaxHandgunLoadBullet, True, WHITE)
hud_bulletMax = defaultBulletFont.render(str_MaxHandgunBullet, True, WHITE)
hud_bulletSlash = defaultBulletFont.render('/', True, WHITE)
hud_playerMana = defaultBulletFont.render('100%', True, WHITE)

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

def generateGlowEffect(glow, rad):
    lightSurface = pygame.Surface((rad * 2, rad * 2), pygame.SRCALPHA)
    layers = 25
    glow = pygame.math.clamp(glow, 0, 255)

    for i in range(layers):
        k = i * glow
        k = pygame.math.clamp(k, 0, 255)

        pygame.draw.circle(lightSurface, (k, k, k), lightSurface.get_rect().center, rad - i * 3)

    return lightSurface

class Player(pygame.sprite.Sprite): # player
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(GameSetting.PLAYER_START_X, GameSetting.PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame1.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.base_player_image = self.image
        self.playerShootFrame = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame2.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.lastTick = pygame.time.get_ticks()
        self.speed = GameSetting.PLAYER_SPEED
        self.playerDashSpeed = GameSetting.PLAYER_DASH_SPEED
        self.shoot = False
        self.isDashing = False
        self.shoot_cooldown = 0
        self.gunBarrelOffset = pygame.math.Vector2(GameSetting.GUN_OFFSET_X, GameSetting.GUN_OFFSET_Y)
        self.playerMana = 100       
        self.playerManaCooldown = 500
        self.playerVignette = pygame.image.load('./src/img/player_deco/vignette.png').convert_alpha()
        self.isDashAble = True
        self.health = 3
        self.hurtCooldown = 100

    def player_rotation(self):
        self.mouse_coords = pygame.mouse.get_pos()
        self.x_change_mouse_player = (self.mouse_coords[0] - GameSetting.WIDTH // 2)
        self.y_change_mouse_player = (self.mouse_coords[1] - GameSetting.HEIGHT // 2)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        self.image = pygame.transform.rotate(self.base_player_image, -self.angle)
        self.rect = self.image.get_rect(center = self.hitbox_rect.center)
       
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
            sfx_handgunFire.play()
        else:
            self.shoot = False

        if keys[pygame.K_SPACE]: # player dash
            self.speed = 5
        else:
            self.speed = 3
    
        if keys[pygame.K_f]: # player slow
            self.playerMana -= GameSetting.PLAYERMANA_REMOVE_VAL
            self.speed = 1
        else:
            self.speed = 3

        if GameSetting.SHOW_PLAYERMANA_CONSOLE == True:
            print(self.playerMana)
        else:
            pass

    def checkMana(self):
        if self.playerMana < 0:
            if self.playerManaCooldown > 0:
                self.playerManaCooldown -= self.lastTick
            else:
                print("INFO: ReAdding Mana..")
                self.playerMana = 100
                self.playerManaCooldown = 500
        else:
            pass

    def checkColliedWithEnemy(self):
        if pygame.sprite.groupcollide(playerGroup, enemyGroup, True, False):
            self.hurtCooldown -= self.lastTick

            if self.hurtCooldown <= 0:
                self.health -= 1
                sfx_playerHurt.play()
                self.hurtCooldown == 100

            if self.health <= 0:
                self.kill()
                self.health = 3


    def is_shooting(self): 
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = GameSetting.BULLET_COOLDOWN
            spawnBulletPos = self.pos + self.gunBarrelOffset.rotate(self.angle)
            self.bullet = Bullet(spawnBulletPos[0], spawnBulletPos[1], self.angle)
            bulletGroup.add(self.bullet)
            allSpritesGroup.add(self.bullet)
            self.bulletLeft = MaxHandgunLoadBullet
            self.bulletLeft -= 1

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center
        
    def update(self):
        self.user_input()
        self.move()
        self.player_rotation()
        self.checkMana()
        self.checkColliedWithEnemy()

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

    def checkColliedwithEnemy(self):
        if pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, False):
            zombie.damage -= 1
            if zombie.damage <= 0:
                zombie.kill()
                zombie.damage = 5

    def checkIsSlowState(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            pass
        else:
            pass

    def update(self):
        self.bullet_movement()
        #self.checkIsSlowState()
        self.checkColliedwithEnemy()

class Camera(pygame.sprite.Group): # custom camera function
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = map_devTest.get_rect(topleft = (0, 0))

    def cameraDraw(self):
        self.offset.x = player.rect.centerx - GameSetting.WIDTH // 2
        self.offset.y = player.rect.centery - GameSetting.HEIGHT // 2

        floor_offset_pos = self.floor_rect.topleft - self.offset # map offset
        screen.blit(map_devTest, floor_offset_pos)

        for sprite in allSpritesGroup:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__(enemyGroup, allSpritesGroup)
        self.image = pygame.image.load('.\\src\\img\\animations\\entity\\enemy\\indiv_animation\\zombie_frame1.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, GameSetting.ENEMY_VIEWSIZE)

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.speed = GameSetting.ENEMY_SPEED

        self.position = pygame.math.Vector2(position)

        self.isPlayerAlive = True

        self.damage = 5

    def pathTracePlayer(self): # path tracing
        if self.isPlayerAlive:
            player_vector = pygame.math.Vector2(player.hitbox_rect.center)
            enemy_vector = pygame.math.Vector2(self.rect.center)
            distance = self.getVectorDistance(player_vector, enemy_vector)

            if distance > 0:
                self.direction = (player_vector - enemy_vector).normalize()
            else:
                self.direction = pygame.math.Vector2()
            
            self.velocity = self.direction * self.speed
            self.position += self.velocity

            self.rect.centerx = self.position.x
            self.rect.centery = self.position.y
        else:
            pass

    def getVectorDistance(self, vector_1, vector_2):
        return (vector_1 - vector_2).magnitude()
    
    def checkIsSlowState(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_f]:
            self.speed = self.speed / 1
        else:
            pass
    
    def update(self):
        self.pathTracePlayer()
        self.checkIsSlowState()

player = Player()
camera = Camera()
allSpritesGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
obstaclesGroup = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
zombie = Enemy((0, 0))

btnStart = Button(32, 530, btn_Start, 1)
btnLoad = Button(32, 560, btn_Load, 1)
btnSetting = Button(31, 590, btn_Setting, 1)
btnCopyright = Button(29, 620, btn_Copyright, 1)
btnExit = Button(30, 650, btn_Exit, 1)

allSpritesGroup.add(player)
playerGroup.add(player)

# main
if GameSetting.RUN_GAME_BEFORE_MENU:
    isMainGameScene = True
    isMainMenuScene = False
else:
    isMainGameScene = False
    isMainMenuScene = True

def gameDemo(): # main game
        print('INFO: Starting..')
        while True: # replay scene
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
                        print(f"Traceback: {traceback.print_exc()}{bcolors.ENDC}")
                    pygame.quit()
                    sys.exit()

            screen.blit(img_backgroundLoop, [0, 0])

            # render
            camera.cameraDraw()
            allSpritesGroup.update()
            playerGroup.update()

            # debug info update
            hud_playerMana = defaultBulletFont.render(f'{str(player.playerMana)}%', True, WHITE)
            hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨)', True, WHITE)
            hud_debugMilliTickScreen = defaultBulletFont.render(f'{math.ceil(clock.get_rawtime())}TICK (반올림됨)', True, WHITE)
            hud_bulletLeft = defaultBulletFont.render(str_MaxHandgunLoadBullet, True, WHITE)

            screen.blit(icn_GunSelect_handGun, [30, 670])
            screen.blit(hud_bulletLeft, [75, 670])
            screen.blit(hud_bulletSlash, [103, 670])
            screen.blit(hud_bulletMax, [115, 670])
            
            if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
                if GameSetting.SHOW_CURRENTFPS == True:
                        pygame.display.set_caption(f"FPS: {clock.get_fps()}")
                else:
                    pass
                if GameSetting.SHOW_DEBUGINFO_TOSCREEN == True:
                    screen.blit(hud_debugFpsScreen, [30, 77])
                    screen.blit(hud_debugMilliTickScreen, [30, 100])
                    screen.blit(hud_playerMana, [30, 120])
            else:
                pass

            if player.health >= 3:
                screen.blit(hud_HealthFull, [30, 20])
                screen.blit(hud_HealthFull, [65, 20])
                screen.blit(hud_HealthFull, [100, 20])
            elif player.health <= 2:
                screen.blit(hud_HealthFull, [30, 20])
                screen.blit(hud_HealthFull, [65, 20])
                screen.blit(hud_HealthEmpty, [100, 20])
            elif player.health <= 0:
                screen.blit(hud_HealthEmpty, [30, 20])
                screen.blit(hud_HealthEmpty, [65, 20])
                screen.blit(hud_HealthEmpty, [100, 20])
        

            pygame.display.update()
            dt = clock.tick(GameSetting.DEF_FPS)
        sys.exit()

def mainMenu(): # main menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
        if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
            if GameSetting.SHOW_CURRENTFPS == True:
                pygame.display.set_caption(f"FPS: {clock.get_fps()}")
            else:
                pass
        else:
            pass

        screen.blit(mainMenu_backgruond, [0, 0])
        screen.blit(text_version, [32, 53])
        screen.blit(text_MainLogoTitle, [30, 20])
        screen.blit(text_copyrightTeamName, [985, 650])
        screen.blit(text_mainMenuMotd, [32, 83])

        if btnStart.drawBtn(screen):
            gameDemo()
                
        if btnLoad.drawBtn(screen):
            isMainGameScene = True
            isMainMenuScene = False
            isMainMenuToDemo = False
                    
            with open('./src/save/0/playerSaveData.json', 'r+') as pSv:
                data = json.load(pSv)
                print(f"{bcolors.OKGREEN}SUCCESS: Loaded.{bcolors.ENDC}")

        btnSetting.drawBtn(screen)

        btnCopyright.drawBtn(screen)

        if btnExit.drawBtn(screen):
            pygame.quit()

        pygame.display.update()
        dt = clock.tick(GameSetting.DEF_FPS)

while running:
    try:
        while isMainGameScene:
            gameDemo()

        while isMainMenuScene:
            mainMenu()
    except:
        print(f"{traceback.format_exc}")
        messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
        print(f"{bcolors.FAIL}ERROR: Error occurred while replaying scene.")
        print(f'{traceback.format_exc()}{bcolors.ENDC}')
        pygame.quit()

pygame.quit()

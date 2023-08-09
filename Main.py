# default imports
import pygame, sys, math, GameSetting, traceback, json, jsonschema, random, FadeInOut
from tkinter import messagebox
from videoplayer import Video
from pygame.locals import *
from ButtonManager import Button
from csv import reader

print('INFO: Loading..')

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (97, 97, 97)
DARK_GRAY = (23, 23, 23)
ORANGE = (252, 186, 3)
PURPLE = (119, 3, 252)
YELLOW = (252, 252, 3)
RED = (255, 0, 0)

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
    # background / Favicon
    img_backgroundLoop = pygame.image.load('./src/img/background/game_default_background.png').convert_alpha()
    img_backgroundLoop = pygame.transform.scale(img_backgroundLoop,(GameSetting.WIDTH, GameSetting.HEIGHT))
    img_gameFavicon = pygame.image.load('./src/img/gameicon_placeholder.png').convert_alpha()
    img_gameLogo = pygame.image.load('./src/img/gamelogo.png').convert_alpha()
    img_gameLogo = pygame.transform.scale(img_gameLogo, (200, 100))

    # icon
    icn_GunSelect_handGun = pygame.image.load('./src/img/icon/indiv_icon/Handgun.png').convert_alpha()
    icn_GunSelect_handGun = pygame.transform.scale(icn_GunSelect_handGun, (32, 32))
    icn_GunSelect_machineGun = pygame.image.load('./src/img/icon/indiv_icon/Machinegun.png').convert_alpha()
    icn_GunSelect_machineGun = pygame.transform.scale(icn_GunSelect_machineGun, (32, 32))
    
    # hud
    hud_HealthFull = pygame.image.load('./src/img/hud/hud_health1.png').convert_alpha()
    hud_HealthFull = pygame.transform.scale(hud_HealthFull, (32, 32))
    hud_HealthHalf = pygame.image.load('./src/img/hud/hud_health_half.png').convert_alpha()
    hud_HealthHalf = pygame.transform.scale(hud_HealthHalf, (32, 32))
    hud_HealthEmpty = pygame.image.load('./src/img/hud/hud_health_empty.png').convert_alpha()
    hud_HealthEmpty = pygame.transform.scale(hud_HealthEmpty, (32, 32))
    hud_radiation = pygame.image.load('./src/img/hud/hud_radiation.png').convert_alpha()
    hud_radiation = pygame.transform.scale(hud_radiation, (32, 32))
    hudBackground_weaponSelect = pygame.image.load('./src/img/hud/weapon_select.png').convert_alpha()

    # button
    btn_Start = pygame.image.load('./src/img/button/menu/start_btn.png').convert_alpha()
    btn_Load = pygame.image.load('./src/img/button/menu/load_btn.png').convert_alpha()
    btn_Setting = pygame.image.load('./src/img/button/menu/setting_btn.png').convert_alpha()
    btn_Copyright = pygame.image.load('./src/img/button/menu/copyright_btn.png').convert_alpha()
    btn_Exit = pygame.image.load('./src/img/button/menu/exit_btn.png').convert_alpha()

    # crosshair
    csrImg_Crosshair = pygame.image.load('./src/img/cursor/default-crosshair.png').convert_alpha()

    # background
    tile_mapDefaultBackground = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png').convert_alpha()
    mainMenu_backgruond = pygame.image.load('.\\src\\img\\background\\menu_background.png').convert_alpha()
    img_demoMapBackground = pygame.image.load('./src/maps/png/dev_test.png').convert_alpha()

    map_devTest = pygame.image.load('./src/maps/png/dev_test.png').convert_alpha()

    # map wall
    backgroundWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile7.png').convert_alpha()
    topWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile1.png').convert_alpha()
    topLeftDownWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile2.png').convert_alpha()
    rightStraightWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile3.png').convert_alpha()
    toprightDownWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile4.png').convert_alpha()
    straightWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile6.png').convert_alpha()
    straightNonDownWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile9.png').convert_alpha()
    topRightWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile10.png').convert_alpha()
    rightNonLeftWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile14.png').convert_alpha()
    topLeftWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile12.png').convert_alpha()
    leftNonRightWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile16.png').convert_alpha()
    nonWall = pygame.image.load('.\\src\\img\\map_tile\\indiv_tile\\Tile13.png').convert_alpha()
    voidWall = pygame.image.load('.\\src\\img\\map_tile\\void.png').convert_alpha()

    entity_Bullet = pygame.image.load('.\\src\\img\\animations\\object\\bullet\\BulletProjectile.png').convert_alpha()

    img_overlayDeadScreenBlack = pygame.image.load('.\\src\\img\\hud\\overlay\\transparentBlack.png').convert_alpha()
    img_blackVoid = pygame.image.load('.\\src\\img\\map_tile\\void.png').convert_alpha()
    img_blackVoid = pygame.transform.scale(img_blackVoid, (GameSetting.WIDTH, GameSetting.HEIGHT))
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
showIfDebugging = defaultBulletFont.render('DEBUG MODE', True, ORANGE)
showIfNonProductMode = defaultBulletFont.render('완성된 제품이 아님', True, YELLOW)

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

def createTitle(title, subtitle, x, y):
    print("[TITLE MANAGER] Creating Title..")
    try:
        lastTick = pygame.time.get_ticks()
        fadeOutValue = 350

        titleFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 30)
        subtitleFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 20)

        titleText = titleFont.render(title, True, (255, 255, 255))
        subtitleText = subtitleFont.render(subtitle, (255, 255, 255))

        screen.blit(titleText, [x, y])
        screen.blit(subtitleText, [x, y+10])

        fadeOutValue -= lastTick

        if fadeOutValue <= 0:
            FadeInOut.FadeManager.fadeOut(titleText)
            FadeInOut.FadeManager.fadeOut(subtitleText)

    except:
        print("[TITLE MANAGER] Error occurred while creating title.")
        print(f"[TITLE MANAGER] Traceback: {traceback.print_exc}")


class Player(pygame.sprite.Sprite): # player
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame1.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.base_player_image = self.image
        self.playerShootFrame = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame2.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.hitbox_rect = self.base_player_image.get_rect(center = pos)
        self.rect = self.hitbox_rect.copy()
        self.lastTick = pygame.time.get_ticks()
        self.speed = GameSetting.PLAYER_SPEED
        self.DashSpeed = GameSetting.PLAYER_DASH_SPEED
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
        self.bulletLeft = LoadedHandgunBullet
        self.vecPos = pygame.math.Vector2(pos)

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
            self.checkShooting()
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

    def checkCollisionWithWall(self, direction):
        for sprite in obstaclesGroup:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == "horizontal":
                    if self.velocity_x > 0:
                        self.hitbox_rect.right = sprite.rect.left
                    if self.velocity_x < 0:
                        self.hitbox_rect.left = sprite.rect.right
                
                if direction == "vertical":
                    if self.velocity_y < 0:
                        self.hitbox_rect.top = sprite.rect.bottom
                    if self.velocity_y > 0:
                        self.hitbox_rect.bottom = sprite.rect.top

    def checkShooting(self): 
        if self.shoot_cooldown == 0:
            spawnBulletPos = self.vec_pos + self.gunBarrelOffset.rotate(self.angle)
            self.bullet = Bullet(spawnBulletPos[0], spawnBulletPos[1], self.angle)
            self.shoot_cooldown = GameSetting.BULLET_COOLDOWN
            bulletGroup.add(self.bullet)
            allSpritesGroup.add(self.bullet)

    def move(self):
        self.hitbox_rect.centerx += self.velocity_x
        self.checkCollisionWithWall("horizontal")

        self.hitbox_rect.centery += self.velocity_y
        self.checkCollisionWithWall("vertical")

        self.hitbox_rect.center = self.hitbox_rect.center 
        
        self.vec_pos = (self.hitbox_rect.centerx, self.hitbox_rect.centery)
        
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
        self.image = entity_Bullet
        self.image = pygame.transform.rotozoom(self.image, 0, GameSetting.BULLET_VIEWSIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.speed = GameSetting.BULLET_SPEED
        self.angle = angle
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
        self.bullet_lifetime = GameSetting.BULLET_LIFETIME
        self.spawn_time = pygame.time.get_ticks() # gets the specific time that the bullet was created, stays static
        

    def bulletMovement(self): 
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime: 
            self.kill()
            sfx_handgunFire.stop()

    def checkCollisionWithWall(self):         
        if pygame.sprite.spritecollide(self, obstaclesGroup, False): # wall collisions
            self.kill()

    def update(self):
        self.bulletMovement()
        self.checkCollisionWithWall()

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
        self.direction_list = [(1,1), (1,-1), (-1,1), (-1,-1)]

    def getNewPathTrace(self):
        self.direction_index = random.randint(0, len(self.direction_list)-1)
        self.steps = random.randint(3, 6) * GameSetting.TILESIZE

    def check_collision(self, direction, move_state):
        for sprite in obstaclesGroup:
            if sprite.rect.colliderect(self.rect):
                self.collide = True
                if direction == "horizontal":
                    if self.velocity.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.velocity.x < 0:
                        self.rect.left = sprite.rect.right 
                if direction == "vertical":
                    if self.velocity.y < 0:
                        self.rect.top = sprite.rect.bottom
                    if self.velocity.y > 0:
                        self.rect.bottom = sprite.rect.top
                if move_state == "roam":
                    self.getNewPathTrace()


    def pathTracePlayer(self): # path tracing
        if self.velocity.x > 0:
            self.current_movement_sprite = 0
        else:
            self.current_movement_sprite = 1
        
        player_vector = pygame.math.Vector2(player.rect.center)
        enemy_vector = pygame.math.Vector2(self.rect.center)
        distance = self.getVectorDistance(player_vector, enemy_vector)

        if distance > 0:
            self.direction = (player_vector - enemy_vector).normalize()
        else:
            self.direction = pygame.math.Vector2()

        self.velocity = self.direction * self.speed
        self.position += self.velocity

        self.rect.centerx = self.position.x
        self.check_collision("horizontal", "hunt")

        self.rect.centery = self.position.y
        self.check_collision("vertical", "hunt")

        self.rect.center = self.rect.center

        self.position = (self.rec.centerx, self.rect.centery)

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

class GameLevel(pygame.sprite.Group): 
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = img_demoMapBackground.get_rect(topleft = (0,0))
        self.enemy_spawn_pos = []
        self.health_spawn_pos = []
        self.create_map()

    def create_map(self):
        layouts = {
                   "boundary": self.import_csv_layout("./src/maps/csv/dev_test/dev_test_Boundary.csv"),
                   "walls": self.import_csv_layout("./src/maps/csv/dev_test/dev_test_Walls.csv"),
                   "enemies": self.import_csv_layout("./src/maps/csv/dev_test/dev_test_Enemy.csv"),
                   "health potions": self.import_csv_layout("./src/maps/csv/dev_test/dev_test_Health.csv")
                  }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * GameSetting.TILESIZE
                        y = row_index * GameSetting.TILESIZE
                        if style == "boundary":
                            Tile((x,y), [obstaclesGroup], "boundary", col)
                        if style == "walls":
                            Tile((x,y), [allSpritesGroup], "walls", col)  
                        if style == "enemies":
                            self.enemy_spawn_pos.append((x, y))
                        if style == "health potions":
                            self.health_spawn_pos.append((x, y))
                    #else:
                    #    Tile((0, 0), [allSpritesGroup], "void", '-1')

    def import_csv_layout(self, path):
        terrain_map = []
        with open(path) as level_map:
            layout = reader(level_map, delimiter=",")
            for row in layout:
                terrain_map.append(list(row))
            return terrain_map
    
    def custom_draw(self): 
        self.offset.x = player.rect.centerx - (GameSetting.WIDTH // 2) # gotta blit the player rect not base rect
        self.offset.y = player.rect.centery - (GameSetting.HEIGHT // 2)

        #draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset

        screen.blit(img_blackVoid, [0, 0])
        screen.blit(img_demoMapBackground, floor_offset_pos)

        # draw the PLAYER'S rectangles for demonstration purposes
        # base_rect = player.base_player_rect.copy().move(-self.offset.x, -self.offset.y)
        # pygame.draw.rect(screen, "red", base_rect, width=2)
        # rect = player.rect.copy().move(-self.offset.x, -self.offset.y)
        # pygame.draw.rect(screen, "yellow", rect, width=2)

        # # draw the ZOMBIE'S rectangles for demonstration purposes
        # base_rect = necromancer.base_zombie_rect.copy().move(-self.offset.x, -self.offset.y)
        # pygame.draw.rect(screen, "red", base_rect, width=2)
        # rect = necromancer.rect.copy().move(-self.offset.x, -self.offset.y)
        # pygame.draw.rect(screen, "yellow", rect, width=2)   

        # print(base_rect.x, base_rect.y)


        for sprite in allSpritesGroup: 
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

class Tile(pygame.sprite.Sprite): 
    def __init__(self, pos, groups, type, unique_id):
        super().__init__(groups)
        if type == "void":
            self.image = voidWall
        elif type == "boundary":
            self.image = backgroundWall
        elif type == "walls":
            if unique_id == "0":
                self.image = topWall
            if unique_id == "1":
                self.image = topLeftDownWall
            if unique_id == "2":
                self.image = rightStraightWall
            if unique_id == "3":
                self.image = toprightDownWall
            if unique_id == "4":
                self.image = straightWall
            if unique_id == "5":
                self.image = straightWall
            if unique_id == "7":
                self.image = straightWall
            if unique_id == "8":
                self.image = straightNonDownWall
            if unique_id == "9":
                self.image = topRightWall
            if unique_id == "10":
                self.image = rightStraightWall
            if unique_id == "11":
                self.image = topLeftWall
            if unique_id == "12":
                self.image = nonWall
            if unique_id == "13":
                self.image = rightNonLeftWall
            if unique_id == "14":
                self.image = rightStraightWall
            if unique_id == "15":
                self.image = leftNonRightWall
        elif type == "void":
            if unique_id == "4":
                self.image = voidWall

        # if type == "props":
        #     self.image = torch_img
        
        self.rect = self.image.get_rect(topleft = pos) 

player = Player((400, 400))
allSpritesGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
obstaclesGroup = pygame.sprite.Group()
floorGroup = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
demoLevel = GameLevel()
#zombie = Enemy((0, 0))

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

def drawDeadScreen():
    if not player.alive:
        game_over_screen_fade = pygame.Surface((GameSetting.WIDTH, GameSetting.HEIGHT))
        game_over_screen_fade.fill((0, 0, 0))
        game_over_screen_fade.set_alpha(160)
        screen.blit(game_over_screen_fade, (0, 0))

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
                        print(f"{bcolors.FAIL}ERROR: Failed to save file to {svFile}.\nERROR: Is file even exist?")
                        print(f"Traceback: {traceback.print_exc()}{bcolors.ENDC}")
                    pygame.quit()
                    sys.exit()

            screen.blit(voidWall, (GameSetting.WIDTH, GameSetting.HEIGHT))

            demoLevel.custom_draw()

            # render
            allSpritesGroup.update()
            playerGroup.update()

            # debug info update
            hud_playerMana = defaultBulletFont.render(f'{str(player.playerMana)}%', True, WHITE)
            hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, WHITE)
            hud_debugMilliTickScreen = defaultBulletFont.render(f'{math.ceil(clock.get_rawtime())}틱 처리중 (반올림됨, 낮을수록 좋음)', True, WHITE)
            hud_bulletLeft = defaultBulletFont.render(str(LoadedHandgunBullet), True, WHITE)
            hud_debugMapInfoScreen = defaultBulletFont.render(f'현재 "dev_test_Boundary.csv, dev_test_Enemy.csv, dev_test_Health.csv, dev_test_Walls.csv" 불러와짐', True, WHITE)
            hud_debugVerInfoScreen = defaultCopyrightFont.render(f'spsro Engine ver {GameSetting.VER}, using some files from pygame 2.5.0', True, WHITE)
            hud_debugScreenResInfoScreen = defaultBulletFont.render(f'{GameSetting.WIDTH} x {GameSetting.HEIGHT} 해당도로 플레이중 (최대 {GameSetting.DEF_FPS}FPS)', True, WHITE)

            if clock.get_fps() <= 30:
                hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, ORANGE)
            elif clock.get_fps() <= 20:
                hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, (235, 232, 52))
            elif clock.get_fps() <= 10:
                hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, RED)

            if math.ceil(clock.get_rawtime()) >= 5:
                hud_debugMilliTickScreen = defaultBulletFont.render(f'{math.ceil(clock.get_rawtime())}틱 처리중 (반올림됨, 낮을수록 좋음) 주의: 처리한 틱 갯수가 일반적인 상황보다 많음', True, ORANGE)
            elif math.ceil(clock.get_rawtime()) >= 15:
                hud_debugMilliTickScreen = defaultBulletFont.render(f'{math.ceil(clock.get_rawtime())}틱 처리중 (반올림됨, 낮을수록 좋음) 경고: 처리한 틱 갯수가 많음', True, (235, 232, 52))
            elif math.ceil(clock.get_rawtime()) >= 45:
                hud_debugMilliTickScreen = defaultBulletFont.render(f'{math.ceil(clock.get_rawtime())}틱 처리중 (반올림됨, 낮을수록 좋음) 경고: 처리한 틱 갯수가 정상적인 상황보다 많음, 최적화 필요', True, RED)

            screen.blit(icn_GunSelect_handGun, [30, 670])
            screen.blit(hud_bulletLeft, [75, 670])
            screen.blit(hud_bulletSlash, [103, 670])
            screen.blit(hud_bulletMax, [115, 670])
            
            if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
                screen.blit(showIfDebugging, [30, 67])

                if GameSetting.ISPRODUCTMODE == False:
                    screen.blit(showIfNonProductMode, [30, 640])

                if GameSetting.SHOW_CURRENTFPS == True:
                        pygame.display.set_caption(f"FPS: {clock.get_fps()}")
                else:
                    pass
                if GameSetting.SHOW_DEBUGINFO_TOSCREEN == True:
                    screen.blit(hud_debugFpsScreen, [30, 97])
                    screen.blit(hud_debugMilliTickScreen, [30, 120])
                    screen.blit(hud_playerMana, [30, 145])
                    screen.blit(hud_debugMapInfoScreen, [30, 170])
                    screen.blit(hud_debugVerInfoScreen, [30, 215])
                    screen.blit(hud_debugScreenResInfoScreen, [30, 195])
            else:
                pass

            pygame.display.update()
            dt = clock.tick(GameSetting.DEF_FPS)

def mainMenu(): # main menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(mainMenu_backgruond, [0, 0])
        screen.blit(text_version, [32, 53])
        screen.blit(text_MainLogoTitle, [30, 20])
        screen.blit(text_copyrightTeamName, [985, 650])
        screen.blit(text_mainMenuMotd, [32, 83])

        # debug info update
        hud_playerMana = defaultBulletFont.render(f'{str(player.playerMana)}%', True, WHITE)
        hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, WHITE)
        hud_debugMilliTickScreen = defaultBulletFont.render(f'{math.ceil(clock.get_rawtime())}TICK (반올림됨, 낮을수록 좋음)', True, WHITE)
        hud_debugMapInfoScreen = defaultBulletFont.render('불러온 맵이 없음', True, WHITE)
        hud_debugVerInfoScreen = defaultCopyrightFont.render(f'spsro Engine ver {GameSetting.VER}, using some files from pygame 2.5.0', True, WHITE)

        if clock.get_fps() <= 30:
            hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, ORANGE)
        elif clock.get_fps() <= 20:
            hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, (235, 232, 52))
        elif clock.get_fps() <= 10:
            hud_debugFpsScreen = defaultBulletFont.render(f'{math.ceil(clock.get_fps())}FPS (반올림됨, 높을수록 좋음)', True, RED)
            
        if GameSetting.IFYOUKNOWWHATAREYOUDOINGRIGHTNOWTURNONTHISFORDEBUG:
            screen.blit(showIfDebugging, [30, 67])
            if GameSetting.ISPRODUCTMODE == False:
                screen.blit(showIfNonProductMode, [30, 640])

            if GameSetting.SHOW_CURRENTFPS == True:
                    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
            else:
                pass
            if GameSetting.SHOW_DEBUGINFO_TOSCREEN == True:
                screen.blit(hud_debugFpsScreen, [30, 97])
                screen.blit(hud_debugMilliTickScreen, [30, 120])
                screen.blit(hud_playerMana, [30, 145])
                screen.blit(hud_debugMapInfoScreen, [30, 170])
                screen.blit(hud_debugVerInfoScreen, [30, 195])
        else:
            pass

        if btnStart.drawBtn(screen):
            gameDemo()
                
        if btnLoad.drawBtn(screen):
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
    except Exception:
        print(f"{traceback.format_exc()}")
        messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
        print(f"{bcolors.FAIL}ERROR: Error occurred while replaying scene.")
        print(f'{traceback.format_exc()}{bcolors.ENDC}')
        pygame.quit()

pygame.quit()

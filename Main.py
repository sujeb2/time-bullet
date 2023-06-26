import pygame, sys, math, GameSetting, time, traceback
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
    print(f"{traceback.format_exc}")
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
    print(f"{traceback.format_exc}")
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
    print(f"{traceback.format_exc}")
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
    print(f"{traceback.format_exc}")
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

hud_bulletLeft = defaultBulletFont.render(str_MaxHandgunLoadBullet, False, WHITE)
hud_bulletMax = defaultBulletFont.render(str_MaxHandgunBullet, False, WHITE)
hud_bulletSlash = defaultBulletFont.render('/', True, WHITE)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(GameSetting.PLAYER_START_X, GameSetting.PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load('./src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame1.png').convert_alpha(), 0, GameSetting.PLAYER_VIEW_SIZE)
        self.base_player_image = self.image
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.speed = GameSetting.PLAYER_SPEED
        self.shoot = False
        self.shoot_cooldown = 0
        self.gunBarrelOffset = pygame.math.Vector2(GameSetting.GUN_OFFSET_X, GameSetting.GUN_OFFSET_Y)
       

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

        if pygame.mouse.get_pressed() == (1, 0, 0) or keys[pygame.K_SPACE]:
            self.shoot = True
            self.is_shooting()
        else:
            self.shoot = False

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

# 메인
print(f"Replaying {str_SceneName}..")
try:
    while isMainMenuScene: # replay scene
        inputKey = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isMainMenuScene = False
                isMainGameScene = False

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
        allSpritesGroup.draw(screen)
        allSpritesGroup.update()

        # debug
        if GameSetting.SHOW_PLAYERHITBOX == True:
            pygame.draw.rect(screen, 'red', player.hitbox_rect, width=2)
            pygame.draw.rect(screen, 'yellow', player.rect, width=2)
        else:
            pass
        
        if GameSetting.SHOW_CURRENTFPS == True:
            pygame.display.set_caption(f"FPS: {clock.get_fps()}")
        else:
            pass

        pygame.display.update()
        dt = clock.tick(60)
except:
    print(f"{traceback.format_exc}")
    messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
    print("Error occurred while replaying scene.")
    quitGame()

pygame.quit()
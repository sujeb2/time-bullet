@echo off
title TIME/BULLET Builder

echo.
echo Please select an option below
echo =============================
echo 1. Build Program (Console)
echo 2. Build Program (Non-Console)
echo 3. Update module
echo 4. Exit
set /p select= >
if /i "%select%" == "1" goto build
if /i "%select%" == "2" goto buildnon
if /i "%select%" == "3" goto update
if /i "%select%" == "4" goto update
pause

:: build program (with console output)
:build
cls
echo Building...
pyinstaller --clean ^
            --log-level DEBUG ^
            --name TIME/BULLET ^
            --console ^
            :: python file
            --add-data="Level.py;." ^
            --add-data="LevelData.py;." ^
            --add-data="MapSetting.py;." ^
            --add-data="supportCSV.py;." ^
            --add-data="TileManager.py;." ^
            --add-data="Title.py;." ^
            --add-data="videoplayer.py;." ^
            :: main data
            :: font
            --add-data="src/font/PretendardVariable.ttf;src/font/" ^
            :: img (animation)
            --add-data="src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame1.png;src/img/animations/entity/player/placeholder/indiv_animation/" ^
            --add-data="src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame2.png;src/img/animations/entity/player/placeholder/indiv_animation/" ^
            --add-data="src/img/animations/entity/player/placeholder/indiv_animation/player_machinegun_frame1.png;src/img/animations/entity/player/placeholder/indiv_animation/" ^
            --add-data="src/img/animations/entity/player/placeholder/indiv_animation/player_machinegun_frame2.png;src/img/animations/entity/player/placeholder/indiv_animation/" ^
            --add-data="src/img/animations/object/bullet/BulletProjectile Dissapate1.png;src/img/animations/object/bullet/" ^
            --add-data="src/img/animations/object/bullet/BulletProjectile Dissapate2.png;src/img/animations/object/bullet/" ^
            --add-data="src/img/animations/object/bullet/BulletProjectile.png;src/img/animations/object/bullet/" ^
            :: img (background)
            --add-data="src/img/background/game_default_background.png;src/img/background/" ^
            :: img (button)
            --add-data="src/img/button/exit_btn.png;src/img/button/" ^
            --add-data="src/img/button/load_btn.png;src/img/button/" ^
            --add-data="src/img/button/setting_btn.png;src/img/button/" ^
            --add-data="src/img/button/start_btn.png;src/img/button/" ^
            :: img (crosshair)
            --add-data="src/img/cursor/default-crosshair.png;src/img/cursor/" ^
            :: img (hud icon)
            --add-data="src/img/hud/hud_health_empty.png;src/img/hud/" ^
            --add-data="src/img/hud/hud_health_half.png;src/img/hud/" ^
            --add-data="src/img/hud/hud_health1.png;src/img/hud/" ^
            --add-data="src/img/hud/hud_radiation.png;src/img/hud/" ^
            --add-data="src/img/hud/weapon_select.png;src/img/hud/" ^
            :: img (normal icon)
            --add-data="src/img/icon/indiv_icon/Bullet.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/BulletEmpty.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/Handgun.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/Knife.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/Machinegun.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/iconwparticle.png;src/img/icon/" ^
            :: img (map sprite)
            --add-data="src/img/map_sprite/light/fake_light_01_800x.png;src/img/icon/map_sprite/light" ^
            --add-data="src/img/map_sprite/light/fake_light_01_normal.png;src/img/map_sprite/light/" ^
            --add-data="src/img/map_sprite/light/fake_light_02_800x.png;src/img/map_sprite/light/" ^
            --add-data="src/img/map_sprite/text/behind-map-cake.png;src/img/map_sprite/text/" ^
            --add-data="src/img/map_sprite/tutorial/tutorial-2.png;src/img/map_sprite/tutorial/" ^
            --add-data="src/img/map_sprite/tutorial/tutorial-3.png;src/img/map_sprite/tutorial/" ^
            --add-data="src/img/map_sprite/tutorial/tutorial-4.png;src/img/map_sprite/tutorial/" ^
            --add-data="src/img/map_sprite/tutorial/tutorial-5.png;src/img/map_sprite/tutorial/" ^
            --add-data="src/img/map_sprite/interior_sprite.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/light_bulb_blue.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/light_bulb_red.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/light_bulb_white.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/light_bulb_yellow.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/lightbulb_tileset.png;src/img/map_sprite/" ^
            :: img (map tile)
            --add-data="src/img/map_tile/Block.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/MapLoadSaveSetup.png.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/MapSetupTileSet.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/NoTexture.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/PlayerSetup.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/Tileset.png;src/img/map_tile/" ^
            :: img (player deco)
            --add-data="src/img/player_deco/vignette.png;src/img/player_deco" ^
            --add-data="src/img/gameicon_placeholder.png;src/img/" ^
            --add-data="src/img/gamelogo.png;src/img/" ^
            :: map data
            --add-data="src/maps/csv/evo_1/evo_1.tmx;src/maps/csv/evo_1/" ^
            --add-data="src/maps/csv/tutorial/tutorial_Base.tmx;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial/tutorial_Deco.csv;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial/tutorial_Object.csv;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial/tutorial_SetupTile.csv;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial/tutorial.csv;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial.tmx;src/maps/" ^
            --add-data="src/maps/README.md;src/maps/" ^
            :: mp4
            --add-data="src/mp4/std_start.mp4;src/mp4" ^
            :: save data
            --add-data="src/save/0/playerSaveData.json;src/save/0/" ^
            :: sound
            --add-data="src/sound/ost/background_ambient1.wav;src/sound/ost/" ^
            ::--add-data="src/sound/ost/background_ambient1.wav;src/sound/sfx/" ^
            :: tileset
            --add-data="src/tileset/easteregg.tsx;src/tileset/" ^
            --add-data="src/tileset/Interior.tsx;src/tileset/" ^
            --add-data="src/tileset/Light.tsx;src/tileset/" ^
            --add-data="src/tileset/MapSetupTileSet.tsx;src/tileset/" ^
            --add-data="src/tileset/MapSprites.tsx;src/tileset/" ^
            --add-data="src/tileset/PlayerSetup.tsx;src/tileset/" ^
            --add-data="src/tileset/Tileset.tsx;src/tileset/" ^

:: build program (without console)
:buildnon
cls
echo Building..
pyinstaller --clean ^
            --log-level DEBUG ^
            --name TIME/BULLET ^
            -w ^
            :: python file
            --add-data="Level.py;." ^
            --add-data="LevelData.py;." ^
            --add-data="MapSetting.py;." ^
            --add-data="supportCSV.py;." ^
            --add-data="TileManager.py;." ^
            --add-data="Title.py;." ^
            --add-data="videoplayer.py;." ^
            :: main data
            :: font
            --add-data="src/font/PretendardVariable.ttf;src/font/" ^
            :: img (animation)
            --add-data="src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame1.png;src/img/animations/entity/player/placeholder/indiv_animation/" ^
            --add-data="src/img/animations/entity/player/placeholder/indiv_animation/player_handgun_frame2.png;src/img/animations/entity/player/placeholder/indiv_animation/" ^
            --add-data="src/img/animations/entity/player/placeholder/indiv_animation/player_machinegun_frame1.png;src/img/animations/entity/player/placeholder/indiv_animation/" ^
            --add-data="src/img/animations/entity/player/placeholder/indiv_animation/player_machinegun_frame2.png;src/img/animations/entity/player/placeholder/indiv_animation/" ^
            --add-data="src/img/animations/object/bullet/BulletProjectile Dissapate1.png;src/img/animations/object/bullet/" ^
            --add-data="src/img/animations/object/bullet/BulletProjectile Dissapate2.png;src/img/animations/object/bullet/" ^
            --add-data="src/img/animations/object/bullet/BulletProjectile.png;src/img/animations/object/bullet/" ^
            :: img (background)
            --add-data="src/img/background/game_default_background.png;src/img/background/" ^
            :: img (button)
            --add-data="src/img/button/exit_btn.png;src/img/button/" ^
            --add-data="src/img/button/load_btn.png;src/img/button/" ^
            --add-data="src/img/button/setting_btn.png;src/img/button/" ^
            --add-data="src/img/button/start_btn.png;src/img/button/" ^
            :: img (crosshair)
            --add-data="src/img/cursor/default-crosshair.png;src/img/cursor/" ^
            :: img (hud icon)
            --add-data="src/img/hud/hud_health_empty.png;src/img/hud/" ^
            --add-data="src/img/hud/hud_health_half.png;src/img/hud/" ^
            --add-data="src/img/hud/hud_health1.png;src/img/hud/" ^
            --add-data="src/img/hud/hud_radiation.png;src/img/hud/" ^
            --add-data="src/img/hud/weapon_select.png;src/img/hud/" ^
            :: img (normal icon)
            --add-data="src/img/icon/indiv_icon/Bullet.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/BulletEmpty.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/Handgun.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/Knife.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/Machinegun.png;src/img/icon/indiv_icon/" ^
            --add-data="src/img/icon/indiv_icon/iconwparticle.png;src/img/icon/" ^
            :: img (map sprite)
            --add-data="src/img/map_sprite/light/fake_light_01_800x.png;src/img/icon/map_sprite/light" ^
            --add-data="src/img/map_sprite/light/fake_light_01_normal.png;src/img/map_sprite/light/" ^
            --add-data="src/img/map_sprite/light/fake_light_02_800x.png;src/img/map_sprite/light/" ^
            --add-data="src/img/map_sprite/text/behind-map-cake.png;src/img/map_sprite/text/" ^
            --add-data="src/img/map_sprite/tutorial/tutorial-2.png;src/img/map_sprite/tutorial/" ^
            --add-data="src/img/map_sprite/tutorial/tutorial-3.png;src/img/map_sprite/tutorial/" ^
            --add-data="src/img/map_sprite/tutorial/tutorial-4.png;src/img/map_sprite/tutorial/" ^
            --add-data="src/img/map_sprite/tutorial/tutorial-5.png;src/img/map_sprite/tutorial/" ^
            --add-data="src/img/map_sprite/interior_sprite.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/light_bulb_blue.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/light_bulb_red.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/light_bulb_white.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/light_bulb_yellow.png;src/img/map_sprite/" ^
            --add-data="src/img/map_sprite/lightbulb_tileset.png;src/img/map_sprite/" ^
            :: img (map tile)
            --add-data="src/img/map_tile/Block.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/MapLoadSaveSetup.png.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/MapSetupTileSet.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/NoTexture.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/PlayerSetup.png;src/img/map_tile/" ^
            --add-data="src/img/map_tile/Tileset.png;src/img/map_tile/" ^
            :: img (player deco)
            --add-data="src/img/player_deco/vignette.png;src/img/player_deco" ^
            --add-data="src/img/gameicon_placeholder.png;src/img/" ^
            --add-data="src/img/gamelogo.png;src/img/" ^
            :: map data
            --add-data="src/maps/csv/evo_1/evo_1.tmx;src/maps/csv/evo_1/" ^
            --add-data="src/maps/csv/tutorial/tutorial_Base.tmx;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial/tutorial_Deco.csv;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial/tutorial_Object.csv;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial/tutorial_SetupTile.csv;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial/tutorial.csv;src/maps/csv/tutorial/" ^
            --add-data="src/maps/csv/tutorial.tmx;src/maps/" ^
            --add-data="src/maps/README.md;src/maps/" ^
            :: mp4
            --add-data="src/mp4/std_start.mp4;src/mp4" ^
            :: save data
            --add-data="src/save/0/playerSaveData.json;src/save/0/" ^
            :: sound
            --add-data="src/sound/ost/background_ambient1.wav;src/sound/ost/" ^
            ::--add-data="src/sound/ost/background_ambient1.wav;src/sound/sfx/" ^
            :: tileset
            --add-data="src/tileset/easteregg.tsx;src/tileset/" ^
            --add-data="src/tileset/Interior.tsx;src/tileset/" ^
            --add-data="src/tileset/Light.tsx;src/tileset/" ^
            --add-data="src/tileset/MapSetupTileSet.tsx;src/tileset/" ^
            --add-data="src/tileset/MapSprites.tsx;src/tileset/" ^
            --add-data="src/tileset/PlayerSetup.tsx;src/tileset/" ^
            --add-data="src/tileset/Tileset.tsx;src/tileset/" ^

:: update modules
:update
cls
echo Updating..
pip install -r requirements.txt
echo Complete!
pause
goto main

:: exit program
:exitp
exit
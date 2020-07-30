from pygame_functions11 import *

#Initial Screen Settings
HUD_Height = 32
tile_size = 32
screen_width=tile_size*32
screen_height=tile_size*24 + HUD_Height
screen = screenSize(screen_width,screen_height)

#Save Select Screen
background = Background()
introMusic = makeMusic("01-intro.mp3")
background.setTiles("saveSelectScreen.png")
select = False
playMusic(99)
selected = 1
yPos = 280
selectRect = drawRect(180, 280, 650, 75, "yellow", 5)
save1Text = makeLabel("Joe", 68, 510, 290, 'white', 'system', 'black')
showLabel(save1Text)
while select == False:
    pause(10)
    if keyPressed("down"):
        screen.blit(background.surface, [0, 0])
        pause(100)
        yPos += 75
        selected +=1
        if yPos > 580:
            yPos = 280
            selected = 1
        #selectRect.move(0, yPos)
        pygame.display.update()
        drawRect(180, yPos, 650, 75, "yellow", 5)
    if keyPressed("up"):
        screen.blit(background.surface, [0, 0])
        pause(100)
        yPos -= 75
        selected -=1
        if yPos < 280:
            yPos = 580
            selected = 5
        #selectRect.move(0, yPos)
        pygame.display.update()
        drawRect(180, yPos, 650, 75, "yellow", 5)
    if keyPressed("return"):
        hideLabel(save1Text)
        select = True
    updateDisplay()
stopMusic()

#Change Music, Unload Only works if pygame2.0
if pygame.version.vernum[0] >=2:
    pygame.mixer.music.unload()
music = makeMusic("linkMusic.mp3")
playMusic(99)

#Set Up HUD
HealthLabel = makeLabel("Health = 6", 32, 50, 8, "white", "system")
RupeeLabel = makeLabel("Rupee = 0", 32, 200, 8, "white", "system")



#Set Up Sprites
setAutoUpdate(False)
link = Player()
sword = Sword(link)

#Change Link's Stuff based upon save file
loadGame(selected, link)
changeLabel(HealthLabel, "Health = " + str(link.health))
changeLabel(RupeeLabel, "Rupee = " + str(link.rupee))

#Set up Scenes
scene1 = Scene(link, "ZeldaMapTilesBrown.png", "map1.txt", 6,8)
scene2 = Scene(link, "ZeldaMapTilesBrown.png", "map2.txt", 6,8)
scene3 = Scene(link, "ZeldaMapTilesWhite.png", "map3.txt", 6,8)
scene4 = Scene(link, "ZeldaMapTilesGreen.png", "map4.txt", 6,8)

scenes = [[scene1, scene3], [scene2, scene4]]
currentScene = scene1


showBackground(currentScene)

showSprite(link)
for enemy in scene1.Enemies:
    showSprite(enemy)

showLabel(HealthLabel)
showLabel(RupeeLabel)

nextFrame = clock()
frame = 0
# i is the list number
# j is the element number
i = 0
j= 0

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
        for wall in currentScene.Wall_Tiles:
            if touching(wall, link):
                link.speed = -link.speed
                link.move(frame)
                link.speed = - link.speed
        
        if keyPressed("down"):
            
            link.orientation =0
            link.move(frame)
        elif keyPressed("up"):
            link.orientation =1
            link.move(frame)
        elif keyPressed("right"):
            link.orientation =2
            link.move(frame)
        elif keyPressed("left"):
            link.orientation =3
            link.move(frame)
        elif keyPressed("space"):
            changeSpriteImage(link, link.orientation + 8)
        #Sword Swing Code
            sword.swing()
            for enemy in currentScene.Enemies:
                if touching(sword, enemy):
                    if enemy.health == 1:
                        currentScene.Enemies.remove(enemy)
                        link.kills += 1
                        itemDrop = dropChart(link.kills)
                        print(itemDrop)
                        if itemDrop == 0:
                            aRupee = Rupee()
                            aRupee.move(enemy.rect.x, enemy.rect.y)
                            currentScene.Items.append(aRupee)
                            showSprite(aRupee)
                        elif itemDrop == 1:
                            aHeart = Heart()
                            aHeart.move(enemy.rect.x, enemy.rect.y)
                            currentScene.Items.append(aHeart)
                            showSprite(aHeart)
                        elif itemDrop == 2:
                            pass
                            #To Do Program Fairy
                        elif itemDrop == 3:
                            pass
                            #To Do Program Bomb
                        elif itemDrop == 4:
                            pass
                            #To Do Program Timer
                        elif itemDrop ==5:
                            aBRupee = BlueRupee()
                            aBRupee.move(x,y)
                            currentScene.Items.append(aBRupee)
                            showSprite(aBRupee)
                    enemy.hit()
        if not keyPressed("space") or keyPressed("left") or keyPressed("right") or keyPressed("up") or keyPressed("down"):
            hideSprite(sword)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        
        for enemy in currentScene.Enemies:
            enemy.move(frame)            
            if touching(enemy, link):
                link.hit(currentScene.Wall_Tiles)
            for wall in currentScene.Wall_Tiles:
                while touching(enemy, wall) or enemy.rect.x > screen_width or enemy.rect.y>screen_height or enemy.rect.x<0 or enemy.rect.y<0:
                    enemy.turn()
                    enemy.move(frame)
        for item in currentScene.Items:
            item.animate(frame)
            if touching(item, link):
                link.collect(item)
                currentScene.Items.remove(item)
                killSprite(item)
                changeLabel(HealthLabel, "Health = " + str(link.health))
                changeLabel(RupeeLabel, "Rupee = " + str(link.rupee))
        if link.rect.x + tile_size//2 > screen_width:
            hideBackground(currentScene)
            i += 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.x = 32
            showSprite(link)
        elif link.rect.x - tile_size//2 < 0:
            hideBackground(currentScene)
            i -= 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.x = screen_width -32
            showSprite(link)
        elif link.rect.y + tile_size//2 > screen_height:
            hideBackground(currentScene)
            j += 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.y = 64
            showSprite(link)
        elif link.rect.y - tile_size//2 < 32:
            hideBackground(currentScene)
            j -= 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.y = screen_height - 32
            showSprite(link)
        updateDisplay()

endWait()
add_library("sound")
import os, random
path=os.getcwd()

class ninja:
    def __init__(self,x,y):
        self.x=x  #x coordinate of starting top left corner
        self.y=y  #y coordinate of the same point
        self.vx=0
        self.w = 126 #dimensions
        self.h = 100
        self.i = 0   # for the frame of animation
        self.keyHandler={32:False} #using SPACE key to trigger jump
        self.dir = False #direction for display and update functions
        self.jump = loadImage(path+'\\images\\Jump__009.png')
        self.lcol=False
        self.rcol=False
        self.boosterCollect=False
        self.images=[] #List which has all frames of running
        self.balconySound=SoundFile(this,path+'/sounds/balcony.wav')
        self.boosterSound=SoundFile(this,path+'/sounds/booster.wav')
        self.bladeSound=SoundFile(this,path+'/sounds/blade.wav')
        self.boosterImg=loadImage(path+'\\images\\air.png')
        for img in range(10):
            self.images.append(loadImage(path+'\\images\\Run__00'+str(img)+'.png'))
                
    def update(self):
        # Checks for collision and updates location considering previous location and pressed keys
        self.collision()
        if self.dir == False:# x velocity is +10 until it reaches right platform

            if self.keyHandler[32]:
                self.vx = 10
                    
            if self.x + 126 >= ninJump.wid-85:
                self.vx=0
                self.keyHandler[32] = False
                self.dir = True
            
        if self.dir == True: # x velocity is -10 until it reaches left platform
        
            if self.keyHandler[32]:
                self.vx = -10
                    
            if self.x <= 85:
                self.vx=0
                self.keyHandler[32] = False
                self.dir = False
            
        # updating location by adding velocity
        if self.lcol != True or self.rcol!=True:
            self.x = self.x + self.vx 
         
        self.y = self.y + self.vy  
        
        # starts looping screen when ninja gets to half screen
        if self.y <= ninJump.heigh//2:
            ninJump.y+=self.vy
            
   
            
   
    def collision(self): # Different actions based on object
        for b in ninJump.allBalc:
            if abs(b.y-self.y)<150 and abs(b.x-self.x)<126 and b.arg==1 and self.dir==False:
                self.vy=12
                self.vx=0.05
                ninJump.dead=True
                if self.lcol!=True:
                    self.balconySound.play()
                self.lcol=True
                
            elif abs(b.y-self.y)<100 and abs(b.x-self.x)<126 and b.arg==1 and self.dir==True and (self.x>85 and self.x<650-85):
                self.vy=12
                self.vx=0.05
                ninJump.dead=True
                if self.lcol!=True:
                    self.balconySound.play()
                self.lcol=True
                
            elif abs(b.y-self.y)<150 and abs(b.x-self.x)<126 and b.arg==2 and self.dir==True:
                self.vy=12
                self.vx=-0.05
                ninJump.dead=True
                if self.rcol!=True:
                    self.balconySound.play()
                self.rcol=True
                
            elif abs(b.y-self.y)<100 and abs(b.x-self.x)<126 and b.arg==2 and self.dir==False and (self.x>85 and self.x<650-85):
                self.vy=12
                self.vx=-0.05
                ninJump.dead=True
                if self.rcol!=True:
                    self.balconySound.play()
                self.rcol=True

                
        for s in ninJump.allStar:
            if abs(s.y-self.y)<100 and abs(s.x-self.x)<126 and s.arg==1 and self.dir==False:
                ninJump.allStar.remove(s)
                del s
                ninJump.stars+=1
                self.bladeSound.play()
                        
            elif abs(s.y-self.y)<100 and abs(s.x-self.x)<126 and s.arg==2 and self.dir==True:
                ninJump.allStar.remove(s)
                del s
                ninJump.stars+=1
                self.bladeSound.play()
                
        for b in ninJump.allBoost:
            if abs(b.y-self.y)<80 and abs(b.x-self.x)<126 and b.arg==1 and self.dir==False:
                ninJump.allBoost.remove(b)
                del b
                self.x=250
                self.boosterSound.play()
                self.boosterCollect=True
                
            elif abs(b.y-self.y)<80 and abs(b.x-self.x)<126 and b.arg==2 and self.dir==True:
                ninJump.allBoost.remove(b)
                del b
                self.x=250
                self.boosterSound.play()
                self.boosterCollect=True
    
    def display(self):
        self.update()
        # Changes which image to display based on location and status
        if self.boosterCollect==True:
            self.img=self.boosterImg
        
        elif self.vx>0 or self.vx<0:
            self.img = self.jump
            
        elif self.vy<0:
            self.i = (self.i+0.5) %10
            self.img= self.images[int(self.i)]
        
        if self.dir == False:
            image (self.img, self.x, self.y-ninJump.y, self.w,self.h,self.w, 0, 0, self.h)
        else:
            image (self.img, self.x, self.y-ninJump.y, self.w,self.h)        

class balcony:
    def __init__(self,yLoc,arg):
        self.y=yLoc
        self.arg = arg
        self.bImg = loadImage(path+'\\images\\balcony'+str(self.arg)+'.png')
        if self.arg == 1:
            self.x = 85
        else:
            self.x = 650-82-150
        
    def display(self):
        fill(0)
        image(self.bImg,self.x,self.y-ninJump.y,150,150)
        
class blade:
    def __init__(self,yLoc,arg):
        self.y = yLoc
        self.arg = arg
        self.bImg = loadImage(path+'\\images\\star1.png')
        if self.arg == 1:
            self.x = 85
        else:
            self.x = 650-82-100
    
    def display(self):
        image(self.bImg,self.x,self.y-ninJump.y)
    
class  booster:
    def __init__(self,yLoc,arg):
        self.y = yLoc
        self.arg = arg
        self.bImg = loadImage(path+'\\images\\booster1.png')
        if self.arg == 1:
            self.x = 85
        else:
            self.x = 650-82-80
    
    def display(self):
        image(self.bImg,self.x,self.y-ninJump.y)
    
class game:
    def __init__(self,wid,heigh,stage,stars,state):
        self.wid = wid
        self.heigh = heigh
        self.stage=stage
        self.stars=stars
        self.y = 0
        self.b1 = loadImage(path+'\\images\\background1.png')
        self.b2 = loadImage(path+'\\images\\background2.png')
        self.character = ninja(85,600)
        self.character.vy=-5-(int(self.stage/2))
        self.loadStage()
        self.state = state
        self.starImg = loadImage(path+'\\images\\star1.png')
        self.dead = False
        self.mImg = loadImage(path+'\\images\\menu.png')
        self.p1 = loadImage(path+'\\images\\passed.png')
        self.winImg = loadImage(path+'\\images\\win.png')
        self.backgroundSound=SoundFile(this,path+'/sounds/backgroundMusic.mp3')
        self.introMusic=SoundFile(this,path+'/sounds/introMusic.mp3')
        self.winMusic=SoundFile(this,path+'/sounds/winSound.wav')
        self.ribbonImg=loadImage(path+'\\images\\ribbon.png')
        self.gameWon=False
         
    def loadStage(self):
        #Resets object lists, appends according to new stage
        self.allBalc=[]
        self.allStar=[]
        self.allBoost=[]
        # Loads stage file
        f = open(path+'/stages/stage'+str(self.stage)+'.csv',"r")
        a = f.readline()
        self.final = int(a)
        
        for l in f:
            l=l.strip().split(",")
            
            if l[0]=='Balcony':
                self.allBalc.append(balcony(int(l[1]),int(l[2])))
            elif l[0]=='Star':
                self.allStar.append(blade(int(l[1]),int(l[2])))
            elif l[0]=='Booster':
                self.allBoost.append(booster(int(l[1]),int(l[2])))
        f.close()
    
    def display(self):
        #frameRate(10)
        if time==1:
            self.backgroundSound.play()
        
        if self.state == "win":
            image(self.winImg,0,0)
            if self.gameWon==False:
                self.winMusic.play()
            self.gameWon=True
    
        elif self.state == "passed":
            image(self.p1,0,0)
                
        elif self.state == "menu":
            image(self.mImg,0,0)
            
        else: # Actual Gameplay
            background(255)
            image(self.b1,0,0)
            image(self.b2,0,-self.y%self.heigh,self.wid,self.heigh+self.y%self.heigh,0,0,self.wid,self.heigh+self.y%self.heigh)
            image(self.b2,0,0,self.wid,self.heigh-self.y%self.heigh,0,self.heigh-self.heigh+self.y%self.heigh,self.wid,self.heigh)
            image(self.ribbonImg,0,self.final-ninJump.y) # Displays all images. Illusion of movement
            textSize(50)
            fill(255)
            text("Level "+str(self.stage),240,80)
                
            #Displays objects based on their relevance    
            for b in self.allBalc:
                if b.y > self.character.y - 600 and b.y < self.character.y + 600:
                    b.display()
                
            for s in self.allStar:
                if s.y > self.character.y - 600 and s.y < self.character.y + 600:
                    s.display()
            
            for b in self.allBoost:
                if b.y > self.character.y - 600 and b.y < self.character.y + 600:
                    b.display()
                
            self.character.display()
            image(self.starImg,300,800,50,50)
            textSize(40)
            fill(255)
            text(str(ninJump.stars),350,840) # Star count display with image
            
            if self.y < self.final and self.stage<5: # Changes state to inbetween stages if final point reached
                self.state = "passed"
            elif self.y < self.final and self.stage ==5: # If final stage won, game won
                self.state = "win"
                self.backgroundSound.stop()
        
            if self.character.vy > 0: # Display Game over if ninja falling
                fill(0)
                textSize(65)
                text("Game Over",150,300)
            
            if self.character.y > 900: # Ninja falls through screen, game begins again
                self.state = "menu"
    
time = 0    
ninJump = game(650,900,1,0,"menu") # Initialising game from Level 1 and Menu. game(width,height,level,stars,state)
ninJump.backgroundSound.play() 
def setup():
    background(255)
    size(ninJump.wid,ninJump.heigh)
    
def draw():
    global time # Using time to delay playback of background music initially
    ninJump.display()
    if time > 0:
        time-=1
    
def keyPressed():
    global time
    if keyCode == 32 and ninJump.character.boosterCollect==True: 
        ninJump.character.boosterCollect=False # Changes status so that boost can be collected again.
    if keyCode == 32 and ninJump.state=="passed": # adds stage and initialises
        ninJump.backgroundSound.stop()
        stage = ninJump.stage+1
        stars = ninJump.stars
        ninJump.__init__(650,900,stage,stars,"play")
        ninJump.backgroundSound.stop()
        ninJump.introMusic.play()
        ninJump.backgroundSound.play()
        
    elif keyCode == 32 and ninJump.state=="play" and not ninJump.dead: 
        ninJump.character.keyHandler[32]=True # Makes the character jump.
        
    elif keyCode == 32 and ninJump.state=="menu":
        ninJump.winMusic.stop()
        ninJump.backgroundSound.stop()
        ninJump.__init__(650,900,1,0,"play") # reintializes after menu.
        ninJump.introMusic.play()
        time = 120
        
    elif keyCode == 32 and ninJump.state=="win": # restarts game from menu after won
        ninJump.__init__(650,900,1,0,"menu")
        ninJump.backgroundSound.play()
        
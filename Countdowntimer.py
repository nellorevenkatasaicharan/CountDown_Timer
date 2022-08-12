import pygame
import sys
import time
def display_screen(hrs,mins,secs):
    print("\n\nPress the Cross button to Stop the timer !!!")
    pygame.init()
    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption("COUNT DOWN TIMER")
    icon=pygame.image.load("rocket.png")
    pygame.display.set_icon(icon)
    font_color=(255,0,0)
    timeron=True
    screen.fill((0,0,102))
    def next_game():
        while True :
            try:
                hrs=int(input("\nEnter Hours Value:"))
            except:
                print("\nEnter integer Values only!!")
            else:
                if 0<=hrs<=100:
                    break
                else:
                    print("\nEnter value between 0 and 100")
        while True:
            try:
                mins=int(input("\nEnter minutes value:"))
            except:
                print('\nEnter integer values only!!')
            else:
                if 0<=mins<=59:
                    break
                else:
                    print("\nEnter value between 0 and 59")
        while True:
            try:
                secs=int(input("\nEnter seconds value:"))
            except:
                print('\nEnter integer values only!!')
            else:
                if 0<=mins<=59:
                    break
                else:
                    print("\nEnter value between 0 and 59")
        display_screen(hrs,mins,secs)
    def stop(k,l,m):
        gameon=True
        while gameon:
            for even in pygame.event.get():
                if even.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if even.type==pygame.MOUSEBUTTONDOWN:
                    if 360<=mouse[0]<=460 and 400<=mouse[1]<=430:
                        gameon=False
                    elif 40<=mouse[0]<=105 and 400<=mouse[1]<=430:
                        pygame.quit()
                        next_game()
            mouse=pygame.mouse.get_pos()
            font=pygame.font.SysFont("Somic Sans MS",150)
            string=str(100) if k==100 else str(k).rjust(2,"0")
            text=font.render(string+":"+str(l).rjust(2,"0")+":"+str(m).rjust(2,"0"),True,font_color)
            screen.blit(text,(50,220))
            pygame.display.flip()
            font=pygame.font.SysFont("Somic Sans MS",150)
            f=pygame.font.SysFont("Aerial",100)
            t=f.render("Timer",True,(255,255,255))
            screen.blit(t,(50,50))
            pygame.draw.rect(screen,(100,100,100),(40,400,65,30))
            pygame.draw.rect(screen,(100,100,100),(160,400,132,30))
            font1=pygame.font.SysFont("TT Bold Italic",35)
            text1=font1.render('Reset',True,(255,165,0))
            screen.blit(text1,(40,400))
            text2=font1.render("Stop/Pause",True,(255,165,0))
            screen.blit(text2,(160,400))
            pygame.draw.rect(screen,(100,100,100),(360,400,100,30))
            text3=font1.render("Resume",True,(255,165,0))
            screen.blit(text3,(360,400))
    while timeron:
        total=hrs*3600+mins*60+secs
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                timeron=False
                h=hrs
                m=mins
                s=secs
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if 40<=mouse[0]<=105 and 400<=mouse[1]<=430:
                    pygame.quit()
                    next_game()
                elif 160<=mouse[0]<=292 and 400<=mouse[1]<=430:
                    h=hrs
                    m=mins
                    s=secs
                    stop(h,m,s)
        mouse=pygame.mouse.get_pos()
        font=pygame.font.SysFont("Somic Sans MS",150)
        f=pygame.font.SysFont("Aerial",100)
        t=f.render("Timer",True,(255,255,255))
        screen.blit(t,(50,50))
        pygame.draw.rect(screen,(100,100,100),(40,400,65,30))
        pygame.draw.rect(screen,(100,100,100),(160,400,132,30))
        font1=pygame.font.SysFont("TT Bold Italic",35)
        text1=font1.render('Reset',True,(255,165,0))
        screen.blit(text1,(40,400))
        text2=font1.render("Stop/Pause",True,(255,165,0))
        screen.blit(text2,(160,400))
        pygame.draw.rect(screen,(100,100,100),(360,400,100,30))
        text3=font1.render("Resume",True,(255,165,0))
        screen.blit(text3,(360,400))
        if total>0:
            string=str(100) if hrs==100 else str(hrs).rjust(2,"0")
            text=font.render(string+":"+str(mins).rjust(2,"0")+":"+str(secs).rjust(2,"0"),True,font_color)
            screen.blit(text,(50,220))
            pygame.display.flip()
            screen.fill((0,0,0))
            time.sleep(1)
            if secs>0:
                secs-=1
            else:
                if mins:
                    mins-=1
                    secs=59
                else:
                    if hrs:
                        hrs-=1
                        mins=59
                        secs=59
        else:
            text=font.render("00:00:00",True,font_color)
            screen.blit(text,(50,220))
            pygame.display.update()
        total-=1
    pygame.quit()
display_screen(0,0,0)

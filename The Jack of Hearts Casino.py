import pygame, threading                                      #Main GUI 
import sys                                                              #Fonts
import random                                                        #Randomises Cards
from time import sleep                                                             #Time
import sqlite3                                                         #Login System Database
import os                                                                #Login System Database
from pygame import mixer                                     #Music
import copy                                                             #Copy's Decks of Cards
from pygame import *                                             #Extra GUI
import turtle                                                            #Roulette
import tkinter                                                          #Roulette
import operator                                                     #Poker

#initliasing pygame
pygame.init()

if os.path.exists("accountsmain.db"):
        conn = sqlite3.connect("accountsmain.db") #Creating the database where the username and password will be stored for the login system
        c = conn.cursor()
        
else:
    conn = sqlite3.connect("accountsmain.db")
    c = conn.cursor()
    c.execute("CREATE TABLE accountsmain (user_text text, user_password_text)")  #Creating the database where the username and password will be stored for the login system

def main_menu(): #function for the main menu window
    screen = pygame.display.set_mode((1380, 840))
    programIcon = pygame.image.load('icon.png')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption("Jack of Hearts - In the Main Menu") #sets caption for the window
    main_font = pygame.font.SysFont("Adobe Arabic", 50)
    clock = pygame.time.Clock()

    #designing the main menu
    background = pygame.image.load("main menu 3.PNG") #plays music while window is open
    pygame.transform.scale(background, (1500,900))

    mixer.init()

    pygame.mixer.set_num_channels(120)
    mixer.music.load('Main Menu Music.mp3')
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('Text to speech 1.mp3')) #sound effects when the function is called
    pygame.mixer.music.play(loops=-1)
    mixer.music.set_volume(0.1)

    screen.blit(background,(0,0))




        

    
    






#class that creates the buttons
    class Button():
            def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = main_font.render(self.text_input, True, "white")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos)) #creates the button

            def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect) #updates the button

            def checkForInput(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): #checks for an input for the button
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Button Sound.wav')) #plays a button pressing sound effect
                            login_username_screen() #calls the function of the button that was pressed

            def checkForInput2(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): #checks for an input for the button
                            pygame.mixer.Channel(2).play(pygame.mixer.Sound('Button Sound.wav'))
                            signup_username_screen()

            def checkForInput3(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): #checks for an input for the button
                            pygame.mixer.Channel(2).play(pygame.mixer.Sound('Button Sound.wav'))
                            pygame.quit()

            def checkForInputO(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): #checks for an input for the button
                            pygame.mixer.Channel(3).play(pygame.mixer.Sound('Button Sound.wav'))
                            options_screen()

            
                            
                            
                    
                                    
            def changeColor(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): #changes the colour of the button when being hovered over
                            self.text = main_font.render(self.text_input, True, "green")
                    else:
                            self.text = main_font.render(self.text_input, True, "white")
    #Creating the Main Menu Buttons
    button_surface = pygame.image.load("button background.png")
    button_surface = pygame.transform.scale(button_surface, (120, 60))

    button = Button(button_surface, 690, 477, "LOGIN")



    button_surface2 = pygame.image.load("button background.png")
    button_surface2 = pygame.transform.scale(button_surface2, (120, 60))

    button2 = Button(button_surface2, 690, 585, "SIGN UP")

    exit_button_surface = pygame.image.load("button background.png")
    exit_button_surface = pygame.transform.scale(exit_button_surface, (120, 60))

    exit_button = Button(exit_button_surface, 690, 695, "EXIT")

    options_button_surface = pygame.image.load("Settings Button Main.PNG")
    options_button_surface = pygame.transform.scale(options_button_surface,(160,100))

    options_button = Button(options_button_surface, 1285, 760, " ")

    while True: #a loop that makes the screen run forever
        for event in pygame.event.get(): #checks for an event
                if event.type == pygame.QUIT: #checks if the window wants to be shut down
                        pygame.quit() #opposite of pygame.init()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN: #checks if a button has been clicked
                        button.checkForInput(pygame.mouse.get_pos()) #calls the checkForInput function for Login
                        button2.checkForInput2(pygame.mouse.get_pos()) #calls the checkForInput function for Sign Up
                        exit_button.checkForInput3(pygame.mouse.get_pos()) #calls the checkForInput function for Exit
                        options_button.checkForInputO(pygame.mouse.get_pos()) #calls the checkForInput function for Settings
                        
                        
                                
                        
##                

        

        button.update()
        button.changeColor(pygame.mouse.get_pos())

        

        button2.update()
        button2.changeColor(pygame.mouse.get_pos())


        exit_button.update()
        exit_button.changeColor(pygame.mouse.get_pos())

        options_button.update()
        options_button.changeColor(pygame.mouse.get_pos())




        pygame.display.update() #displaying the buttons





















#Login System
def login_username_screen():
        while True:
                pygame.display.set_caption("Jack of Hearts - Logging In (Username)")
                programIcon = pygame.image.load('icon.png')
                pygame.display.set_icon(programIcon)
                login_screen = pygame.display.set_mode((1500,900))
                login_font = pygame.font.SysFont("cambria", 30)
                clock = pygame.time.Clock()
                screen.fill("red")
                login_background = pygame.image.load("practice red 2.PNG")
                login_heading = pygame.image.load("login heading main.PNG")
                pygame.transform.scale(login_background, (1500,900))
                username = login_font.render("USERNAME:  ", False, "Black")
                lines_1 = login_font.render("___________________________________________",False, "Black")
                white_background = pygame.image.load("white background.jpg")
                white_background = pygame.transform.scale(white_background, (600, 170))
                base_font = pygame.font.Font(None, 32)
                global user_text
                user_text = ''
                input_rect = pygame.Rect(550, 415, 420, 40)
                color_active = pygame.Color('red')
                color_passive = pygame.Color('grey')
                
                color = color_passive
                
                active = False

                class Button():
                        def __init__(self, image, x_pos, y_pos, text_input):
                                self.image = image
                                self.x_pos = x_pos
                                self.y_pos = y_pos
                                self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                                self.text_input = text_input
                                self.text = login_font.render(self.text_input, True, "white")
                                self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                        def update(self):
                                screen.blit(self.image, self.rect)
                                screen.blit(self.text, self.text_rect)


                        def checkForInput4(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(4).play(pygame.mixer.Sound('Button Sound.wav'))
                                        login_password_screen()

                        def changeColor(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = login_font.render(self.text_input, True, "green")
                                else:
                                        self.text = login_font.render(self.text_input, True, "white")
                
                








                buttonenter_surface = pygame.image.load("main red background.jfif")
                buttonenter_surface = pygame.transform.scale(buttonenter_surface, (300, 150))

                buttonenter = Button(buttonenter_surface, 800, 610, "ENTER")
                
                
                
                
                
                

                login_screen.blit(login_background,(0,100))
                login_screen.blit(login_heading,(667,10))
                login_screen.blit(white_background,(490,350))
                login_screen.blit(username,(550,380))
                login_screen.blit(lines_1,(550,430))
                
                
                
                
                
                
                

                pygame.display.update()

                while True: #a loop that makes the screen run forever
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit() #opposite of pygame.init()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if input_rect.collidepoint(event.pos):
                                                active = True
                                        else:
                                                active = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        buttonenter.checkForInput4(pygame.mouse.get_pos())
                                
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_BACKSPACE:
                                                user_text = user_text[:-1]
                                        else:
                                                user_text += event.unicode


                        buttonenter.update()
                        buttonenter.changeColor(pygame.mouse.get_pos())

                        pygame.display.update()
                                        
                                        
                                        






                        

                        if active:
                                color = color_active
                        else:
                                color = color_passive

                                
                        

                        pygame.draw.rect(login_screen, color, input_rect)

                        text_surface = login_font.render(user_text, True, ("Black"))
                        

                        login_screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                        

                        input_rect.w = max(100, text_surface.get_width()+10)

                        pygame.display.flip()

                        clock.tick(60)

                        
                        
                        


def signup_username_screen():
        while True:
                pygame.display.set_caption("Jack of Hearts - Signing In (Username)")
                programIcon = pygame.image.load('icon.png')
                pygame.display.set_icon(programIcon)
                signup_screen = pygame.display.set_mode((1500,900))
                signup_font = pygame.font.SysFont("cambria", 30)
                clock = pygame.time.Clock()
                screen.fill("red")
                signup_background = pygame.image.load("practice red 2.PNG")
                signup_heading = pygame.image.load("SIGN UP LOGO.PNG")
                pygame.transform.scale(signup_background, (1500,900))
                usernamesignup = signup_font.render("USERNAME:  ", False, "Black")
                lines_11 = signup_font.render("___________________________________________",False, "Black")
                white_background = pygame.image.load("white background.jpg")
                white_background = pygame.transform.scale(white_background, (600, 170))
                global user_text
                user_text = ''
                signup_rect = pygame.Rect(550, 377, 420, 40)
                signupcolor_active = pygame.Color('red')
                signupcolor_passive = pygame.Color('grey')
                
                signupcolor = signupcolor_passive
                
                signupactive = False

                class Button():
                        def __init__(self, image, x_pos, y_pos, text_input):
                                self.image = image
                                self.x_pos = x_pos
                                self.y_pos = y_pos
                                self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                                self.text_input = text_input
                                self.text = signup_font.render(self.text_input, True, "white")
                                self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                        def update(self):
                                screen.blit(self.image, self.rect)
                                screen.blit(self.text, self.text_rect)


                        def checkForInput5(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(5).play(pygame.mixer.Sound('Button Sound.wav'))
                                        
                                        signup_password_screen()

                        def changeColor(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = signup_font.render(self.text_input, True, "green")
                                else:
                                        self.text = signup_font.render(self.text_input, True, "black")
                
                








                buttonenter2_surface = pygame.image.load("main red background.jfif")
                buttonenter2_surface = pygame.transform.scale(buttonenter2_surface, (230, 130))

                buttonenter2 = Button(buttonenter2_surface, 810, 610, "ENTER")
                

                signup_screen.blit(signup_background,(0,100))
                signup_screen.blit(signup_heading,(620,10))
                signup_screen.blit(white_background,(490,318))
                signup_screen.blit(usernamesignup,(530, 330))
                signup_screen.blit(lines_11,(550, 390))

                
                
                
                
                

                

                while True: #a loop that makes the screen run forever
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit() #opposite of pygame.init()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if signup_rect.collidepoint(event.pos):
                                                signupactive = True
                                        else:
                                                signupactive = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        buttonenter2.checkForInput5(pygame.mouse.get_pos())
                                
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_BACKSPACE:
                                                user_text = user_text[:-1] #takes a letter away from the variable
                                        else:
                                                user_text += event.unicode #adds the specific unicode character to the variable


                        buttonenter2.update()
                        buttonenter2.changeColor(pygame.mouse.get_pos())

                        pygame.display.update()


                        if signupactive:
                                signupcolor = signupcolor_active
                        else:
                                signupcolor = signupcolor_passive

                                        
                                

                        pygame.draw.rect(signup_screen, signupcolor, signup_rect)

                        signup_surface = signup_font.render(user_text, True, ("Black"))
                        #creates the surface for the text to be outputed and how it is outputed
                                

                        signup_screen.blit(signup_surface, (signup_rect.x+5, signup_rect.y+5))
                        #outputs the surface on the window
                                

                        signup_rect.w = max(100, signup_surface.get_width()+10)
                        #creates the size of the text box

                        pygame.display.flip()

                        clock.tick(60)

                        
                                        
                


def login_password_screen():
        while True:
                pygame.display.set_caption("Jack of Hearts - Logging In (Password)")
                programIcon = pygame.image.load('icon.png')
                pygame.display.set_icon(programIcon)
                login_password_screen = pygame.display.set_mode((1500,900))
                login_password_font = pygame.font.SysFont("cambria", 30)
                clock = pygame.time.Clock()
                screen.fill("red")
                login_password_background = pygame.image.load("practice red 2.PNG")
                login_password_heading = pygame.image.load("login heading main.PNG")
                pygame.transform.scale(login_password_background, (1500,900))
                password = login_password_font.render("PASSWORD:  ", False, "Black")
                lines_password_1 = login_password_font.render("___________________________________________",False, "Black")
                white_password_background = pygame.image.load("white background.jpg")
                white_password_background = pygame.transform.scale(white_password_background, (600, 170))
                base_password_font = pygame.font.Font(None, 32)
                global user_password_text
                user_password_text = ''
                input_password_rect = pygame.Rect(550, 415, 420, 40)
                color_password_active = pygame.Color('red')
                color_password_passive = pygame.Color('grey')
                
                colorpassword = color_password_passive
                
                active2 = False

                class Button():
                        def __init__(self, image, x_pos, y_pos, text_input):
                                self.image = image
                                self.x_pos = x_pos
                                self.y_pos = y_pos
                                self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                                self.text_input = text_input
                                self.text = login_password_font.render(self.text_input, True, "white")
                                self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                        def update(self):
                                screen.blit(self.image, self.rect)
                                screen.blit(self.text, self.text_rect)


                        def checkForInput6(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(6).play(pygame.mixer.Sound('Button Sound.wav'))
                                        login_system2()
                                        
                                        
                                        
                                        

                        def changeColor(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = login_password_font.render(self.text_input, True, "green")
                                else:
                                        self.text = login_password_font.render(self.text_input, True, "white")
                
                








                buttonenter3_surface = pygame.image.load("main red background.jfif")
                buttonenter3_surface = pygame.transform.scale(buttonenter3_surface, (300, 150))

                buttonenter3 = Button(buttonenter3_surface, 800, 610, "ENTER")

                login_password_screen.blit(login_password_background,(0,100))
                login_password_screen.blit(login_password_heading,(667,10))
                login_password_screen.blit(white_password_background,(490,350))
                login_password_screen.blit(password,(550,380))
                login_password_screen.blit(lines_password_1,(550,430))
                
                
                
                
                
                
                

                

                while True: #a loop that makes the screen run forever
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit() #opposite of pygame.init()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if input_password_rect.collidepoint(event.pos):
                                                active2 = True
                                        else:
                                                active2 = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        buttonenter3.checkForInput6(pygame.mouse.get_pos())
                                
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_BACKSPACE:
                                                user_password_text = user_password_text[:-1]
                                        else:
                                                user_password_text += event.unicode
                                        
                                        
                        buttonenter3.update()
                        buttonenter3.changeColor(pygame.mouse.get_pos())

                        pygame.display.update()           

                        

                        if active2:
                                colorpassword = color_password_active
                        else:
                                colorpassword = color_password_passive

                                
                        

                        pygame.draw.rect(login_password_screen, colorpassword, input_password_rect)

                        text_password_surface = login_password_font.render(user_password_text, True, ("Black"))
                        

                        login_password_screen.blit(text_password_surface, (input_password_rect.x+5, input_password_rect.y+5,))
                        

                        input_password_rect.w = max(100, text_password_surface.get_width()+10)

                        pygame.display.flip()

                        clock.tick(60)

                        
                        
        
       



def signup_password_screen():
        while True:
                pygame.display.set_caption("Jack of Hearts - Signing In (Password)")
                programIcon = pygame.image.load('icon.png')
                pygame.display.set_icon(programIcon)
                signup_password_screen = pygame.display.set_mode((1500,900))
                signup_password_font = pygame.font.SysFont("cambria", 30)
                clock = pygame.time.Clock()
                screen.fill("red")
                signup_password_background = pygame.image.load("practice red 2.PNG")
                signup_password_heading = pygame.image.load("SIGN UP LOGO.PNG")
                pygame.transform.scale(signup_password_background, (1500,900))
                password_signup = signup_password_font.render("PASSWORD:  ", False, "Black")
                lines_password_11 = signup_password_font.render("___________________________________________",False, "Black")
                white_password_background = pygame.image.load("white background.jpg")
                white_password_background = pygame.transform.scale(white_password_background, (600, 170))
                global user_password_text
                user_password_text = ''
                signup_password_rect = pygame.Rect(550, 377, 420, 40)
                signupcolor_password_active = pygame.Color('red')
                signupcolor_password_passive = pygame.Color('grey')
                
                signupcolorpassword = signupcolor_password_passive
                
                signupactivepassword = False

                class Button():
                        def __init__(self, image, x_pos, y_pos, text_input):
                                self.image = image
                                self.x_pos = x_pos
                                self.y_pos = y_pos
                                self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                                self.text_input = text_input
                                self.text = signup_password_font.render(self.text_input, True, "white")
                                self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                        def update(self):
                                screen.blit(self.image, self.rect)
                                screen.blit(self.text, self.text_rect)


                        def checkForInput7(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('Button Sound.wav'))
                                        login_system1()
                                        print("Details Saved")

                        def checkForInputPatak(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(7).play(pygame.mixer.Sound('Button Sound.wav'))
                                        main_menu()

                                        
                                        
                                        

                        def changeColor(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = signup_password_font.render(self.text_input, True, "green")
                                else:
                                        self.text = signup_password_font.render(self.text_input, True, "white")

                buttonenter4_surface = pygame.image.load("main red background.jfif")
                buttonenter4_surface = pygame.transform.scale(buttonenter4_surface, (300, 150))

                buttonenter4 = Button(buttonenter4_surface, 800, 610, "ENTER")

                buttonenterpatak_surface = pygame.image.load("main red background.jfif")
                buttonenterpatak_surface = pygame.transform.scale(buttonenterpatak_surface, (300, 150))

                buttonenterpatak = Button(buttonenterpatak_surface, 800, 810, "EXIT")
                

                signup_password_screen.blit(signup_password_background,(0,100))
                signup_password_screen.blit(signup_password_heading,(620,10))
                signup_password_screen.blit(white_password_background,(490,318))
                signup_password_screen.blit(password_signup,(530, 330))
                signup_password_screen.blit(lines_password_11,(550, 390))
                
                
                
                

                

                while True: #a loop that makes the screen run forever
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit() #opposite of pygame.init()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if signup_password_rect.collidepoint(event.pos):
                                                signupactivepassword = True
                                        else:
                                                signupactivepassword = False

                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        buttonenter4.checkForInput7(pygame.mouse.get_pos())
                                        buttonenterpatak.checkForInputPatak(pygame.mouse.get_pos())
                                
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_BACKSPACE:
                                                user_password_text = user_password_text[:-1]
                                        else:
                                                user_password_text += event.unicode

                        buttonenter4.update()
                        buttonenter4.changeColor(pygame.mouse.get_pos())

                        buttonenterpatak.update()
                        buttonenterpatak.changeColor(pygame.mouse.get_pos())
                        

                        pygame.display.update() 


                        if signupactivepassword:
                                signupcolorpassword = signupcolor_password_active
                        else:
                                signupcolorpassword = signupcolor_password_passive

                                        
                                

                        pygame.draw.rect(signup_password_screen, signupcolorpassword, signup_password_rect)

                        signup_password_surface = signup_password_font.render(user_password_text, True, ("Black"))
                                

                        signup_password_screen.blit(signup_password_surface, (signup_password_rect.x+5, signup_password_rect.y+5))
                                

                        signup_password_rect.w = max(100, signup_password_surface.get_width()+10)

                        pygame.display.flip()

                        clock.tick(60)




        
        
        


def options_screen():
    while True:
        pygame.display.set_caption("Jack of Hearts - Settings")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        options_screen = pygame.display.set_mode((950, 617))
        options_font = pygame.font.SysFont("cambria", 30)
        clock = pygame.time.Clock()
        options_screen_background = pygame.image.load("options main.PNG")
        

        class Button():
                        def __init__(self, image, x_pos, y_pos, text_input):
                                self.image = image
                                self.x_pos = x_pos
                                self.y_pos = y_pos
                                self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                                self.text_input = text_input
                                self.text = options_font.render(self.text_input, True, "white")
                                self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                        def update(self):
                                screen.blit(self.image, self.rect)
                                screen.blit(self.text, self.text_rect)


                        def checkForInput92(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(50).play(pygame.mixer.Sound('green it is.mp3'))
                                        global mainbackground
                                        mainbackground = blackjackgreen_background
                                        

                        def checkForInput93(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(51).play(pygame.mixer.Sound('blue is a good choice.mp3'))
                                        global mainbackground
                                        mainbackground = blackjackblue_background

                        def checkForInput94(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        #pygame.mixer.Channel(51).play(pygame.mixer.Sound('E:/A Level Computer Science/Programming Project/Practice/blue is a good choice.mp3'))
                                        global mainbackground
                                        mainbackground = blackjackred_background

                        def checkForInput100(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        #pygame.mixer.Channel(52).play(pygame.mixer.Sound('E:/A Level Computer Science/Programming Project/Practice/blue is a good choice.mp3'))
                                        global mainbackground
                                        mainbackground = blackjackdarkgreen_background

                        def checkForInput101(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        #pygame.mixer.Channel(51).play(pygame.mixer.Sound('E:/A Level Computer Science/Programming Project/Practice/blue is a good choice.mp3'))
                                        global mainbackground
                                        mainbackground = blackjackorange_background

                        def checkForInput102(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        #pygame.mixer.Channel(51).play(pygame.mixer.Sound('E:/A Level Computer Science/Programming Project/Practice/blue is a good choice.mp3'))
                                        global mainbackground
                                        mainbackground = blackjackpurple_background


                        def checkForInput96(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        main_menu()

                        def checkForInput97(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.music.unpause

                        def checkForInput98(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.music.pause

                        def checkForInput99(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.music.stop
                                        

                                        
                                        
                                        

                        def changeColor1(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = options_font.render(self.text_input, True, "green")
                                else:
                                        self.text = options_font.render(self.text_input, True, "white")

                        def changeColor2(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = options_font.render(self.text_input, True, "blue")
                                else:
                                        self.text = options_font.render(self.text_input, True, "white")

                        def changeColor3(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = options_font.render(self.text_input, True, "red")
                                else:
                                        self.text = options_font.render(self.text_input, True, "white")

                        def changeColor4(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = options_font.render(self.text_input, True, "dark green")
                                else:
                                        self.text = options_font.render(self.text_input, True, "white")

                        def changeColor5(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = options_font.render(self.text_input, True, "orange")
                                else:
                                        self.text = options_font.render(self.text_input, True, "white")

                        def changeColor6(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = options_font.render(self.text_input, True, "purple")
                                else:
                                        self.text = options_font.render(self.text_input, True, "white")

        buttonentergreen_surface = pygame.image.load("purple background.PNG")
        buttonentergreen_surface = pygame.transform.scale(buttonentergreen_surface, (70, 30))

        buttonentergreen = Button(buttonentergreen_surface, 838, 200, "GREEN")

        buttonenterblue_surface = pygame.image.load("purple background.PNG")
        buttonenterblue_surface = pygame.transform.scale(buttonenterblue_surface, (70, 30))

        buttonenterblue = Button(buttonenterblue_surface, 838, 273, "BLUE")

        buttonenterbackfromoptions_surface = pygame.image.load("blue arrow.png")
        buttonenterbackfromoptions_surface = pygame.transform.scale(buttonenterbackfromoptions_surface, (100, 100))

        buttonenterbackfromoptions = Button(buttonenterbackfromoptions_surface, 60, 343, "")

        buttonenterred_surface = pygame.image.load("purple background.PNG")
        buttonenterred_surface = pygame.transform.scale(buttonenterred_surface, (70, 30))

        buttonenterred = Button(buttonenterred_surface, 838, 350, "RED")

        buttonenterdarkgreen_surface = pygame.image.load("purple background.PNG")
        buttonentergreen_surface = pygame.transform.scale(buttonentergreen_surface, (70, 30))

        buttonenterdarkgreen = Button(buttonenterdarkgreen_surface, 838, 427, "DARK GREEN")

        buttonenterorange_surface = pygame.image.load("purple background.PNG")
        buttonenterorange_surface = pygame.transform.scale(buttonenterorange_surface, (70, 30))

        buttonenterorange = Button(buttonenterorange_surface, 838, 504, "ORANGE")

        buttonenterpurple_surface = pygame.image.load("purple background.PNG")
        buttonenterpurple_surface = pygame.transform.scale(buttonenterpurple_surface, (70, 30))

        buttonenterpurple = Button(buttonenterpurple_surface, 838, 581, "PURPLE")

        buttonenterplay_surface = pygame.image.load("purple background.PNG")
        buttonenterplay_surface = pygame.transform.scale(buttonenterplay_surface, (70, 30))

        buttonenterplay = Button(buttonenterplay_surface, 478, 210, "PLAY")

        buttonenterpause_surface = pygame.image.load("purple background.PNG")
        buttonenterpause_surface = pygame.transform.scale(buttonenterpause_surface, (70, 30))

        buttonenterpause = Button(buttonenterpause_surface, 478, 283, "PAUSE")

        buttonenterstop_surface = pygame.image.load("purple background.PNG")
        buttonenterstop_surface = pygame.transform.scale(buttonenterstop_surface, (70, 30))

        buttonenterstop = Button(buttonenterstop_surface, 478, 360, "STOP")
                

                
        


        options_screen.blit(options_screen_background,(0,0))

        

        while True: #a loop that makes the screen run forever
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit() #opposite of pygame.init()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonentergreen.checkForInput92(pygame.mouse.get_pos())
                        buttonenterblue.checkForInput93(pygame.mouse.get_pos())
                        buttonenterbackfromoptions.checkForInput96(pygame.mouse.get_pos())
                        buttonenterred.checkForInput94(pygame.mouse.get_pos())
                        buttonenterdarkgreen.checkForInput100(pygame.mouse.get_pos())
                        buttonenterorange.checkForInput101(pygame.mouse.get_pos())
                        buttonenterpurple.checkForInput102(pygame.mouse.get_pos())
                        buttonenterplay.checkForInput97(pygame.mouse.get_pos())
                        buttonenterpause.checkForInput98(pygame.mouse.get_pos())
                        buttonenterstop.checkForInput99(pygame.mouse.get_pos())



            buttonentergreen.update()
            buttonentergreen.changeColor1(pygame.mouse.get_pos())

            buttonenterblue.update()
            buttonenterblue.changeColor2(pygame.mouse.get_pos())

            buttonenterred.update()
            buttonenterred.changeColor3(pygame.mouse.get_pos())

            buttonenterred.update()
            buttonenterred.changeColor3(pygame.mouse.get_pos())

            buttonenterdarkgreen.update()
            buttonenterdarkgreen.changeColor4(pygame.mouse.get_pos())

            buttonenterorange.update()
            buttonenterorange.changeColor5(pygame.mouse.get_pos())

            buttonenterpurple.update()
            buttonenterpurple.changeColor6(pygame.mouse.get_pos())

            buttonenterplay.update()
            buttonenterplay.changeColor1(pygame.mouse.get_pos())

            buttonenterpause.update()
            buttonenterpause.changeColor1(pygame.mouse.get_pos())

            buttonenterstop.update()
            buttonenterstop.changeColor1(pygame.mouse.get_pos())

            buttonenterbackfromoptions.update()

            pygame.display.update()




        

def login_system1():
    

        c.execute(f"INSERT INTO accountsmain VALUES (?, ?)", [user_text, user_password_text])

        conn.commit()
        conn.close()

        

def login_system2():

        c.execute("SELECT * FROM accountsmain WHERE (user_text=? and user_password_text=?)", [user_text, user_password_text]) #checks if the username and password are in the database

        if c.fetchone() == None:
            print("Incorrect credentials") #if they are not print error message

        else:
            #pygame.mixer.Channel(98).play(pygame.mixer.Sound('E:/A Level Computer Science/Programming Project/Practice/mixkit-casino-bling-achievement-2067.wav'))
            #pygame.mixer.Channel(97).play(pygame.mixer.Sound('welcome back.mp3')) #play welcoming sound effect
            pick_your_game() #display next window
        

    
    

def pick_your_game():
    pygame.display.set_caption("Jack of Hearts - Picking Your Game")
    programIcon = pygame.image.load('icon.png')
    pygame.display.set_icon(programIcon)
    game_choice_screen = pygame.display.set_mode((1380,800))
    game_choice_font = pygame.font.SysFont("Franklin Gothic Heavy", 40)
    clock = pygame.time.Clock()
    game_choice_background = pygame.image.load("Pick Your Game Menu Screen.PNG")
    
    
    
    

    mixer.music.load('Pre Game Lobby Music.mp3')
    pygame.mixer.music.play(loops=-1)
    mixer.music.set_volume(0.1)

    class Button():
        def __init__(self, image, x_pos, y_pos, text_input):
            self.image = image
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_input = text_input
            self.text = game_choice_font.render(self.text_input, True, "white")
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self):
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)


        def checkForInput9(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(8).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                blackjack_menu() #sends the player to Blackjack Menu

        def checkForInput10(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(9).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                horseracing_menu() #Sends the player to Horse Racing Menu

        def checkForInputIR(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(10).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                indianrummy_menu() # Sends the player to Indian Rummy Menu

        def checkForInputSL(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(10).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                roulette_menu() #Sends the player to Roulette Menu

        def checkForInputPO(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(10).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                poker_menu() #Sends the player to Poker Menu

        def checkForInput11(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(10).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                spin_the_wheel() #Sends to player to Spin the wheel minigame

        def checkForInputNU(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(10).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                guess_the_number() #Sends the player to Guess the Number Minigame

        def checkForInput12(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(11).play(pygame.mixer.Sound('Button Sound.wav'))
                        main_menu()


    buttonenter_blackjack_surface= pygame.image.load("blackjack logo.PNG")
    buttonenter_blackjack_surface = pygame.transform.scale(buttonenter_blackjack_surface, (300, 215))

    buttonenter_blackjack = Button(buttonenter_blackjack_surface, 220, 320, "")

    buttonenter_horseracing_surface = pygame.image.load("horse racing logo.PNG")
    buttonenter_horseracing_surface = pygame.transform.scale(buttonenter_horseracing_surface, (366, 237)) #change size

    buttonenter_horseracing = Button(buttonenter_horseracing_surface, 1157, 316, "")

    buttonenter_indianrummy_surface = pygame.image.load("indian rummy logo.jpg")
    buttonenter_indianrummy_surface = pygame.transform.scale(buttonenter_indianrummy_surface, (405, 223))

    buttonenter_indianrummy = Button(buttonenter_indianrummy_surface, 686, 316, "")

    button_slots_surface = pygame.image.load("slot machine.jpg")
    button_slots_surface = pygame.transform.scale(button_slots_surface, (302,213))

    button_slots = Button(button_slots_surface , 435, 602, "")

    button_poker_surface = pygame.image.load("3 card poker logo.jpg")
    button_poker_surface = pygame.transform.scale(button_poker_surface, (302,227))

    button_poker = Button(button_poker_surface , 894, 597, "")

    button_number_surface = pygame.image.load("guess the number logo.jpg")
    button_number_surface = pygame.transform.scale(button_number_surface, (200,100))

    button_number = Button(button_number_surface , 1170, 600, "")

    button_wheel_surface = pygame.image.load("spin the wheel logo.PNG")
    button_wheel_surface = pygame.transform.scale(button_wheel_surface, (200,100))

    button_wheel = Button(button_wheel_surface , 130, 630, "")

    button_back_surface = pygame.image.load("purple arrow.PNG")
    button_back_surface = pygame.transform.scale(button_back_surface, (260,200))

    button_back = Button(button_back_surface , 115, 716, "")

    

    

        

    
     
    game_choice_screen.blit(game_choice_background,(0,0))
    chip_text = game_choice_font.render(f'{chips[0]}', True, 'white')
    game_choice_screen.blit(chip_text, (1242, 10))
    chip_image = pygame.image.load('New Project (1).png')
    game_choice_screen.blit(chip_image, (1190, 10))
    

    buttonenter_blackjack.update()
    buttonenter_horseracing.update()
    buttonenter_indianrummy.update()
    button_slots.update()
    button_poker.update()
    #button_number.update()
    #button_wheel.update()
    button_back.update()
    
    
    

                         

    pygame.display.update()

    while True: #a loop that makes the screen run forever
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit() #opposite of pygame.init()
                        sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttonenter_blackjack.checkForInput9(pygame.mouse.get_pos())
                    buttonenter_horseracing.checkForInput10(pygame.mouse.get_pos())
                    buttonenter_indianrummy.checkForInputIR(pygame.mouse.get_pos())
                    button_slots.checkForInputSL(pygame.mouse.get_pos())
                    button_poker.checkForInputPO(pygame.mouse.get_pos())
                    button_number.checkForInputNU(pygame.mouse.get_pos())
                    button_wheel.checkForInput11(pygame.mouse.get_pos())
                    button_back.checkForInput12(pygame.mouse.get_pos())
                    

def roulette_menu():
        pygame.display.set_caption("Jack of Hearts - In the Roulette Menu")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        roulette_screen = pygame.display.set_mode((1314,782))
        roulette_font = pygame.font.SysFont("Franklin Gothic Heavy", 35)
        clock = pygame.time.Clock()
        roulette_background = pygame.image.load("roulette main menu.PNG")

        

        mixer.music.load('play-roulette-206397.mp3')
        pygame.mixer.music.play(loops=-1)
        mixer.music.set_volume(0.1)

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = roulette_font.render(self.text_input, True, "white")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputroulettePLAY(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(8).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                        roulette_table()

                def checkForInputrouletteCAREER(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(9).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                        roulette_career()

                def checkForInputrouletteEXIT(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                        pick_your_game()

                def checkForInputrouletteRULES(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                        roulette_rules()

                def changeColor1(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = roulette_font.render(self.text_input, True, "green")
                                else:
                                        self.text = roulette_font.render(self.text_input, True, "white")


        button_roulette_back_surface = pygame.image.load("roulette back button.PNG")
        button_roulette_back_surface = pygame.transform.scale(button_roulette_back_surface, (140,80))

        button_roulette_back = Button(button_roulette_back_surface , 83, 734, "")

        button_roulette_play_surface = pygame.image.load("roulette button background.PNG")
        button_roulette_play_surface = pygame.transform.scale(button_roulette_play_surface, (130,35))

        button_roulette_play = Button(button_roulette_play_surface , 725, 718, "PLAY")

        button_roulette_career_surface = pygame.image.load("roulette button background.PNG")
        button_roulette_career_surface = pygame.transform.scale(button_roulette_career_surface, (100,20))

        button_roulette_career = Button(button_roulette_career_surface , 1150, 718, "CAREER")

        button_roulette_rules_surface = pygame.image.load("roulette button background.PNG")
        button_roulette_rules_surface = pygame.transform.scale(button_roulette_rules_surface, (100,20))

        button_roulette_rules = Button(button_roulette_rules_surface , 310, 724, "RULES")

        roulette_screen.blit(roulette_background, (0,0))

        button_roulette_back.update()
        button_roulette_play.update()
        button_roulette_career.update()






        

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                                button_roulette_back.checkForInputrouletteEXIT(pygame.mouse.get_pos())
                                button_roulette_play.checkForInputroulettePLAY(pygame.mouse.get_pos())
                                button_roulette_career.checkForInputrouletteCAREER(pygame.mouse.get_pos())
                                button_roulette_rules.checkForInputrouletteRULES(pygame.mouse.get_pos())

                        button_roulette_back.update()
                        button_roulette_back.changeColor1(pygame.mouse.get_pos())

                        button_roulette_play.update()
                        button_roulette_play.changeColor1(pygame.mouse.get_pos())

                        button_roulette_career.update()
                        button_roulette_career.changeColor1(pygame.mouse.get_pos())

                        button_roulette_rules.update()
                        button_roulette_rules.changeColor1(pygame.mouse.get_pos())

                pygame.display.update()



def roulette_career():
        pygame.display.set_caption("Jack of Hearts - Viewing Career in Roulette")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        roulettec_screen = pygame.display.set_mode((985,612))
        roulettec_font = pygame.font.SysFont("Franklin Gothic Heavy", 35)
        clock = pygame.time.Clock()
        roulettec_background = pygame.image.load("roulette career menu.png")
        roulettec_screen.blit(roulettec_background, (0,0))

        def displayRouletteWins():

            #Displays wins on the screen

            try:
                with open('rouletteWINS.txt') as f:
                    global current_roulettewins
                    current_roulettewins = f.readline()

                total_roulettewins = roulettec_font.render(str(current_roulettewins), False , "White")
                roulettec_screen.blit(total_roulettewins, (90,133))

            except:
                total_roulettewins = roulettec_font.render('Total Earnings: $0', False , "Black")
                roulettec_screen.blit(total_roulettewins, (870,30))

                with open('rouletteWins.txt', 'w') as f:
                    f.write(str(1))


        def displayRoulette361Wins():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('roulette361WINS.txt') as f:
                    global current_roulette361wins
                    current_roulette361wins = f.readline()

                total_roulette361wins = roulettec_font.render(str(current_roulette361wins), False , "White")
                roulettec_screen.blit(total_roulette361wins, (150,197))

            except:
                total_roulette361wins = roulettec_font.render('Total Earnings: $0', False , "Black")
                roulettec_screen.blit(total_roulette361wins, (870,30))

                with open('roulette361WINS.txt', 'w') as f:
                    f.write(str(1))

        def displayRouletteLosses():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('rouletteLOSSES.txt') as f:
                    global current_roulettelosses
                    current_roulettelosses = f.readline()

                total_roulettelosses = roulettec_font.render(str(current_roulettelosses), False , "White")
                roulettec_screen.blit(total_roulettelosses, (109,262))

            except:
                total_roulettelosses = roulettec_font.render('Total Earnings: $0', False , "Black")
                roulettec_screen.blit(total_roulettelosses, (870,30))

                with open('rouletteLOSSES.txt', 'w') as f:
                    f.write(str(1))

        displayRouletteWins()
        displayRoulette361Wins()
        displayRouletteLosses()

        totalgamesR = int(current_roulettewins) +  int(current_roulettelosses)

        totalgameszR = roulettec_font.render(str(totalgamesR), False, "White")
        roulettec_screen.blit(totalgameszR, (159, 328))

        roulette_cover = pygame.image.load("roulette cover.png")
        roulettec_screen.blit(roulette_cover, (25, 385))

        




        

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        roulette_menu()

                pygame.display.update()
        



def roulette_rules():
        pygame.display.set_caption("Jack of Hearts - Learning the Rules of Roulette")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        rouletter_screen = pygame.display.set_mode((785,912))
        rouletter_font = pygame.font.SysFont("Franklin Gothic Heavy", 35)
        clock = pygame.time.Clock()
        rouletter_background = pygame.image.load("roulette rules screen.png")
        rouletter_screen.blit(rouletter_background, (0,0))

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        roulette_menu()

                pygame.display.update()


#functions for all of the numbers of the roulette 


def one():
        global one
        one = True

def two():
        global two
        two = True

def three():
        global three
        three = True

def four():
        global four
        four = True

def five():
        global five
        five = True

def six():
        global six
        six = True

def seven():
        global seven
        seven = True

def eight():
        global eight
        eight = True

def nine():
        global nine
        nine = True

def ten():
        global ten
        ten = True

def eleven():
        global eleven
        eleven = True

def twelve():
        global twelve
        twelve = True

def thirteen():
        global thirteen
        thirteen = True

def fourteen():
        global fourteen
        fourteen = True

def fifteen():
        global fifteen
        fifteen = True

def sixteen():
        global sixteen
        sixteen = True

def seventeen():
        global seventeen
        seventeen = True

def eighteen():
        global eighteen
        eighteen = True

def nineteen():
        global nineteen
        nineteen = True

def twenty():
        global twenty
        twenty = True

def twentyone():
        global twentyone
        twentyone = True

def twentytwo():
        global twentytwo
        twentytwo = True

def twentythree():
        global twentythree
        twentythree = True

def twentyfour():
        global twentyfour
        twentyfour = True

def twentyfive():
        global twentyfive
        twentyfive = True

def twentysix():
        global twentysix
        twentysix = True

def twentyseven():
        global twentyseven
        twentyseven = True

def twentyeight():
        global twentyeight
        twentyeight = True

def twentynine():
        global twentynine
        twentynine = True

def thirty():
        global thirty
        thirty = True

def thirtyone():
        global thirtyone
        thirtyone = True

def thirtytwo():
        global thirtytwo
        thirtytwo = True

def thirtythree():
        global thirtythree
        thirtythree = True

def thirtyfour():
        global thirtyfour
        thirtyfour= True

def thirtyfive():
        global thirtyfive
        thirtyfive = True

def thirtysix():
        global thirtysix
        thirtysix = True

def zero():
        global zero
        zero = True

def doublezero():
        global doublezero
        doublezero = True

def onetotwelve():
        global onetotwelve
        onetotwelve = True

def thirteentotwentyfour():
        global thirteentotwentyfour
        thirteentotwentyfour = True

def twentyfivetothirtysix():
        global twentyfivetothirtysix
        twentyfivetothirtysix = True

def even():
        global even
        even = True

def odd():
        global odd
        odd = True

def black():
        global black
        black = True

def red():
        global red
        red = True



def redfalse():
        red = False



def roulette_table():
        pygame.display.set_caption("Jack of Hearts - Playing Roulette")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        rt_screen = pygame.display.set_mode((1485,782))
        rt_font = pygame.font.SysFont("Franklin Gothic Heavy", 40)
        clock = pygame.time.Clock()
        global rt_background_green, rt_background_purple, rt_background_red
        rt_background_green = pygame.image.load("roulette table background.PNG")
        rt_background_purple = pygame.image.load("test roulette.PNG")
        rt_background_red = pygame.image.load("red roulette table.PNG")
        roulette_backgrounds = [rt_background_green, rt_background_purple, rt_background_red]
        global main_roulette_background
        main_roulette_background = random.choice(roulette_backgrounds)
        rt_screen.blit(main_roulette_background, (0,0))

        table = pygame.image.load("roulette table.png")
        rt_screen.blit(table, (270, 140))

        mixer.music.load('excitement-206401.mp3')
        pygame.mixer.music.play(loops=-1)
        mixer.music.set_volume(0.1)

        
        chip_text_roulette = rt_font.render(f'{chips[0]}', True, 'white')
        rt_screen.blit(chip_text_roulette, (1296, 10))

        
        
        

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = rt_font.render(self.text_input, True, "white")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputpickone(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(8).play(pygame.mixer.Sound('place chips.mp3'))
                        print("1")
                        one()

                def checkForInputpicktwo(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(9).play(pygame.mixer.Sound('place chips.mp3'))
                        print("2")
                        two()
                        

                def checkForInputpickthree(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("3")
                        three()

                def checkForInputpickfour(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("4")
                        four()

                def checkForInputpickfive(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("5")
                        five()

                def checkForInputpicksix(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("6")
                        six()

                def checkForInputpickseven(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("7")
                        seven()

                def checkForInputpickeight(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("8")
                        eight()

                def checkForInputpicknine(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("9")
                        nine()

                def checkForInputpickten(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("10")
                        ten()

                def checkForInputpickeleven(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("11")
                        eleven()

                def checkForInputpicktwelve(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("12")
                        twelve()

                def checkForInputpickthirteen(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("13")
                        thirteen()

                def checkForInputpickfourteen(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("14")
                        fourteen()

                def checkForInputpickfifteen(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("15")
                        fifteen()

                def checkForInputpicksixteen(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("16")
                        sixteen()

                def checkForInputpickseventeen(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("17")
                        seventeen()

                def checkForInputpickeighteen(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("18")
                        eighteen()

                def checkForInputpicknineteen(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("19")
                        nineteen()

                def checkForInputpicktwenty(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("20")
                        twenty()

                def checkForInputpicktwentyone(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("21")
                        twentyone()

                def checkForInputpicktwentytwo(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("22")
                        twentytwo()

                def checkForInputpicktwentythree(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("23")
                        twentythree()

                def checkForInputpicktwentyfour(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("24")
                        twentyfour()

                def checkForInputpicktwentyfive(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("25")
                        twentyfive()

                def checkForInputpicktwentysix(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("26")
                        twentysix()

                def checkForInputpicktwentyseven(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("27")
                        twentyseven()

                def checkForInputpicktwentyeight(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("28")
                        twentyeight()

                def checkForInputpicktwentynine(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("29")
                        twentynine()

                def checkForInputpickthirty(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("30")
                        thirty()

                def checkForInputpickthirtyone(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("31")
                        thirtyone()

                def checkForInputpickthirtytwo(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("32")
                        thirtytwo()

                def checkForInputpickthirtythree(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("33")
                        thirtythree()

                def checkForInputpickthirtyfour(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("34")
                        thirtyfour()

                def checkForInputpickthirtyfive(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("35")
                        thirtyfive()

                def checkForInputpickthirtysix(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("36")
                        thirtysix()

                def checkForInputpickzero(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("0")
                        zero()

                def checkForInputpickdoublezero(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("00")
                        doublezero()

                def checkForInputpickonetotwelve(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("1-12")
                        onetotwelve()

                def checkForInputpickthirteentotwentyfour(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("13-24")
                        thirteentotwentyfour()

                def checkForInputpicktwentyfivetothirtysix(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("25-36")
                        twentyfivetothirtysix()

                def checkForInputpickeven(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("Even")
                        even()
                        

                def checkForInputpickodd(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("Odd")
                        odd()
                        

                def checkForInputpickblack(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("Black")
                        black()
                        
                        

                def checkForInputpickred(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        print("Red")
                        red()

                def checkForInputbet500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet1000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 1000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet1500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 1500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet2000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 2000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet2500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 2500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet3000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 3000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet3500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 3500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet4000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 4000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet4500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 4500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet5000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 5000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet5500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 5500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet6000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 6000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet6500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 6500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet7000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 7000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet7500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 7500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet8000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 8000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet8500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 8500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet9000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 9000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet9500(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 9500
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputbet10000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = 10000
                        chips[0] = chips[0] - chips[1]

                def checkForInputbetALL(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('place chips.mp3'))
                        chips[1] = chips[0]
                        chips[0] = chips[0] - chips[1]
                        

        
                        




                def changeColor(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = rt_font.render(self.text_input, True, "green")
                                else:
                                        self.text = rt_font.render(self.text_input, True, "white")

                
                        

                
                        
                        

                




        button_roulette_one_surface = pygame.image.load("one red.PNG")
        button_roulette_one_surface = pygame.transform.scale(button_roulette_one_surface, (52,65))

        button_roulette_one = Button(button_roulette_one_surface , 403, 464, "") #y coords for numbers = 464, 395, 325

        button_roulette_two_surface = pygame.image.load("two black.PNG")
        button_roulette_two_surface = pygame.transform.scale(button_roulette_two_surface, (52,65))

        button_roulette_two = Button(button_roulette_two_surface , 403, 395, "")

        button_roulette_three_surface = pygame.image.load("three red.PNG")
        button_roulette_three_surface = pygame.transform.scale(button_roulette_three_surface, (52,65))

        button_roulette_three = Button(button_roulette_three_surface , 403, 325, "")

        button_roulette_four_surface = pygame.image.load("four black.PNG")
        button_roulette_four_surface = pygame.transform.scale(button_roulette_four_surface, (52,65))

        button_roulette_four = Button(button_roulette_four_surface , 463, 464, "") #y coords for numbers = 464, 395, 325

        button_roulette_five_surface = pygame.image.load("five red.PNG")
        button_roulette_five_surface = pygame.transform.scale(button_roulette_five_surface, (52,65))

        button_roulette_five = Button(button_roulette_five_surface , 463, 395, "") #x coords are in 60 increments

        button_roulette_six_surface = pygame.image.load("six black.PNG")
        button_roulette_six_surface = pygame.transform.scale(button_roulette_six_surface, (52,65))

        button_roulette_six = Button(button_roulette_six_surface , 463, 325, "")

        button_roulette_seven_surface = pygame.image.load("seven red.PNG")
        button_roulette_seven_surface = pygame.transform.scale(button_roulette_seven_surface, (52,65))

        button_roulette_seven = Button(button_roulette_seven_surface , 523, 464, "") #y coords for numbers = 464, 395, 325

        button_roulette_eight_surface = pygame.image.load("eight black.PNG")
        button_roulette_eight_surface = pygame.transform.scale(button_roulette_eight_surface, (52,65))

        button_roulette_eight = Button(button_roulette_eight_surface , 523, 395, "") #x coords are in 60 increments

        button_roulette_nine_surface = pygame.image.load("nine red.PNG")
        button_roulette_nine_surface = pygame.transform.scale(button_roulette_nine_surface, (52,65))

        button_roulette_nine = Button(button_roulette_nine_surface , 523, 325, "")

        button_roulette_ten_surface = pygame.image.load("ten black.PNG")
        button_roulette_ten_surface = pygame.transform.scale(button_roulette_ten_surface, (52,65))

        button_roulette_ten = Button(button_roulette_ten_surface , 583, 464, "") #y coords for numbers = 464, 395, 325

        button_roulette_eleven_surface = pygame.image.load("eleven black.PNG")
        button_roulette_eleven_surface = pygame.transform.scale(button_roulette_eleven_surface, (52,65))

        button_roulette_eleven = Button(button_roulette_eleven_surface , 583, 395, "") #x coords are in 60 increments

        button_roulette_twelve_surface = pygame.image.load("twelve red.PNG")
        button_roulette_twelve_surface = pygame.transform.scale(button_roulette_twelve_surface, (52,65))

        button_roulette_twelve = Button(button_roulette_twelve_surface , 583, 325, "")

        button_roulette_thirteen_surface = pygame.image.load("thirteen black.PNG")
        button_roulette_thirteen_surface = pygame.transform.scale(button_roulette_thirteen_surface, (52,65))

        button_roulette_thirteen = Button(button_roulette_thirteen_surface , 638, 464, "") #y coords for numbers = 464, 395, 325

        button_roulette_fourteen_surface = pygame.image.load("fourteen red.PNG")
        button_roulette_fourteen_surface = pygame.transform.scale(button_roulette_fourteen_surface, (52,65))

        button_roulette_fourteen = Button(button_roulette_fourteen_surface , 638, 395, "") #x coords are in 60 increments

        button_roulette_fifteen_surface = pygame.image.load("fifteen black.PNG")
        button_roulette_fifteen_surface = pygame.transform.scale(button_roulette_fifteen_surface, (52,65))

        button_roulette_fifteen = Button(button_roulette_fifteen_surface , 638, 325, "")

        button_roulette_sixteen_surface = pygame.image.load("sixteen red.PNG")
        button_roulette_sixteen_surface = pygame.transform.scale(button_roulette_sixteen_surface, (52,65))

        button_roulette_sixteen = Button(button_roulette_sixteen_surface , 698, 469, "") #y coords for numbers = 464, 395, 325

        button_roulette_seventeen_surface = pygame.image.load("seventeen black.PNG")
        button_roulette_seventeen_surface = pygame.transform.scale(button_roulette_seventeen_surface, (52,65))

        button_roulette_seventeen = Button(button_roulette_seventeen_surface , 698, 395, "") #x coords are in 60 increments

        button_roulette_eighteen_surface = pygame.image.load("eighteen red.PNG")
        button_roulette_eighteen_surface = pygame.transform.scale(button_roulette_eighteen_surface, (52,65))

        button_roulette_eighteen = Button(button_roulette_eighteen_surface , 698, 325, "")

        button_roulette_nineteen_surface = pygame.image.load("nineteen red.PNG")
        button_roulette_nineteen_surface = pygame.transform.scale(button_roulette_nineteen_surface, (52,65))

        button_roulette_nineteen = Button(button_roulette_nineteen_surface , 753, 469, "") #y coords for numbers = 464, 395, 325

        button_roulette_twenty_surface = pygame.image.load("twenty black.PNG")
        button_roulette_twenty_surface = pygame.transform.scale(button_roulette_twenty_surface, (52,65))

        button_roulette_twenty = Button(button_roulette_twenty_surface , 753, 395, "") #x coords are in 60 increments

        button_roulette_twentyone_surface = pygame.image.load("twenty one red.PNG")
        button_roulette_twentyone_surface = pygame.transform.scale(button_roulette_twentyone_surface, (52,65))

        button_roulette_twentyone = Button(button_roulette_twentyone_surface , 753, 325, "")

        button_roulette_twentytwo_surface = pygame.image.load("twenty two black.PNG")
        button_roulette_twentytwo_surface = pygame.transform.scale(button_roulette_twentytwo_surface, (52,65))

        button_roulette_twentytwo = Button(button_roulette_twentytwo_surface , 813, 469, "") #y coords for numbers = 464, 395, 325

        button_roulette_twentythree_surface = pygame.image.load("twenty three red.PNG")
        button_roulette_twentythree_surface = pygame.transform.scale(button_roulette_twentythree_surface, (52,65))

        button_roulette_twentythree = Button(button_roulette_twentythree_surface , 813, 395, "") #x coords are in 60 increments

        button_roulette_twentyfour_surface = pygame.image.load("twenty four black.PNG")
        button_roulette_twentyfour_surface = pygame.transform.scale(button_roulette_twentyfour_surface, (52,65))

        button_roulette_twentyfour = Button(button_roulette_twentyfour_surface , 813, 325, "")

        button_roulette_twentyfive_surface = pygame.image.load("twenty five red.PNG")
        button_roulette_twentyfive_surface = pygame.transform.scale(button_roulette_twentyfive_surface, (52,65))

        button_roulette_twentyfive = Button(button_roulette_twentyfive_surface , 873, 469, "") #y coords for numbers = 464, 395, 325

        button_roulette_twentysix_surface = pygame.image.load("twenty six black.PNG")
        button_roulette_twentysix_surface = pygame.transform.scale(button_roulette_twentysix_surface, (52,65))

        button_roulette_twentysix = Button(button_roulette_twentysix_surface , 873, 395, "") #x coords are in 60 increments

        button_roulette_twentyseven_surface = pygame.image.load("twenty seven black.PNG")
        button_roulette_twentyseven_surface = pygame.transform.scale(button_roulette_twentyseven_surface, (52,65))

        button_roulette_twentyseven = Button(button_roulette_twentyseven_surface , 873, 325, "")

        button_roulette_twentyeight_surface = pygame.image.load("twenty eight black.PNG")
        button_roulette_twentyeight_surface = pygame.transform.scale(button_roulette_twentyeight_surface, (52,65))

        button_roulette_twentyeight = Button(button_roulette_twentyeight_surface , 933, 469, "") #y coords for numbers = 464, 395, 325

        button_roulette_twentynine_surface = pygame.image.load("twenty nine black.PNG")
        button_roulette_twentynine_surface = pygame.transform.scale(button_roulette_twentynine_surface, (52,65))

        button_roulette_twentynine = Button(button_roulette_twentysix_surface , 933, 395, "") #x coords are in 60 increments

        button_roulette_thirty_surface = pygame.image.load("thirty red.PNG")
        button_roulette_thirty_surface = pygame.transform.scale(button_roulette_thirty_surface, (52,65))

        button_roulette_thirty = Button(button_roulette_thirty_surface , 933, 325, "")

        button_roulette_thirtyone_surface = pygame.image.load("thirty one black.PNG")
        button_roulette_thirtyone_surface = pygame.transform.scale(button_roulette_thirtyone_surface, (52,65))

        button_roulette_thirtyone = Button(button_roulette_thirtyone_surface , 993, 469, "")

        button_roulette_thirtytwo_surface = pygame.image.load("thirty two red.PNG")
        button_roulette_thirtytwo_surface = pygame.transform.scale(button_roulette_thirtytwo_surface, (52,65))

        button_roulette_thirtytwo = Button(button_roulette_thirtytwo_surface , 993, 395, "")

        button_roulette_thirtythree_surface = pygame.image.load("thirty three black.PNG")
        button_roulette_thirtythree_surface = pygame.transform.scale(button_roulette_thirtythree_surface, (52,65))

        button_roulette_thirtythree = Button(button_roulette_thirtythree_surface , 993, 325, "")

        button_roulette_thirtyfour_surface = pygame.image.load("thirty four red.PNG")
        button_roulette_thirtyfour_surface = pygame.transform.scale(button_roulette_thirtyfour_surface, (52,65))

        button_roulette_thirtyfour = Button(button_roulette_thirtyfour_surface , 1048, 469, "")

        button_roulette_thirtyfive_surface = pygame.image.load("thirty five black.PNG")
        button_roulette_thirtyfive_surface = pygame.transform.scale(button_roulette_thirtyfive_surface, (52,65))

        button_roulette_thirtyfive = Button(button_roulette_thirtyfive_surface , 1048, 395, "")

        button_roulette_thirtysix_surface = pygame.image.load("thirty six red.PNG")
        button_roulette_thirtysix_surface = pygame.transform.scale(button_roulette_thirtysix_surface, (52,65))

        button_roulette_thirtysix = Button(button_roulette_thirtysix_surface , 1048, 325, "")

        button_roulette_zero_surface = pygame.image.load("zero green.PNG")
        button_roulette_zero_surface = pygame.transform.scale(button_roulette_zero_surface, (42,55))

        button_roulette_zero = Button(button_roulette_zero_surface , 350, 445, "")

        button_roulette_doublezero_surface = pygame.image.load("double zero green.PNG")
        button_roulette_doublezero_surface = pygame.transform.scale(button_roulette_doublezero_surface, (42,55))

        button_roulette_doublezero = Button(button_roulette_doublezero_surface , 350, 345, "")

        button_roulette_onetotwelve_surface = pygame.image.load("one to twelve.PNG")
        button_roulette_onetotwelve_surface = pygame.transform.scale(button_roulette_onetotwelve_surface, (220,50))

        button_roulette_onetotwelve = Button(button_roulette_onetotwelve_surface , 490, 545, "")

        button_roulette_thirteentotwentyfour_surface = pygame.image.load("thirteen to twenty four.PNG")
        button_roulette_thirteentotwentyfour_surface = pygame.transform.scale(button_roulette_thirteentotwentyfour_surface, (220,50))

        button_roulette_thirteentotwentyfour = Button(button_roulette_thirteentotwentyfour_surface , 732, 545, "")

        button_roulette_twentyfivetothirtysix_surface = pygame.image.load("twenty five to thirty six.PNG")
        button_roulette_twentyfivetothirtysix_surface = pygame.transform.scale(button_roulette_twentyfivetothirtysix_surface, (170,50))

        button_roulette_twentyfivetothirtysix = Button(button_roulette_twentyfivetothirtysix_surface , 952, 545, "")

        button_roulette_even_surface = pygame.image.load("even.PNG")
        button_roulette_even_surface = pygame.transform.scale(button_roulette_even_surface, (165,55))

        button_roulette_even = Button(button_roulette_even_surface , 465, 605, "")

        button_roulette_odd_surface = pygame.image.load("odd.PNG")
        button_roulette_odd_surface = pygame.transform.scale(button_roulette_odd_surface, (112,35))

        button_roulette_odd = Button(button_roulette_odd_surface , 990, 605, "")

        button_roulette_red_surface = pygame.image.load("red roulette.PNG")
        button_roulette_red_surface = pygame.transform.scale(button_roulette_red_surface, (132,55))

        button_roulette_red = Button(button_roulette_red_surface , 638, 605, "")

        button_roulette_black_surface = pygame.image.load("black roulette.PNG")
        button_roulette_black_surface = pygame.transform.scale(button_roulette_black_surface, (132,55))

        button_roulette_black = Button(button_roulette_black_surface , 815, 605, "")

        button_roulette_500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_500_surface = pygame.transform.scale(button_roulette_500_surface, (132,55))

        button_roulette_500= Button(button_roulette_500_surface , 75, 205, "500")

        button_roulette_1000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_1000_surface = pygame.transform.scale(button_roulette_1000_surface, (132,55))

        button_roulette_1000= Button(button_roulette_1000_surface , 210, 205, "1000")

        button_roulette_1500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_1500_surface = pygame.transform.scale(button_roulette_1500_surface, (132,55))

        button_roulette_1500= Button(button_roulette_1500_surface , 75, 305, "1500")

        button_roulette_2000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_2000_surface = pygame.transform.scale(button_roulette_2000_surface, (132,55))

        button_roulette_2000= Button(button_roulette_2000_surface , 210, 305, "2000")

        button_roulette_2500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_2500_surface = pygame.transform.scale(button_roulette_2500_surface, (132,55))

        button_roulette_2500= Button(button_roulette_2500_surface , 75, 405, "2500")

        button_roulette_3000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_3000_surface = pygame.transform.scale(button_roulette_3000_surface, (132,55))

        button_roulette_3000= Button(button_roulette_3000_surface , 210, 405, "3000")

        button_roulette_3500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_3500_surface = pygame.transform.scale(button_roulette_3500_surface, (132,55))

        button_roulette_3500= Button(button_roulette_3500_surface , 75, 505, "3500")

        button_roulette_4000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_4000_surface = pygame.transform.scale(button_roulette_4000_surface, (132,55))

        button_roulette_4000= Button(button_roulette_4000_surface , 210, 505, "4000")

        button_roulette_4500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_4500_surface = pygame.transform.scale(button_roulette_4500_surface, (132,55))

        button_roulette_4500= Button(button_roulette_4500_surface , 75, 605, "4500")

        button_roulette_5000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_5000_surface = pygame.transform.scale(button_roulette_5000_surface, (132,55))

        button_roulette_5000= Button(button_roulette_5000_surface , 210, 605, "5000")

        button_roulette_5500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_5500_surface = pygame.transform.scale(button_roulette_5500_surface, (132,55))

        button_roulette_5500= Button(button_roulette_5500_surface , 1275, 205, "5500")

        button_roulette_6000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_6000_surface = pygame.transform.scale(button_roulette_6000_surface, (132,55))

        button_roulette_6000= Button(button_roulette_6000_surface , 1400, 205, "6000")

        button_roulette_6500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_6500_surface = pygame.transform.scale(button_roulette_6500_surface, (132,55))

        button_roulette_6500= Button(button_roulette_6500_surface , 1275, 305, "6500")

        button_roulette_7000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_7000_surface = pygame.transform.scale(button_roulette_7000_surface, (132,55))

        button_roulette_7000= Button(button_roulette_7000_surface , 1400, 305, "7000")

        button_roulette_7500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_7500_surface = pygame.transform.scale(button_roulette_7500_surface, (132,55))

        button_roulette_7500= Button(button_roulette_7500_surface , 1275, 405, "7500")

        button_roulette_8000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_8000_surface = pygame.transform.scale(button_roulette_8000_surface, (132,55))

        button_roulette_8000= Button(button_roulette_8000_surface , 1400, 405, "8000")

        button_roulette_8500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_8500_surface = pygame.transform.scale(button_roulette_3500_surface, (132,55))

        button_roulette_8500= Button(button_roulette_8500_surface , 1275, 505, "8500")

        button_roulette_9000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_9000_surface = pygame.transform.scale(button_roulette_9000_surface, (132,55))

        button_roulette_9000= Button(button_roulette_9000_surface , 1400, 505, "9000")

        button_roulette_9500_surface = pygame.image.load("grey blackjack.png")
        button_roulette_9500_surface = pygame.transform.scale(button_roulette_9500_surface, (132,55))

        button_roulette_9500= Button(button_roulette_9500_surface , 1275, 605, "9500")

        button_roulette_10000_surface = pygame.image.load("grey blackjack.png")
        button_roulette_10000_surface = pygame.transform.scale(button_roulette_10000_surface, (132,55))

        button_roulette_10000= Button(button_roulette_10000_surface , 1400, 605, "10000")

        button_roulette_ALL_surface = pygame.image.load("grey blackjack.png")
        button_roulette_ALL_surface = pygame.transform.scale(button_roulette_ALL_surface, (132,55))

        button_roulette_ALL= Button(button_roulette_ALL_surface , 1335, 705, "ALL")

        

        
                

        

        

        button_roulette_one.update()
        button_roulette_two.update()
        button_roulette_three.update()
        button_roulette_four.update()
        button_roulette_five.update()
        button_roulette_six.update()
        button_roulette_seven.update()
        button_roulette_eight.update()
        button_roulette_nine.update()
        button_roulette_ten.update()
        button_roulette_eleven.update()
        button_roulette_twelve.update()
        button_roulette_thirteen.update()
        button_roulette_fourteen.update()
        button_roulette_fifteen.update()
        button_roulette_sixteen.update()
        button_roulette_seventeen.update()
        button_roulette_eighteen.update()
        button_roulette_nineteen.update()
        button_roulette_twenty.update()
        button_roulette_twentyone.update()
        button_roulette_twentytwo.update()
        button_roulette_twentythree.update()
        button_roulette_twentyfour.update()
        button_roulette_twentyfive.update()
        button_roulette_twentysix.update()
        button_roulette_twentyseven.update()
        button_roulette_twentyeight.update()
        button_roulette_twentynine.update()
        button_roulette_thirty.update()
        button_roulette_thirtyone.update()
        button_roulette_thirtytwo.update()
        button_roulette_thirtythree.update()
        button_roulette_thirtyfour.update()
        button_roulette_thirtyfive.update()
        button_roulette_thirtysix.update()
        button_roulette_zero.update()
        button_roulette_doublezero.update()
        button_roulette_onetotwelve.update()
        button_roulette_thirteentotwentyfour.update()
        button_roulette_twentyfivetothirtysix.update()
        button_roulette_even.update()
        button_roulette_odd.update()
        button_roulette_red.update()
        button_roulette_black.update()
        button_roulette_500.update()
        button_roulette_1000.update()
        button_roulette_1500.update()
        button_roulette_2000.update()
        button_roulette_2500.update()
        button_roulette_3000.update()
        button_roulette_3500.update()
        button_roulette_4000.update()
        button_roulette_4500.update()
        button_roulette_5000.update()
        button_roulette_5500.update()
        button_roulette_6000.update()
        button_roulette_6500.update()
        button_roulette_7000.update()
        button_roulette_7500.update()
        button_roulette_8000.update()
        button_roulette_8500.update()
        button_roulette_9000.update()
        button_roulette_9500.update()
        button_roulette_10000.update()
        button_roulette_ALL.update()
        

        pygame.time.set_timer(pygame.USEREVENT, 20000)

        time = 1

        
        



















        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()

                        if event.type == pygame.USEREVENT:
                                time -= 1
                                if time == 0:
                                        roulette()

                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        roulette_menu()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                             button_roulette_one.checkForInputpickone(pygame.mouse.get_pos())
                             button_roulette_two.checkForInputpicktwo(pygame.mouse.get_pos())
                             button_roulette_three.checkForInputpickthree(pygame.mouse.get_pos())
                             button_roulette_four.checkForInputpickfour(pygame.mouse.get_pos())
                             button_roulette_five.checkForInputpickfive(pygame.mouse.get_pos())
                             button_roulette_six.checkForInputpicksix(pygame.mouse.get_pos())
                             button_roulette_seven.checkForInputpickseven(pygame.mouse.get_pos())
                             button_roulette_eight.checkForInputpickeight(pygame.mouse.get_pos())
                             button_roulette_nine.checkForInputpicknine(pygame.mouse.get_pos())
                             button_roulette_ten.checkForInputpickten(pygame.mouse.get_pos())
                             button_roulette_eleven.checkForInputpickeleven(pygame.mouse.get_pos())
                             button_roulette_twelve.checkForInputpicktwelve(pygame.mouse.get_pos())
                             button_roulette_thirteen.checkForInputpickthirteen(pygame.mouse.get_pos())
                             button_roulette_fourteen.checkForInputpickfourteen(pygame.mouse.get_pos())
                             button_roulette_fifteen.checkForInputpickfifteen(pygame.mouse.get_pos())
                             button_roulette_sixteen.checkForInputpicksixteen(pygame.mouse.get_pos())
                             button_roulette_seventeen.checkForInputpickseventeen(pygame.mouse.get_pos())
                             button_roulette_eighteen.checkForInputpickeighteen(pygame.mouse.get_pos())
                             button_roulette_nineteen.checkForInputpicknineteen(pygame.mouse.get_pos())
                             button_roulette_twenty.checkForInputpicktwenty(pygame.mouse.get_pos())
                             button_roulette_twentyone.checkForInputpicktwentyone(pygame.mouse.get_pos())
                             button_roulette_twentytwo.checkForInputpicktwentytwo(pygame.mouse.get_pos())
                             button_roulette_twentythree.checkForInputpicktwentythree(pygame.mouse.get_pos())
                             button_roulette_twentyfour.checkForInputpicktwentyfour(pygame.mouse.get_pos())
                             button_roulette_twentyfive.checkForInputpicktwentyfive(pygame.mouse.get_pos())
                             button_roulette_twentysix.checkForInputpicktwentysix(pygame.mouse.get_pos())
                             button_roulette_twentyseven.checkForInputpicktwentyseven(pygame.mouse.get_pos())
                             button_roulette_twentyeight.checkForInputpicktwentyeight(pygame.mouse.get_pos())
                             button_roulette_twentynine.checkForInputpicktwentynine(pygame.mouse.get_pos())
                             button_roulette_thirty.checkForInputpickthirty(pygame.mouse.get_pos())
                             button_roulette_thirtyone.checkForInputpickthirtyone(pygame.mouse.get_pos())
                             button_roulette_thirtytwo.checkForInputpickthirtytwo(pygame.mouse.get_pos())
                             button_roulette_thirtythree.checkForInputpickthirtythree(pygame.mouse.get_pos())
                             button_roulette_thirtyfour.checkForInputpickthirtyfour(pygame.mouse.get_pos())
                             button_roulette_thirtyfive.checkForInputpickthirtyfive(pygame.mouse.get_pos())
                             button_roulette_thirtysix.checkForInputpickthirtysix(pygame.mouse.get_pos())
                             button_roulette_zero.checkForInputpickzero(pygame.mouse.get_pos())
                             button_roulette_doublezero.checkForInputpickdoublezero(pygame.mouse.get_pos())
                             button_roulette_onetotwelve.checkForInputpickonetotwelve(pygame.mouse.get_pos())
                             button_roulette_thirteentotwentyfour.checkForInputpickthirteentotwentyfour(pygame.mouse.get_pos())
                             button_roulette_twentyfivetothirtysix.checkForInputpicktwentyfivetothirtysix(pygame.mouse.get_pos())
                             button_roulette_even.checkForInputpickeven(pygame.mouse.get_pos())
                             button_roulette_odd.checkForInputpickodd(pygame.mouse.get_pos())
                             button_roulette_red.checkForInputpickred(pygame.mouse.get_pos())
                             button_roulette_black.checkForInputpickblack(pygame.mouse.get_pos())
                             button_roulette_500.checkForInputbet500(pygame.mouse.get_pos())
                             button_roulette_1000.checkForInputbet1000(pygame.mouse.get_pos())
                             button_roulette_1500.checkForInputbet1500(pygame.mouse.get_pos())
                             button_roulette_2000.checkForInputbet2000(pygame.mouse.get_pos())
                             button_roulette_2500.checkForInputbet2500(pygame.mouse.get_pos())
                             button_roulette_3000.checkForInputbet3000(pygame.mouse.get_pos())
                             button_roulette_3500.checkForInputbet3500(pygame.mouse.get_pos())
                             button_roulette_4000.checkForInputbet4000(pygame.mouse.get_pos())
                             button_roulette_4500.checkForInputbet4500(pygame.mouse.get_pos())
                             button_roulette_5000.checkForInputbet5000(pygame.mouse.get_pos())
                             button_roulette_5500.checkForInputbet5500(pygame.mouse.get_pos())
                             button_roulette_6000.checkForInputbet6000(pygame.mouse.get_pos())
                             button_roulette_6500.checkForInputbet6500(pygame.mouse.get_pos())
                             button_roulette_7000.checkForInputbet7000(pygame.mouse.get_pos())
                             button_roulette_7500.checkForInputbet7500(pygame.mouse.get_pos())
                             button_roulette_8000.checkForInputbet8000(pygame.mouse.get_pos())
                             button_roulette_8500.checkForInputbet8500(pygame.mouse.get_pos())
                             button_roulette_9000.checkForInputbet9000(pygame.mouse.get_pos())
                             button_roulette_9500.checkForInputbet9500(pygame.mouse.get_pos())
                             button_roulette_10000.checkForInputbet10000(pygame.mouse.get_pos())
                             button_roulette_ALL.checkForInputbetALL(pygame.mouse.get_pos())
                             
                             


                        button_roulette_one.update()
                        button_roulette_two.update()
                        button_roulette_three.update()
                        button_roulette_four.update()
                        button_roulette_five.update()
                        button_roulette_six.update()
                        button_roulette_seven.update()
                        button_roulette_eight.update()
                        button_roulette_nine.update()
                        button_roulette_ten.update()
                        button_roulette_eleven.update()
                        button_roulette_twelve.update()
                        button_roulette_thirteen.update()
                        button_roulette_fourteen.update()
                        button_roulette_fifteen.update()
                        button_roulette_sixteen.update()
                        button_roulette_seventeen.update()
                        button_roulette_eighteen.update()
                        button_roulette_nineteen.update()
                        button_roulette_twenty.update()
                        button_roulette_twentyone.update()
                        button_roulette_twentytwo.update()
                        button_roulette_twentythree.update()
                        button_roulette_twentyfour.update()
                        button_roulette_twentyfive.update()
                        button_roulette_twentysix.update()
                        button_roulette_twentyseven.update()
                        button_roulette_twentyeight.update()
                        button_roulette_twentynine.update()
                        button_roulette_thirty.update()
                        button_roulette_thirtyone.update()
                        button_roulette_thirtytwo.update()
                        button_roulette_thirtythree.update()
                        button_roulette_thirtyfour.update()
                        button_roulette_thirtyfive.update()
                        button_roulette_thirtysix.update()
                        button_roulette_zero.update()
                        button_roulette_doublezero.update()
                        button_roulette_onetotwelve.update()
                        button_roulette_thirteentotwentyfour.update()
                        button_roulette_twentyfivetothirtysix.update()
                        button_roulette_even.update()
                        button_roulette_odd.update()
                        button_roulette_red.update()
                        button_roulette_black.update()

                        button_roulette_500.changeColor(pygame.mouse.get_pos())
                        button_roulette_500.update()

                        button_roulette_1000.changeColor(pygame.mouse.get_pos())
                        button_roulette_1000.update()

                        button_roulette_1500.changeColor(pygame.mouse.get_pos())
                        button_roulette_1500.update()

                        button_roulette_2000.changeColor(pygame.mouse.get_pos())
                        button_roulette_2000.update()

                        button_roulette_2500.changeColor(pygame.mouse.get_pos())
                        button_roulette_2500.update()

                        button_roulette_3000.changeColor(pygame.mouse.get_pos())
                        button_roulette_3000.update()

                        button_roulette_3500.changeColor(pygame.mouse.get_pos())
                        button_roulette_3500.update()

                        button_roulette_4000.changeColor(pygame.mouse.get_pos())
                        button_roulette_4000.update()

                        button_roulette_4500.changeColor(pygame.mouse.get_pos())
                        button_roulette_4500.update()

                        button_roulette_5000.changeColor(pygame.mouse.get_pos())
                        button_roulette_5000.update()

                        button_roulette_5500.changeColor(pygame.mouse.get_pos())
                        button_roulette_5500.update()

                        button_roulette_6000.changeColor(pygame.mouse.get_pos())
                        button_roulette_6000.update()

                        button_roulette_6500.changeColor(pygame.mouse.get_pos())
                        button_roulette_6500.update()

                        button_roulette_7000.changeColor(pygame.mouse.get_pos())
                        button_roulette_7000.update()

                        button_roulette_7500.changeColor(pygame.mouse.get_pos())
                        button_roulette_7500.update()

                        button_roulette_8000.changeColor(pygame.mouse.get_pos())
                        button_roulette_8000.update()

                        button_roulette_8500.changeColor(pygame.mouse.get_pos())
                        button_roulette_8500.update()

                        button_roulette_9000.changeColor(pygame.mouse.get_pos())
                        button_roulette_9000.update()

                        button_roulette_9500.changeColor(pygame.mouse.get_pos())
                        button_roulette_9500.update()

                        button_roulette_10000.changeColor(pygame.mouse.get_pos())
                        button_roulette_10000.update()

                        button_roulette_ALL.changeColor(pygame.mouse.get_pos())
                        button_roulette_ALL.update()

                        

                        

                        

                pygame.display.update()

        
def placeholder():
        pygame.display.set_caption("Jack of Hearts - Playing Roulette")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        rtp_screen = pygame.display.set_mode((1435,782))
        rtp_font = pygame.font.SysFont("Franklin Gothic Heavy", 40)
        clock = pygame.time.Clock()
        rt_background = pygame.image.load("roulette table background.PNG")
        rtp_screen.blit(rt_background, (0,0))

        pygame.time.set_timer(pygame.USEREVENT, 3000)

        time = 1


        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()

                        if event.type == pygame.USEREVENT:
                                time -= 1
                                if time == 0:
                                        roulette()

                pygame.display.update()        



def roulette():
        turtle.TurtleScreen._RUNNING = True
        turtle.title('Jack of Hearts - Playing Roulette')
        img = tkinter.Image("photo", file="icon.png")
        turtle._Screen._root.iconphoto(True, img)

        

        wn = turtle.Screen()
        global tablecolour, main_roulette_background

        if main_roulette_background == rt_background_purple:
                tablecolour = "purple"
        elif main_roulette_background == rt_background_red:
                tablecolour = "#AE0000" #COLOUR CODE FOR DARK RED
        elif main_roulette_background == rt_background_green:
                tablecolour = "#14B063"

        wn.bgcolor(tablecolour)

        pygame.mixer.Channel(10).play(pygame.mixer.Sound('Roulette Wheel Spinning, With Ball Dropping Into The Slot - QuickSounds.com.mp3'))

        size = 30
        speed = 6 #30 seconds at 10, 3 seconds at 4, 2 seconds at 2, then 0
        timer = 0

        imageone = "main boarder.gif"
        #imagetwo = "wheel middle main.gif"


        spoke1 = turtle.Turtle()
        spoke2 = turtle.Turtle()
        spoke3 = turtle.Turtle()
        spoke4 = turtle.Turtle()
        spoke5 = turtle.Turtle()
        spoke6 = turtle.Turtle()
        spoke7 = turtle.Turtle()
        spoke8 = turtle.Turtle()
        spoke9 = turtle.Turtle()
        spoke10 = turtle.Turtle()
        spoke11 = turtle.Turtle()
        spoke12 = turtle.Turtle()
        spoke13 = turtle.Turtle()
        spokecolour = turtle.Turtle()
        player = turtle.Turtle()
        playertwo = turtle.Turtle()
        spokes = [spoke1, spoke2, spoke3, spoke4, spoke5, spoke6, spoke7, spoke8, spoke9, spoke10, spoke11, spoke12, spoke13]
        images = [player]
        #imagestwo = [playertwo]
        spokecolours = [spokecolour]


        wn.addshape(imageone)
        player.shape(imageone)
        player.penup()

        


        _ = 0
        for spoke in spokes:
            spoke.speed(0)
            spoke.shape('square')
            spoke.shapesize(stretch_wid=0.1,stretch_len=30)
            spoke.left(15*_)
            _ += 1

        for spokecolour in spokecolours:
            spoke.speed(0)
            spoke.shape('arrow')
            spoke.shapesize(stretch_wid=1,stretch_len=30)   #arrow, width 1 len 30 square width 30 len 0.1
            spoke.left(15*_)
            _ += 1

        __ = 0
        for player in images:
            player.speed(0)
            player.left(15*__)
            __ += 1

##        __ = 0
##        for playertwo in imagestwo:
##            playertwo.speed(0)
##            playertwo.left(15*__)
##            __ += 1

        #rim = turtle.Pen()
        #rim.width(70)
        #rim.speed(0)
        #rim.up()
        #rim.forward(size*10)
        #rim.down()
        #rim.left(90)

        #rim.circle(size*10)

        def changespeed():
            speed = 0

##        wn.addshape(imagetwo)
##        playertwo.shape(imagetwo)
##        playertwo.penup()
        

        global timers
        global maintimer

            

        timers = [1870, 1830, 1780, 1740, 1710, 1670, 470, 510, 550, 580, 630, 660, 720, 750, 800, 840, 880, 930, 970, 1010, 1050, 1090, 1130, 1170, 1210, 1250, 1290, 1330, 1370, 1420, 1450, 1480, 1530, 1570, 1610, 430, 390, 350]
        maintimer = random.choice(timers) #1670 is 3 go from 470
        #print(maintimer)
        

       

        


        while True:
            for spoke in spokes:
                spoke.left(speed)
                timer = timer + 1
                if timer == maintimer:
                    speed = 3
                if timer == 1900:
                    speed = 2
                if timer == 2050:
                    speed = 0
                    if speed == 0:
                            sleep(3)
                            turtle.bye()
                            roulette_outcomes()
                
               

        while True:
            for player in images:
                player.left(speed)


        #THERE WILL BE A GOLDEN LINE THAT MEANS WHICH EVER THE GOLDEN LINE LANDS ON IS THE OUTCOME
        #EACH OUTCOME WILL HAVE A CORRESPONDING TIMER, ALL TIMERS WILL BE IN AN ARRAY, WHICH THE ODDS CAN BE DETERMINED

        turtle.ontimer(changespeed, t=10)

        turtle.done()


def roulette_outcomes():
        pygame.display.set_caption("Jack of Hearts - Playing Roulette")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        ro_screen = pygame.display.set_mode((1415,782))
        ro_font = pygame.font.SysFont("Franklin Gothic Heavy", 40)
        ro_results_font = pygame.font.SysFont("Franklin Gothic Heavy", 55)
        

        if tablecolour == "purple":
                ro_background = pygame.image.load("roulette results screen purple.PNG")
        elif tablecolour == "#AE0000":
                ro_background = pygame.image.load("roulette results screen red.PNG")
        elif tablecolour == "#14B063":
                ro_background = pygame.image.load("roulette results screen.PNG")

        
        
        ro_screen.blit(ro_background, (0,0))

        

        def displayRouletteWins():

                    #Display earnings on start screen, if file which money is stored doesn't exist then
                        # a file is created.

                    try:
                        with open('rouletteWINS.txt') as f:
                            current_roulettewins = f.readline()

                        #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                        #screen.blit(total_earnings, (870,80))

                    except:
                        #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                        #screen.blit(total_earnings, (870,30))

                        with open('rouletteWINS.txt', 'w') as f:
                            f.write(str(1))

        def increaseRouletteWins():
                

            

                     with open('rouletteWINS.txt') as f:
                        current_roulettewins = f.readline()
                        current_roulettewins = int(current_roulettewins)

                     if current_roulettewins > 0 and current_roulettewins < 100000:

                        with open('rouletteWINS.txt', 'w') as f:
                            global new_roulettewins
                            new_roulettewins = int(current_roulettewins) + 1
                            f.write(str(new_roulettewins))

        def displayRoulette361Wins():

                    #Display earnings on start screen, if file which money is stored doesn't exist then
                        # a file is created.

                    try:
                        with open('roulette361WINS.txt') as f:
                            current_roulette361wins = f.readline()

                        #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                        #screen.blit(total_earnings, (870,80))

                    except:
                        #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                        #screen.blit(total_earnings, (870,30))

                        with open('roulette361WINS.txt', 'w') as f:
                            f.write(str(1))

        def increaseRoulette361Wins():
                

            

                     with open('roulette361WINS.txt') as f:
                        current_roulette361wins = f.readline()
                        current_roulette361wins = int(current_roulette361wins)

                     if current_roulette361wins > 0 and current_roulette361wins < 100000:

                        with open('roulette361WINS.txt', 'w') as f:
                            global new_roulette361wins
                            new_roulette361wins = int(current_roulette361wins) + 1
                            f.write(str(new_roulette361wins))


        def displayRouletteLosses():

                    #Display earnings on start screen, if file which money is stored doesn't exist then
                        # a file is created.

                    try:
                        with open('rouletteLOSSES.txt') as f:
                            current_roulettelosses = f.readline()

                        #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                        #screen.blit(total_earnings, (870,80))

                    except:
                        #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                        #screen.blit(total_earnings, (870,30))

                        with open('rouletteLOSSES.txt', 'w') as f:
                            f.write(str(1))

        def increaseRouletteLosses():
                

            

                     with open('rouletteLOSSES.txt') as f:
                        current_roulettelosses = f.readline()
                        current_roulettelosses = int(current_roulettelosses)

                     if current_roulettelosses > 0 and current_roulettelosses < 100000:

                        with open('rouletteLOSSES.txt', 'w') as f:
                            global new_roulettelosses
                            new_roulettelosses = int(current_roulettelosses) + 1
                            f.write(str(new_roulettelosses))

                        

        

        #if statements

        
        if maintimer == 1870:
                if maintimer == 1870 and seventeen == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1870 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1870 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1870 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                          

                
                

        elif maintimer == 1830:
                if maintimer == 1830 and five == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1830 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1830 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1830 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 1780:
                if maintimer == 1780 and twentytwo == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1780 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1780 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1780 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

                
                

        elif maintimer == 1740:
                if maintimer == 1740 and thirtyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1740 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1740 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1740 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 1710:
                if maintimer == 1710 and fifteen == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
        
                
                elif maintimer == 1710 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1710 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1710 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

                
                

        elif maintimer == 1670:
                if maintimer == 1670 and three == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1670 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                elif maintimer == 1670 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chipsroulette[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chipsroulette[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                elif maintimer == 1670 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 470:
                if maintimer == 470 and eleven == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 470 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 470 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 470 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 510:
                if maintimer == 510 and thirty == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 510 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 510 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 510 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 550:
                if maintimer == 550 and twentysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 550 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 550 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 550 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 580:
                if maintimer == 580 and nine == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 580 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 580 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 580 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 630:
                if maintimer == 630 and twentyeight == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 630 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 630 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 630 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 670:
                if maintimer == 670 and zero == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 670 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 720:
                if maintimer == 720 and two == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 720 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 720 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 720 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 750:
                if maintimer == 750 and fourteen == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 750 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 750 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 750 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 800:
                if maintimer == 800 and thirtyfive == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 800 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 800 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 800 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 840:
                if maintimer == 840 and twentythree == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 840 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 840 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 840 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 880: #start
                if maintimer == 880 and four == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 880 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 880 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 880 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 930:
                if maintimer == 930 and sixteen== True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 930 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 930 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 930 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 970:
                if maintimer == 970 and thirtythree == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 970 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 970 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 970 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 1010:
                if maintimer == 1010 and twentyone == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1010 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                elif maintimer == 1010 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                elif maintimer == 1010 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 1050:
                if maintimer == 1050 and six == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1050 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1050 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1050 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1090:
                if maintimer == 1090 and eighteen == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1090 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1090 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1090 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1130:
                if maintimer == 1130 and thirtyone == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1130 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1130 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1130 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1170:
                if maintimer == 1170 and nineteen == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1170 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1170 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1170 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1210:
                if maintimer == 1210 and eight == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1210 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1210 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1210 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1250:
                if maintimer == 1250 and twelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1250 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1250 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1250 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1290:
                if maintimer == 1290 and twentynine == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1290 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1290 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1290 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1330:
                if maintimer == 1330 and thirtyfive == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1330 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1330 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1330 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1370:
                if maintimer == 1370 and ten == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1370 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1370 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1370 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1420:
                if maintimer == 1420 and twentyseven == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1420 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1420 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1420 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1450:
                if maintimer == 1450 and doublezero == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1450 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                
                
                

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 1480:
                if maintimer == 1480 and one == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1480 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1480 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1480 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()
                

        elif maintimer == 1530:
                if maintimer == 1530 and thirteen == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1530 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1530 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1530 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1570:
                if maintimer == 1570 and thirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1570 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                elif maintimer == 1570 and twentyfivetothirtysix == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()

                elif maintimer == 1570 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 1610:
                if maintimer == 1610 and twentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 1610 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1610 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 1610 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 350:
                if maintimer == 350 and thirtytwo == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 350 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chipsroulette[2] = chipsroulette[1] * 2
                        chipsroulette[0] = chipsroulette[0] + chipsroulette[2]
                        chip_text_roulette = ro_font.render(f' {chipsroulette[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chipsroulette[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 350 and twentyfivetothirtysix== True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 350 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 390:
                if maintimer == 390 and twenty == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 390 and even == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 390 and thirteentotwentyfour == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 390 and black == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        elif maintimer == 430:
                if maintimer == 430 and seven == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 36
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRoulette361Wins()
                        increaseRoulette361Wins()
                
                elif maintimer == 430 and odd == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 430 and onetotwelve == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                
                elif maintimer == 430 and red == True:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render(f'YOU WIN {chips[2]} CHIPS', True, 'white')
                        ro_screen.blit(results_text, (400, 700))
                        displayRouletteWins()
                        increaseRouletteWins()
                else:
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('claps and appluases.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))
                        chip_text_roulette = ro_font.render(f' {chips[0]}', True, 'white')
                        ro_screen.blit(chip_text_roulette, (1249, 4))
                        results_text = ro_results_font.render('YOU LOSE', True, 'white')
                        ro_screen.blit(results_text, (460, 700))
                        displayRouletteLosses()
                        increaseRouletteLosses()

        redfalse()

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = ro_font.render(self.text_input, True, "white")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputplayagain(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        roulette_menu()

                def changeColor(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = ro_font.render(self.text_input, True, "green")
                                else:
                                        self.text = ro_font.render(self.text_input, True, "white")

                
                        

                
                        
                        

                




        button_roulette_playagain_surface = pygame.image.load("green bass.PNG")
        button_roulette_playagain_surface = pygame.transform.scale(button_roulette_playagain_surface, (212,65))

        button_roulette_playagain = Button(button_roulette_playagain_surface , 1293, 744, "PLAY AGAIN")

        button_roulette_playagain.update()
                        
                        

        
                        
                        

        
                        
                        
                









        

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                                button_roulette_playagain.checkForInputplayagain(pygame.mouse.get_pos())



                button_roulette_playagain.changeColor(pygame.mouse.get_pos())
                button_roulette_playagain.update()


                pygame.display.update()

        







def indianrummy_menu():
        pygame.display.set_caption("Jack of Hearts - In the Indian Rummy Menu")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        ir_screen = pygame.display.set_mode((814,815))
        ir_font = pygame.font.SysFont("arial", 30)
        clock = pygame.time.Clock()
        ir_background = pygame.image.load("indian rummy menu.PNG")

        mixer.music.load('indian rummy menu music.mp3')
        pygame.mixer.music.play(loops=-1)
        mixer.music.set_volume(0.1)

        

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = ir_font.render(self.text_input, True, "white")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputIRPLAY(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(8).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                        indianrummy()

                def checkForInputIRCAREER(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(9).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                        indianrummy_career()

                def checkForInputIRRULES(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(9).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                        indianrummy_rules()

                def checkForInputIREXIT(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound('mixkit-casino-bling-achievement-2067.wav'))
                        pick_your_game()

                def changeColor1(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = ir_font.render(self.text_input, True, "green")
                                else:
                                        self.text = ir_font.render(self.text_input, True, "black")


        button_IR_back_surface = pygame.image.load("indian rummy button background.PNG")
        button_IR_back_surface = pygame.transform.scale(button_IR_back_surface, (100,20))

        button_IR_back = Button(button_IR_back_surface , 440, 777, "EXIT")

        button_IR_play_surface = pygame.image.load("indian rummy button background.PNG")
        button_IR_play_surface = pygame.transform.scale(button_IR_play_surface, (100,20))

        button_IR_play = Button(button_IR_play_surface , 440, 578, "PLAY")

        button_IR_rules_surface = pygame.image.load("indian rummy button background.PNG")
        button_IR_rules_surface = pygame.transform.scale(button_IR_rules_surface, (100,20))

        button_IR_rules = Button(button_IR_rules_surface , 440, 644, "RULES")

        button_IR_career_surface = pygame.image.load("indian rummy button background.PNG")
        button_IR_career_surface = pygame.transform.scale(button_IR_career_surface, (100,20))

        button_IR_career = Button(button_IR_career_surface , 440, 707, "CAREER")

        ir_screen.blit(ir_background, (0,0))

        button_IR_back.update()
        button_IR_play.update()
        button_IR_career.update()
        button_IR_rules.update()
        

        

        
        

        

        while True: #a loop that makes the screen run forever
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit() #opposite of pygame.init()
                        sys.exit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        button_IR_back.checkForInputIREXIT(pygame.mouse.get_pos())
                        button_IR_play.checkForInputIRPLAY(pygame.mouse.get_pos())
                        button_IR_career.checkForInputIRCAREER(pygame.mouse.get_pos())
                        button_IR_rules.checkForInputIRRULES(pygame.mouse.get_pos())



                button_IR_back.update()
                button_IR_back.changeColor1(pygame.mouse.get_pos())

                button_IR_play.update()
                button_IR_play.changeColor1(pygame.mouse.get_pos())

                button_IR_career.update()
                button_IR_career.changeColor1(pygame.mouse.get_pos())

                button_IR_rules.update()
                button_IR_rules.changeColor1(pygame.mouse.get_pos())




                pygame.display.update()

        

        

def indianrummy():
        import indianrummy


        
        

        
        
        
        
def indianrummy_rules():
        pygame.display.set_caption("Jack of Hearts - Learning the Rules of Indian Rummy")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        irr_screen = pygame.display.set_mode((1323, 810))
        irr_font = pygame.font.SysFont("Franklin Gothic Heavy", 35)
        clock = pygame.time.Clock()
        irr_screen_background = pygame.image.load("indian rummy rules screen.PNG")
        irr_screen.blit(irr_screen_background, (0,0))

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        indianrummy_menu()

                pygame.display.update()
        










def indianrummy_career():
        pygame.display.set_caption("Jack of Hearts - Viewing Career in Indian Rummy")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        irc_screen = pygame.display.set_mode((1250, 700))
        irc_font = pygame.font.SysFont("Franklin Gothic Heavy", 35)
        clock = pygame.time.Clock()
        irc_screen_background = pygame.image.load("indian rummy career menu.PNG")
        irc_screen.blit(irc_screen_background, (0,0))

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = irc_font.render(self.text_input, True, "grey")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputircback(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(16).play(pygame.mixer.Sound('Button Sound.wav'))
                        indianrummy_menu()

        buttonenter_irc_back_surface= pygame.image.load("neon purple arrow.PNG")
        buttonenter_irc_back_surface = pygame.transform.scale(buttonenter_irc_back_surface, (100, 60))

        buttonenter_irc_back = Button(buttonenter_irc_back_surface, 70, 520, "")

        buttonenter_irc_back.update()



        

        def displayirWins():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('irWINS.txt') as f:
                    global current_irwins
                    current_irwins = f.readline()

                total_irwins = irc_font.render(str(current_irwins), False , "White")
                irc_screen.blit(total_irwins, (595,231))

            except:
                total_irwins = irc_font.render(str(current_irwins), False , "White")
                irc_screen.blit(total_irwins, (870,30))

                with open('irWINS.txt', 'w') as f:
                    f.write(str(1))


        def displayirLosses():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('irLOSSES.txt') as f:
                    global current_irlosses
                    current_irlosses = f.readline()

                total_irlosses = irc_font.render(str(current_irlosses), False , "White")
                irc_screen.blit(total_irlosses, (621,298))

            except:
                total_irlosses = irc_font.render(str(current_irwins), False , "White")
                irc_screen.blit(total_irlosses, (870,30))

                with open('irLOSSES.txt', 'w') as f:
                    f.write(str(1))

        displayirWins()
        displayirLosses()

        totalgamesIR = int(current_irwins) + int(current_irlosses)

        totalgameszIR = irc_font.render(str(totalgamesIR), False, "White")
        irc_screen.blit(totalgameszIR, (725, 360))


        

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                buttonenter_irc_back.checkForInputircback(pygame.mouse.get_pos())


                buttonenter_irc_back.update()

                pygame.display.update()
        






def blackjack_menu():
    pygame.display.set_caption("Jack of Hearts - In the BlackJack Menu")
    programIcon = pygame.image.load('icon.png')
    pygame.display.set_icon(programIcon)
    blackjack_screen = pygame.display.set_mode((1450, 800))
    blackjack_font = pygame.font.SysFont("Franklin Gothic Heavy", 35)
    clock = pygame.time.Clock()
    blackjack_screen_background = pygame.image.load("BlackJack Menu Screen.PNG")
    global blackjacktotalwins, blackjacktotaldraws, blackjacktotallosses # totalchipswon, totalchipsspent, profit
    blackjacktotalwins = []
    blackjacktotaldraws = []
    blackjacktotallosses = []
    #totalchipswon = 0
    #totalchipsspent = 0
    #profit = 0

    mixer.music.load('Pre Game Lobby Music 2.mp3')
    pygame.mixer.music.play(loops=-1)
    mixer.music.set_volume(0.1)

    class Button():
        def __init__(self, image, x_pos, y_pos, text_input):
            self.image = image
            self.x_pos = x_pos
            self.y_pos = y_pos 
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_input = text_input
            self.text = blackjack_font.render(self.text_input, True, "grey")
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self):
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)


        def checkForInput13(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(12).play(pygame.mixer.Sound('Button Sound.wav'))
                blackjack()

        def checkForInput14(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(13).play(pygame.mixer.Sound('Button Sound.wav')) #need to do
                blackjack_career_menu()

        def checkForInput15(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(14).play(pygame.mixer.Sound('Button Sound.wav'))
                pick_your_game()

        def checkForInput16(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(15).play(pygame.mixer.Sound('Button Sound.wav'))
                        rules_screen()

        def changeColor(self, position):
                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        self.text = blackjack_font.render(self.text_input, True, "yellow")
                else:
                        self.text = blackjack_font.render(self.text_input, True, "grey")

    buttonenter_blackjack_play_surface= pygame.image.load("grey blackjack.png")
    buttonenter_blackjack_surface_play = pygame.transform.scale(buttonenter_blackjack_play_surface, (200, 105))

    buttonenter_blackjack_play = Button(buttonenter_blackjack_play_surface, 732, 680, "PLAY")

    buttonenter_blackjack_career_surface = pygame.image.load("grey blackjack.PNG")
    buttonenter_blackjack_career_surface = pygame.transform.scale(buttonenter_blackjack_career_surface, (200, 80)) #change size

    buttonenter_blackjack_career = Button(buttonenter_blackjack_career_surface, 1120, 680, "CAREER")

    buttonenter_blackjack_exit_surface = pygame.image.load("blackjack back button.PNG")
    buttonenter_blackjack_exit_surface = pygame.transform.scale(buttonenter_blackjack_exit_surface, (120, 140))

    buttonenter_blackjack_exit = Button(buttonenter_blackjack_exit_surface, 75, 690, "")

    button_blackjack_rules_surface = pygame.image.load("grey blackjack.PNG")
    button_blackjack_rules_surface = pygame.transform.scale(button_blackjack_rules_surface, (160,60))

    button_blackjack_rules = Button(button_blackjack_rules_surface , 350, 683, "RULES")

                

    blackjack_screen.blit(blackjack_screen_background,(0,0))

    buttonenter_blackjack_play.update()
    buttonenter_blackjack_career.update()
    buttonenter_blackjack_exit.update()
    button_blackjack_rules.update()
    
    

    pygame.display.update()

    while True: #a loop that makes the screen run forever
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit() #opposite of pygame.init()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttonenter_blackjack_play.checkForInput13(pygame.mouse.get_pos())
                    buttonenter_blackjack_career.checkForInput14(pygame.mouse.get_pos())
                    buttonenter_blackjack_exit.checkForInput15(pygame.mouse.get_pos())
                    button_blackjack_rules.checkForInput16(pygame.mouse.get_pos())

                
                    
                    
                    
        button_blackjack_rules.changeColor(pygame.mouse.get_pos())
        button_blackjack_rules.update()

        buttonenter_blackjack_play.changeColor(pygame.mouse.get_pos())
        buttonenter_blackjack_play.update()

        buttonenter_blackjack_career.changeColor(pygame.mouse.get_pos())
        buttonenter_blackjack_career.update()

        pygame.display.update()

    

    








def horseracing_menu():
    pygame.display.set_caption("Jack of Hearts - In the Horse Racing Menu")
    programIcon = pygame.image.load('icon.png')
    pygame.display.set_icon(programIcon)
    hr_screen = pygame.display.set_mode((1450, 800))
    hr_font = pygame.font.SysFont("arial", 30)
    clock = pygame.time.Clock()
    hr_screen_background = pygame.image.load("horse racing background.jpg")

    mixer.music.load('urban-hip-hop-117973.mp3')
    pygame.mixer.music.play(loops=-1)
    mixer.music.set_volume(0.1)

    class Button():
        def __init__(self, image, x_pos, y_pos, text_input):
            self.image = image
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_input = text_input
            self.text = hr_font.render(self.text_input, True, "grey")
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self):
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)


        def checkForInput17(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(16).play(pygame.mixer.Sound('Button Sound.wav'))
                horseracing()

        def checkForInput18(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(17).play(pygame.mixer.Sound('Button Sound.wav')) #need to do
                horseracing_career()

        def checkForInput20(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(17).play(pygame.mixer.Sound('Button Sound.wav')) #need to do
                horseracing_rules()
                

        def checkForInput19(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                pygame.mixer.Channel(18).play(pygame.mixer.Sound('Button Sound.wav'))
                pick_your_game()
                

        

        def changeColor(self, position):
                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        self.text = hr_font.render(self.text_input, True, "green")
                else:
                        self.text = hr_font.render(self.text_input, True, "black")


    buttonenter_hr_play_surface= pygame.image.load("HORSE RACING 1.PNG")
    buttonenter_hr_surface_play = pygame.transform.scale(buttonenter_hr_play_surface, (60, 60))

    buttonenter_hr_play = Button(buttonenter_hr_play_surface, 727, 103, "PLAY")

    buttonenter_hr_career_surface = pygame.image.load("HORSE RACING 1.PNG")
    buttonenter_hr_career_surface = pygame.transform.scale(buttonenter_hr_career_surface, (90, 40)) #change size

    buttonenter_hr_career = Button(buttonenter_hr_career_surface, 727, 173, "CAREER")

    buttonenter_hr_rules_surface = pygame.image.load("HORSE RACING 1.PNG")
    buttonenter_hr_rules_surface = pygame.transform.scale(buttonenter_hr_rules_surface, (90, 30)) #change size

    buttonenter_hr_rules = Button(buttonenter_hr_rules_surface, 727, 238, "RULES")

    buttonenter_hr_exit_surface = pygame.image.load("HORSE RACING 1.PNG")
    buttonenter_hr_exit_surface = pygame.transform.scale(buttonenter_hr_exit_surface, (10, 10))

    buttonenter_hr_exit = Button(buttonenter_hr_exit_surface, 727, 300, "EXIT")


    hr_screen.blit(hr_screen_background,(0,0))

    buttonenter_hr_play.update()
    buttonenter_hr_career.update()
    buttonenter_hr_rules.update()
    buttonenter_hr_exit.update()
    

    pygame.display.update()

    while True: #a loop that makes the screen run forever
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit() #opposite of pygame.init()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttonenter_hr_play.checkForInput17(pygame.mouse.get_pos())
                    buttonenter_hr_career.checkForInput18(pygame.mouse.get_pos())
                    buttonenter_hr_rules.checkForInput20(pygame.mouse.get_pos())
                    buttonenter_hr_exit.checkForInput19(pygame.mouse.get_pos())

        buttonenter_hr_play.changeColor(pygame.mouse.get_pos())
        buttonenter_hr_play.update()

        buttonenter_hr_career.changeColor(pygame.mouse.get_pos())
        buttonenter_hr_career.update()

        buttonenter_hr_rules.changeColor(pygame.mouse.get_pos())
        buttonenter_hr_rules.update()

        buttonenter_hr_exit.changeColor(pygame.mouse.get_pos())
        buttonenter_hr_exit.update()

        pygame.display.update()

        
def horseracing_rules():
        pygame.display.set_caption("Jack of Hearts - Learning the Rules of Horse Racing")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        hrr_screen = pygame.display.set_mode((1310, 700))
        hrr_font = pygame.font.SysFont("cambria", 30)
        hrr_numbers_font = pygame.font.SysFont("cambria", 70)
        hrr_bet_font = pygame.font.SysFont("cambria", 80)
        hrr_chips_font = pygame.font.SysFont("cambria", 30)
        clock = pygame.time.Clock()
        hrr_screen_background = pygame.image.load("horse racing rules.png")
        hrr_screen.blit(hrr_screen_background, (0,0))

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()

                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        horseracing_menu()

                pygame.display.update()



def horseracing_betting_menu():
        pygame.display.set_caption("Jack of Hearts - Betting on a Horse")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        hrb_screen = pygame.display.set_mode((1530, 800))
        hrb_font = pygame.font.SysFont("cambria", 30)
        hrb_numbers_font = pygame.font.SysFont("cambria", 70)
        hrb_bet_font = pygame.font.SysFont("cambria", 80)
        hrb_chips_font = pygame.font.SysFont("cambria", 30)
        clock = pygame.time.Clock()
        hrb_screen_background = pygame.image.load("horse racing betting background main.PNG")
        hrb_screen.blit(hrb_screen_background, (0,0))

        
        chip_text_hrb = hrb_font.render(f' Current Chips = {chips[0]}', True, 'white')
        hrb_screen.blit(chip_text_hrb, (1090, 265))
        
        

        

        
        

        

        mixer.music.load('robbery-of-the-century-152126.mp3')
        pygame.mixer.music.play(loops=-1)
        mixer.music.set_volume(0.1)

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = hrb_font.render(self.text_input, True, "grey")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputHRBACK(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(52).play(pygame.mixer.Sound('Button Sound.wav'))
                        horseracing_menu()

                def checkForInputHRPLACEBETS(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(53).play(pygame.mixer.Sound('Button Sound.wav'))
                        horseracing()
                        

                def checkForInputHR2000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(54).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                        chips[1] = 2000
                        chips[0] = chips[0] - chips[1]
                        
                        
                        

                def checkForInputHR4000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(55).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                        chips[1] = 4000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputHR6000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(56).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                        chips[1] = 6000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputHR8000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(57).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                        chips[1] = 8000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputHR10000(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(58).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                        chips[1] = 10000
                        chips[0] = chips[0] - chips[1]
                        

                def checkForInputHRALL(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(59).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                        chips[1] = chips[0]
                        chips[0] = chips[0] - chips[1]
                        

                def changeColorBig(self, position):
                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                self.text = hrb_bet_font.render(self.text_input, True, "green")
                        else:
                                self.text = hrb_bet_font.render(self.text_input, True, "black")

                def changeColorSmall(self, position):
                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                self.text = hrb_font.render(self.text_input, True, "green")
                        else:
                                self.text = hrb_font.render(self.text_input, True, "white")

                def changeColorNumbers(self, position):
                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                self.text = hrb_numbers_font.render(self.text_input, True, "green")
                        else:
                                self.text = hrb_numbers_font.render(self.text_input, True, "white")




        buttonenter_hrb_back_surface= pygame.image.load("purple arrow.PNG")
        buttonenter_hrb_back_surface = pygame.transform.scale(buttonenter_hrb_back_surface, (100, 60))

        buttonenter_hrb_back = Button(buttonenter_hrb_back_surface, 70, 750, "")

        buttonenter_hrb_bets_surface= pygame.image.load("bets background 1.PNG")
        buttonenter_hrb_bets_surface = pygame.transform.scale(buttonenter_hrb_bets_surface, (170, 30))

        buttonenter_hrb_bets = Button(buttonenter_hrb_bets_surface, 1130, 600, "PLACE BETS")

        buttonenter_hrb_2000_surface= pygame.image.load("currency background.PNG")
        buttonenter_hrb_2000_surface = pygame.transform.scale(buttonenter_hrb_2000_surface, (170, 30))

        buttonenter_hrb_2000 = Button(buttonenter_hrb_2000_surface, 1080, 320, "2000")

        buttonenter_hrb_4000_surface= pygame.image.load("currency background.PNG")
        buttonenter_hrb_4000_surface = pygame.transform.scale(buttonenter_hrb_4000_surface, (170, 30))

        buttonenter_hrb_4000 = Button(buttonenter_hrb_4000_surface, 1080, 420, "4000")

        buttonenter_hrb_6000_surface= pygame.image.load("currency background.PNG")
        buttonenter_hrb_6000_surface = pygame.transform.scale(buttonenter_hrb_6000_surface, (170, 30))

        buttonenter_hrb_6000 = Button(buttonenter_hrb_6000_surface, 1080, 520, "6000")

        buttonenter_hrb_8000_surface= pygame.image.load("BACKGROUND 2.PNG")
        buttonenter_hrb_8000_surface = pygame.transform.scale(buttonenter_hrb_8000_surface, (170, 30))

        buttonenter_hrb_8000 = Button(buttonenter_hrb_8000_surface, 1300, 320, "8000")

        buttonenter_hrb_10000_surface= pygame.image.load("currency background.PNG")
        buttonenter_hrb_10000_surface = pygame.transform.scale(buttonenter_hrb_10000_surface, (170, 30))

        buttonenter_hrb_10000 = Button(buttonenter_hrb_10000_surface, 1300, 420, "10000")

        buttonenter_hrb_ALL_surface= pygame.image.load("currency background.PNG")
        buttonenter_hrb_ALL_surface = pygame.transform.scale(buttonenter_hrb_ALL_surface, (170, 30))

        buttonenter_hrb_ALL = Button(buttonenter_hrb_ALL_surface, 1300, 520, "ALL")

        buttonenter_hrb_back.update()
        buttonenter_hrb_bets.update()
        buttonenter_hrb_2000.update()
        buttonenter_hrb_4000.update()
        buttonenter_hrb_6000.update()
        buttonenter_hrb_8000.update()
        buttonenter_hrb_10000.update()
        buttonenter_hrb_ALL.update()

        

        
        

        

        

        pygame.display.update()

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                buttonenter_hrb_back.checkForInputHRBACK(pygame.mouse.get_pos())
                                buttonenter_hrb_bets.checkForInputHRPLACEBETS(pygame.mouse.get_pos())
                                buttonenter_hrb_2000.checkForInputHR2000(pygame.mouse.get_pos())
                                buttonenter_hrb_4000.checkForInputHR4000(pygame.mouse.get_pos())
                                buttonenter_hrb_6000.checkForInputHR6000(pygame.mouse.get_pos())
                                buttonenter_hrb_8000.checkForInputHR8000(pygame.mouse.get_pos())
                                buttonenter_hrb_10000.checkForInputHR10000(pygame.mouse.get_pos())
                                buttonenter_hrb_ALL.checkForInputHRALL(pygame.mouse.get_pos())

                buttonenter_hrb_back.update()

                buttonenter_hrb_bets.changeColorBig(pygame.mouse.get_pos())
                buttonenter_hrb_bets.update()

                buttonenter_hrb_2000.changeColorNumbers(pygame.mouse.get_pos())
                buttonenter_hrb_2000.update()

                buttonenter_hrb_4000.changeColorNumbers(pygame.mouse.get_pos())
                buttonenter_hrb_4000.update()

                buttonenter_hrb_6000.changeColorNumbers(pygame.mouse.get_pos())
                buttonenter_hrb_6000.update()

                buttonenter_hrb_8000.changeColorNumbers(pygame.mouse.get_pos())
                buttonenter_hrb_8000.update()

                buttonenter_hrb_10000.changeColorNumbers(pygame.mouse.get_pos())
                buttonenter_hrb_10000.update()

                buttonenter_hrb_ALL.changeColorNumbers(pygame.mouse.get_pos())
                buttonenter_hrb_ALL.update()

                
                
                

                pygame.display.update()

        


        
        
                            
                            

                

##        def horse1_timer():
##                horse1counter = 1
##                pygame.time.set_timer(pygame.USEREVENT, 1000)
##                while True: #a loop that makes the screen run forever
##                        for event in pygame.event.get():
##                                if event.type == pygame.QUIT:
##                                        pygame.quit() #opposite of pygame.init()
##                                        sys.exit()
##                                if event.type == pygame.USEREVENT:
##                                    horse1counter -= 1
##                                    if horse1counter == 0:
##                                        horse1()
                











                

        

def horseracing():
        SCREEN_WIDTH = 1400
        SCREEN_HEIGHT = 800

        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Jack of Hearts - Watching the Horses Race")
        clock = pygame.time.Clock()

        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)

        pygame.mixer.music.load('call-to-post-34068.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        
        

        #Loading Icon
        #icon = pygame.image.load('E:/A Level Computer Science/Programming Project/Horse Racing/icon.jpg')
        #pygame.display.set_icon(icon)

        #Loading Fonts
        font = pygame.font.SysFont('cambria', 40)
        info_font = pygame.font.SysFont('cambria', 35)
        horse_name_font = pygame.font.SysFont('cambria', 30)

        #Loading Images for Background
        bg_images = []

        bg_image_start = pygame.image.load('background main]#.jpg').convert_alpha()
        
        
                
        
        bg_images.append(bg_image_start)

        for i in range (4):
            bg_image_mid = pygame.image.load('background main]#.jpg').convert_alpha()
            bg_images.append(bg_image_mid)
            bg_width = bg_images[i].get_width()

        bg_image_finish = pygame.image.load('finish line main.PNG').convert_alpha()
        bg_images.append(bg_image_finish)

        #Horse Image List
        horse_image_list = ['horse1.png', 'horse2.png', 'horse3.png', 'horse4.png']
        horse_icon_list = ['horse1.png', 'horse2.png', 'horse3.png', 'horse4.png']

        class Horse():
            def __init__(self, horse_image, position_y, colour, name):
                self.postion_x = 0
                self.image = pygame.image.load(horse_image).convert_alpha()
                self.speed = ((1,4))
                self.colour = colour
                self.name = name
                self.rect = self.image.get_rect(midbottom = (self.postion_x, position_y))
                self.movement_count = 0

            def draw(self):
                screen.blit(self.image, self.rect)

            def move_forward(self, range_1, range_2):
                self.rect.x += random.randrange(range_1, range_2)
                self.movement_count += 1


#Creating horse objects of Class Horse

        horse1 = Horse(horse_image_list[0], 340, "orange", "Lonely Stepbrother") 
        horse2 = Horse(horse_image_list[1], 450, "grey", "Snatched Your Mama")
        horse3 = Horse(horse_image_list[2], 575, "blue", "Hard Time Done")
        horse4 = Horse(horse_image_list[3], 720, "green", "Mister Redacted")

        def displayEarnings():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('earnings.txt') as f:
                    current_earnings = f.readline()

                #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                #screen.blit(total_earnings, (870,80))

            except:
                #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                #screen.blit(total_earnings, (870,30))

                with open('earnings.txt', 'w') as f:
                    f.write(str(1))


        def displayEarnings2():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('earnings2.txt') as f:
                    current_earnings = f.readline()

                #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                #screen.blit(total_earnings, (870,80))

            except:
                #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                #screen.blit(total_earnings, (870,30))

                with open('earnings2.txt', 'w') as f:
                    f.write(str(1))
    
        def decreaseEarnings():

            #Decreasing amount of game money using text file methods

            with open('earnings.txt') as f:
                current_earnings = f.readline()
                current_earnings = int(current_earnings)

            if current_earnings > 50:
                with open('earnings.txt', 'w') as f:
                    new_earnings = int(current_earnings) - 1
                    f.write(str(new_earnings))

        def increaseEarnings():
                

            #Increasing amount of game money using text file methods

             with open('earnings.txt') as f:
                current_earnings = f.readline()
                current_earnings = int(current_earnings)

             if current_earnings > 0 and current_earnings < 100000:

                with open('earnings.txt', 'w') as f:
                    global new_earnings
                    new_earnings = int(current_earnings) + 1
                    f.write(str(new_earnings))

        def increaseEarnings2():
                

            #Increasing amount of game money using text file methods

             with open('earnings2.txt') as f:
                current_earnings = f.readline()
                current_earnings = int(current_earnings)

             if current_earnings > 0 and current_earnings < 100000:

                with open('earnings2.txt', 'w') as f:
                    global new_earnings
                    new_earnings = int(current_earnings) + 1
                    f.write(str(new_earnings))

        

        #def displayDistanceLeft():
            #display_distance = info_font.render('Metres left: ' + str(610 - selected_horse.movement_count), False , "white")
            #screen.blit(display_distance, (1000,27.5))

        def playMusic():
            if music_playing:
                pygame.mixer.music.load('wii-wiisports-titlescreen (1).wav')
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)

        def drawBg():
            for x in range (6):
                screen.blit(bg_images[x], ((x * bg_width) - scroll, 0))

        def grabResults():

            #Setting position of horses and storing into dictionary with relevant names

            results_dict = {}

            orange_horse = horse1.rect.x
            black_horse = horse2.rect.x
            blue_horse = horse3.rect.x
            green_horse = horse4.rect.x

            results_dict["Lonely Stepbrother"] = orange_horse
            results_dict["Snatched Your Mama"] = black_horse
            results_dict["Hard Time Done"] = blue_horse
            results_dict["Mister Redacted"] = green_horse

            sortedDict = sorted(results_dict.items(), key=lambda x:x[1], reverse=True)

            return sortedDict

        def checkWinner():

            #Conditional statements to check which horse is in first place during the race

            if horse1.rect.x > horse2.rect.x and horse1.rect.x > horse3.rect.x and horse1.rect.x > horse4.rect.x:
                return "Orange"

            elif horse2.rect.x > horse1.rect.x and horse2.rect.x > horse3.rect.x and horse2.rect.x > horse4.rect.x:
                return "Grey"

            elif horse3.rect.x > horse1.rect.x and horse3.rect.x  > horse2.rect.x and horse3.rect.x > horse4.rect.x:
                return "Blue"

            elif horse4.rect.x > horse1.rect.x and horse4.rect.x > horse2.rect.x and horse4.rect.x > horse3.rect.x:
                return "Green"

            else:
                return "White"

        def displayResults():

            sortedDict = grabResults()

            pygame.mixer.music.load('wii-wiisports-titlescreen (1).wav')
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)

            text = font.render('Results:' , False , "grey")
            screen.blit(text, (300,250))

            if selected_horse.name == sortedDict[0][0]:
                text2 = font.render('1st Place (Winner): ' + str(sortedDict[0][0]), False , "green")
                screen.blit(text2, (300,300))
                pygame.mixer.Channel(64).play(pygame.mixer.Sound('claps and appluases.wav'))
                if selected_horse == horse1:
                        chips[2] = chips[1] * 3
                        chips[0] = chips[0] + chips[2]
                elif selected_horse == horse2:
                        chips[2] = chips[1] * 2
                        chips[0] = chips[0] + chips[2]
                elif selected_horse == horse3:
                        chips[2] = chips[1] * 18
                        chips[0] = chips[0] + chips[2]
                elif selected_horse == horse4:
                        chips[2] = chips[1] * 19
                        chips[0] = chips[0] + chips[2]
                        

            else:
                text_winner = font.render('1st Place (Winner): ' + str(sortedDict[0][0]), False , "yellow")
                screen.blit(text_winner, (300,300))
                pygame.mixer.Channel(65).play(pygame.mixer.Sound('boo-36556.mp3'))
                if chips[0] <= 0:
                        bust_screen()

            text3 = font.render('2nd Place: ' + str(sortedDict[1][0]), False , "white")
            screen.blit(text3, (300,350))

            text4 = font.render('3rd Place: ' + str(sortedDict[2][0]) , False , "white")
            screen.blit(text4, (300,400))

            text5 = font.render('4th Place: ' + str(sortedDict[3][0]) , False , "white")
            screen.blit(text5, (300,450))

            

            if selected_horse.name == sortedDict[0][0]:
                text6= horse_name_font.render('Bet won with: ' + selected_horse.name + " and earned: " + str(chips[2]), False , "green")
                screen.blit(text6, (300,600))
                increaseEarnings()

            else:
                text7= horse_name_font.render('Your have lost your bet with: ' + selected_horse.name , False , "red")
                screen.blit(text7, (300,600))
                increaseEarnings2()

#Initalising Variables
        game_active = True
        start_check = False
        music_playing = True
        scroll = 0

        while True:

            for event in pygame.event.get():
                global selected_horse
                if event.type == pygame.QUIT: sys.exit() 
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1 and start_check == False:
                    start_check = True
                    selected_horse = horse1
                    play_music_game()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and start_check == False:
                    start_check = True
                    selected_horse = horse2
                    play_music_game()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_3 and start_check == False:
                    start_check = True
                    selected_horse = horse3
                    play_music_game()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_4 and start_check == False:
                    start_check = True
                    selected_horse = horse4
                    play_music_game()

                if event.type == MOUSEBUTTONDOWN:
                    if horse1_rect.collidepoint(event.pos):
                        start_check = True
                        selected_horse = horse1
                        play_music_game()

                    if horse2_rect.collidepoint(event.pos):
                        start_check = True
                        selected_horse = horse2
                        play_music_game()

                    if horse3_rect.collidepoint(event.pos):
                        start_check = True
                        selected_horse = horse3
                        play_music_game()

                    if horse4_rect.collidepoint(event.pos):
                        start_check = True
                        selected_horse = horse4
                        play_music_game()

                #Event check to pause and unpause game music
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:

                    if music_playing == True:
                        music_playing = False
                        pygame.mixer.music.pause()

                    else:
                        pygame.mixer.music.unpause()
                        music_playing = True
             
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_active == False:
                    
                    #Resetting Variables for Game Restart
                    horse1.movement_count = 0
                    horse2.movement_count = 0
                    horse3.movement_count = 0
                    horse4.movement_count = 0
                    horse1.rect.x = 0
                    horse2.rect.x = 0
                    horse3.rect.x = 0
                    horse4.rect.x = 0
                    scroll = 0
                    game_active = True

                if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                horseracing_menu()

            if game_active: 
                
                bg_image = pygame.image.load('background main]#.jpg').convert_alpha()
                
                screen.blit(bg_image, (0,0))

                #Grabbing total earnings and outputting to horse selection screen
                displayEarnings()
                displayEarnings2()
                

                if start_check:
                    
                    #Displaying moving background function with multiple images
                    drawBg()

                    #info_bar_image = pygame.image.load('D:/A Level Computer Science/Programming Project/Practice/Loading Bar Background (2).png').convert_alpha()
                    #screen.blit(info_bar_image, (0,0))
                    
                    horse4.draw(), horse3.draw(), horse2.draw(), horse1.draw()

                    winner = checkWinner()

                    default_range = ((1, 4))

                    #Calling Horse class move_forward function to start the race

                    horse1.move_forward(default_range[0], default_range[1]), horse2.move_forward(default_range[0], default_range[1])
                    horse3.move_forward(default_range[0], default_range[1]), horse4.move_forward(default_range[0], default_range[1])

                    scroll += 12 #Incrementing scroll variable by 12 for moving background function

                    #displayDistanceLeft() # Calling function to display metres left in horse race

                    #Ending game if each horse has finished the race and calling the subsequent functions
                    if horse1.movement_count == 610 and horse2.movement_count == 610 and horse3.movement_count == 610 and horse4.movement_count == 610:
                        game_active = False
                        start_check = False
                        #results_board_image = pygame.image.load('E:/A Level Computer Science/Programming Project/Horse Racing/results table.jpg').convert_alpha()
                        #screen.blit(results_board_image, (185,80))
                        displayResults()
                        grabResults()   

                    trophy_image = pygame.image.load('trophy main.PNG').convert_alpha()
                    bg_heading_image = pygame.image.load('black heading.PNG').convert_alpha()
                    display_distance = info_font.render('Metres left: ' + str(610 - selected_horse.movement_count), False , "white")
                    chip_text_hrb = font.render(f' {chips[0]}', True, 'white')
                    chip_image = pygame.image.load('New Project (1).png')
        

                    

                    

                    
                    screen.blit(bg_heading_image, (0,0))
                    screen.blit(display_distance, (900,27.5))
                    screen.blit(trophy_image, (0,0))
                    screen.blit(chip_text_hrb, (1245, 27.5))
                    screen.blit(chip_image, (1205, 27.5))
                    
                    
                    winner_text = info_font.render('1st Place: ', False , "grey")
                    screen.blit(winner_text, (80,27.5))

                    winner_text_colour = info_font.render(str(winner), False , str(winner))
                    screen.blit(winner_text_colour, (230,27.5))

                    current_horse_text = horse_name_font.render('Chosen Horse:', False , "grey")
                    screen.blit(current_horse_text, (390,29))

                    current_horse_colour = horse_name_font.render(selected_horse.name, False , str(selected_horse.colour))
                    screen.blit(current_horse_colour, (590,29))

                else:
                    horse_white_image = pygame.image.load('horse racing betting main.PNG').convert_alpha()
                    
                    screen.blit(horse_white_image, (0,0))

                    horse1_icon = pygame.image.load(horse_icon_list[0]).convert_alpha()
                    horse1_rect = horse1_icon.get_rect(midbottom = (180, 295))
                    screen.blit(horse1_icon, horse1_rect)

                    horse2_icon = pygame.image.load(horse_icon_list[1]).convert_alpha()
                    horse2_rect = horse2_icon.get_rect(midbottom = (180, 410))
                    screen.blit(horse2_icon, horse2_rect)

                    horse3_icon = pygame.image.load(horse_icon_list[2]).convert_alpha()
                    horse3_rect = horse3_icon.get_rect(midbottom = (180, 525))
                    screen.blit(horse3_icon, horse3_rect)

                    horse4_icon = pygame.image.load(horse_icon_list[3]).convert_alpha()
                    horse4_rect = horse4_icon.get_rect(midbottom = (180, 640))
                    screen.blit(horse4_icon, horse4_rect)

                    pygame.display.update()

                    chip_text_hrb = font.render(f' Current Chips = {chips[0]}', True, 'white')
                    screen.blit(chip_text_hrb, (848, 260))

                    placebets = pygame.image.load("PLACE BETS.PNG")
                    screen.blit(placebets, (858, 596))
                    

                    class Button():
                        def __init__(self, image, x_pos, y_pos, text_input):
                            self.image = image
                            self.x_pos = x_pos
                            self.y_pos = y_pos
                            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                            self.text_input = text_input
                            self.text = font.render(self.text_input, True, "grey")
                            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                        def update(self):
                            screen.blit(self.image, self.rect)
                            screen.blit(self.text, self.text_rect)


                        def checkForInputHRBACK(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(52).play(pygame.mixer.Sound('Button Sound.wav'))
                                horseracing_menu()

                        def checkForInputHR2000(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(54).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = 2000
                                chips[0] = chips[0] - chips[1]
                        
                        
                        

                        def checkForInputHR4000(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(55).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = 4000
                                chips[0] = chips[0] - chips[1]
                        

                        def checkForInputHR6000(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(56).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = 6000
                                chips[0] = chips[0] - chips[1]
                                

                        def checkForInputHR8000(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(57).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = 8000
                                chips[0] = chips[0] - chips[1]
                                

                        def checkForInputHR10000(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(58).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = 10000
                                chips[0] = chips[0] - chips[1]
                                

                        def checkForInputHRALL(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(59).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = chips[0]
                                chips[0] = chips[0] - chips[1]
                                

                        def changeColorBig(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = font.render(self.text_input, True, "green")
                                else:
                                        self.text = font.render(self.text_input, True, "black")

                        def changeColorSmall(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = font.render(self.text_input, True, "green")
                                else:
                                        self.text = font.render(self.text_input, True, "white")

                        def changeColorNumbers(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = font.render(self.text_input, True, "green")
                                else:
                                        self.text = font.render(self.text_input, True, "white")




        

                        def changeColorBig(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = font.render(self.text_input, True, "green")
                                else:
                                        self.text = font.render(self.text_input, True, "black")

                    buttonenter_hrb_back_surface= pygame.image.load("purple arrow.PNG")
                    buttonenter_hrb_back_surface = pygame.transform.scale(buttonenter_hrb_back_surface, (100, 60))

                    buttonenter_hrb_back = Button(buttonenter_hrb_back_surface, 70, 750, "")

                    buttonenter_hrb_2000_surface= pygame.image.load("currency background.PNG")
                    buttonenter_hrb_2000_surface = pygame.transform.scale(buttonenter_hrb_2000_surface, (170, 30))

                    buttonenter_hrb_2000 = Button(buttonenter_hrb_2000_surface, 930, 350, "2000")

                    buttonenter_hrb_4000_surface= pygame.image.load("currency background.PNG")
                    buttonenter_hrb_4000_surface = pygame.transform.scale(buttonenter_hrb_4000_surface, (170, 30))

                    buttonenter_hrb_4000 = Button(buttonenter_hrb_4000_surface, 930, 440, "4000")

                    buttonenter_hrb_6000_surface= pygame.image.load("currency background.PNG")
                    buttonenter_hrb_6000_surface = pygame.transform.scale(buttonenter_hrb_6000_surface, (170, 30))

                    buttonenter_hrb_6000 = Button(buttonenter_hrb_6000_surface, 930, 520, "6000")

                    buttonenter_hrb_8000_surface= pygame.image.load("BACKGROUND 2.PNG")
                    buttonenter_hrb_8000_surface = pygame.transform.scale(buttonenter_hrb_8000_surface, (170, 30))

                    buttonenter_hrb_8000 = Button(buttonenter_hrb_8000_surface, 1150, 350, "8000")

                    buttonenter_hrb_10000_surface= pygame.image.load("currency background.PNG")
                    buttonenter_hrb_10000_surface = pygame.transform.scale(buttonenter_hrb_10000_surface, (170, 30))

                    buttonenter_hrb_10000 = Button(buttonenter_hrb_10000_surface, 1150, 440, "10000")

                    buttonenter_hrb_ALL_surface= pygame.image.load("currency background.PNG")
                    buttonenter_hrb_ALL_surface = pygame.transform.scale(buttonenter_hrb_ALL_surface, (170, 30))

                    buttonenter_hrb_ALL = Button(buttonenter_hrb_ALL_surface, 1150, 520, "ALL")

                    buttonenter_hrb_back.update()
                    buttonenter_hrb_2000.update()
                    buttonenter_hrb_4000.update()
                    buttonenter_hrb_6000.update()
                    buttonenter_hrb_8000.update()
                    buttonenter_hrb_10000.update()
                    buttonenter_hrb_ALL.update()

                    

                    pygame.display.update()

                   #a loop that makes the screen run forever
                    for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                    buttonenter_hrb_back.checkForInputHRBACK(pygame.mouse.get_pos())
                                    buttonenter_hrb_2000.checkForInputHR2000(pygame.mouse.get_pos())
                                    buttonenter_hrb_4000.checkForInputHR4000(pygame.mouse.get_pos())
                                    buttonenter_hrb_6000.checkForInputHR6000(pygame.mouse.get_pos())
                                    buttonenter_hrb_8000.checkForInputHR8000(pygame.mouse.get_pos())
                                    buttonenter_hrb_10000.checkForInputHR10000(pygame.mouse.get_pos())
                                    buttonenter_hrb_ALL.checkForInputHRALL(pygame.mouse.get_pos())


                    buttonenter_hrb_back.update()


                    buttonenter_hrb_2000.changeColorNumbers(pygame.mouse.get_pos())
                    buttonenter_hrb_2000.update()

                    buttonenter_hrb_4000.changeColorNumbers(pygame.mouse.get_pos())
                    buttonenter_hrb_4000.update()

                    buttonenter_hrb_6000.changeColorNumbers(pygame.mouse.get_pos())
                    buttonenter_hrb_6000.update()

                    buttonenter_hrb_8000.changeColorNumbers(pygame.mouse.get_pos())
                    buttonenter_hrb_8000.update()

                    buttonenter_hrb_10000.changeColorNumbers(pygame.mouse.get_pos())
                    buttonenter_hrb_10000.update()

                    buttonenter_hrb_ALL.changeColorNumbers(pygame.mouse.get_pos())
                    buttonenter_hrb_ALL.update()

                    #testhr = pygame.image.load("test hr.png")
                    #screen.blit(testhr,(0,0))
                    

                    

            pygame.display.update()
            clock.tick(60)
        
        






def play_music_game():
        pygame.mixer.music.load('single-horse-galopp-6152.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)


##def displayEarnings():
##
##            #Display earnings on start screen, if file which money is stored doesn't exist then
##                # a file is created.
##
##            try:
##                with open('earnings.txt') as f:
##                    global current_earnings
##                    current_earnings = f.readline()
##
##                #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
##                #screen.blit(total_earnings, (870,80))
##
##            except:
##                #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
##                #screen.blit(total_earnings, (870,30))
##
##                with open('earnings.txt', 'w') as f:
##                    f.write(str(1))


def increaseEarnings():
                

            #Increasing amount of game money using text file methods

             with open('earnings.txt') as f:
                current_earnings = f.readline()
                current_earnings = int(current_earnings)

             if current_earnings > 0 and current_earnings < 100000:

                with open('earnings.txt', 'w') as f:
                    global new_earnings
                    new_earnings = int(current_earnings) + 1
                    f.write(str(new_earnings))


def horseracing_career():
        pygame.display.set_caption("Jack of Hearts - Viewing Career In Horse Racing")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        hrc_screen = pygame.display.set_mode((1230, 790))
        hrc_font = pygame.font.SysFont("cambria", 30)
        hrcs_font = pygame.font.SysFont("cambria", 25)
        clock = pygame.time.Clock()
        hrc_screen_background = pygame.image.load("horse racing career menu.PNG")
        hrc_screen.blit(hrc_screen_background, (0,0))

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = hrc_font.render(self.text_input, True, "grey")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputhrcback(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(16).play(pygame.mixer.Sound('Button Sound.wav'))
                        horseracing_menu()

        buttonenter_hrc_back_surface= pygame.image.load("green arrow.PNG")
        buttonenter_hrc_back_surface = pygame.transform.scale(buttonenter_hrc_back_surface, (100, 60))

        buttonenter_hrc_back = Button(buttonenter_hrc_back_surface, 70, 750, "")

        buttonenter_hrc_back.update()
                        

        def displayEarnings():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('earnings.txt') as f:
                    global current_earnings
                    current_earnings = f.readline()

                total_earnings = hrc_font.render(str(current_earnings), False , "Black")
                hrc_screen.blit(total_earnings, (643,274))

            except:
                total_earnings = hrc_font.render('Total Earnings: $0', False , "Black")
                hrc_screen.blit(total_earnings, (870,30))

                with open('earnings.txt', 'w') as f:
                    f.write(str(1))


        def displayEarnings2():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('earnings2.txt') as f:
                    global current_earnings2
                    current_earnings2 = f.readline()

                total_earnings = hrc_font.render(str(current_earnings2), False , "Black")
                hrc_screen.blit(total_earnings, (664,327))

            except:
                total_earnings2 = hrc_font.render('Total Earnings: $0', False , "Black")
                hrc_screen.blit(total_earnings2, (870,30))

                with open('earnings2.txt', 'w') as f:
                    f.write(str(1))

        displayEarnings()
        displayEarnings2()

        horse = hrcs_font.render("Mister Redacted", False , "Green")
        hrc_screen.blit(horse, (655,527))

        totalgamesH = int(current_earnings)  + int(current_earnings2)

        totalgameszH = hrc_font.render(str(totalgamesH), False, "Black")
        hrc_screen.blit(totalgameszH, (690, 425))

        

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                buttonenter_hrc_back.checkForInputhrcback(pygame.mouse.get_pos())

                buttonenter_hrc_back.update()

                pygame.display.update()
        



        

       
##def loading_screen1():
##    pygame.display.set_caption("Jack of Hearts - Getting Ready To Play BlackJack")
##    ld1_screen = pygame.display.set_mode((1130, 700))
##    ld1_font = pygame.font.SysFont("cambria", 30)
##    clock = pygame.time.Clock()
##    ld1_screen_background = pygame.image.load("D:/A Level Computer Science/Programming Project/Practice/Loading Bar Background.png")
##
##    mixer.music.load('D:/A Level Computer Science/Programming Project/Practice/mixkit-game-level-music-689.wav')
##    pygame.mixer.music.play(loops=-1)
##    mixer.music.set_volume(0.1)
##
##    ld1_screen.blit(ld1_screen_background,(0,0))
##
##    counter = 1
##
##
##
##    pygame.time.set_timer(pygame.USEREVENT, 2000)
##    
##    
##
##    
##    
##    
##    
##            
##    
##
##    pygame.display.update()
##
##    
##
##    while True: #a loop that makes the screen run forever
##        for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                        pygame.quit() #opposite of pygame.init()
##                        sys.exit()
##                if event.type == pygame.USEREVENT:
##                    counter -= 1
##                    if counter == 0:
##                        loading_screen2()
##    
##
##
##def loading_screen2():
##    pygame.display.set_caption("Jack of Hearts - Getting Ready To Play BlackJack")
##    ld2_screen = pygame.display.set_mode((1130, 700))
##    ld2_font = pygame.font.SysFont("cambria", 30)
##    clock = pygame.time.Clock()
##    ld2_screen_background = pygame.image.load("E:/A Level Computer Science/Programming Project/Practice/black loading.PNG")
##
##    
##
##    ld2_screen.blit(ld2_screen_background,(0,0))
##
##    counter = 1
##
##
##
##    pygame.time.set_timer(pygame.USEREVENT, 2000)
##    
##    
##    
##            
##    
##
##    pygame.display.update()
##
##    
##
##    while True: #a loop that makes the screen run forever
##        for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                        pygame.quit() #opposite of pygame.init()
##                        sys.exit()
##                if event.type == pygame.USEREVENT:
##                    counter -= 1
##                    if counter == 0:
##                        loading_screen3()
##
##
##def loading_screen3():
##    pygame.display.set_caption("Jack of Hearts - Getting Ready To Play BlackJack")
##    ld3_screen = pygame.display.set_mode((1130, 700))
##    ld3_font = pygame.font.SysFont("cambria", 30)
##    clock = pygame.time.Clock()
##    ld3_screen_background = pygame.image.load("E:/A Level Computer Science/Programming Project/Practice/black loading 3.PNG")
##
##    
##
##    ld3_screen.blit(ld3_screen_background,(0,0))
##
##    counter = 1
##
##
##
##    pygame.time.set_timer(pygame.USEREVENT, 2000)
##    
##    
##    
##            
##    
##
##    pygame.display.update()
##
##    
##
##    while True: #a loop that makes the screen run forever
##        for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                        pygame.quit() #opposite of pygame.init()
##                        sys.exit()
##                if event.type == pygame.USEREVENT:
##                    counter -= 1
##                    if counter == 0:
##                        loading_screen4()
##
##
##
##
##def loading_screen4():
##    pygame.display.set_caption("Jack of Hearts - Getting Ready To Play BlackJack")
##    ld4_screen = pygame.display.set_mode((1130, 700))
##    ld4_font = pygame.font.SysFont("cambria", 30)
##    clock = pygame.time.Clock()
##    ld4_screen_background = pygame.image.load("E:/A Level Computer Science/Programming Project/Practice/loading screen background.PNG")
##
##    
##
##    ld4_screen.blit(ld4_screen_background,(0,0))
##
##    counter = 1
##
##
##
##    pygame.time.set_timer(pygame.USEREVENT, 2000)
##    
##    
##
##    
##    
##    
##    
##            
##    
##
##    pygame.display.update()
##
##    
##
##    while True: #a loop that makes the screen run forever
##        for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                        pygame.quit() #opposite of pygame.init()
##                        sys.exit()
##                if event.type == pygame.USEREVENT:
##                    counter -= 1
##                    if counter == 0:
##                        loading_screen5()
##
##
##    
##def loading_screen5():
##    pygame.display.set_caption("Jack of Hearts - Getting Ready To Play BlackJack")
##    ld5_screen = pygame.display.set_mode((1130, 700))
##    ld5_font = pygame.font.SysFont("cambria", 30)
##    clock = pygame.time.Clock()
##    ld5_screen_background = pygame.image.load("E:/A Level Computer Science/Programming Project/Practice/loading screen 2.PNG")
##
##    
##
##    ld5_screen.blit(ld5_screen_background,(0,0))
##
##    counter = 1
##
##
##
##    pygame.time.set_timer(pygame.USEREVENT, 2000)
##    
##    
##    
##            
##    
##
##    pygame.display.update()
##
##    
##
##    while True: #a loop that makes the screen run forever
##        for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                        pygame.quit() #opposite of pygame.init()
##                        sys.exit()
##                if event.type == pygame.USEREVENT:
##                    counter -= 1
##                    if counter == 0:
##                        loading_screen6()
##
##def loading_screen6():
##    pygame.display.set_caption("Jack of Hearts - Getting Ready To Play BlackJack")
##    ld6_screen = pygame.display.set_mode((1130, 700))
##    ld6_font = pygame.font.SysFont("cambria", 30)
##    clock = pygame.time.Clock()
##    ld6_screen_background = pygame.image.load("E:/A Level Computer Science/Programming Project/Practice/loading screen 3.PNG")
##
##    
##
##    ld6_screen.blit(ld6_screen_background,(0,0))
##
##    counter = 1
##
##
##
##    pygame.time.set_timer(pygame.USEREVENT, 2000)
##    
##    
##    
##            
##    
##
##    pygame.display.update()
##
##    
##
##    while True: #a loop that makes the screen run forever
##        for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                        pygame.quit() #opposite of pygame.init()
##                        sys.exit()
##                if event.type == pygame.USEREVENT:
##                    counter -= 1
##                    #if counter == 0:
##                        #loading_screen3()


def poker_menu():
        pygame.display.set_caption("Jack of Hearts - In the Poker Menu")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        poker_screen = pygame.display.set_mode((1323, 846))
        poker_font = pygame.font.SysFont("Franklin Gothic Heavy", 30)
        clock = pygame.time.Clock()
        poker_screen_background = pygame.image.load("three card poker menu.PNG")
        poker_screen.blit(poker_screen_background, (0,0))

        mixer.music.load('poker-face-206398.mp3')
        pygame.mixer.music.play(loops=-1)
        mixer.music.set_volume(0.1)

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = poker_font.render(self.text_input, True, "grey")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputpokerplay(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(16).play(pygame.mixer.Sound('Button Sound.wav'))
                        poker()
                        

                def checkForInputpokercareer(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(17).play(pygame.mixer.Sound('Button Sound.wav')) #need to do
                        poker_career()
                        

                def checkForInputpokerrules(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(18).play(pygame.mixer.Sound('Button Sound.wav'))
                        poker_rules()
                        

                def checkForInputexit(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(18).play(pygame.mixer.Sound('Button Sound.wav'))
                        pick_your_game()
                        

                

                def changeColor(self, position):
                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                self.text = poker_font.render(self.text_input, True, "green")
                        else:
                                self.text = poker_font.render(self.text_input, True, "black")

        buttonenter_poker_play_surface= pygame.image.load("poker button background.PNG")
        buttonenter_poker_play_surface = pygame.transform.scale(buttonenter_poker_play_surface, (250, 60))

        buttonenter_poker_play = Button(buttonenter_poker_play_surface, 658, 435, "PLAY")

        buttonenter_poker_career_surface= pygame.image.load("poker button background.PNG")
        buttonenter_poker_career_surface = pygame.transform.scale(buttonenter_poker_career_surface, (250, 60))

        buttonenter_poker_career = Button(buttonenter_poker_career_surface, 658, 553, "CAREER")

        buttonenter_poker_rules_surface= pygame.image.load("poker button background.PNG")
        buttonenter_poker_rules_surface = pygame.transform.scale(buttonenter_poker_rules_surface, (250, 60))

        buttonenter_poker_rules = Button(buttonenter_poker_rules_surface, 658, 671, "RULES")


        buttonenter_poker_back_surface= pygame.image.load("poker button background.PNG")
        buttonenter_poker_back_surface = pygame.transform.scale(buttonenter_poker_back_surface, (250, 60))

        buttonenter_poker_back = Button(buttonenter_poker_back_surface, 658, 793, "EXIT")

        buttonenter_poker_play.update()
        buttonenter_poker_career.update()
        buttonenter_poker_rules.update()
        buttonenter_poker_back.update()



        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                 buttonenter_poker_play.checkForInputpokerplay(pygame.mouse.get_pos())
                                 buttonenter_poker_career.checkForInputpokercareer(pygame.mouse.get_pos())
                                 buttonenter_poker_rules.checkForInputpokerrules(pygame.mouse.get_pos())
                                 buttonenter_poker_back.checkForInputexit(pygame.mouse.get_pos())



                buttonenter_poker_play.changeColor(pygame.mouse.get_pos())
                buttonenter_poker_play.update()

                buttonenter_poker_career.changeColor(pygame.mouse.get_pos())
                buttonenter_poker_career.update()

                buttonenter_poker_rules.changeColor(pygame.mouse.get_pos())
                buttonenter_poker_rules.update()

                buttonenter_poker_back.changeColor(pygame.mouse.get_pos())
                buttonenter_poker_back.update()

                pygame.display.update()


def poker_rules():
        pygame.display.set_caption("Jack of Hearts - Learning the Rules of Poker")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        pokerR_screen = pygame.display.set_mode((1323, 746))
        pokerR_font = pygame.font.SysFont("Franklin Gothic Heavy", 30)
        clock = pygame.time.Clock()
        pokerR_screen_background = pygame.image.load("poker rules screen.PNG")
        pokerR_screen.blit(pokerR_screen_background, (0,0))

        pygame.display.update()

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        poker_menu()

def poker_career():
        pygame.display.set_caption("Jack of Hearts - Viewing Career in Poker")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        pokerC_screen = pygame.display.set_mode((1107, 736))
        pokerC_font = pygame.font.SysFont("Franklin Gothic Heavy", 30)
        clock = pygame.time.Clock()
        pokerC_screen_background = pygame.image.load("poker career menu.PNG")
        pokerC_screen.blit(pokerC_screen_background, (0,0))

        def displayPokerWins():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('PokerWINS.txt') as f:
                    global current_Pokerwins
                    current_Pokerwins = f.readline()

                total_Pokerwins = pokerC_font.render(str(current_Pokerwins), False , "Black")
                pokerC_screen.blit(total_Pokerwins, (365,200))

            except:
                total_Pokerwins = pokerC_font.render('Total Earnings: $0', False , "Black")
                pokerC_screen.blit(total_Pokerwins, (870,30))

                with open('PokerWins.txt', 'w') as f:
                    f.write(str(1))


    

        def displayPokerLosses():

                    #Display earnings on start screen, if file which money is stored doesn't exist then
                        # a file is created.

            try:
                with open('PokerLOSSES.txt') as f:
                    global current_Pokerlosses
                    current_Pokerlosses = f.readline()

                total_Pokerlosses = pokerC_font.render(str(current_Pokerlosses), False , "Black")
                pokerC_screen.blit(total_Pokerlosses, (399,298))

            except:
                total_Pokerlosses = pokerC_font.render('Total Earnings: $0', False , "Black")
                pokerC_screen.blit(total_Pokerlosses, (870,30))

                with open('PokerLOSSES.txt', 'w') as f:
                    f.write(str(1))

        def displayPokerFOLDS():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('PokerFOLDS.txt') as f:
                    global current_PokerFOLDS
                    current_PokerFOLDS = f.readline()

                total_PokerFOLDS = pokerC_font.render(str(current_PokerFOLDS), False , "Black")
                pokerC_screen.blit(total_PokerFOLDS, (385,400))

            except:
                total_PokerFOLDS = pokerC_font.render('Total Earnings: $0', False , "Black")
                pokerC_screen.blit(total_PokerFOLDS, (870,30))

                with open('PokerFOLDS.txt', 'w') as f:
                    f.write(str(1))

        displayPokerWins()
        displayPokerLosses()
        displayPokerFOLDS()

        pygame.display.update()

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        poker_menu()
        


def spin_the_wheel():
        turtle.TurtleScreen._RUNNING = True
        turtle.title('Jack of Hearts - Playing Minigames (Spin the Wheel)')
        img = tkinter.Image("photo", file="icon.png")
        turtle._Screen._root.iconphoto(True, img)

        

        wn = turtle.Screen()

        wn.bgcolor("white")

        pygame.mixer.Channel(10).play(pygame.mixer.Sound('wheel of fortune music.mp3'))

        size = 30
        speed = 5 
        timer = 0

        imageone = "test spin wheel main 2.gif"
        #imagetwo = "wheel middle main.gif"


        spoke1 = turtle.Turtle()
        spokecolour = turtle.Turtle()
        player = turtle.Turtle()
        playertwo = turtle.Turtle()
        spokes = [spoke1]
        images = [player]
        #imagestwo = [playertwo]
        spokecolours = [spokecolour]


        wn.addshape(imageone)
        player.shape(imageone)
        player.penup()

        


        _ = 0
        for spoke in spokes:
            spoke.speed(0)
            spoke.shape('square')
            spoke.shapesize(stretch_wid=0.1,stretch_len=30)
            spoke.color("black")
            spoke.left(15*_)
            _ += 1

        for spokecolour in spokecolours:
            spoke.speed(0)
            spoke.shape('arrow')
            spoke.shapesize(stretch_wid=1.5,stretch_len=30)   #arrow, width 1 len 30 square width 30 len 0.1
            spoke.color("black")
            spoke.left(15*_)
            _ += 1

        __ = 0
        for player in images:
            player.speed(0)
            player.left(15*__)
            __ += 1

##        __ = 0
##        for playertwo in imagestwo:
##            playertwo.speed(0)
##            playertwo.left(15*__)
##            __ += 1

        #rim = turtle.Pen()
        #rim.width(70)
        #rim.speed(0)
        #rim.up()
        #rim.forward(size*10)
        #rim.down()
        #rim.left(90)

        #rim.circle(size*10)

        def changespeed():
            speed = 0

##        wn.addshape(imagetwo)
##        playertwo.shape(imagetwo)
##        playertwo.penup()
        

        global timerswheel
        global maintimerwheel

            

        timers = [1830, 1790, 1810, 1768, 1753, 1738, 1715, 1700, 1675, 1659]
        maintimer = random.choice(timers) 
        #print(maintimer)
        #1830 = +50000
        #1790 = +10000
        #1810 = -1000
        #1768 = -500
        #1753 = +20000
        #1738 = +5000
        #1715 = -10000
        #1700 = +500
        #1675 = +15000
        #1659 = -5000
        
        
        
        
        

       

        


        while True:
            for spoke in spokes:
                spoke.left(speed)
                timer = timer + 1
                if timer == maintimer:
                    speed = 3
                if timer == 1900:
                    speed = 2
                if timer == 2050:
                    speed = 1
                if timer == 2200:
                        speed = 0
                        if speed == 0:
                                    sleep(3)
                                    if maintimer == 1830:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] + 50000
                                    elif maintimer == 1790:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] + 10000
                                    elif maintimer == 1810:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] - 1000
                                    elif maintimer == 1768:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] - 500
                                    elif maintimer == 1753:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] + 20000
                                    elif maintimer == 1738:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] + 5000
                                    elif maintimer == 1700:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] + 500
                                    elif maintimer == 1675:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] + 15000
                                    elif maintimer == 1659:
                                            pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                            chips[0] = chips[0] - 5000
                                
                                    turtle.bye()
                                    pick_your_game()
                            
                
               

        while True:
            for player in images:
                player.left(speed)


        #THERE WILL BE A GOLDEN LINE THAT MEANS WHICH EVER THE GOLDEN LINE LANDS ON IS THE OUTCOME
        #EACH OUTCOME WILL HAVE A CORRESPONDING TIMER, ALL TIMERS WILL BE IN AN ARRAY, WHICH THE ODDS CAN BE DETERMINED

        turtle.ontimer(changespeed, t=10)

        turtle.done()


def poker():
        #import PokerModel

        HEIGHT = 720 #settings of the window
        WIDTH = 1280

        mixer.init()

        #Global constants here
        BLACK = (255,255,255) 
        BLACK = (0,0,0)
        GREY  = (50,50,50)
        RED  = (207,0,0)

        mixer.music.load('remembering-paris-212735.mp3') #classical music to capture the theme of Poker
        pygame.mixer.music.play(loops=-1)
        mixer.music.set_volume(0.1)

        ro_font = pygame.font.SysFont("Franklin Gothic Heavy", 40)

        class Control:
                def __init__(self):
                        deck = Deck() #initalising the deck and images
                        self.images = {}
                        self.scale = .5
                        self.cardSize = (WIDTH / 7, WIDTH / 5)
                        self.buffer = 50
                        self.background = pygame.image.load('backgroundpoker.jpg').convert_alpha() #creating the images of the window
                        self.cardBack = pygame.image.load('backmain.png').convert_alpha()
                        self.cardBack = pygame.transform.scale(self.cardBack,(int(self.scale * self.cardSize[0]), int(self.scale * self.cardSize[1]))) #back card


                        font = pygame.font.Font('CoffeeTin.ttf', 50) #text and fonts
                        loadText = font.render("Loading...", 1, BLACK)
                        loadSize = font.size("Loading...")
                        loadLoc = (WIDTH/2 - loadSize[0]/2, HEIGHT/2 - loadSize[1]/2)
                        

                        self.scores = [0,0,0,0] #the array for the 4 players in the game: the player and 3 computers

                        SCREEN.blit(self.background, (-320,-100))

                        SCREEN.blit(loadText, loadLoc)

                        pygame.display.flip()

                        for card in deck:
                                self.images[str(card)] = pygame.image.load(card.image_path).convert_alpha() #loading the cards
                                self.images[str(card)] = pygame.transform.scale(self.images[str(card)], (int(self.scale * self.cardSize[0]), int(self.scale * self.cardSize[1]))) #transforming the cards size

                        self.start_up_init()

                def main(self):
                        if self.state == 0:
                                self.start_up()
                        elif self.state == 1:
                                self.play()
                        elif self.state == 2:
                                self.results()
                        elif self.state == 3:
                                self.new_game()

                def start_up_init(self):
                        #intitialize items for the startup section of the game
                        self.poker = Poker(self.scores)

                        self.font = pygame.font.Font('CoffeeTin.ttf',150)
                        self.font2 = pygame.font.Font('IndianPoker.ttf', 75)
                        self.font2.set_bold(True)

                        self.startText = self.font2.render("Welcome to Poker!", 1, BLACK)
                        self.startSize = self.font2.size("Welcome to Poker!")
                        self.startLoc = (WIDTH/2 - self.startSize[0]/2, self.buffer)

                        self.startButton = self.font.render("  PLAY ", 1, BLACK)
                        self.buttonSize =self.font.size(" Start ")
                        self.buttonLoc = (WIDTH/2 - self.buttonSize[0]/2, HEIGHT/2 - self.buttonSize[1]/2)

                        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
                        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

                        self.state = 0

                def start_up(self):

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit();sys.exit()

                                #when the user clicks the start button, change to the playing state
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                mouseRect = pygame.Rect(event.pos, (1,1))
                                                if mouseRect.colliderect(self.buttonRect):
                                                        self.state += 1
                                                        self.play_init()
                                                        return

                        #draw background
                        SCREEN.blit(self.background, (-320,-100))
                        chip_text = ro_font.render(f' {chips[0]}', True, 'white')
                        SCREEN.blit(chip_text, (1139, 8))
                        chip_image = pygame.image.load('New Project (1).png')
                        SCREEN.blit(chip_image, (1100, 10))

                        #draw welcome text
                        SCREEN.blit(self.startText, self.startLoc)

                        #draw the start button
                        pygame.draw.rect(SCREEN, RED, self.buttonRect)
                        pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
                        SCREEN.blit(self.startButton, self.buttonLoc)

                        pygame.display.flip()

                def play_init(self):
                        #create the new variables
                        self.cardLoc = {}
                        self.round = 0

                        #setup the locations for each card in the hand
                        x = 4.5 * int(self.scale * self.cardSize[0])
                        self.youLoc = (x - 150, self.buffer)

                        for index in range(len(self.poker.playerHand)):
                                self.cardLoc[index] = (x, self.buffer)
                                x += int(self. scale * self.cardSize[0])

                        #setup the text that will be printed to the screen
                        self.font = pygame.font.Font('IndianPoker.ttf', 25)
                        self.font.set_bold(True)
                        self.font2 = pygame.font.Font('CoffeeTin.ttf', 60)
                        self.youText = self.font.render("Your Hand", 1, BLACK)
                        self.youSize = self.font.size("Your Hand")
                        self.youText2 = self.font.render(f' {chips[0]}', True, 'white')
                        self.youSize = self.font.size("Your Hand")

                        

                        self.youLoc = (self.cardLoc[0][0],self.cardLoc[0][1] - 30)#(self.youLoc[0], self.buffer + self.scale * self.cardSize[1]/2 - self.youSize[1]/2)

                        self.replaceButton = self.font2.render(" Replace ", 1, BLACK)
                        self.buttonSize =self.font2.size(" Replace ")

                        

                        self.buttonLoc = (x + 30, self.buffer + self.scale * self.cardSize[1]/2 - self.buttonSize[1]/2)

                        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
                        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

                def play(self):
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit();sys.exit()
                                elif event.type == KEYDOWN:
                                        if event.key == K_ESCAPE:
                                                poker_menu()

                                #when the user clicks on a card, change its color to signify a selection has occurred
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                #create a rectangle for the mouse click and for each card.  check for intersection
                                                mouseRect = pygame.Rect(event.pos, (1,1))
                                                for index in range(len(self.poker.playerHand)):									#this minus thirty fixes a minor bug, do not remove
                                                        cardRect = pygame.Rect(self.cardLoc[index], (int(self.scale * self.cardSize[0]), int(self.scale * self.cardSize[1])))
                                                        if cardRect.colliderect(mouseRect):
                                                                self.poker.playerHand[index].selected = not self.poker.playerHand[index].selected
                                                                break

                                

                                                #check if we clicked the replaceButton
                                                if mouseRect.colliderect(self.buttonRect):
                                                        self.poker.replace(self.poker.playerHand)
                                                        self.poker.computerReplace()
                                                        self.round += 1
                                                        if self.round == 2:
                                                                self.state += 1
                                                                self.results_init()
                                                                return
                                                        

                        #display background	
                        SCREEN.blit(self.background, (-320,-100))

                        #display the player's hand
                        for index in range(len(self.poker.playerHand)):
                                if not self.poker.playerHand[index].selected:
                                        SCREEN.blit(self.images[str(self.poker.playerHand[index])], self.cardLoc[index])
                                else:
                                        SCREEN.blit(self.cardBack, self.cardLoc[index])

                        #display the text
                        SCREEN.blit(self.youText, self.youLoc)
                        pygame.draw.rect(SCREEN, RED, self.buttonRect)
                        pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
                        SCREEN.blit(self.replaceButton, self.buttonLoc)

                        #display the scoreboard
                        self.display_scoreboard()

                        pygame.display.flip()

                def results_init(self):
                        #initialize variables for the button
                        # self.font = pygame.font.Font('font/IndianPoker.ttf', 25)
                        self.replaceButton = self.font2.render(" New Game ", 1, BLACK)
                        self.buttonSize =self.font2.size(" New Game ")

                        self.buttonLoc = (self.buttonLoc[0], self.buffer + self.scale * self.cardSize[1]/2 - self.buttonSize[1]/2)

                        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
                        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

                        #initialize variables for drawing the hands
                        self.comp1Loc = (self.buffer, HEIGHT / 2 - self.scale * self.cardSize[1]/2)
                        self.comp2Loc = (WIDTH - int(5 * self.scale * self.cardSize[0]) - self.buffer, HEIGHT / 2 - self.scale * self.cardSize[1]/2)
                        self.comp3Loc = ( 4.5 * int(self.scale * self.cardSize[0]), HEIGHT - self.scale * self.cardSize[1] - self.buffer)

                        self.result = self.poker.play_round()

                        #initialize variables for labeling the hands
                        playerScore = self.poker.convert_score(self.result[0])
                        self.youText = self.font.render(playerScore, 1, BLACK)
                        self.youSize = self.font.size(playerScore)
                        self.youLoc = (self.cardLoc[0][0],self.cardLoc[0][1] - 30)

                        comp1Score = self.poker.convert_score(self.result[1])
                        self.comp1Label = self.font.render(comp1Score, 1, BLACK)
                        self.comp1LabelSize = self.font.size(comp1Score)
                        self.comp1LabelLoc = (self.comp1Loc[0], self.comp1Loc[1] - 30)

                        comp2Score = self.poker.convert_score(self.result[2])
                        self.comp2Label = self.font.render(comp2Score, 1, BLACK)
                        self.comp2LabelSize = self.font.size(comp2Score)
                        self.comp2LabelLoc = (self.comp2Loc[0], self.comp2Loc[1] - 30)

                        comp3Score = self.poker.convert_score(self.result[3])
                        self.comp3Label = self.font.render(comp3Score, 1, BLACK)
                        self.comp3LabelSize = self.font.size(comp3Score)
                        self.comp3LabelLoc = (self.comp3Loc[0], self.comp3Loc[1] - 30)

                def results(self):
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit();sys.exit()

                                #when the user clicks the start button, change to the playing state
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                mouseRect = pygame.Rect(event.pos, (1,1))
                                                if mouseRect.colliderect(self.buttonRect):
                                                        # self.start_up_init()
                                                        self.state = 1
                                                        self.play_init()
                                                        self.poker = Poker(self.scores)
                                                        return

                        #display background
                        SCREEN.blit(self.background, (-320,-100))

                        #print player hand in the top
                        self.display_hand(self.poker.playerHand, self.cardLoc[0][0], self.cardLoc[0][1])

                        #print computer 1 on the left
                        self.display_hand(self.poker.comp1Hand, self.comp1Loc[0], self.comp1Loc[1])

                        #print computer 2 on the right
                        self.display_hand(self.poker.comp2Hand,self.comp2Loc[0], self.comp2Loc[1])

                        #print computer 3 on the bottom
                        self.display_hand(self.poker.comp3Hand, self.comp3Loc[0], self.comp3Loc[1])

                        #print labels saing what each hand was
                        SCREEN.blit(self.youText, self.youLoc)
                        SCREEN.blit(self.comp1Label, self.comp1LabelLoc)
                        SCREEN.blit(self.comp2Label, self.comp2LabelLoc)
                        SCREEN.blit(self.comp3Label, self.comp3LabelLoc)

                        #display a score screen
                        self.display_scoreboard()

                        #display a play again button
                        

                        

                        pygame.display.flip()

                def display_hand(self, hand, x, y):
                        for card in hand:
                                SCREEN.blit(self.images[str(card)], (x, y))
                                x += int(self.scale * self.cardSize[0])

                def display_scoreboard(self):
                        #create labels for each player
                        self.playerScoreLabel = self.font.render("You: " + str(self.poker.scores[0]), 1, BLACK)
                        self.comp1ScoreLabel = self.font.render("Computer 1: "  +str(self.poker.scores[1]), 1, BLACK)
                        self.comp2ScoreLabel = self.font.render("Computer 2: "  +str(self.poker.scores[2]), 1, BLACK)
                        self.comp3ScoreLabel = self.font.render("Computer 3: "  +str(self.poker.scores[3]), 1, BLACK)

                        SCREEN.blit(self.playerScoreLabel, (10, 10))
                        SCREEN.blit(self.comp1ScoreLabel, (10, 40))
                        SCREEN.blit(self.comp2ScoreLabel, (10, 70))
                        SCREEN.blit(self.comp3ScoreLabel, (10, 100))

                        chip_text = ro_font.render(f' {chips[0]}', True, 'white')
                        SCREEN.blit(chip_text, (1139, 8))
                        chip_image = pygame.image.load('New Project (1).png')
                        SCREEN.blit(chip_image, (1100, 10))

                        pygame.draw.rect(SCREEN, RED, self.buttonRect)
                        pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
                        SCREEN.blit(self.replaceButton, self.buttonLoc)

                        def displayPokerFOLDS():

                                    #Display earnings on start screen, if file which money is stored doesn't exist then
                                        # a file is created.

                                    try:
                                        with open('PokerFOLDS.txt') as f:
                                            current_PokerFOLDS = f.readline()

                                        #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                                        #screen.blit(total_earnings, (870,80))

                                    except:
                                        #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                                        #screen.blit(total_earnings, (870,30))

                                        with open('PokerFOLDS.txt', 'w') as f:
                                            f.write(str(1))

                        def increasePokerFOLDS():
                                        

                                    

                                     with open('PokerFOLDS.txt') as f:
                                        current_PokerFOLDS = f.readline()
                                        current_PokerFOLDS = int(current_PokerFOLDS)

                                     if current_PokerFOLDS > 0 and current_PokerFOLDS < 100000:

                                        with open('PokerFOLDS.txt', 'w') as f:
                                            global new_PokerFOLDS
                                            new_PokerFOLDS = int(current_PokerFOLDS) + 1
                                            f.write(str(new_PokerFOLDS))
                        

                        class Button():
                            def __init__(self, image, x_pos, y_pos, text_input):
                                    self.image = image
                                    self.x_pos = x_pos
                                    self.y_pos = y_pos
                                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                                    self.text_input = text_input
                                    self.text = ro_font.render(self.text_input, True, "white")
                                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                            def update(self):
                                    screen.blit(self.image, self.rect)
                                    screen.blit(self.text, self.text_rect)

                            def checkForInputTest(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-poker-card-flick-2002.wav'))
                                            displayPokerFOLDS()
                                            increasePokerFOLDS()
                                            poker()

                            def checkForInputpoker1000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                            chips[1] = 1000
                                            chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker2000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                            chips[1] = 2000
                                            chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker3000(self, position):
                                     if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                             pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                             chips[1] = 3000
                                             chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker4000(self, position):
                                      if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                              pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                              chips[1] = 4000
                                              chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker5000(self, position):
                                       if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                               pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                               chips[1] = 5000
                                               chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker6000(self, position):
                                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                                chips[1] = 6000
                                                chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker7000(self, position):
                                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                                chips[1] = 7000
                                                chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker8000(self, position):
                                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                                chips[1] = 8000
                                                chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker9000(self, position):
                                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                                chips[1] = 9000
                                                chips[0] = chips[0]  - chips[1]

                            def checkForInputpoker10000(self, position):
                                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                                chips[1] = 10000
                                                chips[0] = chips[0]  - chips[1]

                            def checkForInputpokerALLIN(self, position):
                                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                                chips[1] = chips[0]
                                                chips[0] = chips[0]  - chips[1]

                        
                                            
                                            

            

            
                            
                            
                    
                                    
                            def changeColor(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                            self.text = ro_font.render(self.text_input, True, "green")
                                    else:
                                            self.text = ro_font.render(self.text_input, True, "white")
    
                        button_test_surface = pygame.image.load("button background.png")
                        button_test_surface = pygame.transform.scale(button_test_surface, (120, 60))

                        button_test = Button(button_test_surface, 640, 427, "FOLD")

                        button_poker1000_surface = pygame.image.load("green bass.png")
                        button_poker1000_surface = pygame.transform.scale(button_poker1000_surface, (120, 60))

                        button_poker1000 = Button(button_poker1000_surface, 70, 577, "1000")

                        button_poker2000_surface = pygame.image.load("green bass.png")
                        button_poker2000_surface = pygame.transform.scale(button_poker2000_surface, (120, 60))

                        button_poker2000 = Button(button_poker2000_surface, 200, 577, "2000")

                        button_poker3000_surface = pygame.image.load("green bass.png")
                        button_poker3000_surface = pygame.transform.scale(button_poker3000_surface, (120, 60))

                        button_poker3000 = Button(button_poker3000_surface, 330, 577, "3000")

                        button_poker4000_surface = pygame.image.load("green bass.png")
                        button_poker4000_surface = pygame.transform.scale(button_poker4000_surface, (120, 60))

                        button_poker4000 = Button(button_poker4000_surface, 130, 657, "4000")

                        button_poker5000_surface = pygame.image.load("green bass.png")
                        button_poker5000_surface = pygame.transform.scale(button_poker5000_surface, (120, 60))

                        button_poker5000 = Button(button_poker5000_surface, 270, 657, "5000")

                        button_poker6000_surface = pygame.image.load("green bass.png")
                        button_poker6000_surface = pygame.transform.scale(button_poker6000_surface, (120, 60))

                        button_poker6000 = Button(button_poker6000_surface, 940, 577, "6000")

                        button_poker7000_surface = pygame.image.load("green bass.png")
                        button_poker7000_surface = pygame.transform.scale(button_poker2000_surface, (120, 60))

                        button_poker7000 = Button(button_poker7000_surface, 1070, 577, "7000")

                        button_poker8000_surface = pygame.image.load("green bass.png")
                        button_poker8000_surface = pygame.transform.scale(button_poker8000_surface, (120, 60))

                        button_poker8000 = Button(button_poker8000_surface, 1200, 577, "8000")

                        button_poker9000_surface = pygame.image.load("green bass.png")
                        button_poker9000_surface = pygame.transform.scale(button_poker9000_surface, (120, 60))

                        button_poker9000 = Button(button_poker9000_surface, 1010, 657, "9000")

                        button_poker10000_surface = pygame.image.load("green bass.png")
                        button_poker10000_surface = pygame.transform.scale(button_poker10000_surface, (127, 60))

                        button_poker10000 = Button(button_poker10000_surface, 1150, 657, "10000")

                        button_pokerALLIN_surface = pygame.image.load("green bass.png")
                        button_pokerALLIN_surface = pygame.transform.scale(button_pokerALLIN_surface, (140, 60))

                        button_pokerALLIN = Button(button_pokerALLIN_surface, 640, 327, "ALL IN")

                        button_test.update()
                        button_poker1000.update()
                        button_poker2000.update()
                        button_poker3000.update()
                        button_poker4000.update()
                        button_poker5000.update()
                        button_poker6000.update()
                        button_poker7000.update()
                        button_poker8000.update()
                        button_poker9000.update()
                        button_poker10000.update()
                        button_pokerALLIN.update()



    

    
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        button_test.checkForInputTest(pygame.mouse.get_pos())
                                        button_poker1000.checkForInputpoker1000(pygame.mouse.get_pos())
                                        button_poker2000.checkForInputpoker2000(pygame.mouse.get_pos())
                                        button_poker3000.checkForInputpoker3000(pygame.mouse.get_pos())
                                        button_poker4000.checkForInputpoker4000(pygame.mouse.get_pos())
                                        button_poker5000.checkForInputpoker5000(pygame.mouse.get_pos())
                                        button_poker6000.checkForInputpoker6000(pygame.mouse.get_pos())
                                        button_poker7000.checkForInputpoker7000(pygame.mouse.get_pos())
                                        button_poker8000.checkForInputpoker8000(pygame.mouse.get_pos())
                                        button_poker9000.checkForInputpoker9000(pygame.mouse.get_pos())
                                        button_poker10000.checkForInputpoker10000(pygame.mouse.get_pos())
                                        button_pokerALLIN.checkForInputpokerALLIN(pygame.mouse.get_pos())
                        
                        
                        
                                
                        
##                

        

                        button_test.update()
                        button_test.changeColor(pygame.mouse.get_pos())

                        button_poker1000.update()
                        button_poker1000.changeColor(pygame.mouse.get_pos())

                        button_poker2000.update()
                        button_poker2000.changeColor(pygame.mouse.get_pos())

                        button_poker3000.update()
                        button_poker3000.changeColor(pygame.mouse.get_pos())

                        button_poker4000.update()
                        button_poker4000.changeColor(pygame.mouse.get_pos())

                        button_poker5000.update()
                        button_poker5000.changeColor(pygame.mouse.get_pos())

                        button_poker6000.update()
                        button_poker6000.changeColor(pygame.mouse.get_pos())

                        button_poker7000.update()
                        button_poker7000.changeColor(pygame.mouse.get_pos())

                        button_poker8000.update()
                        button_poker8000.changeColor(pygame.mouse.get_pos())

                        button_poker9000.update()
                        button_poker9000.changeColor(pygame.mouse.get_pos())

                        button_poker10000.update()
                        button_poker10000.changeColor(pygame.mouse.get_pos())

                        button_pokerALLIN.update()
                        button_pokerALLIN.changeColor(pygame.mouse.get_pos())

                        pygame.display.update() #displaying the buttons


        class Card:
                def __init__(self, rank, suit):

                        self.rank = 0
                        self.suit = ''
                        self.image_path = (str(rank) + str(suit) + '.png')
                        self.selected = False

                        #convert the rank to an integer so it's easier to compute the winner of a hand
                        if rank == 'A':
                                self.rank = 14
                        elif rank == 'K':
                                self.rank = 13
                        elif rank == 'Q':
                                self.rank = 12
                        elif rank == 'J':
                                self.rank = 11
                        elif rank == 'T':
                                self.rank = 10
                        else:
                                self.rank = int(rank)

                        self.suit = suit

                def __str__(self):
                        out = ""

                        #convert rank back to a word so it's easier to read
                        if self.rank == 14:
                                out += "Ace"
                        elif self.rank == 13:
                                out += "King"
                        elif self.rank == 12:
                                out += "Queen"
                        elif self.rank == 11:
                                out += "Jack"
                        else:
                                out += str(self.rank)

                        out += ' of '

                        #convert the suit to a word so it's easier to read
                        if self.suit == 'H':
                                out += 'Hearts'
                        elif self.suit == 'S':
                                out += 'Spades'
                        elif self.suit == 'C':
                                out += 'Clubs'
                        else:
                                out += 'Diamonds'

                        return out

        #only exists for the __str__ function
        class Hand:

                def __init__(self, hand):
                        self.hand = hand

                def __str__(self):
                        out = ""
                        for card in self.hand:
                                out += str(card) + ", "
                        return out

                def __getitem__(self, index):
                        return self.hand[index]

                def __len__(self):
                        return len(self.hand)

        class Deck:

                def __init__(self):
                        self.deck = []

                        for suit in ['H','S','C','D']:
                                for rank in range(2,15):
                                        self.deck.append(Card(rank, suit))

                def __str__(self):
                        out = ""
                        for card in self.deck:
                                out += str(card) + "\n"
                        return out

                def __getitem__(self, index):
                        return self.deck[index]

                #return a list a cards taken from the deck
                def deal(self, amount):
                        cards = []

                        #cap out the cards dealt
                        if amount > len(self.deck):
                                print("There are not enough cards!  I can only deal " + str(len(self.deck)) + " cards.")
                                amount = len(self.deck)

                        #create and then return a list of cards taken randomly from the deck
                        for i in range(amount):
                                card = random.choice(self.deck)
                                self.deck.remove(card)
                                cards.append(card)
                        return cards


        class Poker:

                def __init__(self):
                        self.deck = Deck()
                        self.scores = [0,0,0,0] #array of scores

                        self.playerHand = Hand(self.deck.deal(5)) #each player is dealth 5 cards
                        self.comp1Hand = Hand(self.deck.deal(5))
                        self.comp2Hand = Hand(self.deck.deal(5))
                        self.comp3Hand = Hand(self.deck.deal(5))

                def __init__(self, scores):
                        self.deck = Deck()
                        self.scores = scores

                        self.playerHand = Hand(self.deck.deal(5))
                        self.comp1Hand = Hand(self.deck.deal(5))
                        self.comp2Hand = Hand(self.deck.deal(5))
                        self.comp3Hand = Hand(self.deck.deal(5))

                #make each computer take a turn
                def computerReplace(self):
                        self.AI_replace(self.comp1Hand)
                        self.AI_replace(self.comp2Hand)
                        self.AI_replace(self.comp3Hand)

                def get_most_suit(self, hand):
                        suits = {'H':0, 'C':0, 'S':0, 'D':0}
                        for card in hand:
                                suits[card.suit] += 1
                        return max(suits.items(), key=operator.itemgetter(1))[0]

                def get_most_rank(self, hand):
                        ranks = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}
                        for card in hand:
                                ranks[card.rank] += 1
                        return max(ranks.items(), key=operator.itemgetter(1))[0]

                def replace_suit(self, hand):
                        suit = self.get_most_suit(hand)
                        for card in hand:
                                if card.suit != suit:
                                        card.selected = True
                        self.replace(hand)

                def replace_rank(self, hand):
                        rank = self.get_most_rank(hand)
                        for card in hand:
                                if card.rank != rank:
                                        card.selected = True
                        self.replace(hand)

                def AI_replace(self, hand):

                        score = self.get_score(hand)

                        #decide which cards not to toss away so as to keep the same score

                        if str(score)[0] == '1': #High card, try for flush
                                self.replace_suit(hand)
                        elif str(score)[0] == '2': #One pair, switch out cards not paired
                                self.replace_rank(hand)
                        elif str(score)[0] == '3': #Two pair, switch out card not paired
                                self.replace_rank(hand)
                        elif str(score)[0] == '4': #Three of a kind, switch out cards not paired
                                self.replace_rank(hand)
                        elif str(score)[0] == '8': #Four of a kind, switch out the not paired not
                                self.replace_rank(hand)

                        #all other cases are a pass

                #repalces the selected cards in the hand with the top cards on the deck
                def replace(self, hand):
                        count = 0
                        for i in range(3):
                                for card in hand:
                                        if card.selected:
                                                hand.hand.remove(card)
                                                count += 1

                        hand.hand.extend(self.deck.deal(count))

                #plays a round of poker with 4 hands
                #winner is displayed and scores for each hand as well
                #the number of the winner is returned by the function
                def play_round(self):

                        score1 = self.get_score(self.playerHand) #score of players hand
                        score2 = self.get_score(self.comp1Hand) #score of computer 1s hand
                        score3 = self.get_score(self.comp2Hand) #score of computer 2s hand
                        score4 = self.get_score(self.comp3Hand) #score of computer 3s hand

                        winner = max(score1, max(score2, max(score3, score4))) #the highest score wins

                        def displayPokerLosses():

                            #Display earnings on start screen, if file which money is stored doesn't exist then
                                # a file is created.

                            try:
                                with open('PokerLOSSES.txt') as f:
                                    current_Pokerlosses = f.readline()

                                #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                                #screen.blit(total_earnings, (870,80))

                            except:
                                #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                                #screen.blit(total_earnings, (870,30))

                                with open('PokerLOSSES.txt', 'w') as f:
                                    f.write(str(1))

                        def increasePokerLosses():
                

            

                             with open('PokerLOSSES.txt') as f:
                                current_Pokerlosses = f.readline()
                                current_Pokerlosses = int(current_Pokerlosses)

                             if current_Pokerlosses > 0 and current_Pokerlosses < 100000:

                                with open('PokerLOSSES.txt', 'w') as f:
                                    global new_Pokerlosses
                                    new_Pokerlosses = int(current_Pokerlosses) + 1
                                    f.write(str(new_Pokerlosses))

                        

                        if winner == score1:
                                self.scores[0] += 1
                                chips[2] = chips[1] * 4
                                chips[0] = chips[0] + chips[2]
                                pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))

                                def displayPokerWins():

                                    #Display earnings on start screen, if file which money is stored doesn't exist then
                                        # a file is created.

                                    try:
                                        with open('PokerWINS.txt') as f:
                                            current_Pokerwins = f.readline()

                                        #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                                        #screen.blit(total_earnings, (870,80))

                                    except:
                                        #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                                        #screen.blit(total_earnings, (870,30))

                                        with open('PokerWINS.txt', 'w') as f:
                                            f.write(str(1))

                                def increasePokerWins():
                        

                    

                                     with open('PokerWINS.txt') as f:
                                        current_Pokerwins = f.readline()
                                        current_Pokerwins = int(current_Pokerwins)

                                     if current_Pokerwins > 0 and current_Pokerwins < 100000:

                                        with open('PokerWINS.txt', 'w') as f:
                                            global new_Pokerwins
                                            new_Pokerwins = int(current_Pokerwins) + 1
                                            f.write(str(new_Pokerwins))

                                displayPokerWins()
                                increasePokerWins()

                                
                                if chips[0] <= 0:
                                        bust_screen()
                                

                        elif winner == score2:
                                self.scores[1] += 1
                                displayPokerLosses()
                                increasePokerLosses()
                                if chips[0] <= 0:
                                        bust_screen()

                        elif winner == score3:
                                self.scores[2] += 1
                                displayPokerLosses()
                                increasePokerLosses()
                                if chips[0] <= 0:
                                        bust_screen()

                        elif winner == score4:
                                self.scores[3] += 1
                                displayPokerLosses()
                                increasePokerLosses()
                                if chips[0] <= 0:
                                        bust_screen()

                        return [score1, score2, score3, score4]


                #returns an integer that represents a score given to the hand.  The first digits represents the type of hand and the rest represent the cards in the hands
                def get_score(self, hand):
                        #make a dictionary containing the count of each each
                        cardCount = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}

                        for card in hand.hand:
                                cardCount[card.rank] += 1

                        #count number of unique cards
                        uniqueCount = 0
                        for rankCount in cardCount.values():
                                if rankCount > 0:
                                        uniqueCount += 1

                        straight = self.is_straight(hand)
                        flush = self.is_flush(hand)

                        points = 0

                        if straight and flush:
                                points = max(points, 9) #straight flush
                        elif flush and not straight:
                                points = max(points, 6) #flush
                        elif not flush and straight:
                                points = max(points, 5) #straight

                        elif uniqueCount == 2:
                                if max(cardCount.values()) == 4:
                                        points = 8 #four of a kind (2 uniques and 4 are the same)
                                elif max(cardCount.values()) == 3:
                                        points = 7 #full house (2 unique and 3 are the same)

                        elif uniqueCount == 3:
                                if max(cardCount.values()) == 3:
                                        points = 4 #three of a kind (3 unique and 3 are the same)
                                elif max(cardCount.values()) == 2:
                                        points = 3 #two pair (3 uniques and 2 are the same)

                        elif uniqueCount == 4:
                                if max(cardCount.values()) == 2:
                                        points = 2 #one pair (4 uniques and 2 are the same)

                        elif uniqueCount == 5:
                                points = 1 #high card 

                        #print out the values of the cards in order from greatest to least with 2 digits for each card in order to generate a point value
                        sorted_cardCount = sorted(cardCount.items(), key=operator.itemgetter(1,0), reverse=True)
                        for keyval in sorted_cardCount:
                                if keyval[1] != 0:
                                        points = int(str(points) + (keyval[1] * str(keyval[0]).zfill(2)))

                        return points

                #given an integer score, returns the poker term equivalent
                def convert_score(self, score):
                        if str(score)[0] == '1':
                                return "High Card"
                        elif str(score)[0] == '2':
                                return "One Pair"
                        elif str(score)[0] == '3':
                                return "Two Pair"
                        elif str(score)[0] == '4':
                                return "Three of a Kind"
                        elif str(score)[0] == '5':
                                return "Straight"
                        elif str(score)[0] == '6':
                                return "Flush"
                        elif str(score)[0] == '7':
                                return "Full House"
                        elif str(score)[0] == '8':
                                return "Four of a Kind"
                        elif str(score)[0] == '9':
                                return "Straight Flush"

                #a hand is a straight if, when sorted, the current card's rank + 1 is the same as the next card
                def is_straight(self,hand):
                        values = []
                        for card in hand.hand:
                                values.append(card.rank)

                        values.sort()

                        for i in range(0,4):
                                if values[i] + 1 != values[i + 1]:
                                        return False
                        return True

                #a hand is a flush if all the cards are of the same suit
                def is_flush(self,hand):
                        suit = hand.hand[0].suit
                        for card in hand.hand:
                                if card.suit != suit:
                                        return False
                        return True


        #############################################################
        if __name__ == "__main__":
                os.environ['SDL_VIDEO_CENTERED'] = '1' #center screen
                pygame.init()
                pygame.display.set_caption("Jack of Hearts - Playing Poker")
                SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0 ,32)
                
                Runit = Control()
                Myclock = pygame.time.Clock()
                while 1:
                        Runit.main()
                        Myclock.tick(64)










def guess_the_number():
        pygame.display.set_caption("Jack of Hearts - Playing Minigames (Guess The Number)")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        number_screen = pygame.display.set_mode((1270, 822))
        number_font = pygame.font.SysFont("cambria", 30)
        clock = pygame.time.Clock()
        user_number_text = ''
        number_password_rect = pygame.Rect(617, 647, 120, 40)
        numbercolor_password_active = pygame.Color('red')
        numbercolor_password_passive = pygame.Color('grey')
        listofnumber = random.randint(1,101)
        answer = random.choice(str(listofnumber))
        #print(answer)
        #print(answer)
        
                           

        

        mixer.music.load('guess the number music.mp3')
        pygame.mixer.music.play(loops=-1)
        mixer.music.set_volume(0.1)

        
                
        numbercolorpassword = numbercolor_password_passive
                
        numberactivepassword = False

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                        self.image = image
                        self.x_pos = x_pos
                        self.y_pos = y_pos
                        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                        self.text_input = text_input
                        self.text = number_font.render(self.text_input, True, "white")
                        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                        screen.blit(self.image, self.rect)
                        screen.blit(self.text, self.text_rect)


                def checkForInputguess(self, position):
                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(7).play(pygame.mixer.Sound('Button Sound.wav'))
                                if user_number_text == answer:# or user_number_text == answer2 or user_number_text == answer3 or user_number_text == answer or user_number_text == answer :
                                                winning_text = number_font.render('THAT IS THE CORRECT NUMBER', True, 'black')
                                                number_screen.blit(winning_text, (100, 500))
                                                pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                                                chips[0] = chips[0] + 25000
                                                
                                else:
                                                number_screen.blit(number_font.render('WRONG NUMBER', True, 'black'), (100, 500))
                                                chips[0] = chips[0] - 5000
                                                

                def checkForInputguessback(self, position):
                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(7).play(pygame.mixer.Sound('Button Sound.wav'))
                                pick_your_game()
                                

                        

                                        
                                        
                                        

                def changeColor(self, position):
                        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                self.text = number_font.render(self.text_input, True, "green")
                        else:
                                self.text = number_font.render(self.text_input, True, "black")

        buttonenterguess_surface = pygame.image.load("guess the number button.png")
        buttonenterguess_surface = pygame.transform.scale(buttonenterguess_surface, (300, 110))

        buttonenterguess = Button(buttonenterguess_surface, 680, 755, "GUESS THE NUMBER")

        buttonenterguessb_surface = pygame.image.load("white arrow.png")
        buttonenterguessb_surface = pygame.transform.scale(buttonenterguessb_surface, (200, 110))

        buttonenterguessb = Button(buttonenterguessb_surface, 120, 755, "")

        screen.fill("light blue")
        logo = pygame.image.load("guess_the_number_logo-removebg-preview.png")
        number_screen.blit(logo, (7, 0))
        jackofheartslogo = pygame.image.load("jack of hearts logo black small.png")
        number_screen.blit(jackofheartslogo, (1060,0))
        genie = pygame.image.load("genie.png")
        number_screen.blit(genie, (490, 10))
        speechbubble = pygame.image.load("genie speech bubble.PNG")
        number_screen.blit(speechbubble, (740, 0))



        while True: #a loop that makes the screen run forever
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit() #opposite of pygame.init()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        if number_password_rect.collidepoint(event.pos):
                                                numberactivepassword = True
                                        else:
                                                numberactivepassword = False

                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        buttonenterguess.checkForInputguess(pygame.mouse.get_pos())
                                        buttonenterguessb.checkForInputguessback(pygame.mouse.get_pos())
                                        
                                
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_BACKSPACE:
                                                user_number_text = user_number_text[:-1]
                                        else:
                                                user_number_text += event.unicode

                        buttonenterguess.update()
                        buttonenterguess.changeColor(pygame.mouse.get_pos())

                        buttonenterguessb.update()

                        pygame.display.update()

                        if numberactivepassword:
                                numbercolorpassword = numbercolor_password_active
                        else:
                                numbercolorpassword = numbercolor_password_passive

                                        
                                

                        pygame.draw.rect(number_screen, numbercolorpassword, number_password_rect)

                        number_password_surface = number_font.render(user_number_text, True, ("Black"))
                                

                        number_screen.blit(number_password_surface, (number_password_rect.x+5, number_password_rect.y+5))
                                

                        number_password_rect.w = max(100, number_password_surface.get_width()+10)

                        pygame.display.flip()

                        clock.tick(60)

                        #MAIN GAME

                        def linear_search():

                                found = False

                                for index in range(0,len(listofnumbers)):
                                        if user_number_text == listofnumbers[index]:
                                                found = True
                                        return found
                                if found == True:
                                        number_screen.blit(number_font.render('WRONG NUMBER', True, 'black'), (100, 500))

                                                
                                        
                                

        

    
def blackjack_career_menu():
    pygame.display.set_caption("Jack of Hearts - Viewing Career in BlackJack")
    programIcon = pygame.image.load('icon.png')
    pygame.display.set_icon(programIcon)
    career_screen = pygame.display.set_mode((900,570))
    career_font = pygame.font.SysFont("arial",30)
    clock = pygame.time.Clock()
    career_screen_background = pygame.image.load("blackjack career menu.PNG")
    career_screen.blit(career_screen_background, (0,0))

    class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = career_font.render(self.text_input, True, "grey")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputbcback(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(16).play(pygame.mixer.Sound('Button Sound.wav'))
                        blackjack_menu()

    buttonenter_bc_back_surface= pygame.image.load("neon purple arrow.PNG")
    buttonenter_bc_back_surface = pygame.transform.scale(buttonenter_bc_back_surface, (100, 60))

    buttonenter_bc_back = Button(buttonenter_bc_back_surface, 70, 520, "")

    buttonenter_bc_back.update()




    

    def displayBlackjackWins():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('blackjackWINS.txt') as f:
                    global current_wins
                    current_wins = f.readline()

                total_wins = career_font.render(str(current_wins), False , "Black")
                career_screen.blit(total_wins, (155,168))

            except:
                total_wins = career_font.render('Total Earnings: $0', False , "Black")
                career_screen.blit(total_wins, (870,30))

                with open('blackjackWins.txt', 'w') as f:
                    f.write(str(1))


    def displayBlackjackDraws():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('blackjackDRAWS.txt') as f:
                    global current_draws
                    current_draws = f.readline()

                total_draws = career_font.render(str(current_draws), False , "Black")
                career_screen.blit(total_draws, (170,235))

            except:
                total_draws = career_font.render('Total Earnings: $0', False , "Black")
                career_screen.blit(total_draws, (870,30))

                with open('blackjackDRAWS.txt', 'w') as f:
                    f.write(str(1))

    def displayBlackjackLosses():

            #Display earnings on start screen, if file which money is stored doesn't exist then
                # a file is created.

            try:
                with open('blackjackLOSSES.txt') as f:
                    global current_losses
                    current_losses = f.readline()

                total_losses = career_font.render(str(current_losses), False , "Black")
                career_screen.blit(total_losses, (179,298))

            except:
                total_losses = career_font.render('Total Earnings: $0', False , "Black")
                career_screen.blit(total_losses, (870,30))

                with open('blackjackLOSSES.txt', 'w') as f:
                    f.write(str(1))

    displayBlackjackWins()
    displayBlackjackDraws()
    displayBlackjackLosses()

    totalgames = int(current_wins) + int(current_draws) + int(current_losses)

    totalgamesz = career_font.render(str(totalgames), False, "Black")
    career_screen.blit(totalgamesz, (255, 365))
    

    

        

    

    pygame.display.update()

    while True: #a loop that makes the screen run forever
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit() #opposite of pygame.init()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonenter_bc_back.checkForInputbcback(pygame.mouse.get_pos())

        buttonenter_bc_back.update()

        pygame.display.update()
    
#Career Checklist
#Total chips earned
#Wins
#Loses
#Draws
#Total Money Lost
#

def rules_screen():
    pygame.display.set_caption("Jack of Hearts - Learning the Rules of BlackJack")
    programIcon = pygame.image.load('icon.png')
    pygame.display.set_icon(programIcon)
    rules_screen = pygame.display.set_mode((1000,640), 0,2)
    rules_font = pygame.font.SysFont("arial",30)
    clock = pygame.time.Clock()
    rules_screen_background = pygame.image.load("rules screen.PNG")

    rules_screen.blit(rules_screen_background,(0,0))

    pygame.display.update()

    while True: #a loop that makes the screen run forever
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit() #opposite of pygame.init()
                        sys.exit()
                if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                blackjack_menu()
    
def bust_screen():
        pygame.display.set_caption("Bust")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        bust_screen = pygame.display.set_mode((1000,640), 0,2)
        bust_font = pygame.font.SysFont("arial",30)
        clock = pygame.time.Clock()
        bust_screen_background = pygame.image.load("bust screen.PNG")

        bust_screen.blit(bust_screen_background,(0,0))

        pygame.display.update()

        class Button():
                def __init__(self, image, x_pos, y_pos, text_input):
                    self.image = image
                    self.x_pos = x_pos
                    self.y_pos = y_pos
                    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                    self.text_input = text_input
                    self.text = bust_font.render(self.text_input, True, "grey")
                    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                def update(self):
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.text_rect)


                def checkForInputSecret(self, position):
                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                        pygame.mixer.Channel(16).play(pygame.mixer.Sound('Button Sound.wav'))
                        chips[0] = -10000000000000
                        pick_your_game()
                        

        buttonenter_bc_secret_surface= pygame.image.load("2 of Clubs.png")
        buttonenter_bc_secret_surface = pygame.transform.scale(buttonenter_bc_secret_surface, (200, 200))

        buttonenter_bc_secret = Button(buttonenter_bc_secret_surface, 150,150, "")

        buttonenter_bc_secret.update()

        pygame.display.update()

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                buttonenter_bc_secret.checkForInputSecret(pygame.mouse.get_pos())

        buttonenter_bc_secret.update()

        pygame.display.update()

def secret():
        pygame.display.set_caption("PRANKED")
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        PRANK_screen = pygame.display.set_mode((1000,640), 0,2)
        PRANK_font = pygame.font.SysFont("arial",30)
        clock = pygame.time.Clock()
        PRANK_screen_background = pygame.image.load("HACKER.jfif")

        PRANK_screen.blit(PRANK_screen_background,(0,0))

        pygame.display.update()

        while True: #a loop that makes the screen run forever
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit() #opposite of pygame.init()
                                sys.exit()
        
        
def wins():
        global blackjacktotalwins
        blackjacktotalwins = int()
        blackjacktotalwins = blackjacktotalwins + 1

def draws():
        global blackjacktotaldraws
        blackjacktotaldraws = int()
        blackjacktotaldraws = blackjacktotaldraws + 1

def losses():
        global blackjacktotallosses
        blackjacktotallosses = int()
        blackjacktotallosses = blackjacktotallosses + 1
        
                        
def blackjack():
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] #an array for the cards in a deck
        one_deck = 4 * cards #makes 52 cards as there are 4 suits for each card
        decks = 4
        WIDTH = 1530
        HEIGHT = 780
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption('Jack of Hearts - Playing BlackJack')
        programIcon = pygame.image.load('icon.png')
        pygame.display.set_icon(programIcon)
        fps = 60
        timer = pygame.time.Clock()
        font = pygame.font.Font('freesansbold.ttf', 44)
        smaller_font = pygame.font.Font('freesansbold.ttf', 36)
        active = False
        # win, loss, draw/push
        records = [0, 0, 0] #array for the players wins, losses and draws
        player_score = 0 #initialises the players current score
        dealer_score = 0 #initialises the dealers current score
        initial_deal = False #hand has not started yet
        my_hand = [] #creates an array that the players current hand will enter
        dealer_hand = [] #creates and array that the dealers current hand will enter
        outcome = 0 #player total
        reveal_dealer = False #dealer has not started yet
        hand_active = False #player has not started yet
        outcome = 0 #dealer total
        add_score = False
        results = ['', '                                 BUST! ', '                             Player WINS! ', '                                   DEALER WINS ', '                            TIE GAME...','BLACKJACK!']
        #an array which will display a message depending on the outcome of the hand
        
        

        mixer.music.load('intrigue-fun-21661.mp3') #plays the blackjack music
        pygame.mixer.music.play(loops=-1)
        mixer.music.set_volume(0.1)

        twoofclubs = pygame.image.load("2 of Clubs.png") #loads every single card and stores them as variables
        twoofdiamonds = pygame.image.load("2 of Diamonds.png")
        twoofhearts = pygame.image.load("2 of Hearts.png")
        twoofspades = pygame.image.load("2 of Spades.png")
        threeofclubs = pygame.image.load("3 of Clubs.png")
        threeofdiamonds = pygame.image.load("3 of Diamonds.png")
        threeofhearts = pygame.image.load("3 of Hearts.jfif")
        threeofspades = pygame.image.load("3 of Spades.jfif")
        fourofclubs = pygame.image.load("4 of Clubs.png")
        fourofdiamonds = pygame.image.load("4 of Diamonds.png")
        fourofhearts = pygame.image.load("4 of Hearts.png")
        fourofspades = pygame.image.load("4 of Spades.png")
        fiveofclubs = pygame.image.load("5 of Clubs.png")
        fiveofdiamonds = pygame.image.load("5 of Diamonds.png")
        fiveofhearts = pygame.image.load("5 of Hearts.png")
        fiveofspades = pygame.image.load("5 of Spades.png")
        sixofclubs = pygame.image.load("6 of Clubs.png")
        sixofdiamonds = pygame.image.load("6 of Diamonds.png")
        sixofhearts = pygame.image.load("6 of Hearts.png")
        sixofspades = pygame.image.load("6 of Spades.png")
        sevenofclubs = pygame.image.load("7 of Clubs.png")
        sevenofdiamonds = pygame.image.load("7 of Diamonds.jfif")
        sevenofhearts = pygame.image.load("7 of Hearts.png")
        sevenofspades = pygame.image.load("7 of Spades.png")
        eightofclubs = pygame.image.load("8 of Clubs.png")
        eightofdiamonds = pygame.image.load("8 of Diamonds.png")
        eightofhearts = pygame.image.load("8 of Hearts.png")
        eightofspades = pygame.image.load("8 of Spades.png")
        nineofclubs = pygame.image.load("9 of Clubs.png")
        nineofdiamonds = pygame.image.load("9 of Diamonds.png")
        nineofhearts = pygame.image.load("9 of Hearts.png")
        nineofspades = pygame.image.load("9 of Spades.png")
        tenofclubs = pygame.image.load("10 of Clubs.png")
        tenofdiamonds = pygame.image.load("10 of Diamonds.png")
        tenofhearts = pygame.image.load("10 of Hearts.png")
        tenofspades = pygame.image.load("10 of Spades.png")
        jackofclubs = pygame.image.load("Jack of Clubs.png")
        jackofdiamonds = pygame.image.load("Jack of Diamonds.jfif")
        jackofhearts = pygame.image.load("Jack of Hearts.png")
        jackofspades = pygame.image.load("Jack of Spades.jfif")
        queenofclubs = pygame.image.load("Queen of Clubs.png")
        queenofdiamonds = pygame.image.load("Queen of Diamonds.png")
        queenofhearts = pygame.image.load("Queen of Hearts.jfif")
        queenofspades = pygame.image.load("Queen of Spades.png")
        kingofclubs = pygame.image.load("King of Clubs.jfif")
        kingofdiamonds = pygame.image.load("King of Diamonds.png")
        kingofhearts = pygame.image.load("King of Hearts.jfif")
        kingofspades = pygame.image.load("King of Spades.jfif")
        aceofclubs = pygame.image.load("Ace of Clubs.png")
        aceofdiamonds = pygame.image.load("Ace of Diamonds.png")
        aceofhearts = pygame.image.load("Ace of Hearts.png")
        aceofspades = pygame.image.load("Ace of Spades.png")
        
        
        
        
        
        
        

        

        

        def deal_cards(current_hand, current_deck):
            global card
            card = random.randint(0, len(current_deck))
            current_hand.append(current_deck[card - 1])
            current_deck.pop(card - 1)
            
                    
            return current_hand, current_deck

        def draw_scores(player, dealer):
            screen.blit(font.render(f'Your Score is {player}', True, 'white'), (1178, 250))
            if reveal_dealer:
                screen.blit(font.render(f'The Dealers score is {dealer}', True, 'white'), (1020, 310))

        def draw_cards(player, dealer, reveal): #REARRANGE 
            for i in range(len(player)): #player first and second card
                if player[i] == '2':
                        twos = [twoofclubs, twoofdiamonds, twoofhearts, twoofspades]
                        randomtwo = random.choice(twos)
                        screen.blit((twoofclubs), (575 + 70 * i, 485 + 5 * i))
                        

                if player[i] == '3':
                        threes = [threeofclubs, threeofdiamonds, threeofhearts, threeofspades]
                        randomthree = random.choice(threes)
                        screen.blit((threeofdiamonds), (595 + 70 * i, 485 + 5 * i))

                if player[i] == '4':
                        fours = [fourofclubs, fourofdiamonds, fourofhearts, fourofspades]
                        randomfour = random.choice(fours)
                        screen.blit((fourofhearts), (595 + 70 * i, 485 + 5 * i))

                if player[i] == '5':
                        fives = [fiveofclubs, fiveofdiamonds, fiveofhearts, fiveofspades]
                        randomfive = random.choice(fives)
                        screen.blit((fiveofspades), (595 + 70 * i, 485 + 5 * i))

                if player[i] == '6':
                        sixes = [sixofclubs, sixofdiamonds, sixofhearts, sixofspades]
                        randomsix = random.choice(sixes)
                        screen.blit((sixofclubs), (595 + 70 * i, 485 + 5 * i))

                if player[i] == '7':
                        sevens = [sevenofclubs, sevenofdiamonds, sevenofhearts, sevenofspades]
                        randomseven = random.choice(sevens)
                        screen.blit((sevenofdiamonds), (595 + 70 * i, 485 + 5 * i))

                if player[i] == '8':
                        eights = [eightofclubs, eightofdiamonds, eightofhearts, eightofspades]
                        randomeight = random.choice(eights)
                        screen.blit((eightofhearts), (595 + 70 * i, 485 + 5 * i))

                if player[i] == '9':
                        nines = [nineofclubs, nineofdiamonds, nineofhearts, nineofspades]
                        randomnine = random.choice(nines)
                        screen.blit((nineofspades), (595 + 70 * i, 485 + 5 * i))

                if player[i] == '10':
                        tens = [tenofclubs, tenofdiamonds, tenofhearts, tenofspades]
                        randomten = random.choice(tens)
                        screen.blit((tenofclubs), (595 + 70 * i, 485 + 5 * i))

                if player[i] == 'J':
                        jacks = [jackofclubs, jackofdiamonds, jackofhearts, jackofspades]
                        randomjack = random.choice(jacks)
                        screen.blit((jackofhearts), (595 + 70 * i, 485 + 5 * i))

                if player[i] == 'Q':
                        queens = [queenofclubs, queenofdiamonds, queenofhearts, queenofspades]
                        randomqueen = random.choice(queens)
                        screen.blit((queenofdiamonds), (595 + 70 * i, 485 + 5 * i))

                if player[i] == 'K':
                        kings = [kingofclubs, kingofdiamonds, kingofhearts, kingofspades]
                        randomking = random.choice(kings)
                        screen.blit((kingofspades), (595 + 70 * i, 485 + 5 * i))

                if player[i] == 'A':
                        aces = [aceofclubs, aceofdiamonds, aceofhearts, aceofspades]
                        randomace = random.choice(aces)
                        screen.blit((aceofhearts), (595 + 70 * i, 485 + 5 * i))
                            
                #(610 + 70 * i, 380 + 5 * i))
                

            for i in range(len(dealer)):
                #pygame.draw.rect(screen, 'white', [595 + (70 * i), 210 + (5 * i), 120, 220], 0, 5)
                if i != 0 or reveal: #dealer first card
                    if dealer[i] == "2":
                            screen.blit((twoofclubs), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "3":
                            screen.blit((threeofdiamonds), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "4":
                            screen.blit((fourofspades), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "5":
                            screen.blit((fiveofhearts), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "6":
                            screen.blit((sixofclubs), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "7":
                            screen.blit((sevenofdiamonds), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "8":
                            screen.blit((eightofspades), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "9":
                            screen.blit((nineofhearts), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "10":
                            screen.blit((tenofclubs), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "J":
                            screen.blit((jackofspades), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "Q":
                            screen.blit((queenofclubs), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "K":
                            screen.blit((kingofdiamonds), (610 + 70 * i, 205 + 5 * i))

                    if dealer[i] == "A":
                            screen.blit((aceofspades), (610 + 70 * i, 205 + 5 * i))
                            
                else: #dealer face down card
                    facedowncard = pygame.image.load("face down card.PNG")
                    screen.blit(facedowncard,(595,196))
                #pygame.draw.rect(screen, 'blue', [595 + (70 * i), 210 + (5 * i), 120, 220], 5, 5)

        def calculate_score(hand):
            # calculate hand score fresh every time, check how many aces we have
            hand_score = 0
            aces_count = hand.count('A')
            for i in range(len(hand)):
                # for 2,3,4,5,6,7,8,9 - just add the number to total
                for j in range(8):
                    if hand[i] == cards[j]:
                        hand_score += int(hand[i])
                # for 10 and face cards, add 10
                if hand[i] in ['10', 'J', 'Q', 'K']:
                    hand_score += 10
                # for aces start by adding 11, we'll check if we need to reduce afterwards
                elif hand[i] == 'A':
                    hand_score += 11
            # determine how many aces need to be 1 instead of 11 to get under 21 if possible
            if hand_score > 21 and aces_count > 0:
                for i in range(aces_count):
                    if hand_score > 21:
                        hand_score -= 10
            return hand_score

        def draw_game(act, record, result):
            button_list = []
            # initially on startup (not active) only option is to deal new hand
            if not act:
                deal = pygame.draw.rect(screen, 'white', [490, 400, 600, 100], 0, 5)
                pygame.draw.rect(screen, 'green', [490, 400, 600, 100], 3, 5)
                deal_text = font.render('PLACE YOUR BETS', True, 'black') #add currency system
                screen.blit(deal_text, (604, 427))
                chip_text2 = smaller_font.render(f'Chips = {chips[0]}', True, 'white')
                screen.blit(chip_text2, (1215, 85))
                button_list.append(deal)

                class Button():
                        def __init__(self, image, x_pos, y_pos, text_input):
                            self.image = image
                            self.x_pos = x_pos
                            self.y_pos = y_pos
                            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
                            self.text_input = text_input
                            self.text = font.render(self.text_input, True, "grey")
                            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

                        def update(self):
                            screen.blit(self.image, self.rect)
                            screen.blit(self.text, self.text_rect)


                        def checkForInput1000(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(43).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = chips[0]
                                chips[0] = chips[0] - chips[1]
                                
                                

                        def checkForInput2000(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(42).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = 2000
                                chips[0] = chips[0] - 2000
                                

                        def checkForInput3000(self, position):
                            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                pygame.mixer.Channel(44).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                chips[1] = 3000
                                chips[0] = chips[0] - 3000
                        

                        def checkForInput4000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(30).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 4000
                                        chips[0] = chips[0] - 4000

                        def checkForInput5000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(31).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 5000
                                        chips[0] = chips[0] - 5000

                        def checkForInput10000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(32).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 10000
                                        chips[0] = chips[0] - 10000

                        def checkForInput15000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(33).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 15000
                                        chips[0] = chips[0] - 15000

                        def checkForInput20000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(34).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 20000
                                        chips[0] = chips[0] - 20000

                        def checkForInput25000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(35).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 25000
                                        chips[0] = chips[0] - 25000

                        def checkForInput30000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(36).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 30000
                                        chips[0] = chips[0] - 30000

                        def checkForInput35000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(37).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 35000
                                        chips[0] = chips[0] - 35000

                        def checkForInput40000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 40000
                                        chips[0] = chips[0] - 40000

                        def checkForInput45000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(39).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 45000
                                        chips[0] = chips[0] - 45000

                        def checkForInput50000(self, position):
                                    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        pygame.mixer.Channel(40).play(pygame.mixer.Sound('mixkit-clinking-coins-1993.wav'))
                                        chips[1] = 50000
                                        chips[0] = chips[0] - 50000

                        

                        

                        

                        
                                        

                        def changeColor(self, position):
                                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                                        self.text = font.render(self.text_input, True, "yellow")
                                else:
                                        self.text = font.render(self.text_input, True, "grey")

                global buttonenter1000, buttonenter2000, buttonenter3000, buttonenter4000, buttonenter5000, buttonenter10000, buttonenter15000, buttonenter20000, buttonenter25000, buttonenter30000, buttonenter35000, buttonenter40000, buttonenter45000, buttonenter50000


                buttonenter1000_surface = pygame.image.load("grey blackjack.png")
                buttonenter1000_surface = pygame.transform.scale(buttonenter1000_surface, (150, 70))

                buttonenter1000= Button(buttonenter1000_surface, 90, 70, "ALL")

                buttonenter2000_surface = pygame.image.load("grey blackjack.png")
                buttonenter2000_surface = pygame.transform.scale(buttonenter2000_surface, (150, 70))

                buttonenter2000= Button(buttonenter2000_surface, 250, 70, "2000")

                buttonenter3000_surface = pygame.image.load("grey blackjack.png")
                buttonenter3000_surface = pygame.transform.scale(buttonenter3000_surface, (150, 70))

                buttonenter3000= Button(buttonenter3000_surface, 90, 170, "3000")

                buttonenter4000_surface = pygame.image.load("grey blackjack.png")
                buttonenter4000_surface = pygame.transform.scale(buttonenter4000_surface, (150, 70))

                buttonenter4000= Button(buttonenter4000_surface, 250, 170, "4000")

                buttonenter5000_surface = pygame.image.load("grey blackjack.png")
                buttonenter5000_surface = pygame.transform.scale(buttonenter5000_surface, (150, 70))

                buttonenter5000= Button(buttonenter5000_surface, 90, 270, "5000")

                buttonenter10000_surface = pygame.image.load("grey blackjack.png")
                buttonenter10000_surface = pygame.transform.scale(buttonenter10000_surface, (150, 70))

                buttonenter10000= Button(buttonenter10000_surface, 250, 270, "10000")

                buttonenter15000_surface = pygame.image.load("grey blackjack.png")
                buttonenter15000_surface = pygame.transform.scale(buttonenter15000_surface, (150, 70))

                buttonenter15000= Button(buttonenter15000_surface, 90, 370, "15000")

                buttonenter20000_surface = pygame.image.load("grey blackjack.png")
                buttonenter20000_surface = pygame.transform.scale(buttonenter20000_surface, (150, 70))

                buttonenter20000= Button(buttonenter20000_surface, 250, 370, "20000")

                buttonenter25000_surface = pygame.image.load("grey blackjack.png")
                buttonenter25000_surface = pygame.transform.scale(buttonenter25000_surface, (150, 70))

                buttonenter25000= Button(buttonenter25000_surface, 90, 470, "25000")

                buttonenter30000_surface = pygame.image.load("grey blackjack.png")
                buttonenter30000_surface = pygame.transform.scale(buttonenter30000_surface, (150, 70))

                buttonenter30000= Button(buttonenter30000_surface, 250, 470, "30000")

                buttonenter35000_surface = pygame.image.load("grey blackjack.png")
                buttonenter35000_surface = pygame.transform.scale(buttonenter35000_surface, (150, 70))

                buttonenter35000= Button(buttonenter35000_surface, 90, 570, "35000")

                buttonenter40000_surface = pygame.image.load("grey blackjack.png")
                buttonenter40000_surface = pygame.transform.scale(buttonenter40000_surface, (150, 70))

                buttonenter40000= Button(buttonenter40000_surface, 250, 570, "40000")

                buttonenter45000_surface = pygame.image.load("grey blackjack.png")
                buttonenter45000_surface = pygame.transform.scale(buttonenter45000_surface, (150, 70))

                buttonenter45000= Button(buttonenter45000_surface, 90, 670, "45000")

                buttonenter50000_surface = pygame.image.load("grey blackjack.png")
                buttonenter50000_surface = pygame.transform.scale(buttonenter50000_surface, (150, 70))

                buttonenter50000= Button(buttonenter50000_surface, 250, 670, "50000")

                

                buttonenter1000.changeColor(pygame.mouse.get_pos())
                buttonenter1000.update()

                buttonenter2000.changeColor(pygame.mouse.get_pos())
                buttonenter2000.update()

                buttonenter3000.changeColor(pygame.mouse.get_pos())
                buttonenter3000.update()

                buttonenter4000.changeColor(pygame.mouse.get_pos())
                buttonenter4000.update()

                buttonenter5000.changeColor(pygame.mouse.get_pos())
                buttonenter5000.update()

                buttonenter10000.changeColor(pygame.mouse.get_pos())
                buttonenter10000.update()

                buttonenter15000.changeColor(pygame.mouse.get_pos())
                buttonenter15000.update()

                buttonenter20000.changeColor(pygame.mouse.get_pos())
                buttonenter20000.update()

                buttonenter25000.changeColor(pygame.mouse.get_pos())
                buttonenter25000.update()

                buttonenter30000.changeColor(pygame.mouse.get_pos())
                buttonenter30000.update()

                buttonenter35000.changeColor(pygame.mouse.get_pos())
                buttonenter35000.update()

                buttonenter40000.changeColor(pygame.mouse.get_pos())
                buttonenter40000.update()

                buttonenter45000.changeColor(pygame.mouse.get_pos())
                buttonenter45000.update()

                buttonenter50000.changeColor(pygame.mouse.get_pos())
                buttonenter50000.update()

                

                
                       

                











                
            # once game started, shot hit and stand buttons and win/loss records
            else:
                hit = pygame.draw.rect(screen, 'white', [1175, 480, 300, 100], 0, 5)
                pygame.draw.rect(screen, 'green', [1175, 480, 300, 100], 3, 5)
                hit_text = font.render('HIT ', True, 'black')
                screen.blit(hit_text, (1295, 510))
                pygame.time.set_timer(pygame.USEREVENT, 2000)
                button_list.append(hit)
                stand = pygame.draw.rect(screen, 'white', [1175, 605, 300, 100], 0, 5)
                pygame.draw.rect(screen, 'green', [1175, 605, 300, 100], 3, 5)
                stand_text = font.render('STAND', True, 'black')
                screen.blit(stand_text, (1255, 635))
                button_list.append(stand)
                score_text = smaller_font.render(f'Wins: {record[0]}   Losses: {record[1]}   Draws: {record[2]}', True, 'white')
                screen.blit(score_text, (1000, 15))
                chip_text = smaller_font.render(f'Chips = {chips[0]}', True, 'white')
                screen.blit(chip_text, (1215, 85))
            # if there is an outcome for the hand that was played, display a restart button and tell user what happened
            if result != 0:
                screen.blit(font.render(results[result], True, 'white'), (15, 25))
                deal = pygame.draw.rect(screen, 'white', [610, 220, 300, 100], 0, 5)
                pygame.draw.rect(screen, 'green', [610, 220, 300, 100], 3, 5)
                pygame.draw.rect(screen, 'black', [610, 223, 294, 94], 3, 5)
                deal_text = font.render('NEXT HAND', True, 'black')
                screen.blit(deal_text, (625, 250))
                button_list.append(deal)
                buttonenter1000.changeColor(pygame.mouse.get_pos())
                buttonenter1000.update()

                buttonenter2000.changeColor(pygame.mouse.get_pos())
                buttonenter2000.update()

                buttonenter3000.changeColor(pygame.mouse.get_pos())
                buttonenter3000.update()

                buttonenter4000.changeColor(pygame.mouse.get_pos())
                buttonenter4000.update()

                buttonenter5000.changeColor(pygame.mouse.get_pos())
                buttonenter5000.update()

                buttonenter10000.changeColor(pygame.mouse.get_pos())
                buttonenter10000.update()

                buttonenter15000.changeColor(pygame.mouse.get_pos())
                buttonenter15000.update()

                buttonenter20000.changeColor(pygame.mouse.get_pos())
                buttonenter20000.update()

                buttonenter25000.changeColor(pygame.mouse.get_pos())
                buttonenter25000.update()

                buttonenter30000.changeColor(pygame.mouse.get_pos())
                buttonenter30000.update()

                buttonenter35000.changeColor(pygame.mouse.get_pos())
                buttonenter35000.update()

                buttonenter40000.changeColor(pygame.mouse.get_pos())
                buttonenter40000.update()

                buttonenter45000.changeColor(pygame.mouse.get_pos())
                buttonenter45000.update()

                buttonenter50000.changeColor(pygame.mouse.get_pos())
                buttonenter50000.update()
            return button_list

        
                

        def check_endgame(hand_act, deal_score, play_score, result, totals, add):
            
                
    
            if not hand_act and deal_score >= 17:
                if play_score > 21:
                    result = 1
                    
                    
                elif deal_score < play_score <= 21 or deal_score > 21:
                    result = 2
                    
                    
                    
                    
                elif play_score < deal_score <= 21:
                    result = 3
                    
                    
                else:
                    result = 4

                
                    
                if add:
                    if result == 1 or result == 3:
                        totals[1] += 1
                        losses()
                        pygame.mixer.Channel(39).play(pygame.mixer.Sound('boo-36556.mp3'))

                        def displayBlackjackLosses():

                            #Display earnings on start screen, if file which money is stored doesn't exist then
                                # a file is created.

                            try:
                                with open('blackjackLOSSES.txt') as f:
                                    current_losses = f.readline()

                                #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                                #screen.blit(total_earnings, (870,80))

                            except:
                                #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                                #screen.blit(total_earnings, (870,30))

                                with open('blackjackLOSSES.txt', 'w') as f:
                                    f.write(str(1))

                        def increaseBlackjackLosses():
                

            

                             with open('blackjackLOSSES.txt') as f:
                                current_losses = f.readline()
                                current_losses = int(current_losses)

                             if current_losses > 0 and current_losses < 100000:

                                with open('blackjackLOSSES.txt', 'w') as f:
                                    global new_losses
                                    new_losses = int(current_losses) + 1
                                    f.write(str(new_losses))

                        displayBlackjackLosses()
                        increaseBlackjackLosses()

                        
                        if chips[0] <= 0:
                                bust_screen()
                    elif result == 2:
                        totals[0] += 1
                        wins()
                        chips[2] = chips[1] * 2 #player won, doubles chips (2/1 Odds)
                        chips[0] = chips[0] + chips[2] #players total is increased
                        pygame.mixer.Channel(38).play(pygame.mixer.Sound('mixkit-coin-win-notification-1992.wav'))
                        pygame.mixer.Channel(48).play(pygame.mixer.Sound('player wins.mp3'))

                        def displayBlackjackWins():

                            #Display earnings on start screen, if file which money is stored doesn't exist then
                                # a file is created.

                            try:
                                with open('blackjackWINS.txt') as f:
                                    current_wins = f.readline()

                                #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                                #screen.blit(total_earnings, (870,80))

                            except:
                                #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                                #screen.blit(total_earnings, (870,30))

                                with open('blackjackWINS.txt', 'w') as f:
                                    f.write(str(1))

                        def increaseBlackjackWins():
                

            

                             with open('blackjackWINS.txt') as f:
                                current_wins = f.readline()
                                current_wins = int(current_wins)

                             if current_wins > 0 and current_wins < 100000:

                                with open('blackjackWINS.txt', 'w') as f:
                                    global new_wins
                                    new_wins = int(current_wins) + 1
                                    f.write(str(new_wins))

                        displayBlackjackWins()
                        increaseBlackjackWins()


                        
                        if chips[0] <= 0:
                                bust_screen()
                    else:
                        totals[2] += 1
                        draws()
                        chips[0] = chips[0] + chips[1]

                        def displayBlackjackDraws():

                            #Display earnings on start screen, if file which money is stored doesn't exist then
                                # a file is created.

                            try:
                                with open('blackjackDRAWS.txt') as f:
                                    current_draws = f.readline()

                                #total_earnings = info_font.render('Total Earnings: $' + str(current_earnings), False , "White")
                                #screen.blit(total_earnings, (870,80))

                            except:
                                #total_earnings = info_font.render('Total Earnings: $0', False , "Black")
                                #screen.blit(total_earnings, (870,30))

                                with open('blackjackDRAWS.txt', 'w') as f:
                                    f.write(str(1))

                        def increaseBlackjackDraws():
                

            

                             with open('blackjackDRAWS.txt') as f:
                                current_draws = f.readline()
                                current_draws = int(current_draws)

                             if current_draws > 0 and current_draws < 100000:

                                with open('blackjackDRAWS.txt', 'w') as f:
                                    global new_draws
                                    new_draws = int(current_draws) + 1
                                    f.write(str(new_draws))

                        displayBlackjackDraws()
                        increaseBlackjackDraws()


                        
                    add = False
            return result, totals, add

        run = True
        while run:
            # run game at our framerate and fill screen with bg color
            timer.tick(fps)
            screen.blit(mainbackground,(0,0))
            # initial deal to player and dealer
            if initial_deal:
                for i in range(2):
                    my_hand, game_deck = deal_cards(my_hand, game_deck)
                    dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
                initial_deal = False
            # once game is activated, and dealt, calculate scores and display cards
            if active:
                player_score = calculate_score(my_hand)
                draw_cards(my_hand, dealer_hand, reveal_dealer)
                if reveal_dealer:
                    dealer_score = calculate_score(dealer_hand)
                    if dealer_score < 17:
                        dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
                draw_scores(player_score, dealer_score)
            buttons = draw_game(active, records, outcome)

            # event handling, if quit pressed, then exit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                        buttonenter1000.checkForInput1000(pygame.mouse.get_pos())
                        buttonenter3000.checkForInput3000(pygame.mouse.get_pos())
                        buttonenter4000.checkForInput4000(pygame.mouse.get_pos())
                        buttonenter5000.checkForInput5000(pygame.mouse.get_pos())
                        buttonenter10000.checkForInput10000(pygame.mouse.get_pos())
                        buttonenter15000.checkForInput15000(pygame.mouse.get_pos())
                        buttonenter20000.checkForInput20000(pygame.mouse.get_pos())
                        buttonenter25000.checkForInput25000(pygame.mouse.get_pos())
                        buttonenter30000.checkForInput30000(pygame.mouse.get_pos())
                        buttonenter35000.checkForInput35000(pygame.mouse.get_pos())
                        buttonenter40000.checkForInput40000(pygame.mouse.get_pos())
                        buttonenter45000.checkForInput45000(pygame.mouse.get_pos())
                        buttonenter50000.checkForInput50000(pygame.mouse.get_pos())

                if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                blackjack_menu()
                        
                    
                if event.type == pygame.MOUSEBUTTONUP:
                    if not active:
                        if buttons[0].collidepoint(event.pos):
                            active = True
                            initial_deal = True
                            game_deck = copy.deepcopy(decks * one_deck)
                            my_hand = []
                            dealer_hand = []
                            outcome = 0
                            hand_active = True
                            reveal_dealer = False
                            outcome = 0
                            add_score = True
                    else:
                        # if player can hit, allow them to draw a card
                        if buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                            my_hand, game_deck = deal_cards(my_hand, game_deck)
                        # allow player to end turn (stand)
                        elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                            reveal_dealer = True
                            hand_active = False
                        elif len(buttons) == 3:
                            if buttons[2].collidepoint(event.pos):
                                active = True
                                initial_deal = True
                                game_deck = copy.deepcopy(decks * one_deck)
                                my_hand = []
                                dealer_hand = []
                                outcome = 0
                                hand_active = True
                                reveal_dealer = False
                                outcome = 0
                                add_score = True
                                dealer_score = 0
                                player_score = 0

                if hand_active and player_score >= 21:
                        hand_active = False
                        reveal_dealer = True

                outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)

                pygame.display.flip()
        pygame.quit()


        
        

        

        

        
        
        
                                

global chips
chips = [41000, 0, 0] #[0] = current chips, [1] = chips betted, [2] = chips earned
         

        
global mainbackground
global blackjackgreen_background
global blackjackblue_background
global blackjackred_background
global blackjackdarkgreen_background
global blackjackorange_background
global blackjackpurple_background
global blackjackblack_background
global blackjackaqua_background
global blackjackwhite_background
blackjackgreen_background = pygame.image.load("Blackjack Backround main.PNG")
blackjackblue_background = pygame.image.load("blue blackjack table.PNG")
blackjackred_background = pygame.image.load("red blackjack table.PNG")
blackjackorange_background = pygame.image.load("actual orange blackjack table.PNG")
blackjackdarkgreen_background = pygame.image.load("orange blackjack table.PNG")
blackjackpurple_background = pygame.image.load("purple blackjack table.PNG")
blackjackblack_background = pygame.image.load("black blackjack table.PNG")
blackjackaqua_background = pygame.image.load("aqua blackjack table.PNG")
blackjackwhite_background = pygame.image.load("white blackjack background.PNG")
mainbackground = blackjackblue_background


mixer.music.load('mixkit-game-level-music-689.wav')
pygame.mixer.music.play(loops=-1)
mixer.music.set_volume(0.1)        
        
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jack of Hearts")

FONT = pygame.font.SysFont("Roboto", 100)

# Clock
CLOCK = pygame.time.Clock()

# Work
WORK = 10000000

# Loading BG
LOADING_BG = pygame.image.load("Loading Bar Background (2).png")
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))

# Loading Bar and variables
loading_bar = pygame.image.load("Loading Bar.png")  #Loading Bar.png
loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
	# Do some math WORK amount times
	global loading_finished, loading_progress

	for i in range(WORK):
		math_equation = 523687 / 789456 * 89456
		loading_progress = i


	loading_finished = True
	return loading_finished

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

if loading_finished == True:
        pygame.quit()
	



# Thread
threading.Thread(target=doWork).start()

time = 1


pygame.time.set_timer(pygame.USEREVENT, 2000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            time -= 1
            if time == 0:
                main_menu()


		

    
    screen.fill("black")
    #background = pygame.image.load("Pick Your Game Menu Screen.PNG")
    #screen.blit(background, (0,0))
    logo = pygame.image.load("Jack of Hearts Logo (White).png")
    screen.blit(logo, (10, 10))
            

    loading_bar_width = loading_progress / WORK * 720

    loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
    loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))

    

    screen.blit(LOADING_BG, LOADING_BG_RECT)
    screen.blit(loading_bar, loading_bar_rect)
    

            

    pygame.display.update()
    CLOCK.tick(60)





#NEXT STEP MAKE THE USERNAME AND PASSWORD LOGINS ON SERPATE SCREEN WITH SAME BACKGROUND

        

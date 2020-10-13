
#!/usr/bin/python
# Piandora resolution set at  640x430
# This is to be used with a 3.5" HDMI touchscreen or larger
# Tested with the Raspberry pi 2 and raspbian stretch
# The program must be run within the Lxterminal.
# copyright (C) Granpino
# Rev1.0 by Granpino

import sys, pygame
from pygame.locals import *
import time
import datetime
import subprocess
import os
#import requests 

pygame.init()
line1 = "Raspberry pi"
line2 = "Piandora"
play_time = 0
duration = 180
xy = 3

cyan = 50, 255, 255
blue = 26, 0, 255
black = 0, 0, 0
white = 255, 235, 235
red = 255, 0, 0
green = 0, 255, 0
silver = 192, 192, 192
gray = 40, 40, 40

#other

clock = pygame.time.Clock()
subprocess.call("echo  's0' > /home/pi/.config/pianobar/ctl", shell=True)
play = True
STA0 = True
STA1 = False
STA2 = False
STA3 = False
STA4 = False
STA5 = False
STA6 = False
STA7 = False
volume = 70
cover_img = ('cover.jpg')
connection = None

#set size of the screen
size = width, height = 640, 430
### change screen mode for debugging
#screen = pygame.display.set_mode(size) #,pygame.FULLSCREEN)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

#define function that checks for mouse location
def on_click():
	# exit has been pressed
	if 550 < click_pos[0] < 620 and 18 < click_pos[1] < 64:
		print "You pressed exit" 
		button(0)
	# play was pressed
	if 139 <= click_pos[0] <= 261 and 18 <= click_pos[1] <=53:
		print "You pressed  play"
		button(1)

	# station 0  was pressed
	if 18 <= click_pos[0] <= 138 and 333 <= click_pos[1] <370:
		print "You pressed STA0"
		button(2)

	# station 1 was pressed
	if 138 <= click_pos[0] <= 259 and 333 <= click_pos[1] <=370:
		print "You pressed STA1"
		button(3)

	# station 2  was pressed
	if 259 <= click_pos[0] <= 380 and 333 <= click_pos[1] <=370:
		print "You pressed  STA2"
		button(4)
	
	 # next  was pressed
	if 272 <= click_pos[0] <= 382 and 18 <= click_pos[1] <=53:
		print "You pressed button next"
		button(5)

	 # volume down 6 was pressed
	if 500 <= click_pos[0] <= 620 and 380 <= click_pos[1] <= 417:
		print "You pressed volume down"
		button(6)

	 # volume up 7 was pressed
	if 500 <= click_pos[0] <= 620 and 333 <= click_pos[1] <=370:
		print "You pressed volume up"
		button(7)

	 # station 3 was pressed
	if 379 <= click_pos[0] <= 500 and 333 <= click_pos[1] <=370:
		print "pressed STA3"
		button(8)

	 # station 4 was pressed
	if 20 <= click_pos[0] <= 139 and 380 <= click_pos[1] <=417:
		print "You pressed STA4"
		button(9)

     # station 5 was pressed
	if 138 <= click_pos[0] <= 259 and 380 <= click_pos[1] <=417:
		print "You pressed STA5"
		button(10)

     # station 6 was pressed
	if 259 <= click_pos[0] <= 380 and 380 <= click_pos[1] <=417:
		print "You pressed STA6"
		button(11)

     # station 7 was pressed
	if 379 <= click_pos[0] <= 500 and 380 <= click_pos[1] <=417:
		print "You pressed STA7"
		button(12)

      # station like was pressed
	if 20 <= click_pos[0] <= 139 and 18 <= click_pos[1] <=53:
		print "You pressed like"
		button(13)

      # station no-like was pressed
	if 379 <= click_pos[0] <= 500 and 18 <= click_pos[1] <=53:
		print "You pressed nolike"
		button(14)

#define action on pressing buttons
def button(number):
	global album_img
	global play
	global x
	global STA0
	global STA1
	global STA2
	global STA3
	global STA4
	global STA5
	global STA6
	global STA7
	global volume
	print "You pressed button ",number

	if number == 0:    #time to  exit
		font = pygame.font.SysFont('sans', 20, bold=0)
		btn_label1 = font.render("Exit", 1, (white))
		btn_label2 = font.render("Shutdown", 1, (white))
		while 1:
			pygame.draw.rect(screen, white, (69, 197, 541, 113),0)
			pygame.draw.rect(screen, gray, (359, 255, 110, 40),0)
			pygame.draw.rect(screen, gray, (492, 255, 110, 40),0)
			screen.blit(btn_label1,(399, 262))
			screen.blit(btn_label2,(505, 262))
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					click_pos = pygame.mouse.get_pos()
					if 359 < click_pos[0] < 465 and 255 < click_pos[1] < 295:
						subprocess.call("echo -n 'q' > /home/pi/.config/pianobar/ctl", shell=True)
						sys.exit()
					if 492 < click_pos[0] < 598 and 255 < click_pos[1] < 295:

						pygame.display.flip()
						subprocess.call("echo -n 'q' > /home/pi/.config/pianobar/ctl", shell=True)
						os.system("sudo shutdown -h now")
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE: # ESC to exit
						subprocess.call("echo -n 'q' > /home/pi/.config/pianobar/ctl", shell=True)
						sys.exit()
			pygame.display.flip()
		time.sleep(1)
		pygame.display.flip()

	if number == 1: # play / pause
		if play == True:
			subprocess.call("echo -n 'p' > /home/pi/.config/pianobar/ctl", shell=True)

			play = False
		else:
			subprocess.call("echo -n 'p' > /home/pi/.config/pianobar/ctl", shell=True) 
			play = True
		refresh_menu_screen()

	if number == 2: # Station 0.
		subprocess.call("echo  's0' > /home/pi/.config/pianobar/ctl", shell=True)
		STA0, STA1, STA2, STA3, STA4, STA5, STA6, STA7 = True, False, False, False, False, False, False, False
		refresh_menu_screen()

	if number == 3: # Station 1
		subprocess.call("echo 's1' > /home/pi/.config/pianobar/ctl", shell=True)
		STA0, STA1, STA2, STA3, STA4, STA5, STA6, STA7 = False, True, False, False, False, False, False, False
		refresh_menu_screen()

	if number == 4: #station 2
		subprocess.call("echo 's2' > /home/pi/.config/pianobar/ctl", shell=True)
		STA0, STA1, STA2, STA3, STA4, STA5, STA6, STA7 = False, False, True, False, False, False, False, False
		refresh_menu_screen()

	if number == 5:
		subprocess.call("echo -n 'n' > /home/pi/.config/pianobar/ctl", shell=True)
		play = True
		refresh_menu_screen()
	
	if number == 6: # volume down
		if volume < 11:
			volume = 10
		else:
			subprocess.call("echo -n '((((' > /home/pi/.config/pianobar/ctl", shell=True)
			volume = volume - 10
			refresh_menu_screen()
	
	if number == 7:  # volume up
		if volume > 99:
			volume = 100
		else:
			subprocess.call("echo -n '))))' > /home/pi/.config/pianobar/ctl", shell=True)
			volume = volume + 10
	
    #    amixer -c0 set PCM 1% ----will not work with bluetooth
    #	 amixer -q -M sset PCM 50%
		refresh_menu_screen()

	if number == 8:  # station 3
		subprocess.call("echo 's3' > /home/pi/.config/pianobar/ctl", shell=True)
		STA0, STA1, STA2, STA3, STA4, STA5, STA6, STA7 = False, False, False, True, False, False, False, False
		refresh_menu_screen()

	if number == 9: #station 4
		subprocess.call("echo 's4' > /home/pi/.config/pianobar/ctl", shell=True)
		STA0, STA1, STA2, STA3, STA4, STA5, STA6, STA7 = False, False, False, False, True, False, False, False
		refresh_menu_screen()

	if number == 10:  # station 5
		subprocess.call("echo 's5' > /home/pi/.config/pianobar/ctl", shell=True)
		STA0, STA1, STA2, STA3, STA4, STA5, STA6, STA7 = False, False, False, False, False, True, False, False
		refresh_menu_screen()

	if number ==11: #station 6
		subprocess.call("echo 's6' > /home/pi/.config/pianobar/ctl", shell=True)
		STA0, STA1, STA2, STA3, STA4, STA5, STA6, STA7 = False, False, False, False, False, False, True, False
		refresh_menu_screen()

	if number ==12: #station 7
		subprocess.call("echo 's7' > /home/pi/.config/pianobar/ctl", shell=True)
		STA0, STA1, STA2, STA3, STA4, STA5, STA6, STA7 = False, False, False, False, False, False, False, True
		refresh_menu_screen()

	if number ==13: #Like
		subprocess.call("echo -n '+' > /home/pi/.config/pianobar/ctl", shell=True)
		refresh_menu_screen()

	if number ==14: # noLike
		subprocess.call("echo -n '-' > /home/pi/.config/pianobar/ctl", shell=True)
		refresh_menu_screen()

def get_tags():
    global line1
    global line2
    global play_time
    global duration
    global play_time
    global play
    file1 = open("data.txt","r+")
    lines = file1.readline().split(" | ")
    line1 = lines[0]
    line2 = lines[1]
    line2 = line2[:54]
    line3 = lines[2] # start song
    duration = lines[3] # song duration
    if line3 == "rst":
        play_time = 0

    if play == True:
        play_time = play_time + 4
#    print(play)
#    print(int(play_time))
Lfont = pygame.font.Font(None,70)
Mfont = pygame.font.Font(None,32)
M2font = pygame.font.Font(None,40)
Sfont = pygame.font.Font(None,28)
skin1=pygame.image.load("buttons.png")
skin2=pygame.image.load("640x430.png")
def refresh_menu_screen():
	global connect_img
	global CurrPlaylist
	global line1
	global volume
	global play_time
	global duration
	global xy
	current_time = datetime.datetime.now().strftime('%I:%M')
	seconds = datetime.datetime.now().strftime('%S')
	time_label = Lfont.render(current_time, 1, (white))
	sec_label = Mfont.render(seconds, 1, (white))

	Header=M2font.render("Piandora", 1, (white))
	screen.blit(skin2,(0,0))
	screen.blit(skin1,(0,0))
	screen.blit(Header,(250, 72))
	pygame.draw.rect(screen, gray, (463, 110, 155, 49),0)
	screen.blit(time_label,(465, 110))
	screen.blit(sec_label, (590, 115))

	try:
		album_art=pygame.image.load(cover_img) # album art
		album_art=pygame.transform.scale(album_art, (200,150 ))
		screen.blit(album_art,(21,74))
	except pygame.error:
		time.sleep(1)

	#=========================================================
		##### display artist and song ####: 
	song_name=Sfont.render(line1, 1, (white))
	artist=Sfont.render(line2, 1, (white))
	duration_label=Mfont.render(str(duration), 1, (white))
	screen.blit(song_name,(70,241))
	screen.blit(artist,(70,281))
	screen.blit(duration_label, (250, 145))

		### add volume number
	volume_tag=Mfont.render(str(volume) + "%", 1, (white))
	screen.blit(volume_tag,(250,107))

	### the math #####
	# size of bar in pixels= 615 - 240 
	# ratio of bar to seconds = (615-240) / duration 
	# song time = seconds * ratio
	# offset = 240
	ratio = float(375.0 / int(duration))
	ratio = ("%.2f" % round(ratio, 2))	
#	print(ratio)
	play_time = float(play_time)
	ratio = float(ratio)
#	print(play_time)
#	print(type(play_time))
#	print(type(ratio))
	y = (play_time * ratio)
#	print(y)
	y = round(y)
#	print(y)
	xy = (240 + y)
	if xy >= 615: # pause bargraph
		xy = 615

	pygame.draw.line(screen, gray, (240,220), (615, 220), 10)
	pygame.draw.line(screen, green, ((xy), 220), (615, 220), 10)

	if STA0 == True:
		screen.blit(M2font.render('1',1, green), (98, 340))
	else: 
		screen.blit(M2font.render('1',1, white), (98, 340))
	if STA1 == True:
		screen.blit(M2font.render('2',1, green), (220, 340))
	else:
		screen.blit(M2font.render('2',1, white), (220, 340))
	if STA2 == True:
		screen.blit(M2font.render('3',1, green), (340, 340))
	else:
		screen.blit(M2font.render('3',1, white), (340, 340))
	if STA3 == True:
		screen.blit(M2font.render('4',1, green), (460, 340))
	else:
		screen.blit(M2font.render('4',1, white), (460, 340))
	if STA4 == True:
		screen.blit(M2font.render('5',1, green), (98, 385))
	else:
		screen.blit(M2font.render('5',1, white), (98, 385))
	if STA5 == True:
		screen.blit(M2font.render('6',1, green), (220, 385))
	else:
		screen.blit(M2font.render('6',1, white), (220, 385))
	if STA6 == True:
		screen.blit(M2font.render('7',1, green), (340, 385))
	else:
		screen.blit(M2font.render('7',1, white), (340, 385))
	if STA7 == True:
		screen.blit(M2font.render('8',1, green), (460, 385))
	else:
		screen.blit(M2font.render('8',1, white), (460, 385))

	pygame.display.flip()


def main():
    global click_pos
    global line1
    timer = pygame.time.get_ticks()
    while True:
        seconds = (pygame.time.get_ticks() - timer)/1000
        if seconds > 3:
            timer = pygame.time.get_ticks()
#            print("getting media info every 3s")
            get_tags()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                print "screen pressed" #for debugging purposes
                print click_pos #for checking coordinates
                on_click()

            #Press ESC key on the computer to end while in VNC
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # ESC key will kill it
                    sys.exit()
        clock.tick(10) # refresh 
        refresh_menu_screen()

refresh_menu_screen() 
main() # Main loop



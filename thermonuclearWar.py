#!/usr/bin/python

import curses

# First set up the screen, turn off echo of commands and print out the opener.
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
screen.border(0)
screen.addstr(2, 2, "Shall we play a game?")
screen.addstr(4, 4, "1 - Yes")
screen.addstr(6, 4, "2 - No")
screen.addstr(10, 4, "You may exit the program at any time by pressing \"q\"")

event = None

# Note: the "ord" function allows you to use characters for comparisons, otherwise you have to use the ascii values directly. 

while True and event != ord('q'): 
	# Gather the keystrokes by "getch'ing"
   	event = screen.getch() 
   
   	#if event == ord("q"): break 
	if event == ord("1"): 
		screen.clear() 
      		screen.border(0)
      		screen.addstr(2, 2, "Which game would you like to play?")
      		screen.addstr(4, 4, "1 - Thermonuclear War")
	
		insideEvent = screen.getch()
		if insideEvent == ord('1'):
			screen.clear()
			screen.border(0)
			screen.addstr(2, 2, "Excellent, now let us begin...")
			screen.addstr(4, 2, "This game is quite simple, do you wish to strike first or second?")
			screen.addstr(6, 4, "1 - First")
			screen.addstr(8, 4, "2 - Second")
			
			reallyInsideEvent = screen.getch()
			if reallyInsideEvent == ord('1') or reallyInsideEvent == ord('2'):
	                        screen.clear()
	                        screen.border(0)
        	                screen.addstr(2, 2, "First or second, there is no winner in Thermonuclear War.")
                	        screen.addstr(4, 2, "Alas, we have both lost this game.  Perhaps next time we should play a nice game of chess.")
				screen.addstr(6, 2, "Press 1 to start again or q to exit.")

				# Should we grab the output so that you don't go back in the menus?

			elif reallyInsideEvent == ord('q'): break
		elif insideEvent == ord('q'): break		
	elif event == ord('2'): break


# Exit the menu and return to the cursor
curses.endwin()

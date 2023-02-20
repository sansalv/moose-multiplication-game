import time
import random
import os
	
def main():
	
	os.system('cls' if os.name =='nt' else 'clear') # Clear terminal
	
	print('Welcome to the Moose Multiplication Game!')
	print(giveAward('moose0'))
	
	c = 'y'
	
	time.sleep(1)
	r = str(input('\nDo you want to use the default range (2-99)? (y/n)\n'))
	
	if r == 'y':
		minim = 2
		maxim = 99
	else:
		minim = int(input('Enter minimum number:\n'))
		maxim = int(input('Enter maximum number:\n'))
	
	while c == 'y':
		
		os.system("cls" if os.name == "nt" else "clear") # Clear terminal
		
		a = random.randint(minim, maxim)
		b = random.randint(minim, maxim)
		ans = a*b
		
		t_init = time.time()
		
		guess = int(input(f'What is {a} * {b} ?\n'))
		
		while guess != ans and guess != 0:
			guess = int(input(f'\nWrong... Try again\n'))
			if guess == 0:
				break
		if guess == 0:
			print(f'\nYou gave up.\nThe correct answer was {ans}.')
		else:
			t_end = time.time()
			t = round(t_end-t_init,1)
			print(f'\nCorrect! Your time was {t} seconds.')
			if t < 10:
				print(giveAward('bat'))
			elif t >= 10 and t < 20:
				print(giveAward('elephant'))
			else:
			 	print(giveAward('moose'))
		
		c = str(input('\nContinue? (y/n)\n'))
		
	os.system('cls' if os.name =='nt' else 'clear') # Clear terminal
	
	
def giveAward(award):

	moose0 = '''
 ___            ___
/   \          /   \ 
\_   \        /  __/ 
 _\   \      /  /__
 \___  \____/   __/ 
     \_       _/ 
       | @ @  \_
       |
     _/     /\ 
    /o)  (o/\ \_
    \_____/ /
      \____/'''

	moose1 = '''
You got over 20 seconds.
Here's a moose.''' + moose0

	bat1 = '''
 _______________________________________________________________________
|                                                                       |
|                       You got sub 10 seconds.                         |
|                       Here's your award, a bat.                       |
|        ,*-~"`^"*u_                                _u*"^`"~-*,         |
|     p!^       /  jPw                            w9j \        ^!p      |
|   w^.._      /      "\_                      _/"     \        _.^w    |
|        *_   /          \_      _    _      _/         \     _*        |
|          q /           / \q   ( `--` )   p/ \          \   p          |
|          jj5****._    /    ^\_) o  o (_/^    \    _.****6jj           |
|                   *_ /      "==) ;; (=="      \ _*                    |
|                    `/.w***,   /(    )\   ,***w.\`                     |
|                     ^ ilmk ^c/ )    ( \c^      ^                      |
|                             'V')_)(_('V'                              |
|                                 `` ``                                 |
|_______________________________________________________________________|'''
	
	elephant1 = '''
 _______________________________________
|                                       |
|      You got sub 20 seconds.          |
|   Here is your award, an elephant.    |
|                         ____          |
|                    .---'-    \        |
|       .-----------/           \       |
|      /           (         ^  |   __  |
| &   (             \        O  /  / .' |
| '._/(              '-'  (.   (_.' /   |
|      \                    \     ./    |
|       |    |       |    |/ '._.'      |
|        )   @).____\|  @ |             |
|    .  /    /       (    | mrf         |
|   \|, '_:::\  . ..  '_:::\ ..\).      |
|_______________________________________|'''

	if award == 'elephant':
		return elephant1 
	elif award == 'bat':
		return bat1
	elif award == 'moose':
		return moose1
	else:
		return moose0

if __name__ == '__main__':
    main()
		


# MastermindMadness
A game of Mastermind in Python with a GUI

This was made in 2007 using a graphics package from a book by John Zelle. It was my final project for an Intro to Python class.

There are several pieces that can be improved, some easy, some not.

1. The windows should pop to front instead of being hidden behind.
2. Window for new game should stay in same location, but instead it re-initializes window completely.
3. If you don't fill in the black/white dots correctly, it will get stuck in infinite loop.
4. I made it so the player writes the code on paper and the computer guesses. I wanted to make a box so user could
   set the code to guess, but I didn't want people to think the computer was simply looking at their code. 
   But it would be cool for user to have a separate little window to make their code just for reference
5. The initial guess is always four different colors, but as my CS instructor pointed out, it may be statistically
   advantageous if the initial guess is not four different colors. I don't know, but the initial guess should probably
   be more random.
   

I've always been particularly proud of this program. It does a good job playing the game and it took me a long time to get
it to play as well as it does. However, years later I'm a bit overwhelmed trying to understand the process from so many years 
ago. I'm sure there is an easier, more efficient way to guess the codes. Essentially, it randomly creates guess until it 
creates a guess that could be possible based on the previous user feedback. It's near instantaneous because of the 
available computing power, but who knows how many random guesses it creates until it finds a suitable one. 


Thanks!

Jeff

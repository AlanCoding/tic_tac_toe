### Alan and ChatGPT write tic tac toe

This is a demo of me working together with ChatGPT to write a game.

Importantly, this is doing it using a library that I have never used myself.

#### Setup

You need python 3.10. Preferably, do:

```
python3.10 -m venv env
source env/bin/activate
```

This is just me that figured that out, I read the docs.
I don't know if / how ChatGPT could ever assist with that kind of problem.
Just saying...

#### Run

This isn't fancy. It assumes it's a 2-player game, which isn't really that fun.

```
python tic_tac_toe.py
```

But it works, and it's not outright painful to use.
It conforms to the most basic of user expectations.

#### Weird Stuff

The strangest thing I had to edit that ChatGPT wrote, was that it _only_
drew a rectangle separating the game spaces if neither an X or O had been
placed in that spot.
That meant that when you placed an X, the border would decrease, and
with more placements, the border would go away.

Is that a true bug? Eeeeh, yeah.
Might a human have introduced the same bug?
Yeah, but they would have played it and seen it become totally obvious.

It also wanted to close the window in the game loop right after a player won.
This is never ever how a real video game would work.
It's still maybe arguably correct in a Computer Science 101 test answer kind of way.

# Pygame Slots
#### Pygame-based slot machine with easily changeable symbols, sound effects, and music.

## Demos
#### Graphics/music included in this Github repo:

https://user-images.githubusercontent.com/98667270/189539691-6cc22c1d-d719-4339-9889-77163738a07d.mp4

#### Licensed symbols via Adobe Stock and additional sound effects via Google search:

https://user-images.githubusercontent.com/98667270/189508033-ac361229-e493-44d3-a441-e075d22c3ddb.mp4

## Features

- Five reels, each with three symbols in play at any given time
- 300x300 png image symbols that are easy to change via Python dictionary
- Easy-to-import audio (commented out by default)
- Basic win animation
- Basic UI

## Tech

Basically just Pygame:

- [Pygame] - Python game library
- Images/Music/Sound effects

## Installation

Pygame and Python3 are required, as well as the [kidspace.ttf] font in graphics/font/

```sh
pip install -r requirements.txt
```

From cmd/PowerShell:

```sh
python main.py
```

## Media

I have provided some basic symbols that don't look great but they work well enough.  You can simply add a new directory and create a new symbol dictionary in settings.py to replace them.  Same with audio files!  See comments throughout for more info.

## Win Data
win_data is formatted as such:  
`{1: ['symbol_1', [1, 2, 3]], 3: ['symbol_2', [0, 1, 2]]}` 

## Future Development
I will probably try to recreate this in an actual game engine at some point.  Potential future work includes:
- Better animations
- More win scenarios
- Simulations
- Web version

## Thanks
[Clear Code]: If you are new to Pygame, you need to watch Clear Code's videos.  They are incredible!  
Additionally, I had some help on delta_time/animation staggering as well as the music from two of my friends - thank you!
## License

[Creative Commons 0 License]

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [Pygame]: <https://www.pygame.org/docs/>
   [Creative Commons 0 License]: <https://creativecommons.org/share-your-work/public-domain/cc0/>
   [Clear Code]: <https://www.youtube.com/c/ClearCode>
   [kidspace.ttf]: <https://www.dafont.com/kidspace.font>

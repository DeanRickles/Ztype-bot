# Ztype with OpenCV
```
Script to automate playing Ztype on the screen.
```

# To Do:

Key:
```diff 
- = Planned
+ = Completed
| = On-hold
x = Scrapped
```

ToDo:
```diff
+ Get text from screen. (Using B/W with colour mask.)
    - Rename to package to AlterImage

- Readword.
    - OCR on screen.
    - place strings into list.

- Ignore Text from the bottom of screen. ("Type the words to hoot!" & "ENTER for EMP")

- CaptureGame live on screen.
    - set detection area.
    - detected words into List type.
        - Compare with typing out current list vs scanning after each word.

- TypeWord(string list input)
    - closes first or smallest.
    - type word.
    - check if there is a spelling error or miss type.
    
- Testing
    - each package as a module.
    - Docker enviroment (for consistancy.)
    - Misc workstations
```

# Perosnal Note

```
• I'm using this project to learn what OpenCV can do, and become a Ztype winner.
• I forsee this project to go over a number of iterations.
• Do I add the time each time a Todo is completed?
```
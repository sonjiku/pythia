# PythiaRG

> SOME OF THIS INFO IS OUTDATED. THE PROJECT IS UNDERGOING A REWRITE WHICH WILL MAKE IT WAY EASIER TO CONFIGURE YOUR OWN RANDOM GENERATORS.

## Oracle and Random Generator
**pythiarg** is a cli tool that you can use to randomly generate ***stuff*** fast. What kind of stuff can you generate? Pretty much anything.
I made **pythiarg** as a tool to use with my TTRPG games and worldbuilding. 
IMHO best part about `pythiarg` is how modular it is! PythiaRG doesn't let you "generate" what you want? You can have a look at how easy it is [hacking pythiarg to do your bidding](##Hacking-pythiarg) below.


## Installation
1. Install with pip


## Example usage
```
#>pythiarg evank -p

=========
AVAILABLE PRESETS
---------
1: presetFood
2: presetClothing
3: presetCustomDungeon
4: presetCustomPotion
5: presetHexCrawl
=========


#>pythiarg evank -p presetCustomPotion

Custom Potion Recipe: 
Ingredients: 6 Last breath, 5 Killer’s hand, 5 Larkspur, 2 Witch hazel
Potion of Spider tail
Color: Ultramarine
Scent: Bitter
Taste: Sulphur
Texture: Frigid


#>pythiarg evank -p 1

Food: Undercooked Orange
```


## Hacking pythiarg
### Why would I want to do this?
While `pythiarg` should offer you almost anything that you might need for creating adventures set in a fantasy setting, you might want to use it to generate a character using specific rules from your TTRPG of choice. Maybe you are a Game Master, and want to randomly generate a dungeon for your players to explore, or a musician that can't decide which song they're going to start learning next. Whatever the reason may be, randomness can be very fun -sometimes funny- and very useful for a creative person!

If you are not going to need random **things** often, and specifically **things** that you cannot find already in this software, you may decide it is not really worth your time hacking at this

### How do I go about doing this?
pythiarg is written in *Python*. Python is an easy to learn programming language but in all honesty you won't be doing any more programming throughout this process than a kid does making a drawing by filling in colouring books. PythiaRG is written in a way where it is very modular and easy to append to. Just follow this simple recipe:
1. Make a copy of `template.py`.
1. Rename the file to something better and easily memorable.
1. Make your tables inside of the file by following the instructions.
1. Double check everything.
1. Import your tables in `__main__.py`
1. Copy the **arguments def template**, uncomment it and edit it appropriately.
1. Copy the **arguments parser template**, uncomment it and edit it appropriately.
1. Open a command prompt on the directory of the project.
1. Run `python __main__.py -h`
1. If you don't see the *help message* and instead see errors, then you truly need help. Start by checking spelling and missed quotes or commas. Otherwise, try running the command with the arguments you just made.
1. ???
1. Profit.

#### More info

The `template.py` file contains comments explaining everything relevant to making your tables to to help you throughout the process. "Tables" in this context are just lists of stuff formatted in a specific way. Could be a list of songs, colors, tastes, movies, or some oracle or random tables from your favorite TTRPG. If you want to do the last thing, having a copy of the `.pdf` version of the book and using *ChatGPT* to transform the table that you copied into the format we need can be ridiculously faster than just writing every element of the list, one by one. More info in regards to that can be found on the `template.py` file.

After you've made your **"tables"** it's time to make your ***"Table of Tables"***. This part is really important. Make sure there are no typos in the table names anywhere. If the program doesn't run as it you think it should, you most likely have made a spelling mistake somewhere, are missing a comma, parenthesis, quote or bracket.

Editing `__main__.py` could be ridiculously faster than the other file, depending on the amount and sizes of the tables you made.

#### Advanced

### Tables that point to other tables
If you follow the instructions in the `template.py` correctly, you should be able to make it so an element of a list points to another list. Due to the way pythiarg is written, if the element contains a string that matches the **key** of another "table" in your "table of tables", then `pythiarg` will fetch a random element from that table.
This can happen an indefinite amount of times and there are no protections to prevent pythiarg from going into an infinite recursive loop. This will leave her very confused. For your sake, I hope she doesn't get mad at you and lash out on any other programs in memory, though it is unlikely for that to happen.
### Presets
Using the previous bit of knowledge, we can create "Presets". For an example you could try running `python __main__.py spyt --preset potionseller` or `python __main__.py spyt --preset character`.
These two presets are a bit different implementation wise, but they both use the same concept of list elements that point to a random element from another list. Your friend might be happy with your d100 table of surnames, but you can have a dozen different surnames for your vivid character with hopes and dreams during the time it takes for you to roll the dice and look up the result on the table.
#### Implementation 1: Table combinations
The simplest implementation is a small random table that has a combination of words and links that point to different tables. For example, a surname table could be:
- *Name*+son
- *Color*
- *Occupation*
- *Adjective*+*Occupation*
- *Noun*+*Occupation*
- *Item*+man
- *Adjective*
- *Adjective*+*Adjective*
- *Adjective*+*Noun*
- *Noun*+*Noun*
- *Noun*
Now if we have 100 each of Names, Colors, Items, Adjectives and Nouns, we already have enough surnames for a small city in an island.
#### Implementation 2: Programming
Conditionals and loops can help us make some pretty interesting presets, but if you want to learn how to code in Python, then I suggest looking for a tutorial online, or do it the way I did and use [FreeCodeCamp](freecodecamp.org). #NotSponsored


## FAQ
>What is PythiarG?

**pythiarg** was created to be an *automated oracle*, and random *monster/character/item/city* generator for use with TTRPGs, or anything else really.

>Who is Pythia?

[Pythia](https://wikipedia.com/wiki/Pythia), **was** the oracle of Delphi. There are few people with that name.

>What is an automated oracle?

A glorified random list element selector.

>What happened to that ~~YOUTUBER'S_OSR_GAME~~ generator you made?

We don't talk about that here.

> While looking at your code/While using `pythiarg`, I noticed that your available lists are small and so the results predictable. Add more stuff.

Well you can make a **pull request** if you are so smart and creative yourself.

> Why did you make this instead of using the oracles you can find in ~~your choice of an awesome book with oracles or/and/orand random tables~~?

Because I enjoy wasting an amount of time from my life I do not want to disclose in order to save 10 seconds doing something that could be done in 1. Those seconds add up you know! Also, for the heck of it.

> Why use this instead of an online generator?

- You don't have internet.
- You want something you can customize
- You find it faster, simpler or easier to run a command than to use an online tool.
- What you want doesn't exist. (Yet?)
- Cause I made this for you. (And me.)

> I run the example command and I didn't get the result stated.

That's good.

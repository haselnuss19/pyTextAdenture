import random
import time
import webbrowser
#import scenario1

#the users name
userName = input("What´s your name? ")

# Prints a description of the first level in the game
print("""

Welcome to the 1st Level. This is just the begining!
You find yourself in a room. You don´t know who you are or where
you are. 
You wonder what this is. There is a candle on the floor, in front of it is a book. It´s too dark to see anything else.

You can navigate through the game by using the "look around" function, the rest is self explaining. you also have an inventory you can use by pressing "i" 

""")


#print leveldescription of 2nd Level
def LvL2():

  print("""
    
    
    Congratulations, you made it! (not that it was very hard tough... but still.) """
        )
  print("Now the real tower game begins")
  print(
    "You find yourself in a round room just like before, but there is a window at the west wall, and you see everything in the room. There isn´t much to see, just an old man in the middle of the room starring at You."
  )
  print(
    "\033[91m",
    "'Who are you? Are you one of the many trying to get to the top of the tower? Haha. But thats fine with me.'",
    "\033[0m")
  print(
    print(
      "\033[91m",
      "'I haven´t had a conversation in a long time and i would like some company, mabey you will stay here forever with me.'",
      "\033[0m"))
  print("\033[91m", "'Do you want to hear my riddle?' ", "\033[0m")


#prints description of 3rd LvL2
def LvL3():
  print("""
        
        
        The room looks same as the other ones. There is a big artful mirror in the middle of the room. There is a door again, but it has the size a mousehole. There is also a little window on the left wall."""
        )
  print(
    "A little bird appears on the mirror. He talks to you"
    "\033[37m",
    "'You don´t know it anymore? Ask the crow and give something therefor'",
    "\033[0m")


#Lvl4 description
def LvL4():
  print(
    """
  
  
  Your Head hurts. You try to get up but you are too weak. After a few seconds you can finaly look around. You appear to be in somewhat of a clockwork. A mighty drarf with a long beard appears in front of you now. On the second look you recognize him as the doll you jumped on before! You don´t really know what to do. suddenly he beginst speaking to you with a loud, deep voice: """,
    "\033[33m",
    "'Hello human. I am Durin, but that is not important right now. You shoulden´t be here. You were supposed to die in that other room. Somehow you got on my back and came in my kingdom, but i will allow it for one. You see, normally nobody gets further than Level 3. So be aware of the jet unkown challanges that will occur on you path. I WISH YOU LUCK.'",
    "\033[0m",
    " And as he finished the sentence, an axe appearce in his hands and he smashes it in the ground. From on Second to the other, you are in a Room again. There is a creature with only one hand and without a head in the corner and stares at you. It probably wants to talk to you. Threr is also a door at the end again, but it has a blue glammer."
  )


# Function to check if any word in a string is in uppercase
def is_word_upper(string):
  words = string.split()
  for word in words:
    if word.isupper():
      return True
  return False


#this function detects if the first word the player wrote is "go"
def when_input_go(action):
  words = action.split()
  if words[0].lower() == "go":
    return True
  return False


#this function checks if the player has "I" in a sentence so the shout count wont yell at him for nothing
def is_single_word_i(action):
  words = action.split()
  for word in words:
    if word == "I":
      return True
  return False


#this function tells the player that he/she/it can´t take a certain object
def take_object(object):
  print("You try to take the " + object +
        ", but some kind of force is holding it back.")


# #this function detects if a player wrote 2 statements in a row and tells him to stop beeing in such a rush
# def two_commands_at_once(action):
#     global statement_made
#     if statement_made > 1:
#         print("Stop it! Relax, everything is fine. Woah how can you be in such a hurry?      Just enjoy the game that's why it was made!           (You can´t enter two statements at      once.)")
#         statement_made = 0
#     else:
#         statement_made = 0


#this function detects if a player wrote 2 statements (3+ keywords) in a row and tells him to stop beeing in such a rush
def two_statements(action):
  words = action.split()
  count = 0
  for word in words:
    if word in keywords:
      count += 1
    else:
      pass
    if count > 3:
      print(
        "Stop it! Relax, everything is fine. Woah how can you be in such a hurry? Just enjoy the game that's why it was made!"
      )
      return True
  return False


#def IncompetenteStatement(variable):
#  if variable == 3:
#    return True
# return False

#My variables for diffrent events. Kinda self explaining

#how many times the player has heard the riddle in level 2
riddle_count = 0
#to detirmen wether or not the door in the 3rd level has been found
doorOpenLvL2 = False
#A little bool for LvL4
doorIsFree = False
#LvL4
InHole = False
#lvl4
symbolLvl4 = False
#lvl4
creatureLifes = True
#lvl4
wonRPS = False
#LvL4
RockPS = False
#LvL4
creatureSpoke1 = 0
#LvL4
wandOnFloor = False
#LvL4
creatureSpoke = False
#generates a number between 0 and 2
randomNumber = random.randint(0, 2)
#LvL4
voteLink = "https://de.surveymonkey.com/r/MLNCZSM"
#lvl4
#randomNumberDoor = random.randit(1, 5)
#lvl1
WhatCount = False
#LvL4
HoleButtonPressed = False
#lvl4
DoorIsBlocked = True
#You know it. Variable.For the Level 3.
CodeCount = 0
# Bonos Content Level 3
handInGlas = 0
#how many times the player has input something that isn´t part of the loop
HelpMeCount = 0
#to detect if the lighter is on the floor so the player can take it
LighterOnFloor = False
#how many times the olayer has gotten a hint
hintSaid = 0
#How many times the leveldescription on the 2nd Level has been printet so it doesent get printet twice
MassagePrintet = 0
#checks if the player has gone to the closet
ClosetCount = 0
#to kick the player if he/she/it swears
fuckCount = 0
#this variable is counting how many if/elif/else statements has been made (edit: its not used anymore)
statement_made = 0
#defines which words are keywords
keywords = [
  "candle", "book", "lighter", "closet", "fuck", "shit", "where am i",
  "search", "take", "read", "go", "look", "listen", "hint", "punch", "kill",
  "slap", "talk", "hello", "window", "inventory", "help", "yes", "no",
  "around", "mountain", "door", "give", "speak", "man", "tell", "grab", "pick",
  "creature", "mirror", "crow", "door", "light", "option", "enter", "climb",
  "press", "use", "ask", "12243", "orbit", "i", "inventory", "light", "hint",
  "riddle", "sorry", "take", "give", "open"
]
#counts how often the leveldiscription for the 3rd level have been called
PrintCount = 0
#how often you watched youself in the mirror LvL 3
mirrorCount = 0
#a count for how many times the crow has spoke to you(after interuduction)
crowSpoke = 0
#a count for how many times the crow has spoke to you(after interuduction)
crowSpoke_ = 0
#to detect in wich level the player is currently in
LevelCount = 0
#how many wrong answers to the riddle the player has made
FalseAnwser = 0
#how many hints the player has taken
hintCount = 0
#So the consol wont output the shoutstatement twice
ShoutCount = 0
#players inventory
inventory = []
#checks if the 1st room is lit
roomIsLit = False
#loop + try for EOF error
startTime = time.time()
while True:

  try:
    action = input("\033[32m>\033[0m \033[32m")

    print("\033[0m")

    if is_word_upper(action) and is_single_word_i(action) == False:
      print("""
       WHY ARE YOU SHOUTING? STOP SHOUTING AT ME!
       
             """)
      ShoutCount += 1

    if not action:
      print("You did not enter any input. Please try again.")
      continue

    elif action.lower() == "quit":
      break

#   elif IncompetenteStatement(HelpMeCount) == True:
#     print(
#     "God damn it how can you be so incompetent. Never played a viedeogame before? Doesn´t matter. Just use the 'Look around' Function and 'Help'. Imagine you were in this room for real. What would you do? And than just write it down. Easy. Look I don´t wanna be so harsh, but i am just so excited to share my world with you."
#   )
#  HelpMeCount = 0

# #if the player trys to make more than one statement this elif refers to function
#if two_statements == True:
#  print("Stop it! Relax, everything is fine. Woah how can you be in such a hurry? Just enjoy the game that's why it was made!           (You can´t enter two statements at once.)")

#the look around thing. So the player can see his enviroment
    if "look" in action.lower() and "around" in action.lower():
      if LevelCount == 0 and roomIsLit == True:
        print(
          "You see a closet at the wall left to you. It is open and something glitters in the light. There is also a door at the opposite wall of the room. The candle is on fire and the book lays in the corner."
        )

      elif LevelCount == 0 and LighterOnFloor == True:
        print(
          "there is a shadow on the wall at the end of the room. Could be a door. The candle is still on the floor in front of you, same as the book. It´s too dark to see anything else."
        )
        print("What would you like to do next?")

      elif LevelCount == 2:
        print(
          "There is a big artful mirror in the middle of the room. There is a door again, but it has the size a mousehole. The room is very small and there is a little window on the left wall."
        )

      elif LevelCount == 0:
        print(
          "there is a shadow on the wall at the end of the room. Could be a door. The candle is still on the floor in front of you, same as the book. It´s too dark to see anything else."
        )
        print("What would you like to do next?")
      elif LevelCount == 1:
        print(
          "the room looks exactly like the one before. Just that this room is empty. Behind you is the door you entert before, and a old man is sitting in the middle of the room. There is also a window at the west wall."
        )

      elif LevelCount == 3:
        if InHole == False:
          if wandOnFloor == False:
            print(
              "There is a creature in the corner of the room. The door is still coverd in the magical shield."
            )
          elif wandOnFloor == True:
            print(
              "There is a wand lying in the corner of the room where the creature once stood. The door is still coverd in the magical shield."
            )

        elif InHole == True:
          print(
            "There is a ladder and a button on one side of the wall, and a apple-sized hole in the other side of the wall with a sign that says:'here fits a orbit'"
          )

      else:
        pass

    #for kill-ish players
    elif "kill" in action.lower():
      print("HEY!  No violence just jet, ok?")

      #to get admin skip commands
    elif "admin.get.commands" in action.lower():
      userName = "merlin"

    elif userName == "merlin" and "get.everything" in action.lower():
      inventory.append("lighter")
      inventory.append("orbit")
      inventory.append("wand")
      inventory.append("key")

    elif userName == "merlin" and "get.orb" in action.lower():
     inventory.append("orbit")

    elif userName == "merlin" and "skip.lvl" in action.lower():
      LevelCount += 1

    #again when the player tries to "ok" me
    elif action.lower() == "ok":
      print("Don´t 'ok' me god damn it")

      #If the player decides to go in vulginare
    elif "fuck" in action.lower() or "shit" in action.lower():
      fuckCount += 1
      if fuckCount == 1:
        print(
          "Hey Calm down.its just a game. Do this again and you will be kicked."
        )
      elif fuckCount == 2:
        print("You have been kicked. Haha")
        break

    #my place holders for jet not existing commands
    elif when_input_go(action):
      print(
        "You cannot go anywhere. The room has the size of a rich mans toilet.")

    elif "where" in action.lower() and "am" in action.lower():
      print("Do i seem like i know that? No, no i don´t")

    elif "who" in action.lower() and "am" in action.lower():
      print("Do i seem like i know that? No, no i don´t")

    elif "don" in action.lower() and "know" in action.lower():
      print("I know.")

    elif action.lower() == "sleep" or action.lower() == "eat" or action.lower(
    ) == "drink" or action.lower() == "swim" or action.lower(
    ) == "chill" or action.lower() == "nothing":
      print("Seriusly? So childish.")

    elif "you" and "are" in action.lower():
      print("Don´t tell me what i am.")

    elif "look" in action.lower() and "window" in action.lower(
    ) and LevelCount != 0 or "watch" in action.lower(
    ) and "window" in action.lower() and LevelCount != 0:
      print(
        "The window is dirty. there is some kind of crust on the outside, you can only see a small piece of land wich is coverd in gras."
      )

    elif "take" in action.lower() and "candle" in action.lower(
    ) and LevelCount == 0:
      take_object("candle")

    elif "take" in action.lower() and "closet" in action.lower(
    ) and LevelCount == 0:
      take_object("closet")

    elif "take" in action.lower() and "door" in action.lower(
    ) and LevelCount != 1:
      take_object("door")

    elif "take" in action.lower() and "man" in action.lower(
    ) and LevelCount == 1:
      take_object("man")

    elif "take" in action.lower() and "mirror" in action.lower(
    ) and LevelCount == 2:
      take_object("miorror")

    elif "take" in action.lower() and "crow" in action.lower(
    ) and LevelCount == 2:
      take_object("crow")

    elif "take" in action.lower() and "door" in action.lower(
    ) and LevelCount == 2:
      take_object("door")

    elif "take" in action.lower() and "dwarf" in action.lower(
    ) and LevelCount == 2:
      take_object("dwarf")

    elif "take" in action.lower() and "creature" in action.lower(
    ) and LevelCount == 2:
      take_object("creature")

    elif "take" in action.lower() and "ladder" in action.lower(
    ) and LevelCount == 2:
      take_object("ladder")

    elif "take" in action.lower() and "button" in action.lower(
    ) and LevelCount == 2:
      take_object("button")

    #elif action.lower() in ("light candle", "light the candle"):
    #(up is the old code) so the player can light the candle in order to lit the room and see the closet
    elif "light" in action.lower() and "candle" in action.lower(
    ) or "rs2" in action.lower() and userName.lower(
    ) == "merlin" or "on fire" in action.lower() and "candle" in action.loer():
      if "lighter" in inventory and LevelCount == 0:
        print(
          "You light the candle and the room becomes brighter. You now see a closet at the wall left to you. It is open and something glitters in the light. There is also a door at the opposite wall of the room."
        )
        roomIsLit = True
      elif LevelCount == 0:
        print("You need a lighter to light the candle. The room remains dark.")
        print("What would you like to do next?")
      else:
        pass

    #to detect if the player is shouting(entering a word uppercase- see function above)
    elif is_word_upper(action) and ShoutCount == 0 and is_single_word_i(
        action) == False:
      print("WHY ARE YOU SHOUTING? STOP SHOUTING AT ME!")
      ShoutCount += 1

    #a list of all the comands for the room the player is currently in so the player doesn´t get spoilerd
    elif "help" in action.lower() and LevelCount == 0:
      print(""" in this Level you can use following commands:
  'Look around' for seeing your enviroment
  'Inventory' for looking in your inventory
  'Open door' to open the door
  'light the candle' to light the candle if you have the lighter
  'Read the book' to interact with the book
  'search (object)' to interact with the (object)
  'take (object)' to take the (object)  """)

    #the player can open the door with this one- if he/she/it has the key
    elif "door" in action.lower() and "key" in action.lower(
    ) or "use" in action.lower() and "key" in action.lower(
    ) or "open" in action.lower() and "door" in action.lower(
    ) and LevelCount == 0 or "rs4" in action.lower() and userName.lower(
    ) == "merlin":
      if "key" in inventory and LevelCount == 0:
        print(
          "You are turning the key inside the lock and hear a mysterius clicking. It almost sounds like a silent laughter. The door opens and you enter the 2nd level. All out of the sudden the door smashes behind you and there is no way back."
        )
        LevelCount += 1
        LvL2()
      elif LevelCount == 0:
        print("The door is locked. You will need to find a key to unlock it.")
        print("What would you like to do next?")
      else:
        pass

    #this here is to detect if the player has read/took the book so he can get the lighter
    elif "read" in action.lower() and "book" in action.lower(
    ) or "search" in action.lower() and "book" in action.lower(
    ) or "look" in action.lower() and "book" in action.lower(
    ) or "take" in action.lower() and "book" in action.lower(
    ) or "rs1" in action.lower() and userName.lower() == "merlin":
      if "lighter" not in inventory and LevelCount == 0:
        print(
          "The book is written in a strange language. You cannot read it. You throw it away in frustration, and suddenly a lighter falls out of the pages. It falls to the ground and makes a metallic noise."
        )
        LighterOnFloor = True
        #inventory.append("lighter")
        print("What would you like to do next?")

      elif LevelCount == 0:
        print(
          "The book is still written in a strange language. You still cannot read it."
        )
      else:
        pass

        #a action to take the lighter
    elif "take" in action.lower() and "lighter" in action.lower(
    ) and LighterOnFloor == True or "grab" in action.lower(
    ) and "lighter" in action.lower(
    ) and LighterOnFloor == True or "pick" in action.lower(
    ) and "up" in action.lower() and "lighter" in action.lower(
    ) and LighterOnFloor == True or "rsa" in action.lower(
    ) and userName == "melin":
      if "lighter" not in inventory and LevelCount == 0:
        print(
          "You pick up the lighter. It is heavy and has decorations. It is probably made out of steel."
        )
        inventory.append("lighter")
        LighterOnFloor = False

    #if the player really trys to set the closet on fire. little pyromat.
    elif "light" in action.lower() and "closet" in action.lower(
    ) and "candle" not in action.lower(
    ) and roomIsLit == True and LevelCount == 0 or "burn" in action.lower(
    ) and "closet" in action.lower() and "canlde" not in action.lower(
    ) and roomIsLit == True and LevelCount == 0:
      print(
        "You try to hold the lighter under the closet, but as it is under the closet, the flame disappears. Geez, you are really nuts aren´t you? This is a pice of god damn important History!"
      )

    #if the player is stupid enough to try to set the book on fire
    elif "light" in action.lower() and "book" in action.lower(
    ) and LevelCount == 0 and "candle" not in action.lower(
    ) or "burn" in action.lower() and "book" in action.lower(
    ) and LevelCount == 0 and "canlde" not in action.lower():
      print(
        "You try to hold the lighter under the book, but as it is under the book, the flame disappears. Geez, you are really nuts aren´t you? This is a pice of god damn important History!"
      )

    #if the player is stupid enough to try to set the door on fire
    elif "light" in action.lower() and "door" in action.lower(
    ) and "candle" not in action.lower() or "burn" in action.lower(
    ) and "door" in action.lower() and "canlde" not in action.lower():
      print(
        "You try to hold the lighter under the door, but as it is under the door, the flame disappears. Geez, you are really nuts aren´t you? This is a pice of god damn important History!"
      )

    #if the player is stupid enough to try to set the old man on fire
    elif "light" in action.lower() and "man" in action.lower(
    ) and LevelCount == 1 or "burn" in action.lower(
    ) and "man" in action.lower() and LevelCount == 1:
      print(
        "You try to hold the lighter under the man, but as it is under the man, the flame disappears. Geez, you are really nuts aren´t you? This is a pice of god damn important History!"
      )

    #if the player is stupid enough to try to set the crow on fire
    elif "burn" in action.lower() and "crow" in action.lower(
    ) and LevelCount == 2:
      print(
        "You try to hold the lighter under the crow, but as it is under the crow, the flame disappears. Geez, you are really nuts aren´t you? This is a pice of god damn important History!"
      )

    #if the player is stupid enough to try to set the goddamn mirror on fire
    elif "light" in action.lower() and "mirror" in action.lower(
    ) and LevelCount == 2 or "burn" in action.lower(
    ) and "mirror" in action.lower() and LevelCount == 2:
      print(
        "You try to hold the lighter under the mirror, but as it is under the mirror, the flame disappears. Geez, you are really nuts aren´t you? This is a pice of god damn important History!"
      )

    #if the player is stupid enough to try to set the goddamn mirror on fire
    elif "light" in action.lower() and "creature" in action.lower(
    ) and LevelCount == 2 or "burn" in action.lower(
    ) and "creature" in action.lower() and LevelCount == 2:
      print(
        "You try to hold the lighter under the creature, but as it is under the mirror, the flame disappears. Geez, you are really nuts aren´t you? This is a pice of god damn important History!"
      )

    #if someone wants somebody to talk with, they will be rememberd they are at the wrong adress
    elif "hello" in action.lower() or "hi!" in action.lower(
    ) or "how are you" in action.lower() or action.lower(
    ) == "hi" or "do you" in action.lower():
      print(
        "Well hello there. I don´t think you have the time to chit-chat, but do as you like"
      )

    #this here searches the closet so the player can get the key for the door
    elif "search" in action.lower() and "closet" in action.lower(
    ) and LevelCount == 0 or "look" in action.lower(
    ) and "closet" in action.lower(
    ) and LevelCount == 0 or "rs3" in action.lower() and LevelCount == 0:
      if roomIsLit == True and "key" not in inventory:
        print("You open the closet and see a key at the bottom.")
        ClosetCount += 1
        print("What would you like to do next?")
      elif roomIsLit == True and "key" in inventory:
        print(
          "The closet is empty. You still see where the key laid in the dust.")
      else:
        print("you don´t see a closet. Maby it is too dark?")

    #This here is so the player can take the key
    elif "take" in action.lower() and "key" in action.lower(
    ) and roomIsLit == True and ClosetCount == 1 or "grab" in action.lower(
    ) and "key" in action.lower(
    ) and roomIsLit == True and ClosetCount == 1 or "pick" in action.lower(
    ) and "key" in action.lower(
    ) and roomIsLit == True and ClosetCount == 1 or "rsb" in action.lower(
    ) and userName.lower() == "merlin":
      print("You pick up the key. It is a simple key, probably handcraftet.")
      inventory.append("key")

    #if the player wants to see what they currenty have on them
    elif "inventory" in action.lower() or action.lower() in "i":
      if len(inventory) == 0:
        print("Your inventory is empty.")
        print("What would you like to do next?")
      else:
        print("Your inventory contains:", inventory)
        print("What would you like to do next?")

    #if the player doesn´t know how to close a tab or fears the developers anger, the can quit playing here
    elif "quit" in action.lower():
      break

    #the description of the secend level and a little 'make sure' that the massege only gets printet ones
  # elif LevelCount == 1 and MassagePrintet == 0:
  #  print("""

  #Congratulations, you made it! (not that it was very hard tough... but still.) """
  #   )
  # print("Now the real tower game begins")
  # print(
  #  "You find yourself in a round room just like before, but there is a window at the west wall, and you see everything in the room. There isn´t much to see, just an old man in the middle of the room starring at You."
  # )
  # print(
  #  "\033[91m",
  #   "'Who are you? Are you one of the many trying to get to the top of the tower? Haha. But thats fine with me.'",
  #   "\033[0m")
  # print(
  #  print(
  #    "\033[91m",
  #   "'I haven´t had a conversation in a long time and i would like some company, mabey you will stay here forever with me.'",
  #   "\033[0m"))
  #   print("\033[91m", "'Do you want to hear my riddle?' ", "\033[0m")
  #   MassagePrintet += 1

  #if the player wants to hear the riddle from the old man
    elif "listen" in action.lower() and "riddle" in action.lower(
    ) or "hear" in action.lower() and "riddle" in action.lower(
    ) or "tell" in action.lower() and "riddle" in action.lower(
    ) or "what" in action.lower() and "riddle" in action.lower(
    ) or "rs5" in action.lower(
    ) and userName == "melin" or riddle_count == 0 and "yes" in action.lower(
    ) and LevelCount == 1:
      if LevelCount == 1:
        print(
          "\033[91m", """'Well here is my riddle: 
What has roots as nobody sees,
Is taller than trees,
Up, up it goes,
And yet never grows?" 
 if you think you know the answer, feel free to tll me. I got a hint for you, but you have to do something for that.' """,
          "\033[0m")
        riddle_count += 1
        WhatCount = True
      else:
        print(
          "You cannot go fast forward. You don´t have a riddle jet so just relax, be pacient and enjoy the game!"
        )

    elif WhatCount == True and "what" in action.lower():
      if LevelCount == 1:
        print(
          "\033[33m",
          "I will tell you what you have to do for the hint if you ask for one. But remember, this is only the first Room of 13. So I wouldn´t hope too much if i were you and woudn´t be able to just solve a easy reference-riddle.",
          "\033[0m")
        WhatCount = False
      elif LevelCount == 2:
        print("Well i guess you litterally have to 'ask the crow'")
        WhatCount = False

      #if the player enters the correct anwser to the riddle
    elif riddle_count > 0 and "mountain" in action.lower(
    ) and hintCount == 0 or "rs6" in action.lower() and userName == "melin":
      if LevelCount == 1:
        print(
          "\033[91m",
          "'Correct! You truly are diffrent from the others. Mabey you will even make it to the top...'",
          "\033[0m")
        print(
          "The old man snips with his fingers and suddenly you find yourself in a hallway, and in front of you is a door with a sign that says 'level 3' "
        )
        print(
          " you want to look around you, but some kind of force pushes you towards the door while it magicaly opens. you get forced into the room and the door smashes behind you again."
        )
        LevelCount += 1
        LvL3()
      else:
        pass

    # if the player wants to interact with the old man
    elif "speak" in action.lower() and "man" in action.lower(
    ) or "talk" in action.lower() and "man" in action.lower():
      print(
        "The old man seems like he doesn´t care for you. He does not respond.")

    elif "give" in action.lower() and "man" in action.lower():
      print("He does not take it. He is very stoic, but sensible, you know?")

    elif "slap" in action.lower() and "man" in action.lower(
    ) or "kill" in action.lower() and "man" in action.lower(
    ) or "punch" in action.lower() and "man" in action.lower():
      print(
        "You really are stupidly brutal. Be nicer. Do not do that or I will do it to you."
      )

    #if the player entert the correct answer after a hint
    elif riddle_count > 0 and "mountain" in action.lower() and hintCount > 0:
      if LevelCount == 1:
        print(
          "\033[91m",
          "'Yeah.Correct.I hope you keep your promise or you shall be damed to never be able to enter middle earth again.'",
          "\033[0m")
        print(
          "The old man snips with his fingers and suddenly you find yourself in a hallway, and in front of you is a door with a sign that says 'level 3' "
        )
        print(
          " you want to look around you, but some kind of force pushes you towards the door while it magicaly opens. you get forced into the room and the door smashes behind you again."
        )
        LevelCount += 1
      else:
        pass

    #if the player writes he doesent want to hear the riddle
    elif "no" in action.lower() and LevelCount == 1 and hintCount == 0:
      if riddle_count == 0:
        print(
          "\033[91m",
          "'You are not funny. I, the old man of the tower, command you to go fuck yourself.'",
          "\033[0m")
      elif riddle_count > 0:
        print(
          """Are you sure you spelled exactly what you want to do like "Tell me the riddle" or "(anwser)" or "the anwser is (anwser)" or "can I get a hint" ? 
        If you want to see all the Commands, press "Help" 
        """)
        HelpMeCount += 1
      elif LevelCount == 0:
        print(
          """Are you sure you spelled exactly what you want to do like "search (object)" or "search the (object)" or "use (object)" or "use the (object)"? 
        If you want to see all the Commands, press "Help" 
        
        """)
        print("What would you like to do next?")
        HelpMeCount += 1

      else:
        pass

    elif "sorry" in action.lower():
      print("Don´t be sorry about anything just yet. It will get worse.")

    #gives the player a hint if he asks for one
    elif "hint" in action.lower() and riddle_count > 0:
      if LevelCount == 1:
        print(
          "\033[91m",
          "'I am disappointed. You never watched the Hobbit? Well in that case, You could give me something in exchange.' The old man snips and suddenly there is a pipe in his hand. 'Could you light the pipe for me? Then i will give you the hint.'",
          "\033[0m")
        hintSaid += 1
      else:
        pass

    #if the player does something that triggers the hint to be said
    elif hintSaid > 0 and "light" in action.lower() and "pipe" in action.lower(
    ) or hintSaid == 1 and "ok" in action.lower(
    ) and LevelCount == 1 or hintSaid == 1 and "yes" in action.lower(
    ) and LevelCount == 1:
      print(
        "You light the pipe, but as you set the flame to the tabbac, your lighter dissapears. The old man laughs."
      )
      inventory.remove("lighter")
      print(
        "\033[91m",
        "'Well here is the hint: In the Oxford English Dictionary the answer to the riddle is defined as a natural elevation of the earth surface rising more or less abruptly from the surrounding level and attaining an altitude which, relatively to the adjacent elevation, is impressive or notable. And for not so intelligent people: The Mount Everest is the highest ........ on Earth.'",
        "\033[0m")
      hintCount += 1

    elif FalseAnwser > 4:
      print(
        "Come on now! Just ask for the god damn hint will you? I don´t have all day..."
      )
      FalseAnwser = 0

    #displays all the command for level 2
    elif "help" in action.lower() and LevelCount == 1:
      print(""" in this Level you can use following commands:
  'Look around' for seeing your enviroment
  'Inventory' for looking in your inventory
  'Hint' for reciving a hint for the riddle
  '(anwser)' yor anwser to the riddle
  'listen to riddle' to hear the old mans riddle""")

    elif LevelCount == 1 and riddle_count > 0:
      print("""That´s not the correct anwser. if you want a hint just say so. 
     
     Are you sure you spelled exactly what you want to do like "Tell me the riddle" or "(anwser)" or "the anwser is (anwser)" or "can I get a hint" ? 
        If you want to see all the Commands, press "Help" 
        """)
      FalseAnwser += 1
      HelpMeCount += 1

    #displays all the command for level 3
    elif "help" in action.lower() and LevelCount == 2:
      print(""" in this Level you can use following commands:
  'Look around' for seeing your enviroment
  'Inventory' for looking in your inventory
  'Look in the mirror' for looking in the mirror
  'open (object)' to open something
  'break (object)' to break something
  'talk to crow' to talk to crow""")

  #  elif LevelCount == 2 and PrintCount == 0:

  #  print(
  #    "The room looks same as the other ones. There is a big artful mirror in the middle of the room. There is a door again, but      #    it has the size a mousehole. There is also a little window on the left wall."
  #   )
  #   print(
  #     "A little bird appears on the mirror. He talks to you"
  #    "\033[37m",
  #     "'You don´t know it anymore? Ask the crow and give something therefor'",
  #     "\033[0m")
  #   PrintCount += 1

    elif "look" in action.lower() and "mirror" in action.lower(
    ) and LevelCount == 2 or "watch" in action.lower(
    ) and "mirror" in action.lower(
    ) and LevelCount == 2 or "rs7" in action.lower() and userName == "melin":
      print(
        "You are bald and coverd in scratches. There is dry blood all over you and you have a Tatoo on your stomach that says:'34221 siht evresed uoy did uoy tahw fo suaceb"
      )
      mirrorCount += 1

    elif "look" in action.lower() and "door" in action.lower(
    ) and LevelCount == 2 or "open" in action.lower(
    ) and "door" in action.lower(
    ) and LevelCount == 2 or "search" in action.lower(
    ) and "door" in action.lower() and LevelCount == 2 or "go" in action.lower(
    ) and "door" in action.lower(
    ) and LevelCount == 2 or "rs8" in action.lower() and userName == "melin":
      if doorOpenLvL2 == False:
        print(
          "All out ofthe sudden there is a little dwarf shooting out of the little door like a cuckoo. Out of the little doll (unfortunally it´s not living) there comes a little pad with buttons. A little screen blinks and there are 10 buttons from 1 to 10. It appears you can enter a number(s) here."
        )
        doorOpenLvL2 = True
      else:
        print(
          "What door do you want to open, huh? The one that´s already open? Stupid."
        )

    elif "enter" in action.lower(
    ) and LevelCount == 2 and mirrorCount > 0 and doorOpenLvL2 == True and "12243" in action.lower(
    ) or "12243" in action.lower(
    ) and LevelCount == 2 and mirrorCount > 0 and doorOpenLvL2 == True or "rs9" in action.lower(
    ) and userName == "melin":
      print(
        "You hear clicking. The dwarf goes back in the wall and the door closes. Suddenly it gets bigger and bigger until it has the size of the other doors. But there is no keyhole. A sentence is slowly burning into the wood of the door word for word as if it was magic: 'You shall not pass. Everything will be as you kno-' A loud noise. The door is bursting from the inside and a dwarf stands in front of you. The doll has now the size of an nazgul. In you desperatness you climp on it and bounce back into the dark.Something hits you on the head and you pass out."
      )
      LevelCount += 1
      LvL4()

    elif "enter" in action.lower() and "12243" not in action.lower(
    ) and doorOpenLvL2 == True and LevelCount == 2 or "34221" in action.lower(
    ) and doorOpenLvL2 == True and LevelCount == 2 or "press" in action.lower(
    ) and "12243" not in action.lower(
    ) and doorOpenLvL2 == True and LevelCount == 2:
      print(
        "Thats not the correct code. Have you made sure that you entered everything in the right order and wrote it like that:'11111'?"
      )

    elif "talk" in action.lower() and "crow" in action.lower(
    ) or "ask" in action.lower() and "crow" in action.lower():
      print(
        "\033[37m",
        "'Are you ready to know more about you past? Krah Krah. Then give me the lighter fast and my anwsers shall past Krah Krah your ears'",
        "\033[0m")
      crowSpoke += 1

    elif "give" in action.lower() and "lighter" in action.lower(
    ) and LevelCount == 2 and crowSpoke >= 1:
      if "lighter" in inventory:
        print(
          "\033[37m",
          "'You aren´t here on purpose. The brought you here, they fought you here, they taught you here. They are gone, you are here. Here is my hint: Break the Mirror to gain your 7 years of bad luck.'",
          "\033[0m", "Your lighter is now gone.")
        crowSpoke_ += 1
        inventory.remove("lighter")
      else:
        print("'You cannot trick me. You don´t have a lighter eh? Krah Krah'")

    elif HelpMeCount == 3 and action.lower() not in keywords:
      print(
        "God damn it how can you be so incompetent. Never played a viedeogame before? Doesn´t matter. Just use the 'Look around' Function and 'Help'. Imagine you were in this room for real. What would you do? And than just write it down word for word. Easy. Look I don´t wanna be so harsh, but i am just so excited to share my world with you."
      )
      HelpMeCount = 0

    elif "talk" in action.lower() and "crow" in action.lower(
    ) and crowSpoke_ > 0 or "ask" in action.lower() and "crow" in action.lower(
    ) and crowSpoke_ > 0:
      print(
        "The crow doesen´t react. it looks like she doesen´t have anything to say to you anymore"
      )
    elif "break" in action.lower() and "window" in action.lower(
    ) and handInGlas == 0 or "break" in action.lower(
    ) and "mirror" in action.lower() and handInGlas == 0:
      print(
        "As you try to break the glas with your hands, your hand just disappears in the glas. You hear crunches and pull it out. there is a new tatto on your arm now that says: 9122_"
      )
      handInGlas += 1

    elif "91227" in action.lower(
    ) and LevelCount == 2 and handInGlas > 0 or "91223" in action.lower(
    ) and LevelCount == 2 and handInGlas > 0:
      if doorOpenLvL2 == True:
        print(
          "As you typed in the last number you start to feel a bit numb. everything spinns and you fall to the ground. You open your eyes and suddenly there is a man with an tattoed head above you and stares you in the eys. Your sight isn´t clear just yet, you see him starting to raise his axe above his head, you want to roll to the side, but you cant move. You just watch him splattering his axe right next to your Head. You can feel the splitters in your face. As he raises his axe again, you close your eyes. Suddenly you wake up in the on the floor in front of the buttons, and you now have some kind of mettalic tiny ball of the size of a apple in your hand."
        )
        inventory.append("orbit")

      else:
        print(
          "You do not know what to do with this code just jet. Keep looking throughout the level."
        )

    elif "help" in action.lower() and LevelCount == 3:
      print(""" in this Level you can use following commands:
  'Look around' for seeing your enviroment
  'Inventory' for looking in your inventory
  'open (object)' to open something
  'I choose option 1/2' to choose one of the options
  'climb the ladder' to climb up the ledder
  'press button' to press the button
  'use orbit' to use the orbit
  'take object' to take the object
  'Rock', 'paper', or 'scissors' to play with the creature
  'Magician', 'human', 'Mutant', 'Lion' or 'Spider' to try to open the door
  'talk to creature' to talk to the creature""")

    elif "open" in action.lower() and "door" in action.lower(
    ) and LevelCount == 3 or "rs10" in action.lower() and userName.lower(
    ) == "merlin":
      if "wand" in inventory:
        print(
          "Well the door is not surrounded by a magic shield anymore. But you can reach the lock now. you want to open it, but some kind of second lock appears. There are 5 signs, 'Magician', 'human', 'Mutant', 'Lion' and 'Spider'. Apparently you have to choose one of them."
        )
        symbolLvl4 = True
      else:
        print(
          "You try to open the door, but it appears that there is some kind of magical shield arround the door. You can not open it."
        )

    elif "magician" in action.lower() or "human" in action.lower(
    ) or "mutant" in action.lower() or "lion" in action.lower(
    ) or "spider" in action.lower():
      if symbolLvl4 == True:
        print(
          """You coosed the right sign. You hear clicking and the second lock disappears in the wall as fast as it appeard. And again you turn the key in the lock, but this time you can´t pull it out anymore. It is stuck in the doorlock wich now smashes behind you and the door is closed. You are now at Level 5.
          
          
          """
        )
        inventory.remove("key")

        endTime = time.time()
        passedTime = endTime - startTime
        hours = int(passedTime / 3600)
        minutes = int((passedTime % 3600) / 60)
        seconds = int(passedTime % 60)
        print(
          "Congrats", userName + "! you completed the first 4 Levels of 'the tower' in " + str(hours) +
          ":" + str(minutes) + ":" + str(seconds) +
          ". Thats not that bad. See you in the next Level.")
        print("(if you want to play the other Levels, just leave a vote on the site below)")
        anwser = input("Do you want to vote? (Yes/No)")
        if "yes" in anwser.lower():
          webbrowser.open(voteLink)
        else:
          print("Well, thanks for playing then.")
        break
        

    elif "talk" in action.lower() and "creature" in action.lower(
    ) or "ask" in action.lower() and "creature" in action.lower():
      if creatureLifes == True:
        print(
          "\033[34m",
          "'You have two options: eithe  play a  ound of  ock, pape , scisso s with me to spend some time o  i can tell you how to get though that doo . You choose(Only one though)'",
          "\033[0m")
        creatureSpoke = True
        creatureSpoke1 = 1
      else:
        print("There is no Creature anymore")

    elif creatureSpoke == True and creatureSpoke1 == 1 and "play" in action.lower(
    ) or creatureSpoke == True and "option" in action.lower(
    ) and "one" in action.lower(
    ) or creatureSpoke == True and "option" in action.lower(
    ) and "1" in action.lower():
      if creatureLifes == True and RockPS == False:
        print("\033[34m", "'Good choise, ", userName,
              ". Lets play a  ound! You begin.'", "\033[0m")
        print("I guess you have to say either rock, paper or scissors")
        RockPS = True

      else:
        print("You know thats not an option")

    elif RockPS == True and "rock" in action.lower(
    ) and wonRPS == False or RockPS == True and "paper" in action.lower(
    ) and wonRPS == False or RockPS == True and "scissors" in action.lower(
    ) and wonRPS == False:
      if randomNumber == 1:
        print(
          """You Won! In his anger the creature begans to stomp on the floor and mumbaling some words.
        The floor begins to shake. The stone it is made of begins to burst and the creature laughs. 
        You fall through a crack in the floor and hit hard on the ground. 
        It wasn´t so high that you could get injured, but it wasn´t pretty low either. 
        You swear and look around. there is a ladder on the wall but is´t too high to reach and a button besides it. 
        There is also a hole on the other side of the room of the sice of an apple, and there is a sign that says: 'here fits the orbit'(Mabey check if this item is in you inventory)."""
        )
        InHole = True
        wonRPS = True
      else:
        print(
          "You loose! Loser. Do you want to play again? I think you have no other choice than type in either rock, paper or scissors again."
        )

    elif creatureSpoke == True and "option" in action.lower(
    ) and "2" in action.lower(
    ) or creatureSpoke == True and "option" in action.lower(
    ) and "two" in action.lower() or creatureSpoke == True and "tell" in action.lower(
    ) and "door" in action.lower():
      if creatureLifes == True:
        print(
          "\033[34m",
          "'Well, it is p etty simple. Just  epeat the unspeakable lette  3 times'",
          "\033[0m")

    elif "rrr" in action.lower() and LevelCount == 3:
      print(
        "The floor begins to shake. The stone it is made of begins to burst and the creature laughs. You fall through a crack in the floor and hit hard on the ground. It wasn´t so high that you could get injured, but it wasn´t pretty low either. You swear and look around. there is a ladder on the wall but is´t too high to reach and a button besides it. There is also a hole on the other side of the room of the sice of an apple, and there is a sign that says: 'here fits the orbit'(Mabey check if this item is in you inventory)."
      )
      InHole = True

    elif InHole == True and LevelCount == 3 and "press" in action.lower(
    ) and "button" in action.lower():
      print(
        "You hear buzzing. Suddenly the ladder falls down to you, so you can climb it now."
      )
      HoleButtonPressed = True

    elif InHole == True and LevelCount == 3 and "climb" in action.lower(
    ) and "ladder" in action.lower(
    ) or InHole == True and LevelCount == 3 and "climb" in action.lower(
    ) or InHole == True and LevelCount == 3 and "use" in action.lower(
    ) and "ladder" in action.lower():
      if HoleButtonPressed == True:
        print(
          "You climb out the hole. The creature still stands in the corner like nothing happend. In your rage you try to attack it, but as you touch it, it disappears. Your hand glides through nothing. Were the creature once stud, there is a wand."
        )
        InHole = False
        creatureLifes == False
        wandOnFloor = True
      elif HoleButtonPressed == False:
        print("The ladder is too high as that you could reach it.")

    elif "take" in action.lower() and "wand" in action.lower(
    ) or "grab" in action.lower() and "wand" in action.lower(
    ) or "pick" in action.lower() and "up" in action.lower(
    ) and "wand" in action.lower():
      if "wand" not in inventory and LevelCount == 3 and InHole == False:
        inventory.append("wand")
        wandOnFloor = False
        print(
          "You now have a wand. Congratulations! The magical Shield arround the door suddenly vanished."
        )
      else:
        pass

    elif "orbit" in inventory and "orbit" in action.lower(
    ) and LevelCount == 3 and InHole == True:
      print(
        " You hear Surring. Then the Orbit disappears in the wall. Suddenly, with an enourmus speed, a little golden Object shoots out of the hole. It glows in heat, but as you pick it up it is pretty cool. You now appear to have somewhat of a golden nugget. There is also a message in the hole where the orbit was now. It says: 'You are Grain, son of dwain, son of the great Vurin. Once this all was your Kingdom, now it is your prison. and all of that just because of what you did.' the orbit comes out of the hole and you take it again"
      )
      inventory.append("goldenNugget")

    elif "what" in action.lower() and "do" in action.lower(
    ) and LevelCount > 0:
      print(
        "You don´t remember? Well, it is not on me to tell you this. Ask the prayerer when you see him. And stop asking."
      )

    else:
      if LevelCount == 1:
        print(
          """Are you sure you spelled exactly what you want to do like "Tell me the riddle" or "(anwser)" or "the anwser is (anwser)" or "can I get a hint" ? 
        If you want to see all the Commands, press "Help" 
        """)
        HelpMeCount += 1
      elif LevelCount == 0:
        print(
          """Are you sure you spelled exactly what you want to do like "search (object)" or "search the (object)" or "use (object)" or "use the (object)"? 
        If you want to see all the Commands, press "Help" 
        
        """)
        print("What would you like to do next?")
        HelpMeCount += 1

      elif LevelCount == 2:
        print(
          """Are you sure you spelled exactly what you want to do like "look in/at (object)" or "open (object)" or "use (object)" or "enter/write (...)"? 
        If you want to see all the Commands, press "Help" 
        
        """)
        print("What would you like to do next?")
        HelpMeCount += 1

      elif LevelCount == 3:
        print(
          """Are you sure you spelled exactly what you want to do like "Press (object)" or "I choose Option ..." or "climb (object)" or "Open (object)" or "Speak to ..."? 
        If you want to see all the Commands, press "Help" 
        
        """)
        print("What would you like to do next?")
        HelpMeCount += 1

  except EOFError:
    print("You did not enter any input. Please try again.")

import scenario1

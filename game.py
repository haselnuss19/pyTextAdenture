
# Prints a description of the first level in the game
print("""Welcome to the 1st Level. This is just the begining!
You find yourself in a room. You don´t know who you are or where
you are. 
You wonder what this is. There is a candle on the floor, in front of it is a book. It´s too dark to see anything else.

You can navigate through the game by using the "look around" function, the rest is self explaining. you also have an inventory you can use by pressing "i" 

""")


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
  if "go" in words:
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
#         print("Stop it! Relax, everything is fine. Woah how can you be in such a hurry? Just enjoy the game that's why it was made!           (You can´t enter two statements at once.)")
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


#My variables for diffrent events. Kinda self explaining

#how many times the player has heard the riddle in level 2
riddle_count = 0
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
  "around", "mountain", "door", "give", "speak", "man", "tell", "grab", "pick"
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
while True:
  try:
    action = input("> ")
    if is_word_upper(action) and is_single_word_i(action) == False:
      print("""
       WHY ARE YOU SHOUTING? STOP SHOUTING AT ME!
       
             """)
      ShoutCount += 1

    if not action:
      print("You did not enter any input. Please try again.")
      continue

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
      else:
        pass

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
    elif when_input_go == True:
      print(
        "You cannot go anywhere. The room has the size of a rich mans toilet.")

    elif "where" in action.lower() and "am" in action.lower():
      print("Do i seem like i know that? No, no i don´t")

    elif "who" in action.lower() and "am" in action.lower():
      print("Do i seem like i know that? No, no i don´t")

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

    #elif action.lower() in ("light candle", "light the candle"):
    #(up is the old code) so the player can light the candle in order to lit the room and see the closet
    elif "light" in action.lower() and "candle" in action.lower(
    ) or "rs2" in action.lower(
    ) or "on fire" in action.lower() and "candle" in action.loer():
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
    ) or "rs4" in action.lower():
      if "key" in inventory and LevelCount == 0:
        print(
          "You are turning the key inside the lock and hear a mysterius clicking. It almost sounds like a silent laughter. The door opens and you enter the 2nd level. All out of the sudden the door smashes behind you and there is no way back."
        )
        LevelCount += 1
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
    ) or "rs1" in action.lower():
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
    ) and LighterOnFloor == True or "rsa" in action.lower():
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
    elif "light" in action.lower() and "crow" in action.lower(
    ) and LevelCount == 2 or "burn" in action.lower(
    ) and "crow" in action.lower() and LevelCount == 2:
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

    #if someone wants somebody to talk with, they will be rememberd they are at the wrong adress
    elif "hello" in action.lower() or "hi!" in action.lower(
    ) or "how are you" in action.lower():
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
    ) and roomIsLit == True and ClosetCount == 1 or "rsb" in action.lower():
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
    elif LevelCount == 1 and MassagePrintet == 0:
      print("""
    
    
    Congratulations, you made it! (not that it was very hard tough... but still.) """
            )
      print("Now the real tower game begins")
      print(
        "You find yourself in a round room just like before, but there is a window at the west wall, and you see everything in the room. There isn´t much to see, just an old man in the middle of the room starring at You."
      )
      print(
        "'Who are you? Are you one of the many trying to get to the top of the tower? Haha. But thats fine with me.'"
      )
      print(
        "'I haven´t had a conversation in a long time and i would like some company, mabey you will stay here forever with me.'"
      )
      print("'Do you want to hear my riddle?' ")
      MassagePrintet += 1

    #if the player wants to hear the riddle from the old man
    elif "listen" in action.lower() and "riddle" in action.lower(
    ) or "hear" in action.lower() and "riddle" in action.lower(
    ) or "tell" in action.lower() and "riddle" in action.lower(
    ) or "what" in action.lower() and "riddle" in action.lower(
    ) or "rs5" in action.lower(
    ) or riddle_count == 0 and "yes" in action.lower():
      if LevelCount == 1:
        print("""'Well here is my riddle: 
    "What has roots as nobody sees,
Is taller than trees,
Up, up it goes,
And yet never grows?" 
 if you think you know the answer, feel free to tll me. I got a hint for you, but you have to do something for that.' """
              )
        riddle_count += 1
      else:
        print(
          "You cannot go fast forward. You don´t have a riddle jet so just relax, be pacient and enjoy the game!"
        )

        #if the player enters the correct anwser to the riddle
    elif riddle_count > 0 and "mountain" in action.lower(
    ) and hintCount == 0 or "rs6" in action.lower():
      if LevelCount == 1:
        print(
          "'Correct! You truly are diffrent from the others. Mabey you will even make it to the top...'"
        )
        print(
          "The old man snips with his fingers and suddenly you find yourself in a hallway, and in front of you is a door with a sign that says 'level 3' "
        )
        print(
          " you want to look around you, but some kind of force pushes you towards the door while it magicaly opens. you get forced into the room and the door smashes behind you again."
        )
        LevelCount += 1
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
          "'Yeah.Correct.I hope you keep your promise or you shall be damed to never be able to enter middle earth again.'"
        )
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
    elif "no" in action.lower() and riddle_count == 0 and hintCount == 0:
      if LevelCount == 1:
        print(
          "'You are not funny. I, the old man of the tower, command you to go fuck yourself.'"
        )
      elif LevelCount == 1:
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

    #gives the player a hint if he asks for one
    elif "hint" in action.lower() and riddle_count > 0:
      if LevelCount == 1:
        print(
          "'I am disappointed. You never watched the Hobbit? Well in that case, You could give me something in exchange.' The old man snips and suddenly there is a pipe in his hand. 'Could you light the pipe for me? Then i will give you the hint. And please watch the Hobbit'"
        )
        hintSaid += 1
      else:
        pass

    #if the player does something that triggers the hint to be said
    elif hintSaid > 0 and "light" in action.lower() and "pipe" in action.lower(
    ):
      print(
        "You light the pipe, but as you set the flame to the tabbac, your lighter dissapears. The old man laughs."
      )
      inventory.remove("lighter")
      print(
        "'Well here is the hint: In the Oxford English Dictionary the answer to the riddle is defined as a natural elevation of the earth surface rising more or less abruptly from the surrounding level and attaining an altitude which, relatively to the adjacent elevation, is impressive or notable.'"
      )
      hintCount += 1

    elif FalseAnwser > 4:
      print(
        "Come on now! Just ask for the god damn hint will you? I don´t have all day..."
      )

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
  'talk to raven' to talk to raven""")

    elif LevelCount == 2 and PrintCount == 0:

      print(
        "The room looks same as the other ones. There is a big artful mirror in the middle of the room. There is a door again, but it has the size a mousehole. There is also a little window on the left wall."
      )
      print(
        "A little bird appears on the mirror. He talks to you 'You don´t know it anymore? Ask the crow and give something therefor'"
      )
      PrintCount += 1

    elif "look" in action.lower() and "mirror" in action.lower(
    ) and LevelCount == 2 or "watch" in action.lower(
    ) and "mirror" in action.lower(
    ) and LevelCount == 2 or "rs7" in action.lower():
      print(
        "You are bald and coverd in scratches. There is dry blood all over you and you have a Tatoo on your stomach that says:'34221 siht evresed uoy did uoy tahw fo suaceb"
      )
      mirrorCount += 1

    elif "look" in action.lower() and "door" in action.lower(
    ) and LevelCount == 2 or "open" in action.lower(
    ) and "door" in action.lower() or "search" in action.lower(
    ) and "door" in action.lower() and LevelCount == 2 or "go" in action.lower(
    ) and "door" in action.lower(
    ) and LevelCount == 2 or "rs8" in action.lower():
      print(
        "All out ofthe sudden there is a little dwarf shooting out of the little door like a cuckoo. Out of the little doll (unfortunally it´s not living) there comes a little pad with buttons. A little screen blinks and there are 10 buttons from 1 to 10."
      )

    elif "enter" in action.lower(
    ) and LevelCount == 2 and mirrorCount > 0 or "press" in action.lower(
    ) and LevelCount == 2 and mirrorCount > 0:
      if "12243" in action.lower():
        print(
          "You hear clicking. The dwarf goes back in the wall and the door closes. Suddenly it gets bigger and bigger until it has the size of the other doors. But there is no keyhole. A sentence is slowly burning into the wood of the door word for word as if it was magic: 'You shall not pass. Everything will be as you kno- A loud noise. The door is bursting from the inside and a dwarf stands in front of you. The doll has now the size of an nazgul. In you desperatness you climp on it and bounce back into the dark.Something hits you on the head and you pass out."
        )
        break
      else:
        print(
          "Thats not the correct code. Have you made sure that you entered everything in the right order and wrote it like that:'11111'?"
        )

    elif "talk" in action.lower() and "crow" in action.lower(
    ) or "ask" in action.lower() and "crow" in action.lower():
      print(
        "'Are you ready to know more about you past? Krah Krah. Then give me the lighter fast and my anwsers shall past Krah Krah your ears'"
      )
      crowSpoke += 1

    elif "give" in action.lower() and "lighter" in action.lower(
    ) and LevelCount == 2 and crowSpoke >= 1:
      if "lighter" in inventory:
        print(
          "'You aren´t here on purpose. The brought you here, they fought you here, they taught you here. Tey are gone, you are here.' Your lighter is now gone."
        )
        crowSpoke_ += 1
        inventory.remove("lighter")
      else:
        print("'You cannot trick me. You don´t have a lighter eh? Krah Krah'")
    elif HelpMeCount == 3:
      print(
        "God damn it how can you be so incompetent. Never played a viedeogame before? Doesn´t matter. Just use the 'Look around' Function and 'Help'. Imagine you were in this room for real. What would you do? And than just write it down. Easy. Look I don´t wanna be so harsh, but i am just so excited to share my world with you."
      )
      HelpMeCount = 0

    elif "talk" in action.lower() and "crow" in action.lower(
    ) or "ask" in action.lower() and "crow" in action.lower(
    ) and crowSpoke_ > 0:
      print(
        "The crow doesen´t react. it looks like she doesen´t have anything to say to you anymore"
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

  except EOFError:
    print("You did not enter any input. Please try again.")

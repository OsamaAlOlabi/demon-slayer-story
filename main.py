print('''
*******************************************************************************
                               `...`                                                            
                               :sdNMMMMMmy/`                                                        
                             :mMMMMMMMMMMMMNo`                                                      
                            oMMMMMMMMMMMMMMMMd`                                                     
                           /MMMMMMMMMMMMMMMMMMh                                                     
                           hMMMMMMMMMMMMMMMMMMM`                                                    
                           yMMMMMMMMMMMMMMMMMMM`                                                    
                           -MMMMMMMMMMMMMMMMMMs                                                     
                            /NMMMMMMMMMMMMMMMy`                                                     
                             -yNMMMMMMMMMMMNo-....................................................` 
                               ./ydmmMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNm+
                          `-://:-.`.hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        :ymNMMMMMmhsMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmmmmmmmmd+
                      `sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/`````````` 
                      sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo            
                     -MMMMMMMMMMMMMMMMssyhhhhhhhmMMMMMMMMMMMMMmhhhhmMMMMMMMMMMMMMMMds/.             
                     yMMMMMMMMMMMMMMMMy.      `/mMMMMMMMMMMMMd-  `+mMMMMMMMMMMMMMd/`                
                    -MMMMMMMMMMMMMMMMMMNs.   -hMMMMMMMMMMMMNo` .+mMMMMMMMMMMMMMd/`                  
                    hMMMMMMMMMMMMMMMMMMMMNs:oNMMMMMMMMMMMMMmo:oNMMMMMMMMMMMMMm+`                    
                   :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd+`                      
                   dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/                         
                  /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm/                           
                  mMMMMMMMMMMMMMMMNdMMMMMMMMMMMMMMMdhNMMMMMMMMMMMMMMMd/                             
                 +MMMMMMMMMMMMMMMMo -ohNMMMMMMMNho-  `:ohNMMMMMMMNho-                               
                `NMMMMMMMMMMMMMMMN`     `--::-`           `--:--.                                   
                oMMMMMMMMMMMMMMMM+                                                                  
               `NMMMMMMMMMMMMMMMm                                                                   
               oMMMMMMMMMMMMMMMM/                                                                   
               NMMMMMMMMMMMMMMMd                                                                    
               NMMMMMMMMMMMMMMMh.                                                                   
               NMMMMMMMMMMMMMMMMNh:                                                                 
              `MMMMMMMMMMMMMMMMMMMMm+`                                                              
              :MMMMMMMMMMMMMMMMMMMMMMmo`                                                            
              sMMMMMMMMMMMMMMMMMMMMMMMMm+`                                                          
             `mMMMMMMMMMM/yNMMMMMMMMMMMMMm+`                                                        
             +MMMMMMMMMMd  .+mMMMMMMMMMMMMMd:                                                       
            .mMMMMMMMMMM/    `+dMMMMMMMMMMMMNs.                                                     
            yMMMMMMMMMMd       `/mMMMMMMMMMMMMm/                                                    
           oMMMMMMMMMMN:         `+mMMMMMMMMMMMMs`                                                  
          oMMMMMMMMMMMo            .yNMMMMMMMMMMMm-                                                 
        `sMMMMMMMMMMMy               :dMMMMMMMMMMMN/                                                
       .hMMMMMMMMMMMh`                `sNMMMMMMMMMMMs`                                              
      /mMMMMMMMMMMMh`                   :mMMMMMMMMMMMy`                                             
    .hMMMMMMMMMMMMy`                     .dMMMMMMMMMMMh`                                            
  .sNMMMMMMMMMMMN+                        `yMMMMMMMMMMMh`                                           
`sNMMMMMMMMMMMMd-                           sMMMMMMMMMMMy`                                          
dMMMMMMMMMMMMNo`                             oMMMMMMMMMMMo                                          
MMMMMMMMMMMMy-                                oMMMMMMMMMMh                                          
sMMMMMMMMMh-                                   sMMMMMMMMN-                                          
 /hNMMMNy-                                      -ymMMNdo`                                           
    ..`                                                                                  
*******************************************************************************
''')

# Highlighting Important Messages
def border_msg(msg):
    count = len(msg) + 2  # dash will need +2 too
    dash = "-" * count

    print(f"+{dash}+")
    print(f"| {msg} |")
    print(f"+{dash}+")


# Username
user_name = input("What is your name?\n")

# Welcome Message
welcome_message = print(f"Welcome to hell lord {user_name}.\nThere is one rule here, SURVIVE.")

# Keep track if the game ended or not (Game still on = True, Game ended = False)
game_state = True

# Main game code in here
def first_assignment():

    global game_state

    # if game state is TRUE keep playing, if FALSE stop the game
    while game_state == True:

        event1 = print('''\nYou have just arrived to the Devil's facility in AREA 51. 
What do you want to do?:
(1)- Walk inside
(2)- Run away and abandon the training''')
        user_input = input("> ")

        if user_input == "1":
            while True:
                event2 = print('''
You open the door to see a locked gate infront of you and you find a sword laid down on the floor.
You notice a note near the sword that says "This cursed sword, is forged from the devil himself.
What do you do?:
(1)- Pick up the sword
(2)- Knock on the locked gate
''')
                user_input = input("> ")

                if user_input == "1":
                    while True:
                        print(f'''
Once you pick it up you feel your whole body is being filled with power, dark power.
The gate opens, and a hundreds of demons start running towards you screaming lord {user_name}.
What do you do?:
(1)- Fight them all
(2)- Throw the sword away and run.
''')
                        user_input = input("> ")
                        if user_input == "1":
                            print("You have slain every demon in Hell.\nCongratiolations you are the DEVIL")
                            game_state = False
                            repeat()
                            break
                        elif user_input == "2":
                            print("Did you really thought you could outrun demons?. A demon has picked up the sword and thrusted it through your heart."
                                  "\nThe demon got a huge promotion and became the DEVIL")
                            game_state = False
                            repeat()
                            break
                        else:
                            print("Invalid choice. Please type a number from the list")
                elif user_input == "2":
                    print("The wolves heard you and ate you.")

                    break
                else:
                    print("Invalid choice. Please type a number from the list")


        elif event1 == "2":
            while True:
                event2 = input('You\' reached a frozen lake. There is an island at the end of the lake. Type "wait" '
                                'to wait for a boat. Type "walk" to walk across.\n').lower()
                if event2 == "wait":
                    print("while waiting your hands got frozen, which led to your feet to freeze which was the result "
                          "of your death")

                    break
                elif event2 == "walk":
                    print("The ice cracked while you were walking, you fell into the cold water, and get eaten by a shark.")

                    break
                else:
                    print("Invalid choice. Please type something from the list")

        else:
            print("Invalid choice. Please type something from the list")


def repeat():

    global game_state

    while game_state == False:

        play_again = border_msg('The game has ended. Would you like to play again? "Y" or "N"')

        user_input = input("> ")

        if user_input == "y":
            game_state = True
            first_assignment()
        elif user_input == "n":
            print("Game Over")
            exit()
            break
        else:
            print("Choose Y or N")


first_assignment()
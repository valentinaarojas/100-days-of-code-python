def play_game():

    print('''
     _                                     _     _                 _ 
    | |                                   (_)   | |               | |
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
     \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                    
    ''')
    print("Welcome to Treasure Island.\n")

    print("Since the dawn of the Age of Exploration, explorers from around the world have set out to seas\n"
        "in an attempt to discover the hidden treasure that is said to be located in the heart of the jungle of Treasure Island.\n") 
    print("Christopher Columbus, Ferdinand Magellan, and even Marco Polo have all attempted\n" 
        "to discover the hidden treasure, but none have prevailed.\n")
    print("As a seasoned explorer, you took it upon yourself to try to be the first person to discover the hidden treasure.\n")

    print("Your mission is to find the hidden treasure unharmed. Your choices matter.\n")

    print('''
    ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⠿⢿⣿⣿⣿⣿⡿⠿⠟⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⢸⡇⢸⡇⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣷⣄⠀⠀⠈⠛⢿⣿⣿⣿⣿⣶⣾⡇⢸⣷⣶⣿⣿⣿⣿⡿⠛⠁⠀⠀⣠⣾⣿
    ⣿⣿⣿⣷⣄⠀⠀⠀⠈⠻⢿⣿⣿⣿⡇⢸⣿⣿⣿⡿⠟⠁⠀⠀⠀⣠⣾⣿⣿⣿
    ⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠙⠻⣿⣷⣾⣿⠟⠋⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣯⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣽⣿⣿⣿⣿⣿
    ''')

    print("\nAs you go deeper into the jungle, you come across a crossroads.\n"
        "The left path is one of which many explorers have previously followed, "
        "while the right is an uncharted path.")

    first_choice = input("\nDo you want to go left or right?\n\n").lower()

    if first_choice == "left":

        print('''
             ."`".
         .-./ _=_ \.-.
        {  (,(oYo),) }}
        {{ |   "   |} }
        { { \(---)/  }}
        {{  }'-=-'{ } }
        { { }._:_.{  }}
        {{  } -:- { } }
        {_{ }`===`{  _}
       ((((\)     (/))))
        ''')

        print("\nWise choice. As you continue on your journey, you stumble upon a rabid baboon staring you\n"
            "down in the middle of the trail. Baboons are known to be rife with violence.\n"
            "You could either stand your ground and fight it or run away from it.")
        
        second_choice = input("\nFight or flight?\n\n").lower()

        if second_choice == "fight":

            print('''
    |                         |    |                        |
    |                    \__r'|    |             .   ~   .  |
    |                   o'   \|    | -oof-                  |
    |                      '  |    |      o_  '             |
    |         o               |    |     (       ro         |
    |        '=\    _  -  '   |    |      \  * -{ `         |
    |        r \              |    |             \          |
    '"""""""""""""""""""""""""'    '""""""""""""""""""""""""'               
            ''')

            print("You charge towards the baboon and it charges towards you, until you meet in the middle and start wrestling.\n"
                "It\'s a tough fight, but you finally knock out the baboon and continue on your way until you\'ve finally reached\n"
                "the heart of the jungle where a mysterious temple stands.\n")
            
            print('''
                        |
                      .' `.
                   : (     ) :
        .      |  ( )`._ _.'( )  |      .
        O  .   |`-  -|  .  |-  -'|   .  O
        H  o   |A /\ | ( ) | /\ A|   o  H
        H  I   |  -' | | | | `-  |   I  H
        .H__T___|_|___|_|_|_|___|_|___T__H.
        |_________________________________|
                    /       \  
                   /         \ 
                  /           \ ''')

            print("\nIts ancient stone walls are covered in thick vines and strange glowing symbols that pulse with an otherworldly blue light.\n"
                "The massive doorway seems to beckon you forward, but as you approach, you notice something odd - there's no door, just a\n" 
                "shimmering barrier of energy that ripples like water. Through the barrier, you can only make out what appears to be\n" 
                "a golden idol sitting atop a pedestal. Would you like to try to walk through the barrier, look for another way in,\n"
                "or throw a rock at the barrier to test it?")
            
            third_choice = input("\nWalk, look, or throw?\n\n").lower()

            if third_choice == "walk":

                print('''          
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
    ⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
    ⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
    ⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
    ⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
    ⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁

    ⠀⠀⠀⠀YOUR TIME HAS COME⠀⠀⠀⠀    
                ''')

                print("\nYou bravely step into the shimmering barrier, but instantly feel your body being "
                    "ripped apart by the ancient magic. Game over.\n")

            elif third_choice == "look":

                print('''
         _.--""--._
        /  _    _  \ 
     _  ( (_\  /_) )  _
    { \._\   /\   /_./ }
    /_"=-.}______{.-="_\ 
     _  _.=("""")=._  _
    (_'"_.-"`~~`"-._"'_)
     {_"            "_}
          uh ohhhh
                ''')

                print("\nAs you circle the temple looking for another entrance, you accidentally trigger "
                    "a trap door and fall into a pit of spikes. Game over.\n")

            elif third_choice == "throw":
                print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/________
    *******************************************************************************
                ''')

                print("\nThe rock passes through the barrier and topples over the golden idol. The barrier dissipates!\n"
                    "You walk into the temple to find mounds of gold and jewels that flood the room.\n"
                    "You've completed your quest! YOU WIN!\n")

            else:
                print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣀⣀⣀⣀⣀⣴⣶⣦⣄⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⡴⣶⠞⠛⠛⠋⠉⢉⡟⠁⠀⠀⠉⠉⠉⣩⠟⠛⠛⠛⠿⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠿⠋⠉⠀⠀⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⣀⠽⠟⠿⣷⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢠⣶⡶⠚⠙⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⠀⠀⠀⠀⠙⠻⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠛⠻⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⡠⠊⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢧⠀⠀⠀⠀⠀⠀⠀⠀
    ⢠⣾⠛⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠼⠿⣦⣤⠀⠀⠀⠀⠀
    ⣿⠈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀
    ⠘⠶⣴⡄⠀⠀⠀⠀⠀⠀⠀⢀⣤⠤⠤⢽⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣣⡀⠀⠀⠀
    ⠀⠀⠈⣿⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠈⠳⡍⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⢿⣦⠀⠀
    ⠀⠀⠀⢻⡇⠀⠀⠀⢠⣟⡈⠻⠷⠦⢤⣀⡀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣘⣿⠀⠀
    ⠀⠀⠀⠀⢻⡄⠀⠀⢸⠁⠉⠙⠲⢦⣄⡀⠉⠙⢻⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣩⡭⠭⠭⣍⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢹⣆⠀
    ⠀⠀⠀⠀⠀⠹⣆⠀⠸⡇⠀⠀⠀⠀⠀⠉⠙⠛⡿⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠉⠀⠀⠀⠀⠀⠈⠓⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀
    ⠀⠀⠀⠀⠀⠀⠘⢧⡀⠙⢦⡀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟⠒⢶⣤⡤⢤⣀⣀⣀⡀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⣦
    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠉⠓⠒⠒⠊⠁⠀⠀⠀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⣼⠓⠒⠤⢭⣀⣀⣀⣀⠉⠉⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠋⠉⡿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠈⠉⠉⠙⠛⡻⠁⠀⠀⠀⠀⠀⠀⢀⣀⠼⠳⠶⠛⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣄⡀⠀⠀⠀⠀⠐⠻⣦⣤⣤⣄⣀⣠⣤⡄⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⣀⠴⠁⠀⠀⠀⠀⣀⣤⠖⠋⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⣦⣄⡀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠒⠒⠋⠁⠀⠀⠀⣀⡴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⠿⠛⠲⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⣀⡜⢁⣸⣿⠭⠙⢳⡶⠶⢶⠶⠶⢶⡶⠒⠒⠺⣟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠙⣷⠉⢿⣉⣭⣥⠀⢹⡶⠾⠦⢤⠾⠖⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⣿⠀⠀⠁⣤⢾⡄⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠷⣤⣀⣀⣻⣆⣀⣀⣲⡿⠷⢯⣀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠛⠯⣀⣩⠟⠯⢥⣤⡤⠤⣏⠉⠙⣲⡖⠒⠛⠋⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠈⠒⠖⠋⠉⠳⠦⠤⠴⠾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣤⣄⣀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠉⠉⠓⠦⣤⠼⠟⠓⠲⠤⢤⣀⡀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠲⠶⠶⠶⢾⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠶⠶⠶⠶⠶⠶⠶⠶⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ''')
                print("\nAs you gaze at the temple confused, a strange being comes up behind you and snaps your neck. Game over.\n")
                

        elif second_choice == "flight":

            print('''
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     / ,  `\_/
                 |     \ '
    /\_        /`      /\ 
   /' /_``--.__/\  `,. /  \ 
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \ 
                            `\ \ 
                              \_\__
                               \___)

            ''')

            print("\nAs you take off running, the baboon charges after you. Right when you think " 
                "you\'ve gained advantage,\nyou trip on a tree root and the baboon tackles you and bites your face off. "
                "Game over.\n")

        else:
            print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⣀⣾⣄⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⣠⣴⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣶⣦⣤⡀⠀⠀
    ⠀⢠⡿⢉⣤⣤⣤⣿⣿⡿⠛⠛⠛⢿⣿⣿⣿⠟⠛⠛⢿⣿⣿⣦⣤⣤⡉⢻⡆⠀
    ⠀⣾⡇⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⢈⣿⣿⣿⣿⣿⡇⢸⣿⠀
    ⠀⠸⣷⡘⠻⠿⠟⠻⣿⣿⣦⣤⣴⡿⣿⣿⠿⣦⣤⣤⣾⣿⡟⠻⠿⠟⢃⣼⠏⠀
    ⠀⠀⠈⠻⠷⣶⡶⠿⠛⠻⣿⣿⣿⠀⣾⣿⠀⣿⣿⣿⠿⠛⠻⢶⣶⠶⠟⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣈⡉⠙⠛⠛⠛⠛⠛⢉⣁⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ''')
            print("\nYou freeze up in front of the baboon and it mauls you before you could think to do anything reasonable. Game over.\n")

    elif first_choice == "right":
        print('''
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡿⠛⠋⠁⠀⠀⢀⣀⣀⣀⣠⣤⣤⣄⣀⣀⣀⡀⠀⠀⠈⠙⠛⢿⣿⣿⣿
    ⣿⡿⠃⠀⢀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀⠀⠘⢿⣿
    ⣿⡇⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢸⣿
    ⣿⣷⡄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢠⣾⣿
    ⣿⣿⣿⣷⣤⣌⡙⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⢋⣡⣤⣾⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ''')

        print("\nAs you continue your trek into the jungle, you fall into a sink hole.\n"
            "Silly. Game over.\n")

    else:
        print('''
         O
        /|\   <-- Before
        / \ 
        ~~~~~~~~~~~~  <-- Cliff edge
                
                   \ | / 
                    
                    \O/
                     |    <-- After hahaha
                    / \ 
        ''')
        print("\nWrong way. You fall off a cliff and die. Game over.\n")

def main():
    while True: # this is the main game loop - it keeps running until broken
        play_game() # runs game once
        while True: # this is the input validation loop
            play_again = input("Would you like to play again? (yes/no):\n").lower()
            if play_again in ['yes', 'no']:
                break
            print("\nPlease enter 'yes' or 'no'.\n")
        
        if play_again == 'no':
            print("\nThanks for playing! Goodbye!\n")
            break

# this ensures the game only starts if the file is run directly
if __name__ == "__main__":
    main()
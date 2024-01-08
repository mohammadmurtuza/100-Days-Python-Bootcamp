import time,sys,os
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0001)  # Adjust the sleep duration for the desired typing speed
    print("")

print('''
                                                .------..------..------..------.      .------..------.          
                                                |G.--. ||A.--. ||M.--. ||E.--. |.-.   |O.--. ||F.--. |          
                                                | :/\: || (\/) || (\/) || (\/) ((5))  | :/\: || :(): |          
                                                | :\/: || :\/: || :\/: || :\/: |'-.-. | :\/: || ()() |          
                                                | '--'G|| '--'A|| '--'M|| '--'E| ((1))| '--'O|| '--'F|          
                                                `------'`------'`------'`------'  '-' `------'`------'          
                                                .------..------..------..------..------..------..------..------.
                                                |T.--. ||H.--. ||R.--. ||O.--. ||N.--. ||E.--. ||S.--. ||!.--. |
                                                | :/\: || :/\: || :(): || :/\: || :(): || (\/) || :/\: || (\/) |
                                                | (__) || (__) || ()() || :\/: || ()() || :\/: || :\/: || :\/: |
                                                | '--'T|| '--'H|| '--'R|| '--'O|| '--'N|| '--'E|| '--'S|| '--'!|
                                                `------'`------'`------'`------'`------'`------'`------'`------'
''')
print("Welcome to the Game of Thrones.")
house = input("Select your House: \n1)Stark\'s \n2)Targaryen\'s \n3)Lannister\'s \n4)Baratheon\'s  \nEnter your choice: \nMy Lord ")

if house == "1":
    S_logo ='''
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣀⠀⠀⠀⠀⠙⣟⡓⠲⠶⠤⠤⠶⠒⠛⠙⢓⣲⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢛⣯⣉⠉⠉⠩⣭⡭⠴⠶⠶⠿⢄⠀⠀⠀⠀⠀⣀⣀⡤⠽⠿⠿⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣖⣒⠛⠉⢉⡄⢖⠒⠚⠋⣁⣤⣀⣰⣄⣀⣤⠑⠀⠀⠀⢀⣠⡤⣤⣤⠤⢤⣽⡈⠳⠦⣤⣤⣄⣀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⣀⣀⡤⠤⠖⠛⡽⠋⠉⣹⠏⠀⠀⠙⠲⣄⠰⠬⢭⡀⠁⠈⠁⠑⠲⠯⠑⣦⠀⠙⢄⡈⢙⡾⠷⠒⠉⢉⣉⣀⣉⡉⠛⢷⡶⠦⣤
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣉⣽⡶⠶⠖⣾⠁⠀⠐⠛⡲⠦⠤⢴⠆⠈⠳⣄⠀⠙⠋⠉⠉⠁⠂⠀⠀⠛⢀⣠⠴⠚⣋⡀⠐⠒⠒⠲⣤⡀⠀⠉⠲⡀⠙⣯⠋
                                                ⠀⠀⠀⠀⠀⠀⠀⠈⠳⢖⡛⠉⠉⠁⡼⠀⠀⠐⣻⠶⠶⠶⣾⠁⠀⠀⢸⠀⠀⠀⠈⠙⠛⠛⠉⣩⠉⠂⠀⡠⠚⠉⣠⠶⢯⠉⡉⠓⠦⣄⡀⠀⠙⢄⡀⠀⢀⡴⠃⠀
                                                ⠀⠀⠀⢀⣀⣀⣠⡤⠴⠒⣻⠟⢛⣽⣃⣀⢀⣼⠃⠀⠀⠀⡏⠀⣀⣀⣼⠴⠒⠒⢶⠁⠀⠀⠉⠁⠀⠀⡘⠁⣠⡎⠙⠦⠚⢯⣩⠷⡖⣬⣭⠷⢦⣤⣤⡤⠞⠀⠀⠀
                                                ⠀⠀⠀⠀⠉⢓⡦⢤⣀⡼⠃⠀⢠⠏⠁⠉⣩⣇⣀⣀⣤⡞⠋⠉⠉⢸⠃⠀⠀⠀⢸⠀⠀⠀⢀⡄⠀⠀⠁⡞⠹⡙⢶⣾⣀⡄⠁⠀⠉⠀⠸⠗⢊⣏⡜⠀⠀⠀⠀⠀
                                                ⠠⣤⡤⠴⠚⠉⣰⠋⠛⠓⠒⢶⡟⠀⠀⢀⡟⠉⠀⠀⢸⡇⠀⠀⠀⣼⢀⣀⣀⣠⡿⠒⠒⠚⣿⠁⠀⠀⠀⠁⠀⠦⣀⠉⠢⢼⡤⢶⡄⡀⠀⢀⡌⠁⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠙⠲⠤⣼⠃⠀⠀⠀⣐⡿⠒⠶⠶⢾⠀⠀⠀⢀⣾⡥⠤⠴⣾⠛⠉⠉⠉⡏⠀⠀⠀⠀⣿⠀⠀⢀⡰⠀⠀⠀⠀⠙⠲⢄⡈⠛⠯⣼⠚⣡⠃⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠒⢹⡏⠉⠛⠉⡟⠀⠀⠀⢀⣾⡤⠴⠖⡿⠁⠀⠀⠀⡇⠀⠀⠀⢠⣇⣤⣤⡤⢶⡷⠶⡞⠉⢀⡴⠚⠉⠉⠉⠲⡀⠈⠒⠀⠀⡹⠁⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⣸⣀⣠⣤⣴⣧⠤⠤⠶⣾⠁⠀⠀⠀⡇⠀⠀⠀⣰⣧⠤⠤⣶⠋⠁⢠⡇⠀⠀⣀⣼⠁⣰⠋⠀⠀⠀⠀⠀⢀⠷⠶⣾⣃⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠁⠀⠀⠀⡟⠀⠀⠀⢀⡇⠀⠀⣀⣰⡷⠖⠒⣻⠏⠀⠀⠀⣿⠀⠀⠸⠗⣻⠋⢉⣼⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠐⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⣀⣀⣤⡾⠛⠉⠉⢹⠏⠀⠀⠀⢹⡀⠀⠀⢀⣿⣀⣤⡤⠞⣿⢀⡞⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢸⡇⠀⠀⠀⢸⠀⠀⠀⢀⣸⣧⠴⠖⠋⠁⢸⠃⠀⣴⢿⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⣀⣀⣤⣿⠗⠛⠋⠉⢹⡇⠀⠀⠀⢀⣿⠀⡼⠁⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠰⡏⠀⠀⠀⠀⣼⣇⣤⡴⠖⢋⣽⣶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⣀⣀⣤⣶⠋⠁⢸⡇⢀⡞⠁⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⣠⣿⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⡼⠁⠈⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''
    print(S_logo)
    S_scene1 = '''
    You wake up in a rustic hut, surrounded by the chilling winds of the North. The walls are adorned with furs and banners 
    bearing the sigil of House Stark – the direwolf. Outside, the snow-covered landscape stretches endlessly, and the air is 
    crisp with the scent of pine.
    '''
    print_slow(S_scene1)
    time.sleep(3)
    S_intro = '''    You are.........\n
    Alaric Stark, named after the legendary King in the North, stands as the living embodiment of his noble lineage. Born to Lord Eddard Stark 
    and Lady Catelyn Tully, he shares a unique bond with his twin, Bran. Instead of jesting at Arya, Alaric chose to be her steadfast ally,
    practicing swordplay together and forming an unbreakable bond.
    Trained by his elder brothers Robb and Jon, Alaric developed into a formidable fighter, his skills honed on the foundations of loyalty 
    and family. His undying devotion to the Starks is evident in his readiness to lay down his life for their cause, a testament to the 
    enduring strength of House Stark. In times of peril, Alaric remains an unwavering shield for his kin, embodying the essence of honor, 
    duty, and familial love within the storied halls of Winterfell.
    '''
    print_slow(S_intro)
    print_slow("    Chapter 1: The Mysterious Letter............\n\n")
    print_slow('''
    In the quiet chambers of Winterfell, a raven descends, delivering a cryptic missive sealed with the emblem of House Baratheon. 
    As you break the wax seal, the parchment unfolds, revealing Brystan's words woven with intrigue. The inked script speaks 
    of shared destinies and the urgency of a clandestine rendezvous. The quill strokes dance like shadows, leaving you with a sense 
    of foreboding. A choice looms in the inked lines — to embrace the whispered fate or dismiss it to the winds of Winterfell.\n\n ''')
    S_choice = input("    What to do with the letter My Lord:\n    1) Respond positively and arrange a clandestine meeting.\n    2)Disregard the letter, skeptical of its authenticity.\n    3)Share the letter with trusted family members.\n    Enter Here: ")
    print_slow(S_choice)
    if S_choice == "1":
        print_slow('''    
    Beneath the cloak of night, You and Brystan Baratheon converge at a secluded spot, the moon casting a silvery glow on their faces. As they exchange glances,
    the weight of shared destinies hangs in the air, an unspoken understanding that binds their fates. Words spoken in hushed tones echo the ancient pact forming between 
    Stark and Baratheon, a clandestine alliance forged in the crucible of destiny. Shadows dance around them, concealing the secrets they've uncovered, as the bond 
    between the two houses takes root in the shadows of Westeros.\n\n''')
    elif S_choice == "2":
        print_slow('''
    The revelation of your hesitancy to heed Brystan's call resonates like a distant thunderclap. A fracture appears in the trust that once held the 
    promise of unity. Brystan Baratheon, feeling the weight of skepticism, withdraws into the shadows of doubt. The tendrils of mistrust weave through the tapestry 
    of potential alliances, casting a looming shadow over the prospects that once shimmered on the horizon. The delicate dance of allegiance stumbles, leaving the 
    fate of future alliances hanging in the balance.\n\n''')
    elif S_choice == "3":
        print_slow('''
    Within the stone walls of Winterfell, family members gather, their expressions a mosaic of concern and curiosity. Alaric Stark's decision to share the mysterious 
    letter sparks a deliberative air. Concerned whispers weave through the chambers, yet beneath the familial concern, there lies a foundation of trust. The Stark kin, 
    bound by blood and loyalty, respect Alaric's choice, fostering a sense of unity. In the crucible of shared secrets, the Stark legacy weathers the storm, standing 
    resilient against the winds of uncertainty.    \n\n''')
    else:
        print_slow("    Please choose, My Lord........")
    
    print_slow("    Chapter 2: Shadows of Dragons............\n\n")

    print_slow('''    
    You, delving into the ancient tapestry of Winterfell\'s history, stumbles upon a clandestine thread woven with the sigil of House 
    Targaryen. The hushed whispers of hidden connections reverberate through the stone walls, hinting at a Targaryen legacy buried 
    beneath the snow-laden grounds of the ancestral Stark seat. As Alaric\'s curiosity leads him deeper, the secrets of dragon 
    fire and ice unravel, revealing a chapter in Winterfell\'s past that holds the potential to shape the destinies of Houses Stark 
    and Targaryen alike.
    ''')

    

elif house == "2":
    T_logo ='''
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣴⣯⣿⣶⣶⣶⠖⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡄⠀⠀⠠⣦⣀⣛⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢀⣀⣀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣶⣶⣤⡄⠀⠉⢩⣿⣿⣿⣿⣛⠫⠙⠂⣻⣿⣿⣷⡌⠙⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠈⠋⠁⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠀⠀⣠⣼⣿⣿⣿⣷⣶⣦⣄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣾⣿⣿⡿⠟⠂⠉⠛⢿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⠿⠀⣰⣿⣿⠟⠉⠉⢹⣿⡿⢿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⢿⢿⣿⣟⡋⠀⠀⠀⠀⠘⣻⣿⣿⣦⠀⠀⠀⠀⣀⣿⣿⣿⣿⡿⠟⠀⠀⢹⣿⣿⡀⠀⠀⣼⣿⡿⠈⢻⣿⣿⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠐⣬⣉⠔⢱⣿⡟⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⡏⠀⣀⣴⣿⣿⣿⣿⡟⠟⠁⠀⠀⠀⠀⠛⣿⣿⣶⣿⣿⡿⠃⠀⠈⠉⣽⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠙⠉⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣧⣾⣿⣿⡿⢿⠏⠉⠀⢀⣀⣠⣤⣤⣤⣤⣬⣿⣿⣍⡉⠀⠀⠀⠀⠀⠀⢽⣿⣿⣿⣤⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⣼⠀⢀⡄⢀⣴⣆⣴⣶⣤⣤⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⠿⠁⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠉⣻⣿⣿⣇⠀⠀⠀⠀
                                                ⠀⠀⢰⣏⣰⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⣀⠀⣼⣿⣿⣿⣿⡿⠇⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠈⠻⣿⣿⡆⠀⠀⠀
                                                ⠀⢀⣾⣿⣿⣿⣿⠿⠋⠉⠉⠉⠻⠿⣿⣿⣿⣿⣥⣼⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠙⠻⣿⣿⣿⣿⣿⣿⣿⣦⡀⠈⠻⢿⣷⡄⠀⠀
                                                ⠀⣟⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠈⠉⠛⠀⢀⠀⠈⢻⣿⣿⠿⣿⣿⣿⣿⣦⠈⠻⣿⣷⣠⠀
                                                ⠀⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⣠⠀⣠⣾⣿⣿⠿⠛⠓⠀⠀⠀⠀⢠⣿⣷⣦⣄⠙⠁⠀⠈⢿⣿⣿⣿⣷⡀⢾⣿⣿⡀
                                                ⢰⣿⢻⣻⣿⡏⠀⠀⠀⠀⠀⢤⣤⣤⣶⡄⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣤⣤⡄⢀⣠⣿⣿⣿⣿⣿⣷⡄⠀⠀⠘⣿⣿⣿⣿⣷⡈⢿⣿⡇
                                                ⠻⠟⢸⠇⠿⠿⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⢻⣿⣿⣿⣿⣷⠈⣿⡇
                                                ⠐⠶⣋⠀⠀⠀⠀⠀⠀⠁⠙⠻⢿⣿⣿⣿⡆⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠸⡿⣿⣿⣿⣿⡇⠸⡇
                                                ⠀⣿⣿⠀⠀⠀⠀⣠⡤⠀⠀⠀⠀⠙⢿⣿⣷⡀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠹⣿⣿⣷⠀⠃
                                                ⠀⢿⣿⠀⢴⣷⣾⣿⣿⣿⣿⣂⡀⠀⢸⣿⣿⣷⡄⠀⠀⠀⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⢀⣿⣿⣿⠀⠀
                                                ⠀⣾⣿⣇⣾⡟⠁⠀⠀⠉⢿⣿⡟⠂⢿⣿⠉⢻⣿⣦⣀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀
                                                ⠀⠨⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣷⡆⠛⠁⠀⠀⠙⠻⣿⣿⣶⣤⣼⣿⣿⣿⣿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡇⠀⣿⣿⣿⣿⣿⠀⠀⣾⣿⣿⡿⠀⠀
                                                ⠀⠀⠘⣿⣷⣄⠀⠀⠀⢀⣰⣿⡏⠃⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⣿⣿⣿⣿⣿⠀⠀⢹⣿⣿⡇⠀⠀
                                                ⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⡟⠹⠃⠀⠀⠀⠀⢠⣤⡀⠀⠀⠀⠀⠈⣻⡿⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⠟⢻⣿⣿⣿⣿⣿⡉⠃⢠⣿⣿⣿⣿⣿⠀⠀⠀⣿⡿⠀⠀⠀
                                                ⠀⠀⠀⠈⣻⣿⡄⠀⠘⠉⠀⠀⠀⠀⠀⢀⣴⣶⣾⣿⣄⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⡏⠀⣼⣿⣿⣿⣿⣿⡗⠀⠀⠈⣿⣿⣿⡇⠀⠀⢰⣿⠃⠀⠀⠀
                                                ⠀⠀⠀⠀⠙⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣇⠃⠀⠀⣼⣿⣿⣿⠁⠀⢠⣿⠃⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⢾⣿⣧⡀⠀⠀⠀⠀⠀⠘⠙⠉⠉⠛⠻⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⡿⠿⣿⠇⢰⣿⣿⣿⣿⢿⡏⠀⣠⣾⣿⣿⣿⠃⠀⣠⡿⠃⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⢩⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⣠⣿⣿⣿⣿⡿⠈⠀⢺⣿⣿⣿⡿⠃⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣛⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⢈⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⡟⠛⠁⠀⠀⢈⣿⣿⠟⠁⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⠻⠟⠁⠀⠀⢀⣤⣾⡿⠋⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⠟⠻⠟⠁⠀⣰⣶⣶⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⢻⣿⣿⡿⠛⣻⣿⡿⠋⠙⠋⠁⠀⠀⢀⣠⣾⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⣤⣤⣤⣤⣴⣶⡾⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''
    print(T_logo)
    T_scene1 = '''
    As your eyes flutter open, you find yourself in a humble dwelling, far removed from the opulence of Dragonstone. 
    The air is heavy with the scent of smoke and the sound of crackling flames. You're not in a grand castle, but in 
    a place that speaks of exile. House Targaryen, once rulers of the Seven Kingdoms, now finds solace in the simplicity 
    of a borrowed hearth, a reminder of the tumultuous journey that led them to this humble abode.
    '''
    print_slow(T_scene1)
    time.sleep(3)
    T_intro = '''    You are.........\n
    Rhaenyra Targaryen, her violet eyes ablaze with an indomitable spirit, emerges as the resolute and spirited younger sister of Daenerys. 
    Six years her junior, Rhaenyra carries a fervent determination to restore the tarnished name of Targaryen to its former glory. Possessing
    the rare gift of being a true blood, impervious to flame, she stands as a living testament to the ancient Targaryen lineage. Her dragon,
    named in honor of Syrax, soars alongside her, the embodiment of their shared quest to reshape the destiny of Westeros and revive the 
    greatness of House Tragaryen.
    '''
    print_slow(T_intro)

elif house == "3":
    L_logo ='''
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣵⣠⣴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠉⣿⣯⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣼⠀⡆⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⢀⣆⣸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣾⣉⣻⣿⣿⣿⡿⣾⣷⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢠⣶⣦⠄⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣷⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣙⣿⣿⣿⣿⣿⣷⣀⠀⠀⠸⣿⣿⣦⣤⣼⠿⠥⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣀⠀⣀⣀⣤⡿⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠉⠉⠁⢰⣷⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠀⠀⠀⢀⣴⣿⠿⠛⠛⠛⣿⣿⣿⣿⣿⣯⣀⣀⡴⠀⢠
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⠟⢻⣿⣿⣿⣿⣧⣀⠀⠀⣀⣀⡉⠁⣀⣶⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠄⠀⢠⣿⠟⠁⠀⡄⠀⣰⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⡞
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢠⣿⡟⠀⠀⠀⠛⠛⠛⠁⠸⣿⣿⣿⣿⣿⣿⣿⣿⡄
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⠋⠀⣼⣿⡇⠀⠀⠀⠀⢀⣾⣀⣰⣿⣿⣿⣿⣿⣯⠁⠈⡇
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣤⡾⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⣿⡇⠀⠀⢻⣿⡇⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⠇⢹⣿⡿⠀⠈⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠉⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⣿⡿⠁⠠⠾⠟⠁⠀⠀⠀
                                                ⠀⡀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⠐⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣧⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⣀⣀⣀⡀⠘⠷⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⢈⣹⣿⣿⣿⣶⣤⣄⣀⡀⠀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠛⠛⠋⠀⠀⠀⠸⣿⡇⣴⣿⣿⣿⠿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⣀⣀⣙⣿⣿⣿⣿⠀⠀⢈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠸⠛⠛⢋⣉⣷⣿⣿⢟⣿⣿⣿⡟⠻⣿⡏⠙⣿⠟⢻⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣦⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠉⠉⠉⠀⠊⠁⠈⠛⠓⠀⠈⠁⠈⠉⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣆⠀⠀⠀⠸⡏⠉⣹⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠏⠀⡞⠙⠛⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢠⠀⠀⠀⣰⣾⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⢀⣠⣤⣤⣤⣤⣠⡀⠀⠘⢿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⣿⣄⣀⣀⣩⣿⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣸⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣧⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⣀⣾⣿⠋⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠛⢋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢿⣿⣶⣶⣶⣶⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⣿⣿⣿⣿⣿⣿⣿⣧⡸⠛⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⢀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠛⣿⣿⣿⣿⣟⠿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣼⣿⣿⣿⣿⣿⣿⣦⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⠿⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⣿⡿⣿⣿⣿⢿⣿⣿⣿⠁⢸⠟⠁⠀⠀⢼⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠏⢹⡿⠿⠋⣨⡿⠟⠁⠀⠀⠀⠀⠠⢴⡟⠋⠀⠀⠻⢿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⡉⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡇⢹⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⡟⢿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⡏⢿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠏⣿⣿⣿⣿⡟⠉⠀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⠈⠿⣋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''
    print(L_logo)
    L_scene1 = '''
    Your journey begins within the majestic halls of Casterly Rock, where every step echoes with the history of House Lannister.
    The wealth of the Westerlands surrounds you, and the air is filled with the whispers of alliances and schemes that define the 
    Lannister legacy.
    '''
    print_slow(L_scene1)
    time.sleep(3)
    L_intro = '''    You are.........\n
    Seraphina Lannister, the legendary lioness, stands as the fierce guardian of House Lannister\'s ancestral pride, her ferocity resonating 
    through the ages. Younger than Cersei, Jaime, and Tyrion, her loyalty and fearsome protection make her an indomitable force within the 
    golden halls of Casterly Rock. Cherished by all, Seraphina\'s beauty rivals Cersei\'s, yet her intellect and insatiable thirst for knowledge 
    mirror Tyrion\'s own. It is in this brotherly bond with Tyrion that her true strength lies, an unbreakable connection that transcends the 
    complexities of the Lannister legacy, marking her as both a captivating beauty and a formidable mind within the lion\'s den.
    '''
    print_slow(L_intro)

elif house == "4":
    B_logo ='''
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡄⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⢀⠀⠀⠀⢸⣿⡆
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠐⢦⣀⣀⣠⣿⣧⠀⠀⠀⠀⠀⠙⠲⣤⣾⣿⣿
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠀⠀⠀⡀⠀⠀⠀⠙⣿⣿⣿
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠀⠀⠀⠀⠀⢿⡀⠀⠀⠤⣀⣀⣀⣨⣿⣿⣿⠃⠀⡀⠘⣦⡀⠀⢀⣿⣿⡟
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⢸⣧⠀⠀⢀⠆⠉⢿⣿⣿⣿⣿⢀⡞⠀⠀⢸⣿⣿⣿⣿⡿⠁
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡄⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⣼⡿⠀⠀⣾⠀⠀⠀⣿⣿⣿⢇⣾⠀⠀⠀⣸⣿⣿⣿⠟⠁⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣄⣀⠈⠳⣤⣀⣀⣤⣴⡶⠿⠿⠿⠿⠿⣿⣶⣶⣿⣤⣤⣄⣛⣛⣃⣾⣿⣀⣠⣴⣿⠿⠛⠁⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡈⠛⠻⢶⣜⣿⣿⣯⣥⣤⣶⣿⣦⣤⣤⣀⣀⣰⣶⣽⡭⠍⠙⠛⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣟⣣⣤⣭⣿⣿⠅⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⡿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⡏⣾⣿⣍⡉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣟⣽⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣏⠉⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣾⣀⣤⣾⢿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠿⠟⠛⢾⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣯⣒⢤⡀⢸⡿⠿⠓⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣮⣕⡢⣄⠰⠿⠧⣤⠯⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣦⡀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⠶⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⣠⣼⡿⠛⠙⣿⣷⡄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⢀⣠⣾⠿⠋⠀⣶⣿⣾⣟⡻⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⣠⣿⡿⠏⠀⠀⠀⣿⣿⠛⠿⣿⣷⣯⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠼⠛⠛⠁⠀⠀⠀⠀⣿⣿⠀⠀⠀⠙⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⢸⡿⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄⠀⠀⠀⠀⠁⠙⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⠛⠟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣻⢿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣾⡍⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⠷⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⠋⠀⠹⢿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠀⢻⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣤⣤⣶⣶⣿⣿⣿⡆⠀⢻⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''
    print(B_logo)
    B_scene1 = '''
    As you awaken, the Red Keep looms in the distance, a symbol of the authority that House Baratheon now holds over the Seven Kingdoms. 
    The room, though not as lavish as the Lannister quarters, speaks of the newfound rulership and responsibilities that come with being 
    seated on the Iron Throne.
    '''
    print_slow(B_scene1)
    time.sleep(3)
    B_intro = '''    You are.........\n
    Brystan Baratheon, the clandestine legacy forged in the shadows, is the legitimate and eldest son of Robert Baratheon, a master smith 
    and warrior renowned for crafting the Baratheon path. Born of a secret union with Lady Elara Stark, a distant cousin sought after the 
    tragic death of Lyanna Stark, their love was shrouded in magic and secrecy. Elara, carrying the weight of this clandestine bond, gave 
    birth to Brystan before meeting her untimely end. Hidden from even the knowledge of Ned Stark, Brystan\'s existence intertwines with the 
    complexities of love, loss, and the veiled history of House Baratheon.
    '''
    print_slow(B_intro)



else:
    print("You belong to a small house, this is no place here for a lowborn. low borns should address Mi Lord...")
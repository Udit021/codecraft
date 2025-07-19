showed_pattern_art = False
showed_code_art = False

while True:
    print('\033[34m                 === Pattern printer and Code Converter ===\033[0m')
    print("What would you like to do?")
    print('''\033[33m 1
 ____       _   _                    ____       _       _   _             
|  _ \ __ _| |_| |_ ___ _ __ _ __   |  _ \ _ __(_)_ __ | |_(_)_ __   __ _ 
| |_) / _` | __| __/ _ \ '__| '_ \  | |_) | '__| | '_ \| __| | '_ \ / _` |
|  __/ (_| | |_| ||  __/ |  | | | | |  __/| |  | | | | | |_| | | | | (_| |
|_|   \__,_|\__|\__\___|_|  |_| |_| |_|   |_|  |_|_| |_|\__|_|_| |_|\__, |
                                                                    |___/  \033[0m ''')
    print('''\033[32m2 
  ____          _         ____                              _             
 / ___|___   __| | ___   / ___|___  _ ____   _____ _ __ ___(_) ___  _ __  
| |   / _ \ / _` |/ _ \ | |   / _ \| '_ \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
| |__| (_) | (_| |  __/ | |__| (_) | | | \ V /  __/ |  \__ \ | (_) | | | |
 \____\___/ \__,_|\___|  \____\___/|_| |_|\_/ \___|_|  |___/_|\___/|_| |_| \033[0m''')
    print("Type '\033[31mstop\033[0m' to exit.")

    main_choice = input('\033[33mEnter your choice (1/2/stop): \033[0m').strip().lower()

    if main_choice == "stop":
        print("\033[33mThank you for using the Pattern and Code Converter. Goodbye!\033[0m")
        break

    elif main_choice == "1":
        if not showed_pattern_art:
            print('''\033[33m                                                                                                              
              ........                                                                                         
           .....:++:...                                     .....  .....                                       
           ...:++++++:.                                     .*%%.  .-%%.                                       
         ....++++++++:.              ....        ......     .*%%.  .-%%.     ......        .....    ......     
      .....=+++++++-..=+:..     :%%+*%%%%#-.   .-#%%%%*=%%-.#%%%%%:=%%%%%=..-#%%%%*:.  -%%+#%%%:-%%+#%%%%=.    
    .....=+++++++-..=+++++:...  :%%%%=::#%%#...#%%#-:-%%%%-.=%%%*+.-*%%**:.#%%*::+%%*..-%%%#-+-.-%%%+::#%%+.   
    ...=+++++++=..=+++++++-...  :%%*.    -%%*.+%%=.  ..+%%- .*%%.  .-%%. .*%%+=+++*%%=.-%%+..  .-%%+. ..#%%.   
  ...-++++++++..=++++++++..     :%%=     .%%#.*%%:    .-%%- .*%%.  .-%%. .#%%%%%%%%%%+.-%%=.   .-%%=   .#%%..  
  ..++++++++...++++++++..       :%%#.....-%%*.+%%+.....#%%- .*%%.  .-%%. .=%%-....:%-..-%%=.   .-%%=   .#%%..  
  ...-++++......-++++....       :%%%%%#%%%%+. .=%%%%%%%%%%- .*%%.  .-%%.  .+%%%##%%%#..-%%=.   .-%%=   .#%%.   
    ...:..... ....:....         :%%+.*##*+..    .-*#**:-**: .=*+.  ..**..  ..-****=..  :**-.   .:**:   .+*+.   
                                :%%+ .                                                                         
                                :%%+                                                                          
                               .:%%+.                                                                         
                               .....                                                                          
            \033[0m''')
            showed_pattern_art = True

        print('\033[34m\n               =======Pattern Types=======')
        print("1. Square")
        print("2. Right-Angle Triangle")
        print("3. Inverted Right-Angle Triangle")
        print("4. Pyramid")
        print("5. Diamond")
        print("6. Pascal's Triangle")
        print("7. Hollow Square")
        print("8. Hollow Pyramid\033[0m")

        pattern_choice = input('\033[33mChoose pattern type (1–8): \033[0m')

        if pattern_choice == "1":
            n = int(input("Enter size: "))
            i = 0
            while i < n:
                print('\033[33m' + "* " * n + '\033[0m')
                i += 1

        elif pattern_choice == "2":
            n = int(input("Enter height: "))
            i = 1
            while i <= n:
                print('\033[33m' + "* " * i + '\033[0m')
                i += 1

        elif pattern_choice == "3":
            n = int(input("Enter height: "))
            i = n
            while i >= 1:
                print('\033[33m' + "* " * i + '\033[0m')
                i -= 1

        elif pattern_choice == "4":
            n = int(input("Enter height: "))
            i = 0
            while i < n:
                print('\033[33m' + " " * (n - i - 1) + "* " * (i + 1) + '\033[0m')
                i += 1

        elif pattern_choice == "5":
            n = int(input("Enter height: "))
            i = 0
            while i < n:
                print('\033[33m' + " " * (n - i - 1) + "* " * (i + 1) + '\033[0m')
                i += 1
            i = n - 2
            while i >= 0:
                print('\033[33m' + " " * (n - i - 1) + "* " * (i + 1) + '\033[0m')
                i -= 1

        elif pattern_choice == "6":
            rows = int(input("Enter number of rows: "))
            i = 0
            while i < rows:
                print(" " * (rows - i), end="")
                j = 0
                val = 1
                while j <= i:
                    print('\033[33m' + f"{val} " + '\033[0m', end="")
                    val = val * (i - j) // (j + 1)
                    j += 1
                print()
                i += 1

        elif pattern_choice == "7":
            n = int(input("Enter size: "))
            i = 0
            while i < n:
                if i == 0 or i == n - 1:
                    print('\033[33m' + "* " * n + '\033[0m')
                else:
                    print('\033[33m' + "* " + "  " * (n - 2) + "* " + '\033[0m')
                i += 1

        elif pattern_choice == "8":
            n = int(input("Enter height: "))
            i = 1
            while i <= n:
                line = " " * (n - i)
                j = 1
                while j <= (2 * i - 1):
                    if j == 1 or j == (2 * i - 1) or i == n:
                        line += "*"
                    else:
                        line += " "
                    j += 1
                print('\033[33m' + line + '\033[0m')
                i += 1

        else:
            print('\033[31mInvalid pattern option. Please try again.\033[0m')

    elif main_choice == "2":
        if not showed_code_art:
            print('''\033[31m
                              .@@@%:.  .:%@@@.                              
                             .%@@@@@@@@@@@@@@%.                             
                             :@@@@@@@@@@@@@@@@:                             
                             -@@@@@@@@@@@@@@@@-                             
                            .@@@@@@@@@@@@@@@@@@.                            
                            .@@@@@@@@@@@@@@@@@@..                           
                 .*@@@@@@@@@*@@@@@@@@@@@@@@@@@@*@@@@@@@@@*.                 
                 *@@@@@@@@@%   ..-+#%%%%#+-..  .#@@@@@@@@@#.                
                 :@@@@@@@@@@#-..            ..-#@@@@@@@@@@:.                
                  .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.                 
                      .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.                     
                     ..#@@@ ....:=*##%%##*=:.....@@@#.                     
                    +@@@@@@:+@@@@@@@@##@@@@@@@@+:@@@@@@+.                  
                  +@@@@@@@@@.-@@@@@@:  :@@@@@@-.@@@@@@@@@+.                
                .%@@@@@@@@@@=                  =@@@@@@@@@@@.               
                 .@@@@@@@@@@@.                .@@@@@@@@@@@.                
                  .*@@@@@@@@@@:              :@@@@@@@@@@*.                 
                    .=@@@@@@@@@*           .+@@@@@@@@@+.                   
                  .:@@@:#@@@@@@@@=.      .=@@@@@@@@#:@@@:.                 
                :@@@@@@@@@%-@@@@@@@@+..+@@@@@@@@=%@@@@@@@@@:               
              .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..           
             -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=           
              .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.            
                .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.              
                  ..*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.                 
                       .*@@@@@@@@@@@@@@@@@@@@@@@@@@#:.                    
                            ..-*@@@@@@@@@@@@#=:..                          
            \033[0m''')
            showed_code_art = True

        print('\033[34m\nCode Conversion Options:')
        print("1. Text to Morse Code")
        print("2. Text to NATO Code")
        print("3. Morse Code to Text")
        print("4. NATO Code to Text\033[0m")

        code_choice = input('\033[33mChoose code conversion option (1–4): \033[0m')

        if code_choice == "1":
            morse = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', ' ': '/'
            }
            print("\033[36m(Note: Only letters A–Z and space are supported)\033[0m")
            text = input("Enter text to convert: ").upper()
            code = ""
            for ch in text:
                if ch in morse:
                    code += morse[ch] + " "
                else:
                    print(f"\033[31mUnsupported character skipped: {ch}\033[0m")
            print('\033[33mMorse Code:\033[0m\n', code)

        elif code_choice == "2":
            nato = {
                'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
                'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
                'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
                'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
                'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
                'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
                'Y': 'Yankee', 'Z': 'Zulu', ' ': '/'
            }
            print("\033[36m(Note: Only letters A–Z and space are supported)\033[0m")
            text = input("Enter text to convert: ").upper()
            code = ""
            for ch in text:
                if ch in nato:
                    code += nato[ch] + " "
                else:
                    print(f"\033[31mUnsupported character skipped: {ch}\033[0m")
            print('\033[33mNATO Code:\033[0m\n', code)

        elif code_choice == "3":
            morse_inv = {
                '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                '-.--': 'Y', '--..': 'Z', '/': ' '
            }
            code = input("Enter Morse Code (space-separated): ").split()
            text = ""
            for symbol in code:
                if symbol in morse_inv:
                    text += morse_inv[symbol]
                else:
                    print(f"\033[31mUnknown Morse code skipped: {symbol}\033[0m")
            print('\033[33mConverted Text:\033[0m\n',text)

        elif code_choice == "4":
            nato_inv = {
                'ALPHA': 'A', 'BRAVO': 'B', 'CHARLIE': 'C', 'DELTA': 'D',
                'ECHO': 'E', 'FOXTROT': 'F', 'GOLF': 'G', 'HOTEL': 'H',
                'INDIA': 'I', 'JULIETT': 'J', 'KILO': 'K', 'LIMA': 'L',
                'MIKE': 'M', 'NOVEMBER': 'N', 'OSCAR': 'O', 'PAPA': 'P',
                'QUEBEC': 'Q', 'ROMEO': 'R', 'SIERRA': 'S', 'TANGO': 'T',
                'UNIFORM': 'U', 'VICTOR': 'V', 'WHISKEY': 'W', 'X-RAY': 'X',
                'YANKEE': 'Y', 'ZULU': 'Z', '/': ' '
            }
            code = input("Enter NATO Code (space-separated): ").upper().split()
            text = ""
            for word in code:
                if word in nato_inv:
                    text += nato_inv[word]
                else:
                    print(f"\033[31mUnknown NATO code skipped: {word}\033[0m")
            print('\033[33mConverted Text:\033[0m\n', text)

        else:
            print('\033[31mInvalid code option. Please try again.\033[0m')

    else:
        print('\033[31mInvalid choice. Please enter 1, 2, or stop.\033[0m')

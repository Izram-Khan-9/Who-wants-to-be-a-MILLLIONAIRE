import time
import sys

# Prize bank
bank = 0

# All questions
questions = [
    # 🧠 General Knowledge
    ["What is the capital city of Japan?", "Seoul", "Tokyo", "Beijing", "Kyoto"], # B
    ["Which language has the most native speakers worldwide?", "English", "Mandarin Chinese", "Spanish", "Hindi"], # B

    # 🧪 Science
    ["What gas do plants absorb during photosynthesis?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"], # C
    ["What part of the human brain controls balance and coordination?", "Cerebellum", "Cerebrum", "Medulla", "Thalamus"], # A

    # 🧮 Mathematics
    ["What is the sum of all interior angles in a hexagon?", "540°", "600°", "720°", "900°"], # C
    ["The golden ratio is approximately equal to which number?", "1.414", "1.5", "2.0", "1.6"], # D

    # 💻 Technology / Computer Science
    ["Which data structure uses the principle of 'First In, First Out'?", "Stack", "Queue", "Tree", "Graph"], # B
    ["Which company developed the first commercially successful microprocessor?", "Intel", "IBM", "Motorola", "Apple"], # A

    # 📜 History
    ["Who was the first emperor of China?", "Kublai Khan", "Qin Shi Huang", "Sun Yat-sen", "Han Wudi"], # B
    ["The fall of the Berlin Wall occurred in which year?", "1985", "1987", "1989", "1991"], # C

    # 🌍 Geography
    ["Which African country has the largest population?", "Nigeria", "Ethiopia", "Egypt", "South Africa"], # A
    ["What is the longest river in the world?", "Nile", "Amazon", "Yangtze", "Mississippi"], # A

    # 📚 Literature
    ["Who wrote 'One Hundred Years of Solitude'?", "Mario Vargas Llosa", "Pablo Neruda", "Jorge Luis Borges", "Gabriel García Márquez"], # D

    # 🔢 Logic / Philosophy
    ["In logic, what does the statement '¬(A ∨ B)' mean according to De Morgan’s laws?", "¬A ∧ ¬B", "A ∧ B", "¬A ∨ ¬B", "A ∨ ¬B"], # A

    # 🚀 Advanced Science
    ["Which fundamental force is responsible for radioactive decay?", "Gravitational", "Electromagnetic", "Strong Nuclear", "Weak Nuclear" ] # D
]

# Animation function for the loading of all the questions
def progress_bar(message='Checking your answer', delay=0.1, length=20):
    for i in range(length + 1):
        bar = '█' * i + '-' * (length - i)
        print(f'\r{message}: [{bar}] {int(i/length*100)}%', end='', flush=True)
        time.sleep(delay)
    print()

# Animation function for the winner

# Func_1
def typing_effect_1(text='🎉🎉🎉CONGRATULATIONS🎉🎉🎉', delay= 0.06):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(delay)

# Func_2
def typing_effect_2(text='🏆🏆 YOU BEAT THE GAME! 🏆🏆🏆', delay = 0.06):
    for i in text:
        print(i, end = '', flush=True)
        time.sleep(delay)

# Func_3
def typing_effect_3(text='🔥❤️‍🔥YOU ARE NOW A MILLIONAIRE❤️‍🔥🔥', delay=0.06):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Func_4. For the message "LEGEND"
def typing_effect_4(text, delay = 0.02):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Function for asking all questions
def ask_1():
    global bank
    print("\n===============================")
    print(f"Q1 ➤ {questions[0][0]}")
    print("===============================")
    print(f"(A) {questions[0][1]}     (B) {questions[0][2]}")
    print(f"(C) {questions[0][3]}     (D) {questions[0][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'B':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_1 = 50
            bank += prize_1 
            print(f"You've earned ${prize_1} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[0][2]}')
            print('\n💸 You lost everything!')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_2():
    global bank
    print("\n===============================")
    print(f"Q2 ➤ {questions[1][0]}")
    print("===============================")
    print(f"(A) {questions[1][1]}     (B) {questions[1][2]}")
    print(f"(C) {questions[1][3]}     (D) {questions[1][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'B':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_2 = 100
            bank += prize_2
            print(f"You've earned ${prize_2} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[1][2]}')
            print('\n💸 You lost everything!')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_3():
    global bank
    print("\n===============================")
    print(f"Q3 ➤ {questions[2][0]}")
    print("===============================")
    print(f"(A) {questions[2][1]}     (B) {questions[2][2]}")
    print(f"(C) {questions[2][3]}     (D) {questions[2][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'C':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_3 = 150
            bank += prize_3 
            print(f"You've earned ${prize_3} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'B', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[2][3]}')
            print('\n💸 You lost everything!')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_4():
    global bank
    print("\n===============================")
    print(f"Q4 ➤ {questions[3][0]}")
    print("===============================")
    print(f"(A) {questions[3][1]}     (B) {questions[3][2]}")
    print(f"(C) {questions[3][3]}     (D) {questions[3][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'A':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_4 = 250
            bank += prize_4
            print(f"You've earned ${prize_4} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['B', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[3][1]}')
            print('\n💸 You lost everything!')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_5():
    global bank
    print("\n===============================")
    print(f"Q5 ➤ {questions[4][0]}")
    print("===============================")
    print(f"(A) {questions[4][1]}     (B) {questions[4][2]}")
    print(f"(C) {questions[4][3]}     (D) {questions[4][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'C':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_5 = 500
            bank += prize_5
            print(f"You've earned ${prize_5} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'B', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[4][3]}')
            print('\n💸 You lost everything!')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_6():
    global bank
    print("\n===============================")
    print(f"Q6 ➤ {questions[5][0]}")
    print("===============================")
    print(f"(A) {questions[5][1]}     (B) {questions[5][2]}")
    print(f"(C) {questions[5][3]}     (D) {questions[5][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'D':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_6 = 1000
            bank += prize_6
            print(f"You've earned ${prize_6} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'B', 'C']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[5][4]}')
            bank = 2050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_7():
    global bank
    print("\n===============================")
    print(f"Q7 ➤ {questions[6][0]}")
    print("===============================")
    print(f"(A) {questions[6][1]}     (B) {questions[6][2]}")
    print(f"(C) {questions[6][3]}     (D) {questions[6][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'B':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_7 = 2000
            bank += prize_7
            print(f"You've earned ${prize_7} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[6][2]}')
            bank = 2050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_8():
    global bank
    print("\n===============================")
    print(f"Q8 ➤ {questions[7][0]}")
    print("===============================")
    print(f"(A) {questions[7][1]}     (B) {questions[7][2]}")
    print(f"(C) {questions[7][3]}     (D) {questions[7][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'A':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_8 = 4000
            bank += prize_8 
            print(f"You've earned ${prize_8} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['B', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[7][1]}')
            bank = 2050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_9():
    global bank
    print("\n===============================")
    print(f"Q9 ➤ {questions[8][0]}")
    print("===============================")
    print(f"(A) {questions[8][1]}     (B) {questions[8][2]}")
    print(f"(C) {questions[8][3]}     (D) {questions[8][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'B':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_9 = 8000
            bank += prize_9
            print(f"You've earned ${prize_9} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[8][2]}')
            bank = 2050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_10():
    global bank
    print("\n===============================")
    print(f"Q10 ➤ {questions[9][0]}")
    print("===============================")
    print(f"(A) {questions[9][1]}     (B) {questions[9][2]}")
    print(f"(C) {questions[9][3]}     (D) {questions[9][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'C':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_10 = 16000
            bank += prize_10
            print(f"You've earned ${prize_10} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'B', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[9][3]}')
            bank = 2050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_11():
    global bank
    print("\n===============================")
    print(f"Q11 ➤ {questions[10][0]}")
    print("===============================")
    print(f"(A) {questions[10][1]}     (B) {questions[10][2]}")
    print(f"(C) {questions[10][3]}     (D) {questions[10][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'A':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_11 = 32000
            bank += prize_11
            print(f"You've earned ${prize_11} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['B', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[10][1]}')
            bank = 32050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_12():
    global bank
    print("\n===============================")
    print(f"Q12 ➤ {questions[11][0]}")
    print("===============================")
    print(f"(A) {questions[11][1]}     (B) {questions[11][2]}")
    print(f"(C) {questions[11][3]}     (D) {questions[11][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'A':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_12 = 63500
            bank += prize_12
            print(f"You've earned ${prize_12} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['B', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[11][1]}')
            bank = 32050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_13():
    global bank
    print("\n===============================")
    print(f"Q13 ➤ {questions[12][0]}")
    print("===============================")
    print(f"(A) {questions[12][1]}     (B) {questions[12][2]}")
    print(f"(C) {questions[12][3]}     (D) {questions[12][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'D':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_13 = 127000
            bank += prize_13
            print(f"You've earned ${prize_13} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['A', 'B', 'C']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[12][4]}')
            bank = 32050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_14():
    global bank
    print("\n===============================")
    print(f"Q14 ➤ {questions[13][0]}")
    print("===============================")
    print(f"(A) {questions[13][1]}     (B) {questions[13][2]}")
    print(f"(C) {questions[13][3]}     (D) {questions[13][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'A':
            print("\n💥💥💥 CORRECT! 💥💥💥")
            prize_14 = 254000
            bank += prize_14
            print(f"You've earned ${prize_14} 🪙")
            print(f"Total in bank: ${bank} 💰")
            break
        elif ans in ['B', 'C', 'D']:
            print('\n❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[13][1]}')
            bank = 32050
            print(f'\n💸 You lost!. You are taking ${bank} to your home.')
            print('──────────────────────────────')
            print('        💀 GAME OVER 💀        ')
            print('──────────────────────────────')
            bank = 0
            break
        else:
            print('\nPlease enter (A/B/C/D)')

def ask_15():
    global bank
    print("\n===============================")
    print(f"Q15 ➤ {questions[14][0]}")
    print("===============================")
    print(f"(A) {questions[14][1]}     (B) {questions[14][2]}")
    print(f"(C) {questions[14][3]}     (D) {questions[14][4]}")
    print("===============================")

    while True:
        ans = input('\nEnter your answer (A/B/C/D): ').upper()
        progress_bar()
        if ans == 'D':
            print('\n')
            typing_effect_1()
            typing_effect_2()
            typing_effect_3()
            typing_effect_4('''
            ──────────────────────────────
                    👑 LEGEND 👑         
            ──────────────────────────────
''')

            final_prize = 508000
            bank += final_prize
            print(f"\nFinal Bank: ${bank} 💵")
            break
        
        elif ans in ['A', 'B', 'C']:
            print('\n😱 SO CLOSE... 😱')
            print('❌ WRONG ANSWER ❌')
            print(f'💡 Correct answer: {questions[14][4]}')
            print('\n💥 You lost it all right at the end 💥')
            print('──────────────────────────────')
            print('       💔 GAME OVER 💔        ')
            print('──────────────────────────────')
            bank = 0
            break
        
        else:
            print('\nPlease enter (A/B/C/D)')

# A function for help
def help():

    print('\n')
    print("──────────────────────────────")
    print("        ℹ️ HELP MENU ℹ️       ")
    print("──────────────────────────────")
    time.sleep(0.5)
    print("""
🎯 GAME RULES:
• You will be asked 15 multiple-choice questions.
• Each correct answer increases your bank amount.
• One wrong answer ends the game instantly.

💰 CHECKPOINTS:
• After Question 5 → $2,050 guaranteed
• After Question 10 → $32,050 guaranteed
• Win all 15 → $1,000,000 and become the 👑 LEGEND 👑

🕹️ CONTROLS:
• Enter A, B, C, or D to select your answer.
• Type carefully — only the first letter counts.

Good luck, challenger!
──────────────────────────────
""")

def intro():
    title = """
────────────────────────────────────────────
      🎮 WHO WANTS TO BE A MILLIONAIRE 🎮
────────────────────────────────────────────
"""
    for char in title:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

    time.sleep(0.5)
    print("\nWelcome, challenger! 💪")
    time.sleep(0.7)
    print("You are about to enter the ultimate quiz arena!")
    time.sleep(0.7)
    print("15 questions stand between you and $1,000,000 💰")
    time.sleep(0.7)
    print("But beware — one wrong answer... and it’s all gone! 💀")
    time.sleep(1)
    print("\n────────────────────────────────────────────")
    print("           Let the game begin! 🚀")
    print("────────────────────────────────────────────\n")
    time.sleep(1)

# Main function to ask all questions
def play_game():
    global bank
    
    question_functions = [
        ask_1, ask_2, ask_3, ask_4, ask_5,
        ask_6, ask_7, ask_8, ask_9, ask_10,
        ask_11, ask_12, ask_13, ask_14, ask_15
        ]
    
    for i, func in enumerate(question_functions, start=1):
        prev_bank = bank
        func()
        
        if bank == 0:
            
            if i <= 5:
                print("\n💸 You leave with $0")
            elif i <= 10:
                print('\n💰 You reached the first checkpoint! You leave with $2050')   
            else:
                print("\n💰 You reached the second checkpoint! You leave with $32050") 
            break

        else:
            continue

# Starting from introduction
intro()

# Main loop to run the whole code
while True:
    
    print('\n1. Play')
    print('2. Help')
    print('3. Exit')
    
    user_choice = input('\nEnter you choice (1/2/3): ')
    
    if user_choice == '2':
        help()
        
    elif user_choice == '3':
        print('\nYou exited the program.')
        break
    
    elif user_choice == '1':
        play_game()
        break
        
    else:
        print('\nPlease enter a valid choice.')

#____________________________________THE-END____________________________________

# Created by: Izram Khan
# AI usage: 30%
# Completed on: 19/sep/2025
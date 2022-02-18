import random 

def is_empty(your_set):
    if len(your_set) != 0:
        return your_set
    else:
        return None

with open('word_list.txt') as f:
    raw_list = f.readline()
word_list = raw_list.split(',')

try:
    if input("\nGuess a five letter word? (Y/N)\n\n").lower() == 'y':
        while True:
            print('\nInput your answer after the row number.\n')
            target = random.choice(word_list)
            row_num = 1
            green = set()
            yellow = set()
            while row_num < 7 :
                guess = input('\U0001f4dd'+ 'Row ' + str(row_num) + '\n')
                if len(guess) > 5:
                    print('\nUgh you need to input a five letter word...\U0001f629')
                    print('Game Over!!!\n')
                    raise SystemExit
                if guess != target:
                    for index in range(5):
                        if guess[index] == target[index]:
                            green.add(guess[index])
                        elif guess[index] in target:
                            yellow.add(guess[index])
                    print('\n\U0001F978')
                    print('Yellow tiles - alphabet(s) guessed in the target word but at the wrong position: ', is_empty(yellow))
                    print('Green tiles - alphabet(s) guessed in the target word and at the correct position: ', is_empty(green))
                    print('\n')      
                    row_num += 1
                else: 
                    print('\n\U0001F929\U0001F929\U0001F929\U0001F929\U0001F929\n')
                    print("WOHOO! That's the word!")   
                    print(str(row_num) + "/6\n")
                    break
                if row_num == 7: 
                    print('\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\n')
                    print('Oh too bad... You run out of guesses \U0001f972.')
                    print('The word is ' + target +'.')
                    print('Hey you can play again! Maybe next time better luck!!\n\n') 
            if input('Do you want to play again right now? (Y/N)\n').lower() != 'y':
                print('\n')
                raise SystemExit   
            else:
                True

                        
    else:
        print('\nUgh boring...BYE!!\n')
        raise SystemExit
except IndexError:
    print('\nUgh you need to input a five letter word...\U0001f629')
    print('Game Over!!!\n')
    raise SystemExit
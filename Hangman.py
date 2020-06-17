import random
import re

def get_word_from_system():
    fname = 'listOfWords.txt'
    fh = open(fname)
    r_no = str(random.randrange(1,11))
    for line in fh:
        line = line.rstrip()
        if not line.startswith(r_no):
            continue
        list_r_word = re.findall('\.([^ ]*)',line)
        return list_r_word[0]

def check_letter(l,word):
    if l in word:
        to_print_list.clear()
        print('***** Bingo! This letter is present -> -> -> -> -> -> -> ',end='  ')
        for l1 in word:
            correct_tries_list.append(l)
            if l1 in correct_tries_list:
                print(l1,end=' ')
                to_print_list.append(l1)
            else:
                print('_',end=' ')
                to_print_list.append('_')
        return l
    else:
        incorrect_tries_list.append(l)
        print('*************** Sorry! This letter is not present')
        print('*************** You have %d more INCORRECT try(s) left'%(5 - wrong_tries_count ))
        print(' The list of INCORRECT letter(s) you guessed is/are : ',incorrect_tries_list,end=' ')
        return wrong_tries_count + 1

def get_letter():
    print()
    l = input('\nEnter a letter: ')
    l = l.upper()
    return l

print('************************ Welcome to the HANGMAN GAME !************************')
word = get_word_from_system()
#word= 'EXCELLENT'
print(word)
wrong_tries_count = 0
incorrect_tries_list = []
correct_tries_list = []
to_print_list = []

for i in range(len(word)):
    print('_',end=' ')

while wrong_tries_count < 6:
    l = get_letter()
    c_l = str(check_letter(l,word))
    if c_l.isdigit():
        wrong_tries_count = int(c_l)
    if '_' not in to_print_list and len(to_print_list) != 0:
        break

if wrong_tries_count >= 6:
    print('\n\n***************** OOPS ! YOU lost the game...Better Luck Next Time *****************')
else:
    print('\n\n************************ CONGRATULATIONS ! You Won the game ************************')

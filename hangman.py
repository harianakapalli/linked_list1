# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r') 
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if letters_guessed in secret_word:
      return letters_guessed
    else:
       a=False
       return a
        
        
        
def get_guessed_word(a,b):

    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
     '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str_1=""
    length=len(secret_word)
    for i in b:
      if i in a:
        str_1+=i
      else:
        str_1=str_1+"_"
    return str_1
def get_available_letters(guessed_char):
 
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
     '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str_1=""
    str_2=""
    letters=string.ascii_lowercase
    for i in letters:
        if i in guessed_char:
            str_1+=i
        else:
            str_2+=i
    total="Available letters: {0}"
    print(total.format(str_2))

def hangman(secret_word,counter):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
 
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"    
    guess=6-counter
    str_2="You have {} guesses left"
    print(str_2.format(guess))



 
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# --------------- --------------------
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
          False otherwise:  
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_with_no_spaces = ''
    letters_guessed = []
    for char in my_word:
        if char != ' ':
            my_word_with_no_spaces += char
            
        if char.isalpha():
            letters_guessed.append(char)
        
    if len(my_word_with_no_spaces.strip()) != len(other_word.strip()):
        return False
    
    for i in range(len(my_word_with_no_spaces)):
        current_letter =  my_word_with_no_spaces[i]
        other_letter = other_word[i]
        if current_letter.isalpha():
            has_same_letter = current_letter == other_letter
            if not has_same_letter:
                return False
        else:
            if current_letter == '_' and other_letter in letters_guessed:
                return False
            
    return True
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed. 
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''  
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)
    
    if len(matched_words) > 0:
      print("Possible word matches are:")
      for word in matched_words:
          print(word, end=' ')
      print()
    else:
        print('No matches found')
 


def hangman_with_hints(secret_word,counter):
    '''
    secret_word: string, the secret word to guess.
      
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess   
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
       
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess=6-counter
    str_2="You have {} guesses left"
    print(str_2.format(guess))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

char_1=[]
def cheking_uni_char(a):
    if a in char_1:
        return False
    elif a.isalpha():
        char_1.append(a)
        return True
  
if __name__ == "__main__":
    


    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
  
    
  secret_word = choose_word(wordlist)
  print("Welcome to the game Hangman!")
  length=len(secret_word)
  str_4="I am thinking of a word that is {} letters long."
  print(str_4.format(length))
  print("you have 3 warnings left. ")
  print("-"*10)
  print("You have 6 guesses left.")
  a=string.ascii_lowercase
  str_5="Available letters: {0}"
  print(str_5.format(a))
  counter=0
  count=6
  list_1=[]
  guessed_char=[]
  Warning=1
  while counter<=count:
    result=get_guessed_word(a=list_1,b=secret_word)
    if not("_") in result:
      print("Congratulations, you won!")
      a=set(result)
      length=len(a)
      remaining=6-counter
      str_13="Your total score for this game is: {}"
      print(str_13.format(remaining*length))
      break
    if counter==5:
      result=get_guessed_word(a=list_1,b=secret_word)
      if "_" in result:
        print("Sorry, you ran out of guesses. The word was else.")
        break
      else:
        print("Congratulations, you won!")
        a=set(result)
        length=len(a)
        remaining=6-counter
        str_13="Your total score for this game is: {}"
        print(str_13.format(remaining*length))
        break
    letters_guessed=input().lower()
    guessed_char.append(letters_guessed)
    checking=cheking_uni_char(letters_guessed)
    if letters_guessed.isalpha() and len(letters_guessed)==1 and checking==True:
      total=is_word_guessed(secret_word,letters_guessed)
      list_1.append(total)
      if total==False:
        list_3=["a","e","i","o","u"]
        if letters_guessed in list_3:
          counter+=2
        else:
          counter+=1
        hangman(secret_word,counter)
        #hangman_with_hints(secret_word,counter)
        result=get_guessed_word(a=list_1,b=secret_word)
        get_available_letters(guessed_char)
        str_8="Please guess a letter: {0}"
        print(str_8.format(letters_guessed))
        print("Oops! That letter is not in my word. ")
        str_8="Please guess a letter: {0}"
        print(str_8.format(result))
        print("-"*10)
      else:
        hangman(secret_word,counter)
        #hangman_with_hints(secret_word,counter)
        get_available_letters(guessed_char)
        result=get_guessed_word(a=list_1,b=secret_word)
        str_8="Please guess a letter: {0}"
        print(str_8.format(letters_guessed))
        str_9="Good guess: {0}"
        print(str_9.format(result))
        print("-"*10)
    elif letters_guessed=="*":
      str_8="Please guess a letter: {0}"
      print(str_8.format(letters_guessed))
      my_word=get_guessed_word(a=list_1,b=secret_word)
      other_word=show_possible_matches(my_word)

    elif checking==False and Warning<3:
      hangman(secret_word,counter)
      #hangman_with_hints(secret_word,counter)
      get_available_letters(guessed_char)
      str_8="Please guess a letter: {0}"
      print(str_8.format(letters_guessed))
      result=get_guessed_word(a=list_1,b=secret_word)
      str_9="Oops! You've already guessed that letter. You have {0} warnings left: {1} "
      print(str_9.format(3-Warning,result))
      Warning+=1
      print("-"*10)
    elif Warning<=3 and (letters_guessed.isdigit or not(letters_guessed.isalpha())):
      result=get_guessed_word(a=list_1,b=secret_word)
      hangman(secret_word,counter)
      #hangman_with_hints(secret_word,counter)
      get_available_letters(guessed_char)
      str_8="Please guess a letter: {0}"
      print(str_8.format(letters_guessed))
      str_3="Oops! That is not a valid letter. You have {0} warnings left: {1}"
      print(str_3.format(3-Warning,result))
      Warning+=1
      print("-"*10)
    else:
      counter+=1
      hangman(secret_word,counter)
      #hangman_with_hints(secret_word,counter)
      get_available_letters(guessed_char)
      str_8="Please guess a letter: {0}"
      print(str_8.format(letters_guessed))
      result=get_guessed_word(a=list_1,b=secret_word)
      str_10="Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {0}"
      print(str_10.format(result))
      print("-"*10)
  
      
     

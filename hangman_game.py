import random
import os


def ramdon_word():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        word = list(f)
        word = random.choice(word) 
        return word.strip().upper()


def run():
    hangmandoll= [
  """ 
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""",
  """ 
      +---+
      |   |
      O   |
    /|\   |
    /     |
          |
    =========""",
   """ 
      +---+
      |   |
      O   |
    /|\   |
          |
          |
    =========""",
  """ 
      +---+
      |   |
      O   |
    /|    |
          |
          |
    =========""",
  """ 
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
  """ 
      +---+
      |   |
          |
          |
          |
          |
    =========""",
  """""" 
  ]


    word = [word for word in(ramdon_word())]
    progress = []  
    attemps = 6
    letters_chosen =  []

    for i in range(len(word)):
      progress.append("_ ")

    word_win = "".join(word) 


    while attemps > 0:
        os.system("cls")
        os.system("clear")

        print('¡Adivina la palabra!')
        print(hangmandoll[ attemps], '\n')
        print(''.join(progress))
        print(f'\nTienes {attemps} vidas. 💚\n')


        letter_choosen_user = input(f'Elige una letra: ').strip().upper()
        assert letter_choosen_user.isalpha(), "Debes ingresar una letra"


        letters_chosen.append(letter_choosen_user)

        counter = True

    
        for i in range(len(word)):
          if letter_choosen_user in word[i]:
            progress[i] = letter_choosen_user
            counter = False
        

        for x in range(len(letter_choosen_user)):
          if letter_choosen_user in letters_chosen[x]:
            counter = False


        if counter == True:
          attemps -= 1 
          if attemps == 0:
            os.system("cls")
            os.system("clear")
            print('¡No lograste adivinar la palabra!')
            print(hangmandoll[0],"\n")
            print(f'Perdiste 😪. Exitos en la próxima. La palabra era {word_win}.')


        if progress == word:
            os.system("cls")
            os.system("clear")
            print(f'¡Ganaste!. La palabra era {word_win}. 👏')
            break


      
if __name__ == '__main__':
  run()
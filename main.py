import sys
import os
from data_service import return_to_start_words, get_possible_words, filter_words_with_two_letters, get_best_unique_letter_word_by_frequency
def main():
   
    

    return_to_start_words()
    while True:
        print("Action 1: Enter word with letter colors \n")
        print("Action 2: reset \n")
        print("Action 3: two hint letters \n")
        print("Action 4: exit \n")
        c = input("Enter action: ")
        match c:
            case "1":

                word = input("w: ")
                first_letter = input("l1: ")
                second_letter = input("l2: ")
                third_letter = input("l3: ")
                fourth_letter =input("l4: ")
                fifth_letter = input("l5: ")
                fw = get_possible_words(word,first_letter,second_letter,third_letter,fourth_letter,fifth_letter)
                print("Possible words:")
                print(fw)
                print("\nMost probable word: "+fw[0]+"\n")
                try:
                    
                    ##
                    with open("guessed_words.txt","a")as f:
                        f.write(word)
                    best_word2 = get_best_unique_letter_word_by_frequency(word)
                    if best_word2:
                        print("Most valuable word: "+best_word2+"\n")
                except Exception as e:
                    print(e)
            case "2":
                return_to_start_words()
                with open("guessed_words.txt","w") as f:
                    f.write("")
            case "3":
                l1 = input("l1: ")
                l2 = input("l2: ")
                print(filter_words_with_two_letters(l1,l2))
                try:
                    
                   ##
                    with open("guessed_words.txt","a")as f:
                        f.write(l1+l2)
                    best_word2 = get_best_unique_letter_word_by_frequency(l1+l2)
                    if best_word2:
                        print(best_word2+"\n")
                except Exception as e:
                    print(e)
                
            case "4":
                with open("guessed_words.txt","w") as f:
                    f.write("")
                sys.exit()
                
main()
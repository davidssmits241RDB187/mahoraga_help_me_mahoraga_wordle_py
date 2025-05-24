

def get_possible_words(guessed_word: str, first_letter: str, second_letter: str, third_letter: str, fourth_letter: str, fifth_letter: str):
    colors_word = [first_letter, second_letter, third_letter, fourth_letter, fifth_letter]
  
    with open("possible_words.txt", "r") as f:
        words = [line.strip() for line in f]
        
    filtered_words = []

   
    required_letters = {}
    for i, color in enumerate(colors_word):
        if color in ("green", "yellow"):
            required_letters[guessed_word[i]] = required_letters.get(guessed_word[i], 0) + 1
            
    for w in words:
        
        valid = True
        
        for i in range(5):
            guess_letter = guessed_word[i]
            word_letter = w[i]
            color = colors_word[i]
            
            if color == "green":
                if guess_letter != word_letter:
                    valid = False
                    
                    break
            elif color == "yellow":
                if guess_letter == word_letter or guess_letter not in w:
                    valid = False
                    
                    break
            elif color == "gray":
                if guess_letter in w:
                    count_in_word = w.count(guess_letter)
                    if count_in_word >= required_letters.get(guess_letter, 0) + 1:
                        valid = False
                      
                        break

        for letter, count in required_letters.items():
            if w.count(letter) < count:
                valid = False
                
                break

        if valid:
            filtered_words.append(w)

    with open("possible_words.txt","w") as f:
        for w in filtered_words:
            f.write(w+"\n")
    return filtered_words
def return_to_start_words():
    
    words = []
    with open("words.txt", "r") as src:
        words = [line for line in src]
            
    with open("possible_words.txt", "w") as dest:
        for line in words:
            dest.write(line)
        

    

                
                
    
                
                    



            
    
from collections import defaultdict, Counter
from collections import Counter
from itertools import permutations
def get_possible_words(guessed_word: str, first_letter: str, second_letter: str, third_letter: str, fourth_letter: str, fifth_letter: str):
    colors_word = [first_letter, second_letter, third_letter, fourth_letter, fifth_letter]
  
    with open("possible_words.txt", "r") as f:
        words = [line.strip() for line in f]
        
    filtered_words = []

    required_letters = {}
    for i, color in enumerate(colors_word):
        if color in ("3", "2"):
            required_letters[guessed_word[i]] = required_letters.get(guessed_word[i], 0) + 1
            
    for w in words:
        valid = True
        
        for i in range(5):
            guess_letter = guessed_word[i]
            word_letter = w[i]
            color = colors_word[i]
            
            if color == "3":
                if guess_letter != word_letter:
                    valid = False
                    break
            elif color == "2":
                if guess_letter == word_letter or guess_letter not in w:
                    valid = False
                    break
            elif color == "1":
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

    # Recalculate frequency from filtered words
    updated_letter_rank = get_dynamic_letter_rank(filtered_words)
    
    # Sort using the new rank
    filtered_words = sort_words_by_frequency(filtered_words, updated_letter_rank)
   
    with open("possible_words.txt", "w") as f:
        for w in filtered_words:
            f.write(w + "\n")

    return filtered_words

def return_to_start_words():
    with open("words.txt", "r") as src:
        words = [line for line in src]
    with open("possible_words.txt", "w") as dest:
        for line in words:
            dest.write(line)

def get_dynamic_letter_rank(words):
    frequency = Counter()
    for word in words:
        frequency.update(set(word))  # use set to count unique letters per word
    
    sorted_letters = [letter for letter, _ in frequency.most_common()]
    return {letter: rank for rank, letter in enumerate(sorted_letters)}

def sort_words_by_frequency(words, letter_rank, index=0):
    if len(words) <= 1 or index >= 5:
        return words
    
    groups = defaultdict(list)
    for word in words:
        key = word[index] if index < len(word) else ''
        groups[key].append(word)

    sorted_group_keys = sorted(groups.keys(), key=lambda k: letter_rank.get(k, float('inf')))
    sorted_words = []
    for key in sorted_group_keys:
        sorted_words.extend(sort_words_by_frequency(groups[key], letter_rank, index + 1))
    
    return sorted_words
def filter_words_with_two_letters(letter1, letter2):
   
    with open("possible_words.txt", "r") as f:
        words = [line.strip() for line in f]
    
   
    new_words = [word for word in words if letter1 in word and letter2 in word]
    
   
    updated_letter_rank = get_dynamic_letter_rank(new_words)
    
    
    sorted_words = sort_words_by_frequency(new_words, updated_letter_rank)
    

    with open("possible_words.txt", "w") as f:
        for w in sorted_words:
            f.write(w + "\n")
    
    return sorted_words







def get_best_unique_letter_word_by_frequency(entered_word: str):
    with open("possible_words.txt", "r") as f:
        possible_words = [line.strip() for line in f]
    with open("words.txt", "r") as f:
        words = [line.strip() for line in f]
    with open("guessed_words.txt","r") as f:
        entered_word+=f.read()
    
    usable_words =[]
    entered_word_set = set(entered_word)

    for w in words:
        if len(set(w)) < len(w):
            continue
        contains_possible_letters = any(letter in w for word in possible_words for letter in word)
        does_not_contain_entered_letters = all(letter not in entered_word_set for letter in w)
        if contains_possible_letters and does_not_contain_entered_letters:
            usable_words.append(w)
    
    letter_rank = get_dynamic_letter_rank(usable_words)
    usable_words = sort_words_by_frequency(usable_words,letter_rank)
    
    if usable_words[0]:
        return usable_words[0]
    return None



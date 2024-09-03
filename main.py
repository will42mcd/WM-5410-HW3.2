import string
import re

def process_file(fname,enc):
    with open(fname, 'r', encoding=enc) as file:
        dat = file.read()
        dat = perform_re(dat)
    return dat.split()
#end function

def write_results(fname, data, enc):
    with open(fname, 'w',encoding=enc) as file:
        file.write(data)
#end function

def words_to_dict(all_words, dictionary):
    for w in all_words:
        w = clean_word(w)
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
#end function

def clean_word(word):
    for p in string.punctuation:
        word = word.replace(p, "")
    return word.lower()
#end function

def perform_re(text):
    text = re.sub(r'(CHAPTER) ([IVXLC]+.)', '\\1\\2', text)
    return text
#end function

def main():
    while True:
        unique_words1 = {}
        unique_words2 = {}
        unique_words3 = {}
        texts = {"1": "alice.txt", "2": "the blue castle.txt", "3": "A room with a view.txt", "4": "Frankenstein.txt", "5": "great gatsby.txt" }
        text1, text2 = input("\nWhich two texts would you like to compare? (Type the 2 numbers corresponding to the text with no spaces)\n\n1. Alice's Adventures in Wonderland\n2. The Blue Castle\n3. A Room with a View\n4. Frankenstein\n5. The Great Gatsby\n")
        words1 = process_file(texts[text1], 'UTF-8')
        words2 = process_file(texts[text2], 'UTF-8')
        words_to_dict(words1, unique_words1)
        words_to_dict(words2, unique_words2)
        print(f"Found {len(unique_words1.keys())} unique words out of {len(words1)} total words in first choice.")
        print(f"Found {len(unique_words2.keys())} unique words out of {len(words2)} total words in first choice.\n")
        text3 = input("Would you like to compare a third choice?\n\n1. Alice's Adventures in Wonderland\n2. The Blue Castle\n3. A Room with a View\n4. Frankenstein\n5. The Great Gatsby\n")
        words3 = process_file(texts[text3], 'UTF-8')
        words_to_dict(words1, unique_words3)
        TTR1 = len(unique_words1.keys())/len(words1)
        TTR2 = len(unique_words2.keys())/len(words2)
        TTR3 = len(unique_words3.keys())/len(words3)
        print(f"Found {len(unique_words1.keys())} unique words out of {len(words1)} total words in first choice. The TTR is {TTR1}")
        print(f"Found {len(unique_words2.keys())} unique words out of {len(words2)} total words in first choice. The TTR is {TTR2}")
        print(f"Found {len(unique_words3.keys())} unique words out of {len(words3)} total words in first choice. The TTR is {TTR3}\n")

        if abs(len(words1)-len(words2)) >= 3000:
            print("TTR is not a reliable comparison for chosen texts for choices 1 and 2.")
        if abs(len(words2)-len(words3)) >= 3000:
            print("TTR is not a reliable comparison for chosen texts for choices 2 and 3.")
        if abs(len(words1)-len(words3)) >= 3000:
            print("TTR is not a reliable comparison for chosen texts for choices 1 and 3.")
        if abs(len(words1)-len(words2)) <= 3000:
            print("TTR is between comparable texts for choices 1 and 2.")
        if abs(len(words2)-len(words3)) <= 3000:
            print("TTR is between comparable texts for choices 2 and 3.")
        if abs(len(words3)-len(words1)) <= 3000:
            print("TTR is between comparable texts for choices 1 and 3.\n")
        wordSearch = input("What word would you like to search for in these three texts?\n")
        result1 = unique_words1.get(wordSearch, 0)
        result2 = unique_words2.get(wordSearch, 0)
        result3 = unique_words3.get(wordSearch, 0)
        print(f'{wordSearch} appears {result1} times in choice 1.')
        print(f'{wordSearch} appears {result2} times in choice 2.')
        print(f'{wordSearch} appears {result3} times in choice 3.')
        break
#end main function

if __name__ == "__main__":
    main()
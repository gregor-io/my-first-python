from english import english as english_dictionary

def split_string(source, splitlist):
    split_list = []
    result = []
    for c in splitlist:
        split_list.append(c)
    word = ''
    for letter in source:
        if letter not in split_list:
            word = word + letter
        if letter in split_list:
            if word != '':
                result.append(word.lower())
                word = ''
    if source.find(letter, len(source) - 1) == len(source) - 1 and letter not in split_list:
        result.append(word.lower())
    return result

def split_text():
    article_str = open("bible.txt", "r").read()
    article_list = split_string(article_str, " .,!:;123*4567890()[}]{")
    #article_list = article_str.split()
    with open('text_as_list.py', 'w') as f:
        f.write("text = %s" % article_list)


def build_dictionary():
    from text_as_list import text as article_list
    word_loc = 0
    doc_len = len(article_list)
    print(doc_len)
    while word_loc < doc_len:
        next_word = ""
        word = article_list[word_loc]
        if word_loc < doc_len - 1:
            next_word = article_list[word_loc + 1]
            print(word_loc + 1)
        if "\n\n" in word:
            word = word[2:]
        if word in english_dictionary:
            english_dictionary[word][0] = english_dictionary[word][0] + 1
            if next_word != "":
                if next_word in english_dictionary[word][1]:
                    english_dictionary[word][1][next_word] = english_dictionary[word][1][next_word] + 1
                else:
                    english_dictionary[word][1][next_word] = 1
        elif word not in english_dictionary:
            english_dictionary[word] = [0, {}]
            if next_word != "":
                english_dictionary[word][1][next_word] = 1
        word_loc = word_loc + 1
        #print(word_loc)
    with open('english.py', 'w') as f:
            f.write("english = %s" % english_dictionary)
    return
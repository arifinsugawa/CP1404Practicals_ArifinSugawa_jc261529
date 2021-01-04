word_dict = {}

sentence = input("Enter a sentence :")
sentence_list = sentence.split(" ")
for word in sentence_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

#change word_dict.keys to a list to sort
word_list = list(word_dict.keys())
word_list.sort()

#find longest word in list
longest_word_length = 0
for word in word_list:
    if len(word) > longest_word_length:
        longest_word_length = len(word)

for word in word_list:
    print("{:{}} : {}".format(word,longest_word_length,word_dict[word]))

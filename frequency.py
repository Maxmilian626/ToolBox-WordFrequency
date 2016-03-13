""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """
import string




def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	source = open(file_name)
	txt = source.read()
	for i in txt:
		if i in string.punctuation:
			txt.replace(i, "")
	word_list = text.split()
	return text.split()


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	pass 

counter = dict()
count_list[]

word_list = get_word_list("pg32325.txt")
for word in word_list:
	if word not in counter:
		counter[word] = 1
	else: 
		counter[word] += 1

for word in word_list:
	count_list.append(counter[word], word)

count_list.sort(reverse=True)

top100 = count_list[0:100]
print top100 #the buzzwords delivered.  
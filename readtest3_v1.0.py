
def file_read(file_name) :
	word = []
	with open(file_name, "r", encoding = "Big5") as f:
		for w in f :
			word.append(w.strip())
	return word


def dictionary(r_file_read) :
	dictionary = {}
	for line in r_file_read :
		for w in line :
			dictionary[w] = w
			if w in dictionary :
				continue
			else :
				dictionary[w] = w
	return dictionary

def word_statistic(r_file_read, r_dictionary) :
	count = {}
	for w in r_dictionary :
		n = 0
		for line in r_file_read :
			for s in line :
				if w == s :
					n += 1
					count[w] = n
				else :
					continue
	return count

def main() :
	word = file_read("dict.txt")
	dictionary1 = dictionary(word)
	count = word_statistic(word, dictionary1)
	print(count)

main()
	



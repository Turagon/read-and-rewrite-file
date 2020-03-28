import os



def read_file(filename) :
	lines = []	
	with open(filename, "r", encoding = "utf-8-sig") as f :
		for line in f :
			lines.append(line.strip())
	return lines

def convert(r_from_read) :
	sum_allen = 0
	sum_allen_pic = 0
	sum_viki = 0
	sum_viki_pic = 0
	for line in r_from_read :
		if "Allen" in line and "圖片" not in line :
			sum_allen = sum_allen + len(line) - 12
		elif "Allen" in line and "圖片" in line :
			sum_allen_pic += 1
		if "Viki" in line and "圖片" not in line :
			sum_viki = sum_viki + len(line) - 11
		elif "Viki" in line and "圖片" in line :
			sum_viki_pic += 1
	print("Allen typed "+str(sum_allen)+" words")
	print("Viki typed "+str(sum_viki)+" words")
	print("Allen sent "+str(sum_allen_pic)+" pics")
	print("Viki sent "+str(sum_viki_pic)+" pics")

def chat(r_from_read) :
	chat = []
	for line in r_from_read :
		chat.append(line.split(" "))
	return chat
	
def count_word(r_from_chat) :
	sum_allen = 0
	sum_viki = 0
	for record in r_from_chat :
		if record[1] == "Allen" and record[2] != ("圖片" or "貼圖"):
			for allen in record[2: ] :
				sum_allen = sum_allen + len(allen) 
		elif record[1] == "Viki" and record[2] != ("圖片" or "貼圖"):
			for viki in record[2: ] :
				sum_viki = sum_viki + len(viki) 
	print("Allen typed "+str(sum_allen)+" words")
	print("Viki typed "+str(sum_viki)+" words")

def count_pic(r_from_chat) :
	a_pic = 0
	v_pic = 0
	a_moji = 0
	v_moji = 0
	for record in r_from_chat :
		if record[1] == "Allen" and record[2] == "圖片" :
			a_pic += 1
		elif record[1] == "Viki" and record[2] == "圖片" :
			v_pic += 1
		if record[1] == "Allen" and record[2] == "貼圖" :
			a_moji += 1
		elif record[1] == "Viki" and record[2] == "貼圖" :
			v_moji += 1
	print("Allen sent "+str(a_pic)+" pics")
	print("Viki sent "+str(v_pic)+" pics")
	print("Allen sent "+str(a_moji)+" emojis")
	print("Viki sent "+str(v_moji)+" emojis")

def main() :
	lines = read_file("input_1.txt")
	chat1 = chat(lines)
	count_word(chat1)
	count_pic(chat1)
	convert(lines)

	


main()







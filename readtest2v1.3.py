import os



def read_file(filename) :
	lines = []	
	with open(filename, "r", encoding = "utf-8-sig") as f :
		for line in f :
			lines.append(line.strip())
	return lines

def chat(r_from_read) :
	chat = []
	for line in r_from_read :
		chat.append(line.split(" "))
	return chat
	
def count_word(r_from_chat) :
	sum_allen = 0
	sum_viki = 0
	for record in r_from_chat :
		if record[1] == "Allen" and record[2] not in ("圖片", "貼圖"):
			for allen in record[2: ] :
				sum_allen += len(allen) 
		elif record[1] == "Viki" and record[2] not in ("圖片", "貼圖"):
			for viki in record[2: ] :
				sum_viki += len(viki)
				
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
	

main()







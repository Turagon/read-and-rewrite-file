import os



def read_file(filename) :
	lines = []	
	with open(filename, "r", encoding = "utf-8-sig") as f :
		for line in f :
			lines.append(line.strip())
	return lines

def convert(raw_content) :
	new = []
	person = None
	for line in raw_content :
		if line == "Allen" :
			person = "Allen"
			continue
		elif line == "Tom" :
			person = "Tom"
			continue
		if person :
			new.append(person+": "+line)
	return new

def write_file(filename, content) :
	with open(filename, "w", encoding = "utf-8") as f :
		for line in content :
			f.write(line+"\n")
		

def main() :
	lines = read_file("input.txt")
	new = convert(lines)
	write_file("output.txt", new)


main()
with open("output.txt", "r", encoding = "utf-8") as f :
	for line in f :
		print(line)






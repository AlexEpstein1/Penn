def indent(n):
	return ( " " * n) 


def is_true(s):
	s_lower = s.lower() 
	for i in s:
		if ord(i)<65:
			if ord(i) != 32:
				return False 

	if s_lower.find("true") != -1:
		return True


def contains_rep(s,t):
	if s.find(t) != -1:
		return True 

	return False


def shift_char(ch, n):
	
	ch_index = ord(ch)
	ch_index += n 


	if ch_index > 122:
		ch_index= 96 + (ch_index-122)

	elif ch_index<97:
		ch_index = 123 - (97- ch_index)

	letter = chr(ch_index)
	return letter



def average_ch(s):
	total = 0 
	for ch in s:
		total+= ord(ch)

	return chr(total // len(s))



def mix_cased(s):
	mod_value = 0
	answer = ''
	for i in s:
		if mod_value % 2 == 0:
			answer += i.lower()
		else:
			answer += i.upper()
		mod_value += 1
	return answer


def occurances(s, t):
	occurance = 0
	for i in range(len(s)-(len(t)-1)):
		if s[i:i + len(t)] == t:
			occurance+=1
	return occurance



def sum_numbers(s):
	final = 0
	x = 0
	while x < len(s):
		if s[x].isdigit():
			n = 0
			while x < len(s) and s[x].isdigit():
				n = int(str(n) + str(s[x]))
				x += 1
			final += n
		x+=1
	return final


def intersperse(s, t):
	if len(s) == 0:
		return ''
	elif len(s) == 1:
		return s[0] + intersperse(s[1:],t)
	return s[0] + t + intersperse(s[1:],t)


def swap_at(s,n):
	return s[n:] + s[0:n]
	


def evaluate(s):
	return eval(s)

def main():
	print(indent(3))
	print(is_true("tRue "))
	print(contains_rep("t","tt"))
	print(shift_char('a', 3))
	print(shift_char('a', -1))
	print(shift_char('z', 2))
	print(average_ch("ac"))
	print(mix_cased("hello world! a"))
	print(occurances("aaaaa", "aa" ))
	print(sum_numbers("abs50k50"))
	print(intersperse("hello world!","-"))
	print(swap_at("hello world!",5))
	print(evaluate("32+2-1"))

main()





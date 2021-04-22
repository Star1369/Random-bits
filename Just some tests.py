
def Googleimage(itemtosearch):
	'''use pip install undetected-chromedriver to work'''
	'''opens a new instance of stealth chrome'''
	import undetected_chromedriver as uc
	newchrome = uc.Chrome()
	newchrome.get('https://www.google.com/search?q=agua&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjqu7fnupLwAhXUnpUCHfvXD70Q_AUoAXoECAIQAw&biw=1280&bih=781')
Googleimage('agua')

# not finished yet


def metertofeet(num):
	x = num
	y = x*3.28084
	print(y)

x = 0
while x < 100:
	x += 0.1
	metertofeet(x)

import linecache as ln
import string

def fileread(filepath):
	a = ln.getlines(filepath)
	return a

filea = (r"C:\Users\Usuario\Desktop\lorem ipsum.txt")

def wordcounter(filepath):
	a = 0
	line = fileread(filepath)
	for line in line:
		a += (len(line.split(' ')))
	return a

# print(wordcounter(filea))
def putlinesinlistmanually():
	a = []
	x = 0
	while x <= 100:

		a += [ln.getline(filea, x )]
		x += 1

	print(a)


Usuario = 'xxxxx'
Senha = 'xxxxx'


Chropen = None
linxopen = None
searchopen = None


def aguardarelemento(id ,tempo = 15):
	import time
	while tempo > 0:
		try:
			driver.find_element_by_id(id)
			# print('aguardou')
			time.sleep(5)
			tempo = 0
		except:
			time.sleep(1)
			tempo -= 1
			# print(tempo)
			continue


def aguardarxpath(xpath ,tempo = 15):
	import time
	while tempo > 0:
		try:
			driver.find_element_by_xpath(xpath)
			# print('aguardou')
			time.sleep(5)
			tempo = 0
		except:
			time.sleep(1)
			tempo -= 1
			# print(tempo)
			continue



def abrechrome():
	global driver
	global Chropen
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.options import Options
	from selenium import webdriver
	chrome_options = Options()
	#chrome_options.add_argument("--disable-extensions")
	#chrome_options.add_argument("--disable-gpu")
	#chrome_options.add_argument("--no-sandbox") # linux only
	chrome_options.add_argument("--headless")
	# chrome_options.headless = True # also works
	driver = webdriver.Chrome(options=chrome_options)
	Chropen = 1
	return driver

def abremicrovix(user, password, empresa = 1):
	from selenium.webdriver.common.keys import Keys
	global linxopen

	if Chropen != 1:
		print('Chrome not open')
		abrechrome()

	"""Else"""

	driver.get('http://erp.microvix.com.br/')
	driver.find_element_by_id('f_login').send_keys(user , '\t')
	driver.find_element_by_id('f_senha').send_keys(password, '\n')
	print('login feito')
	aguardarelemento('sel_empresa_portal_usuario')
	driver.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/button').send_keys(empresa , Keys.ENTER)
	driver.find_element_by_id('btnselecionar_empresa').send_keys(Keys.ENTER)
	aguardarelemento('lupaBuscaMenu')
	linxopen = 1
	# print('fim')


#def Abrepesquisa(usuario = None , senha = None , loja = 1 , data = None):
#	import time
#	from selenium.webdriver.common.keys import Keys
#	global searchopen
#	if linxopen != 1:
#		abremicrovix(usuario , senha , loja)
#		time.sleep(5)
#	driver.find_element_by_xpath('//*[@id="lupaBuscaMenu"]/a').click()
#	searchopen = 1

def RelatorioVendaporvendedor(usuario = None , senha = None , loja = 1 , data = None):
	from selenium.webdriver.common.keys import Keys
	import time
	import string
	if linxopen != 1:
		abremicrovix(usuario , senha , loja)
		time.sleep(5)

	time.sleep(3)
	driver.get('https://linx.microvix.com.br:8371/gestor_web/faturamento/relatorio_fat_vendedor.asp')
	aguardarelemento('pos2_botao')
	driver.find_element_by_xpath('//*[@id="pos2_botao"]/input').click()
	alltext = driver.find_element_by_tag_name('html').text
	time.sleep(1)
	driver.close()
	vendedor = ['']
	x = 3
	y = 10
	textdic = alltext.split('\n')
	while y > 0:
		x += 1
		y -= 1
		if textdic[x] == 'Totais:':

			break
		
		
	print(vendedor)

	

	# print(alltext)

RelatorioVendaporvendedor(Usuario, Senha , 2)

import math

def makelist(lv, lf = 'vazio'):
	if lf == 'vazio':
		lv.sort()
		return lv
	nlist = []
	for v, f in zip(lv, lf):
		nlist += [v]*f
	return nlist

#Redundante, ja existe a função sum()
def somatoria(lista):
	print('somatoria')
	sm = 0
	for x in lista:
		sm += x

	return sm


def xbarra(lista): #Média
	print('x|')
	return somatoria(lista)/len(lista)


def dbarra(lista, mean = 'vazio'): #Desvio Quadrático
	print('d|')
	if mean == 'vazio':
		mean = xbarra(lista)
	tbs = []
	for x in lista:
		tbs.append((x - mean)**2)
	return somatoria(tbs)


def vbarra(lista, dsvq = 'vazio'): #Variâcia
	print('v|')
	if dsvq == 'vazio':
		dsvq = dbarra(lista) 
	return dsvq/(len(lista)-1)


def sbarra(lista, vran = 'vazio'): #Desvio Padrão (da medida)
	print('s|')
	if vran == 'vazio':
		vran = vbarra(lista)
	return (vran**(1/2))


def smbarra(lista, dsvp = 'vazio'): #Desvio Padrão da Média
	print('sm|')
	if dsvp == 'vazio':
		dsvp = sbarra(lista)
	return dsvp/(len(lista)**(1/2))


def getall(lista):
	x = xbarra(lista)
	d = dbarra(lista, x)
	v = vbarra(lista, d)
	s = sbarra(lista, v)
	sm = smbarra(lista, s)

	print(
		'n = ',len(lista),
		'\nMédia:						', x,
		'\nDesvio Quadrático:			', d,
		'\nVariância:					', v,
		'\nDesvio Padrão:				', s,
		'\nDesvio Padrão da Média:		', sm)




if __name__ == '__main__':

	valor = [5,6,7,8,9] #Coloca os Valores
	freq = [10,30,30,20,10] #Coloca a Frequência, se tiver

	if freq:
		lista = makelist(valor, freq)
	else:
		lista = makelist(valor)

	getall(lista)

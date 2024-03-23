def fatores_primos(valor_original):

	fatores = []

	if valor_original > 1:

		fator = 1

		while valor_original != 1:

			fator += 1
			expoente = 0

			while valor_original % fator == 0:

				expoente += 1
				valor_original /= fator

			for i in range(expoente):
				
				fatores.append(fator)

	return fatores

def fatores_comuns(n, m):

	A, B = fatores_primos(n), fatores_primos(m)
	C = []
	for a in A:
		for b in B:
			if a == b:
				C.append(a)
				B.remove(a)
				break

				
	return C





class Ratio:

	def __init__(self, numerador, denominador=1):

		if isinstance(numerador, Ratio):

			self.numerador = numerador.numerador
			self.denominador = numerador.denominador
			self.ratio = numerador.ratio

		else:

			self.numerador = numerador
			self.denominador = denominador
			self.ratio = f'{self.numerador}/{self.denominador}'

	def __str__(self):

		if self.denominador == 1:
			return str(self.numerador)

		else:
			return str(self.ratio)

	def __repr__(self):
		
		if self.denominador == 1:
			return str(self.numerador)

		else:
			return str(self.ratio)

	def __mul__(self, multiplicador):

		if isinstance(multiplicador, Ratio):

			numerador_produto = int(self.numerador * multiplicador.numerador)
			denominador_produto = int(self.denominador * multiplicador.denominador)

			produto = Ratio(numerador_produto, denominador_produto).simplifica()

			return produto


		else: 
			raise TypeError('Só pode operar objetos do mesmo tipo.')

	def __truediv__(self, divisor):

		if isinstance(divisor, Ratio):

			numerador_quociente = int(self.numerador * divisor.denominador)
			denominador_quociente = int(self.denominador * divisor.numerador)

			quociente = Ratio(numerador_quociente, denominador_quociente).simplifica()
			
			return quociente


		else: 
			raise TypeError('Só pode operar objetos do mesmo tipo.')

	def __add__(self, fator):

		if isinstance(fator, Ratio):

			if self.denominador == fator.denominador:
				numerador_soma = int(self.numerador + fator.numerador)
				denominador_soma = int(self.denominador)

			elif self.denominador != fator.denominador:
				numerador_soma = int((self.numerador * fator.denominador) + (fator.numerador * self.denominador))
				denominador_soma = int(self.denominador * fator.denominador)

			soma = Ratio(numerador_soma, denominador_soma).simplifica()

			return soma
			
		else: 
			raise TypeError('Só pode operar objetos do mesmo tipo.')

	def __sub__(self, subtraendo):

		if isinstance(subtraendo, Ratio):

			if self.denominador == subtraendo.denominador:
				numerador_resto = int(self.numerador- subtraendo.numerador)
				denominador_resto = int(self.denominador)

			elif self.denominador != subtraendo.denominador:
				numerador_resto = int((self.numerador * subtraendo.denominador) - (subtraendo.numerador * self.denominador))
				denominador_resto = int(self.denominador * subtraendo.denominador)

			resto = Ratio(numerador_resto, denominador_resto).simplifica()

			return resto

		else: 
			raise TypeError('Só pode operar objetos do mesmo tipo.')

	def simplifica(self):

		if self.numerador == 0 and self.denominador !=0:

			numerador_simplificado = 0
			denominador_simplificado = 1

		elif abs(self.numerador) == abs(self.denominador):

			numerador_simplificado = self.numerador / self.denominador
			denominador_simplificado = abs(numerador_simplificado) # 1

		elif self.denominador < 0:

			if self.numerador < 0:

				numerador_simplificado = abs(self.numerador)
				denominador_simplificado = abs(self.denominador)

			elif self.numerador > 0:

				numerador_simplificado = self.numerador * -1
				denominador_simplificado = self.denominador * -1

		elif self.denominador == 0:

			raise ZeroDivisionError('Denominador igual a 0.')

		else:

			numerador_simplificado = self.numerador
			denominador_simplificado = self.denominador

			for i in fatores_comuns(self.numerador, self.denominador):

				numerador_simplificado /= i
				denominador_simplificado /= i

		simplificado = Ratio(int(numerador_simplificado), int(denominador_simplificado))

		return simplificado
















class Linha:
	
	def __init__(self, v=[]):

		self.valor = v

	def __str__(self):
		return str(self.valor)

	def __repr__(self):
		return str(self.valor)

	def __len__(self):
		return len(self.valor)

	def __getitem__(self, i):
		return self.valor[i]

	def __add__(self, x):

		result = Linha([None]*len(self))

		for i in range(len(self)):
			result.valor[i] = self.valor[i] + x.valor[i]

		return result

		

	def __sub__(self, x):

		result = Linha([None]*len(self))

		for i in range(len(self)):
			result.valor[i] = self.valor[i] - x.valor[i]

		return result

	def __mul__(self, x):

		result = Linha([None]*len(self))

		for i in range(len(self)):
			result.valor[i] = self.valor[i]*Ratio(x)

		return result

	def __truediv__(self, x):

		result = Linha([None]*len(self))

		for i in range(len(self)):
			result.valor[i] = self.valor[i]/Ratio(x)

		return result










class Sistema:

	def __init__(self, *lines):

		for i, l in enumerate(lines):
			lin = f'Linha{i+1}'

			setattr(self, f'Linha{i+1}', Linha(l))

	def __str__(self):

		s = ''

		for x in self.__dict__.values():

			#l = eval(f'self.{x}')

			s += f'{x}\n'
		return s

	def __len__(self):
		return len(self.__dict__)

	def __iter__(self):
		for x in self.__dict__.values():
			yield x

	def __getitem__(self, v):

		if type(v) == type(1):
			termo = f'Linha{v+1}'
			r = eval(f'self.{termo}')
			return r

		elif type(v) == type((1,2)):
			i, j = v
			termo = f'Linha{i+1}'
			r = eval(f'self.{termo}')[j]

			return r












def resolve_sistema(a):


	for j in range(len(a[0])-1):
		for i in range((len(a))):
			lin_name = f'Linha{i+1}'

			if i != j and a[i, j] != Ratio(0):
				const = (Ratio(a[i, j]) / Ratio(a[j, j]))

				print(f'\nLinha {i+1} --> Linha {i+1} - Linha {j+1}*({const})')

				opera = f'a.Linha{i+1} -=' + f' a.Linha{j+1}*{const}'

				exec(opera)
				print(a[i])

			elif i == j and a[i, j] != Ratio(1):
				try:
					const = (Ratio(1) / Ratio(a[i, j]))
				except ZeroDivisionError:
					raise ZeroDivisionError('O elemento (i, i) é 0.')


				print(f'\nLinha {i+1} --> Linha {i+1}*({const})')

				opera = f'a.Linha{i+1} = a.Linha{i+1}*{const}'

				exec(opera)
				print(a[i])
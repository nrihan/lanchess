class Peca:
	def __init__(self, posicao, cor = '', pecaChar = ''):
		self.cor = cor
		self.posicao = posicao

		if(pecaChar == ''):
			self.pecaChar = '|_|'
		else:
			self.pecaChar = pecaChar

class Peao(Peca):
	def __init__(self, posicao, cor=True, orientacao=True):
		pecaChar = '|♟|' if cor else '|♙|'
		cor = 'Brancas' if cor else 'Pretas'
		
		Peca.__init__(self, posicao, cor, pecaChar)

		self.orientacao = orientacao

	def verificaMovimento(self, outraPeca, tabuleiro):
		posicao = outraPeca.posicao
		
		if(self.orientacao):
			if self.cor == 'Brancas':
				if outraPeca.pecaChar == '|_|':
					if posicao[0] + 1 != self.posicao(self)[0]:
						return False
					if posicao[1] != self.posicao(self)[1]:
						return False
				else:
					if posicao[0] + 1 != self.posicao(self)[0]:
						return False
					if posicao[1] - 1 != self.posicao(self)[1] and posicao[1] + 1 != self.posicao(self)[1]:
						return False
					if  outraPeca.cor == self.cor(self):
						return False
				return True
			if self.cor == 'Pretas':
				if outraPeca.pecaChar == '|_|':
					if posicao[0] - 1 != self.posicao(self)[0]:
						return False
					if posicao[1] != self.posicao(self)[1]:
						return False
				else:
					if posicao[0] - 1 != self.posicao(self)[0]:
						return False
					if posicao[1] - 1 != self.posicao(self)[1] and posicao[1] + 1 != self.posicao(self)[1]:
						return False
					if  outraPeca.cor == self.cor(self):
						return False
				return True

		else:
			if self.cor(self) == 'Brancas':
				if outraPeca.pecaChar == '|_|':
					if posicao[0] - 1 != self.posicao(self)[0]:
						return False
					if posicao[1] != self.posicao(self)[1]:
						return False
				else:
					if posicao[0] - 1 != self.posicao(self)[0]:
						return False
					if posicao[1] + 1 != self.posicao(self)[1] and posicao[1] + 1 != self.posicao(self)[1]:
						return False
					if  outraPeca.cor == self.cor(self):
						return False
				return True
			if self.cor(self) == 'Pretas':
				if outraPeca.pecaChar == '|_|':
					if posicao[0] + 1 != self.posicao(self)[0]:
						return False
					if posicao[1] != self.posicao(self)[1]:
						return False
				else:
					if posicao[0] + 1 != self.posicao(self)[0]:
						return False
					if posicao[1] + 1 != self.posicao(self)[1] and posicao[1] - 1 != self.posicao(self)[1]:
						return False
					if  outraPeca.cor == self.cor(self):
						return False
				return True


class Cavalo(Peca):
	def __init__(self, posicao, cor=True):
		pecaChar = '|♞|' if cor else '|♘|'
		cor = 'Brancas' if cor else 'Pretas'
		
		Peca.__init__(self, posicao, cor, pecaChar)

	def verificaMovimento(self, outraPeca, tabuleiro):
		posicao = outraPeca.posicao
		
		if ((posicao[0] - 2 == self.posicao(self)[0] or posicao[0] + 2 == self.posicao(self)[0]) and
		(posicao[1] - 1 == self.posicao(self)[1] or posicao[1] + 1 == self.posicao(self)[1])):
			if outraPeca.pecaChar == '|_|':
				return True
			if outraPeca.cor != self.cor(self):
				return True
		elif ((posicao[1] - 2 == self.posicao(self)[1] or posicao[1] + 2 == self.posicao(self)[1]) and
		(posicao[0] - 1 == self.posicao(self)[0] or posicao[0] + 1 == self.posicao(self)[0])):
			if outraPeca.pecaChar == '|_|':
				return True
			if outraPeca.cor != self.cor(self):
				return True
			
		return False


class Bispo(Peca):
	def __init__(self, posicao, cor=True):
		pecaChar = '|♝|' if cor else '|♗|'
		cor = 'Brancas' if cor else 'Pretas'
		
		Peca.__init__(self, posicao, cor, pecaChar)

	def verificaMovimento(self, outraPeca, tabuleiro):
		posicao = outraPeca.posicao
		diferencaX = posicao[0] - self.posicao[0]
		diferencaY = posicao[1] - self.posicao[1]

		if abs(diferencaX) != abs(diferencaY):
			return False
		
		if outraPeca.pecaChar != '|_|' and outraPeca.cor == self.cor:
			return False
		
		incrementoJ = 1 if diferencaX == diferencaY else -1
		
		if (diferencaX > 0):

			j = self.posicao[1]
			for i in range(self.posicao[0] + 1, posicao[0]):
				j += incrementoJ
				if tabuleiro[i][j].pecaChar != '|_|':
					return False
		
		else:

			j = posicao[1]
			for i in range(posicao[0] + 1, self.posicao[0]):
				j += incrementoJ
				if tabuleiro[i][j].pecaChar != '|_|':
					return False
		
		return True

class Torre(Peca):
	def __init__(self, posicao, cor=True):
		pecaChar = '|♜|' if cor else '|♖|'
		cor = 'Brancas' if cor else 'Pretas'
		
		Peca.__init__(self, posicao, cor, pecaChar)

	def verificaMovimento(self, outraPeca, tabuleiro):
		posicao = outraPeca.posicao

		if posicao[0] != self.posicao[0] and posicao[1] != self.posicao[1]:
			return False

		if posicao[0] != self.posicao[0]:

			maior = posicao[0]
			menor = self.posicao[0]

			if self.posicao[0] > posicao[0]:
				
				maior = menor
				menor = posicao[0]
			
			for x in range(menor + 1, maior):
				if tabuleiro[x][posicao[1]].pecaChar != '|_|':
					return False
		
		else:

			maior = posicao[1]
			menor = self.posicao[1]

			if self.posicao[1] > posicao[1]:
				
				maior = menor
				menor = posicao[1]
			
			for x in range(menor + 1, maior):
				if tabuleiro[posicao[0]][x].pecaChar != '|_|':
					return False
		
		if outraPeca.pecaChar != '|_|' and outraPeca.cor == self.cor:
			return False
		
		return True


class Dama(Peca):
	def __init__(self, posicao, cor=True):
		pecaChar = '|♛|' if cor else '|♕|'
		cor = 'Brancas' if cor else 'Pretas'
		
		Peca.__init__(self, posicao, cor, pecaChar)
		
	def verificaMovimento(self, outraPeca, tabuleiro):
		return Bispo.verificaMovimento(self, outraPeca, tabuleiro) or Torre.verificaMovimento(self, outraPeca, tabuleiro)


class Rei(Peca):  # O rei tem valor absoluto infinito, mas pra facilitar nossa vida definimos com 0
	def __init__(self, posicao, cor=True):
		pecaChar = '|♚|' if cor else '|♔|'
		cor = 'Brancas' if cor else 'Pretas'
		
		Peca.__init__(self, posicao, cor, pecaChar)

	def verificaMovimento(self, outraPeca, tabuleiro):
		
		posicao = outraPeca.posicao

		if abs(posicao[0] - self.posicao[0]) > 1 or abs(posicao[1] - self.posicao[1]) > 1:
			return False

		if outraPeca.pecaChar != '|_|' and outraPeca.cor == self.cor:
			return False
		
		return True
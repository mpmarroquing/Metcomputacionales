#definir objetos

class balon                                #definir clase
g=9.8

	def _init_(self, y0,Vy0, m0):          #inicializar valores
		self.y=y0
		self.Vy= Vy0
		self.m=m0
	def calculaFuerza (self):              #función
		self.Fy= -self.m*balon.g
		
pelota=balon(0.0,4.0,0.453)                #inicializa objetos
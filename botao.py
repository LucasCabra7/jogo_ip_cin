import pygame

# Classe do botão
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width() # Largura
		height = image.get_height() # Altura
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # Trasnformar a imagem com lagura * escala e altura * escada
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y) # Canto superior
		self.clicked = False # Inciando o click do mouse

	def draw(self, surface):
		action = False
		# Pegar a posição do mouse
		pos = pygame.mouse.get_pos()

		# verificar condições de mouse e clique
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0: # Arrastar o mouse por cima.
			self.clicked = False

		# Desenhar o botão na tela
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
import pygame
import sys


# Inicializa pygame e mixer
print('Iniciando pygames...')
pygame.init()
pygame.mixer.init()

# Carrega e toca a música
print('Carregando música...')
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

# Cria a janela (com tamanho em tupla)
print('Criando janela...')
screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Tocando música")

# Loop principal: fica rodando até você fechar a janela
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Espera um pouco a cada loop para não travar a CPU
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
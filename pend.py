import pygame
import sys
from math import sin, cos, radians
import conexao


# Inicialização do Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aeropêndulo com Hélice Horizontal")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Definindo a posição inicial do pêndulo
origin = (width // 2, height // 4)  # O ponto de suspensão do pêndulo
length = 200  # Comprimento da haste do pêndulo (L)

# Definindo o ângulo inicial do pêndulo e da hélice
pendulum_angle = 0  # em graus
propeller_angle = 0  # em graus

clock = pygame.time.Clock()


# Conexão UDP
conn = conexao.conectar()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar lógica do pêndulo
    # (Substitua isto com a lógica de atualização de ângulo baseada nos seus dados)

    # Recebe informação de ângulo com dados do socket
    data, addr = conn.recvfrom(1024)
    
    pendulum_angle = int(data.decode())
    print(pendulum_angle)
    #if pendulum_angle >= 360:
        #pendulum_angle = 0

    # Atualizar lógica da hélice
    propeller_angle += 20  # A hélice gira mais rápido que o pêndulo
    if propeller_angle >= 360:
        propeller_angle = 0

    # Calcular a posição do fim do pêndulo
    radian_angle = radians(pendulum_angle)
    end_x = origin[0] + length * sin(radian_angle)
    end_y = origin[1] + length * cos(radian_angle)
    end_pos = (int(end_x), int(end_y))

    # Desenhar tudo
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, origin, end_pos, 2)  # Haste do pêndulo
    pygame.draw.circle(screen, BLUE, origin, 20)  # Ponto de suspensão do pêndulo
    pygame.draw.circle(screen, BLACK, end_pos, 15)  # Massa do pêndulo

    # Desenhar hélice na ponta do pêndulo
    blade_length = 20
    blade_width = 5
    radian_propeller_angle = radians(propeller_angle)
    for i in [0, 180]:
        angle_offset = radians(i)
        blade_x = end_x + blade_length * cos(radian_propeller_angle + angle_offset)
        blade_y = end_y + blade_length * sin(radian_propeller_angle + angle_offset)
        pygame.draw.rect(
            screen, BLACK,
            pygame.Rect(blade_x - blade_width / 2, blade_y - blade_length / 2, blade_width, blade_length)
        )

    pygame.display.flip()
    clock.tick(60)  # Limita a 60 FPS

pygame.quit()
sys.exit()

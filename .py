import pygame
import random
import sys
from pygame.locals import *

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Preguntas")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fuentes
font = pygame.font.Font(None, 40)

# Banco de preguntas
questions = [
    {"question": "¿El cielo es azul?", "options": ["Rojo", "Azul"], "correct": "Azul", "value": 100},
    {"question": "¿El fuego es rojo?", "options": ["Rojo", "Azul"], "correct": "Rojo", "value": 200},
    {"question": "¿El agua es azul?", "options": ["Rojo", "Azul"], "correct": "Azul", "value": 300},
]

# Función para obtener votos de los votantes
def generate_votes():
    return [random.choice(["Rojo", "Azul"]) for _ in range(5)]

# Función para calcular porcentajes
def calculate_percentages(votes):
    rojo = votes.count("Rojo")
    azul = votes.count("Azul")
    total = len(votes)
    return {"Rojo": (rojo / total) * 100, "Azul": (azul / total) * 100}

# Juego principal
def game():
    clock = pygame.time.Clock()
    running = True
    question_index = 0
    player_money = 0

    while running and question_index < len(questions):
        question = questions[question_index]
        votes = generate_votes()
        percentages = calculate_percentages(votes)

        timer = 15  # Temporizador de 15 segundos

        # Ciclo de la pregunta
        while timer > 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:  # Opción Rojo
                        player_choice = "Rojo"
                    elif event.key == K_b:  # Opción Azul
                        player_choice = "Azul"
                    else:
                        continue
                    
                    # Mostrar votos y verificar respuesta
                    if player_choice == question["correct"]:
                        player_money += question["value"]
                        question_index += 1
                    else:
                        running = False
                    break

            # Dibujar en pantalla
            screen.fill(WHITE)
            # Mostrar pregunta
            question_text = font.render(question["question"], True, BLACK)
            screen.blit(question_text, (50, 50))

            # Mostrar opciones
            rojo_text = font.render("Rojo (R)", True, RED)
            azul_text = font.render("Azul (B)", True, BLUE)
            screen.blit(rojo_text, (50, 150))
            screen.blit(azul_text, (50, 200))

            # Mostrar votos
            votes_text = font.render(f"Votos: {', '.join(votes)}", True, BLACK)
            screen.blit(votes_text, (50, 300))

            # Mostrar porcentajes
            percent_text = font.render(f"Rojo: {percentages['Rojo']:.2f}% | Azul: {percentages['Azul']:.2f}%", True, BLACK)
            screen.blit(percent_text, (50, 350))

            # Mostrar temporizador
            timer_text = font.render(f"Tiempo restante: {timer}", True, BLACK)
            screen.blit(timer_text, (50, 400))

            # Actualizar pantalla
            pygame.display.flip()
            clock.tick(1)
            timer -= 1

        # Si se agota el tiempo, termina el juego
        if timer <= 0:
            running = False

    # Fin del juego
    screen.fill(WHITE)
    end_text = font.render(f"Juego terminado. Ganaste: ${player_money}", True, BLACK)
    screen.blit(end_text, (50, 300))
    pygame.display.flip()
    pygame.time.wait(5000)

# Ejecutar el juego
game()
pygame.quit()

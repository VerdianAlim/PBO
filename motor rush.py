import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Konfigurasi layar dan warna
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Motor Rush: Avoid the Traffic")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (169, 169, 169)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 51)
CYAN = (0, 255, 255)

# FPS Controller
CLOCK = pygame.time.Clock()

# Ukuran gambar
MOTOR_WIDTH, MOTOR_HEIGHT = 50, 60
CAR_WIDTH, CAR_HEIGHT = 50, 80

# Gambar
MOTOR_IMG = pygame.image.load("motor.png")
CAR_IMG = pygame.image.load("car.png")
MOTOR_IMG = pygame.transform.scale(MOTOR_IMG, (MOTOR_WIDTH, MOTOR_HEIGHT))
CAR_IMG = pygame.transform.scale(CAR_IMG, (CAR_WIDTH, CAR_HEIGHT))


# Fungsi untuk menggambar rectangle dengan sudut tumpul
def draw_rounded_rect(surface, rect, color, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)


# Kelas Motor
class Motor:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed

    def draw(self):
        SCREEN.blit(MOTOR_IMG, (self.x, self.y))

    def get_position(self):
        return self.x, self.y, MOTOR_WIDTH, MOTOR_HEIGHT


# Kelas Car
class Car:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed

    def reset_position(self):
        self.y = -CAR_HEIGHT
        self.x = random.randint(100, SCREEN_WIDTH - 100 - CAR_WIDTH)

    def draw(self):
        SCREEN.blit(CAR_IMG, (self.x, self.y))

    def get_position(self):
        return self.x, self.y, CAR_WIDTH, CAR_HEIGHT


# Kelas Road
class Road:
    @staticmethod
    def draw():
        SCREEN.fill(GRAY)
        pygame.draw.rect(SCREEN, WHITE, (100, 0, SCREEN_WIDTH - 200, SCREEN_HEIGHT))  # Jalur utama
        pygame.draw.line(SCREEN, BLACK, (100, 0), (100, SCREEN_HEIGHT), 10)  # Pembatas kiri
        pygame.draw.line(SCREEN, BLACK, (700, 0), (700, SCREEN_HEIGHT), 10)  # Pembatas kanan
        for y in range(0, SCREEN_HEIGHT, 40):
            pygame.draw.rect(SCREEN, WHITE, (395, y, 10, 30))  # Garis putus-putus


# Kelas Game
class Game:
    def __init__(self):
        self.motor = Motor(SCREEN_WIDTH // 2 - MOTOR_WIDTH // 2, SCREEN_HEIGHT - MOTOR_HEIGHT - 10, 10)
        self.cars = [Car(random.randint(100, SCREEN_WIDTH - 100 - CAR_WIDTH), -CAR_HEIGHT, 5)]
        self.score = 0
        self.difficulty_timer = 0
        self.running = True
        self.paused = False

    def add_car(self):
        self.cars.append(Car(random.randint(100, SCREEN_WIDTH - 100 - CAR_WIDTH), -CAR_HEIGHT, random.randint(4, 7)))

    def handle_collision(self):
        motor_x, motor_y, motor_width, motor_height = self.motor.get_position()
        for car in self.cars:
            car_x, car_y, car_width, car_height = car.get_position()
            if (motor_x < car_x + car_width and motor_x + motor_width > car_x and
                    motor_y < car_y + car_height and motor_y + motor_height > car_y):
                self.running = False
                self.game_over_screen()
def update(self):
        for car in self.cars:
            car.move()
            if car.y > SCREEN_HEIGHT:
                car.reset_position()
                self.score += 1

        self.difficulty_timer += 1
        if self.difficulty_timer > 300:
            self.add_car()
            self.difficulty_timer = 0

    def draw(self):
        Road.draw()
        self.motor.draw()
        for car in self.cars:
            car.draw()
        font = pygame.font.SysFont(None, 27)
        score_text = font.render(f"Score: {self.score}", True, YELLOW)
        SCREEN.blit(score_text, (10, 10))

    def toggle_pause(self):
        self.paused = not self.paused

    def pause_menu(self):
        menu_running = True
        selected_option = "resume"

        while menu_running:
            self.draw()
            overlay_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay_surface.fill((0, 0, 0, 150))
            SCREEN.blit(overlay_surface, (0, 0))

            border_rect = pygame.Rect(200, 150, 400, 350)
            draw_rounded_rect(SCREEN, border_rect, CYAN, 20)

            inner_rect = border_rect.inflate(-10, -10)
            draw_rounded_rect(SCREEN, inner_rect, BLACK, 20)

            font_score = pygame.font.SysFont(None, 60)
            score_text = font_score.render(f"Score: {self.score}", True, YELLOW)
            SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, inner_rect.y + 40))

            font_option = pygame.font.SysFont(None, 50)
            resume_color = YELLOW if selected_option == "resume" else WHITE
            restart_color = YELLOW if selected_option == "restart" else WHITE
            exit_color = YELLOW if selected_option == "exit" else WHITE

            resume_text = font_option.render("Resume", True, resume_color)
            restart_text = font_option.render("Restart", True, restart_color)
            exit_text = font_option.render("Exit", True, exit_color)

            SCREEN.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, inner_rect.y + 150))
            SCREEN.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, inner_rect.y + 220))
            SCREEN.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, inner_rect.y + 290))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if selected_option == "resume":
                            selected_option = "exit"
                        elif selected_option == "restart":
                            selected_option = "resume"
                        elif selected_option == "exit":
                            selected_option = "restart"
                    if event.key == pygame.K_DOWN:
                        if selected_option == "resume":
                            selected_option = "restart"
                        elif selected_option == "restart":
                            selected_option = "exit"
                        elif selected_option == "exit":
                            selected_option = "resume"
                    if event.key == pygame.K_RETURN:
                        if selected_option == "resume":
                            self.paused = False
                            menu_running = False
                        elif selected_option == "restart":
                            menu_running = False
                            self.__init__()
                            game_loop(self)
                        elif selected_option == "exit":
                            menu_running = False
                            main_menu()
                            return
            CLOCK.tick(60)

def game_over_screen(self):
        menu_running = True
        selected_option = "play_again"

        while menu_running:
            self.draw()
            overlay_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay_surface.fill((0, 0, 0, 150))
            SCREEN.blit(overlay_surface, (0, 0))

            border_rect = pygame.Rect(150, 150, 500, 300)
            draw_rounded_rect(SCREEN, border_rect, CYAN, 20)

            inner_rect = border_rect.inflate(-10, -10)
            draw_rounded_rect(SCREEN, inner_rect, BLACK, 20)

            font_game_over = pygame.font.SysFont(None, 75)
            game_over_text = font_game_over.render("Game Over!", True, RED)
            SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, inner_rect.y + 40))

            font_score = pygame.font.SysFont(None, 50)
            score_text = font_score.render(f"Score: {self.score}", True, CYAN)
            SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, inner_rect.y + 110))

            font_option = pygame.font.SysFont(None, 50)
            play_again_color = YELLOW if selected_option == "play_again" else WHITE
            exit_color = YELLOW if selected_option == "exit" else WHITE

            play_again_text = font_option.render("Play Again", True, play_again_color)
            exit_text = font_option.render("Exit", True, exit_color)

            SCREEN.blit(play_again_text, (inner_rect.x + 50, inner_rect.y + 200))
            SCREEN.blit(exit_text, (inner_rect.x + 350, inner_rect.y + 200))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        selected_option = "play_again"
                    if event.key == pygame.K_RIGHT:
                        selected_option = "exit"
                    if event.key == pygame.K_RETURN:
                        if selected_option == "play_again":
                            menu_running = False
                            game_loop(Game())  # Start new game
                        elif selected_option == "exit":
                            menu_running = False
                            main_menu()  # Go back to main menu
            CLOCK.tick(60)


def main_menu():
    menu_running = True
    selected_option = "play"

    while menu_running:
        Road.draw()
        overlay_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay_surface.fill((0, 0, 0, 150))
        SCREEN.blit(overlay_surface, (0, 0))

        border_rect = pygame.Rect(200, 150, 400, 350)
        draw_rounded_rect(SCREEN, border_rect, CYAN, 20)

        inner_rect = border_rect.inflate(-10, -10)
        draw_rounded_rect(SCREEN, inner_rect, BLACK, 20)

        font_title = pygame.font.SysFont(None, 75)
        title_text = font_title.render("Motor Rush", True, CYAN)
        SCREEN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, inner_rect.y + 40))

        font_option = pygame.font.SysFont(None, 50)
        play_color = YELLOW if selected_option == "play" else WHITE
        exit_color = YELLOW if selected_option == "exit" else WHITE
        play_text = font_option.render("Play Game", True, play_color)
        exit_text = font_option.render("Exit", True, exit_color)

        SCREEN.blit(play_text, (SCREEN_WIDTH // 2 - play_text.get_width() // 2, inner_rect.y + 150))
        SCREEN.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, inner_rect.y + 220))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    selected_option = "play" if selected_option == "exit" else "exit"
                if event.key == pygame.K_RETURN:
                    if selected_option == "play":
                        menu_running = False
                        game_loop(Game())  # Start new game
                    elif selected_option == "exit":
                        pygame.quit()
                        quit()
        CLOCK.tick(60)


def game_loop(game):
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                game.toggle_pause()
        if game.paused:
            game.pause_menu()
            continue
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and game.motor.x > 100:
            game.motor.move("left")
        if keys[pygame.K_RIGHT] and game.motor.x < SCREEN_WIDTH - 100 - MOTOR_WIDTH:
            game.motor.move("right")
        game.update()
        game.handle_collision()
        game.draw()
        pygame.display.update()
        CLOCK.tick(60)


if __name__ == "__main__":
    main_menu()

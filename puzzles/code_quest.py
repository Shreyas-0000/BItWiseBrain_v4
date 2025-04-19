import pygame
import sys
from pygame import Rect
import textwrap
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
import io
from contextlib import redirect_stdout

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
EDITOR_WIDTH = 400
GAME_AREA_WIDTH = WINDOW_WIDTH - EDITOR_WIDTH
FONT_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)

# Game setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Code Quest")
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = 5
        self.color = BLUE
    
    def move(self, dx, dy):
        self.x = max(0, min(GAME_AREA_WIDTH - self.width, self.x + dx))
        self.y = max(0, min(WINDOW_HEIGHT - self.height, self.y + dy))
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

class CodeEditor:
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.text = "# Write your code here\n"
        self.active = False
        self.cursor_pos = len(self.text)
        self.output = ""
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.text += '\n'
                self.cursor_pos += 1
            elif event.key == pygame.K_BACKSPACE:
                if self.cursor_pos > 0:
                    self.text = self.text[:self.cursor_pos-1] + self.text[self.cursor_pos:]
                    self.cursor_pos -= 1
            elif event.key == pygame.K_F5:  # Execute code on F5
                self.execute_code()
            else:
                if event.unicode:
                    self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                    self.cursor_pos += 1

    def execute_code(self):
        try:
            f = io.StringIO()
            with redirect_stdout(f):
                exec(self.text)
            self.output = f.getvalue()
        except Exception as e:
            self.output = f"Error: {str(e)}"

    def draw(self, surface):
        # Draw editor background
        pygame.draw.rect(surface, GRAY, self.rect)
        
        # Draw code text
        y_offset = 5
        wrapped_lines = textwrap.wrap(self.text, width=40)
        for line in wrapped_lines:
            text_surface = font.render(line, True, WHITE)
            surface.blit(text_surface, (self.rect.x + 5, self.rect.y + y_offset))
            y_offset += FONT_SIZE

        # Draw output
        output_rect = Rect(self.rect.x, self.rect.y + self.rect.height//2, 
                          self.rect.width, self.rect.height//2)
        pygame.draw.rect(surface, BLACK, output_rect)
        
        y_offset = self.rect.height//2 + 5
        wrapped_output = textwrap.wrap(self.output, width=40)
        for line in wrapped_output:
            text_surface = font.render(line, True, GREEN)
            surface.blit(text_surface, (self.rect.x + 5, self.rect.y + y_offset))
            y_offset += FONT_SIZE

class Challenge:
    def __init__(self, x, y, description, test_code):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.description = description
        self.test_code = test_code
        self.completed = False
        self.color = WHITE
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        if not self.completed:
            text = font.render("?", True, BLACK)
            text_rect = text.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
            surface.blit(text, text_rect)

def main():
    player = Player(100, 100)
    editor = CodeEditor(GAME_AREA_WIDTH, 0, EDITOR_WIDTH, WINDOW_HEIGHT)
    
    # Create first challenge
    challenge = Challenge(300, 300, 
        "Print 'Hello, World!' to complete this challenge",
        "print('Hello, World!')")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            editor.handle_event(event)

        # Handle player movement
        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player.speed
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player.speed
        player.move(dx, dy)

        # Clear screen
        screen.fill(BLACK)
        
        # Draw game elements
        player.draw(screen)
        challenge.draw(screen)
        editor.draw(screen)

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 
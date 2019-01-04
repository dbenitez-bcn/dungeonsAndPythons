import pygame
import os

_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def get_text(text, color):
    font_type = 'assets/fonts/phosphate.ttf'
    size = 45

    text = str(text)
    font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)

    return text

def displayImage(viewToDraw, spritePath, xPosition, yPosition):
    viewToDraw.blit(get_image(spritePath), (xPosition, yPosition))

def displayText(viewToDraw, text, xPosition, yPosition, color = (255, 255, 255)):
    viewToDraw.blit(get_text(text, color), (xPosition, yPosition))

def displayTextButton(viewToDraw, text, xPosition, yPosition, color):
    text = get_text(text, color)
    textPosition = text.get_rect()
    textPosition.center = ((xPosition+(375/2)), (yPosition+(75/2)+2))

    viewToDraw.blit(text, textPosition)
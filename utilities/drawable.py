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

def get_text(text, color, fontSize):
    font_type = 'assets/fonts/phosphate.ttf'

    text = str(text)
    font = pygame.font.Font(font_type, fontSize)
    text = font.render(text, True, color)

    return text

def displayImage(viewToDraw, spritePath, xPosition, yPosition):
    viewToDraw.blit(get_image(spritePath), (xPosition, yPosition))

def displayText(viewToDraw, text, xPosition, yPosition, color = (255, 255, 255), fontSize = 45):
    viewToDraw.blit(get_text(text, color, fontSize), (xPosition, yPosition))

def displayTextButton(viewToDraw, text, xPosition, yPosition, color = (255, 255, 255), width = 375, height = 75, fontSize = 45):
    text = get_text(text, color, fontSize)
    textPosition = text.get_rect()
    textPosition.center = ((xPosition+(width/2)), (yPosition+(height/2)+2))

    viewToDraw.blit(text, textPosition)
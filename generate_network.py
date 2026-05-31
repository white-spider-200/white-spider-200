import math
import random
from PIL import Image, ImageDraw

WIDTH = 800
HEIGHT = 200
NUM_NODES = 50
MAX_DIST = 90
FRAMES = 80
SPEED = 1.5

class Node:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle) * SPEED
        self.vy = math.sin(angle) * SPEED

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

nodes = [Node() for _ in range(NUM_NODES)]
images = []

bg_color = (13, 17, 23)
line_color = (0, 199, 183)

for _ in range(FRAMES):
    img = Image.new('RGB', (WIDTH, HEIGHT), bg_color)
    draw = ImageDraw.Draw(img)
    
    for i in range(NUM_NODES):
        for j in range(i + 1, NUM_NODES):
            n1 = nodes[i]
            n2 = nodes[j]
            dist = math.hypot(n1.x - n2.x, n1.y - n2.y)
            if dist < MAX_DIST:
                ratio = 1 - (dist / MAX_DIST)
                r = int(bg_color[0] + (line_color[0] - bg_color[0]) * ratio)
                g = int(bg_color[1] + (line_color[1] - bg_color[1]) * ratio)
                b = int(bg_color[2] + (line_color[2] - bg_color[2]) * ratio)
                draw.line([(n1.x, n1.y), (n2.x, n2.y)], fill=(r, g, b), width=1)
                
    for n in nodes:
        draw.ellipse([(n.x-2, n.y-2), (n.x+2, n.y+2)], fill=(124, 58, 237))
        n.update()
        
    images.append(img)

images[0].save('assets/network.gif', save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
print("GIF generated successfully at assets/network.gif")

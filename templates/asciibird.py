def main():
    import time
    from ascii_renderer import AsciiRenderer
    import keyboard
    import random
    
    class Pipe():
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.gap = 16
            self.x = width
            self.y = random.randint(self.gap, height-self.gap)

        def reset(self):
            self.x = self.width
            self.y = random.randint(self.gap, self.height-self.gap)

        def update(self):
            self.x -= 1
            if self.x <= -5:
                self.reset()
                return True
            return False
        
        def draw(self):
            return (self.x, self.y, 5, self.height-self.y, self.x, 0, 5, self.y - self.gap)
    
    class Bird():
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.vel = [0,0]
            self.jumpVelocity = -3
            self.gravity = 1
            self.MAX_VEL = 2
            self.first_jump = False
            self.alive = True
            self.width = width
            self.height = height
        
        def flap(self):
            self.vel[1] = self.jumpVelocity
            self.first_jump = True

        def update(self):
            if self.alive:
                if self.first_jump == True:
                    self.vel[1] += self.gravity
                
                self.x += self.vel[0]
                self.y += self.vel[1]
                if self.vel[1] >= self.MAX_VEL:
                    self.vel[1] = self.MAX_VEL
                

            if self.y <= 0:
                self.alive = False
            
            elif self.y >= self.height:
                self.alive = False

        def kill(self):
            self.alive = False
        
        def reset(self):
            self.x = 5
            self.y = 10
            self.vel = [0,0]
            self.jumpVelocity = -3
            self.gravity = 1
            self.MAX_VEL = 2
            self.first_jump = False
            self.alive = True

        def draw(self):
            return (self.x, self.y, 2)

    #Variables
    FPS = 24
    score = 0
    v = False

    # dimensions of screen
    width = 50
    height = 40

    player = Bird(5, 10, width, height)
    pipes = Pipe(width, height)

    # create renderer object
    renderer = AsciiRenderer(width, height)

    def checkPipeCollisions(birdX, birdY, pipeX, pipeCenter):
        if birdX >= pipeX - 1 and birdX <= pipeX + 6:
            if (birdY < pipeCenter - pipes.gap/2) or (birdY > pipes.y - 1):
                player.kill()

    #game loop
    running = True
    while running:
        renderer.clear()
        
        #logic loop
        if keyboard.is_pressed("space"):
            player.flap()
        
        if keyboard.is_pressed("r"):
            player.reset()
            pipes.reset()
            score = 0

        checkPipeCollisions(player.x, player.y, pipes.x, pipes.y - 3)
        player.update()

        if player.first_jump == True and player.alive == True:
            v = pipes.update()
        if v == True:
            score += 1
        
        #Draw loop
        try:
            PL_X, PL_Y, radius = player.draw()
            renderer.draw_ellipse(PL_X, PL_Y, radius, radius)
            
            p1x, p1y, p1W, p1H, p2x, p2y, p2W, p2H = pipes.draw() #Dont judge me man I was rushing
            renderer.draw_rect(p1x, p1y, p1W, p1H, fill=True)
            renderer.draw_rect(p2x, p2y, p2W, p2H, fill=True)
            
            renderer.draw_text(25, 5, str(score))
        except:
            pass
        
        renderer.render(border=True)
        time.sleep(1/FPS)

if __name__ == "__main__":
    main()
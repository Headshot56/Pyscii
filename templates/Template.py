def main():
    import time
    import pyscii_renderer


    #Setup variables
    FPS = 5
    x = 10
    y = 10
    vx = 1
    vy = 1

    #Screen dimensions. Make sure the console buffer is the right size or you get flicker
    #Small sizes are reccomended.
    width = 50
    height = 20

    #Create renderer object
    renderer = pyscii_renderer.AsciiRenderer(width, height)

    #Draw loop
    while True:
        #Clear frame buffer
        renderer.clear()

        #Logic loop
        x += vx
        y += vy

        if x <= 1 or x >= width - 5:
            vx *= -1
        if y <= 1 or y >= height - 2:
            vy *= -1
            
            
        #Draw objects to screen
        renderer.draw_text(x, y, "Ball")

        #Render screen
        renderer.render(border=True)

        #Pause before next frame
        time.sleep(1/FPS)

if __name__ == "__main__":
    main()
# import pygame,random module
import pygame,random

# initialise pygame attributes
# init() method returns one tuple of successful and failur operations
pygame.init()

# defined RGB values for particular colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 400
display_height = 400

# set snake each part size (in pixels)
block_size = 10

# Create pygame surface object of speified dimensions
gameDisplay = pygame.display.set_mode((display_width , display_height ))

# give name to the pygame surface object
pygame.display.set_caption("Slither")

# flip() method do whole surface update
#pygame.display.flip()

# update the surface object in particular region
# provided by the user o/w bydefault whole surface
# update
#pygame.display.update()



# create a clock object
clock = pygame.time.Clock()

# frame per second
FPS = 15
"""
left -ve,right +ve
up -ve, down +ve
"""

# create a font object
font = pygame.font.SysFont(None,25)

def snake(block_size,snakeList) :
    for XnY in snakeList :
        # draw a rectangle of specified dimensions on pygame surface object
        pygame.draw.rect(gameDisplay,green,[XnY[0], XnY[1], block_size, block_size])

        
# this function print the msg on the screen
def message_to_screen(msg, color) :

    # rendering the message
    screen_text = font.render(msg, True, color)

    # blitting the screen_text to the pygame surface object.
    gameDisplay.blit(screen_text,[display_width / 2, display_height / 2])

def gameLoop() :

    # starting coordinate of the given object such as block
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0
    
    gameExit = False
    gameOver = False

    # list of list
    # store coordinates of blocks 
    snakeList = []

    # in starting only one block is present that is head
    # this varable plays very important rule in determining
    # the length of snakes
    snakeLength = 1
    
    # we apply round and some arithmetic for making this value as a multiple of 10
    # so that this value will just similar as a lead_x value (mulitple of 10)
    # overlapping of two objects is done so smoothly due to this.
    randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10
    randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10
    
    # loop run untill gameExit not become True
    while not gameExit :

        # loop run till gameOver is not equal to False
        while gameOver == True :
            # fill pygame surface object with white colour
            gameDisplay.fill(white)
            message_to_screen("Game Over, press C to play again and  press Q to quit :",red)

            # update the pygame surface object 
            pygame.display.update()

            # pygame.event.get() method return inbuilt events of the pygame
            # iterate through all the inbuilt events of the pygame
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q :
                        gameExit = True
                        gameOver = False
                        
                    if event.key == pygame.K_c :
                        gameLoop()
                        
        # iterate through all the inbuilt events of the pygame
        for  event in pygame.event.get() :
            #print(event)
            
            # if quit event is performed then set gameExit variable value to True
            if event.type == pygame.QUIT :
                gameExit = True

            # checking the pressing of key
            if event.type == pygame.KEYDOWN :
                
                # we can also use elif here,understand
                # check for whivh key is pressed
                if event.key == pygame.K_LEFT :
                    # give change in pixel value
                    #lead_x -= 10
                    lead_x_change = -block_size
                    lead_y_change = 0
                    
                if event.key == pygame.K_RIGHT :
                    #lead_x += 10
                    lead_x_change = block_size
                    lead_y_change = 0
                    
                # check for whivh key is pressed
                if event.key == pygame.K_UP :
                    
                    # give change in pixel value
                    lead_y_change = -block_size
                    lead_x_change = 0
                    
                if event.key == pygame.K_DOWN :
                    
                    lead_y_change = block_size
                    lead_x_change = 0


                
            """
            if event.type == pygame.KEYUP :

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                    lead_x_change = 0
            """
            
        # this line is useful in setting the boundary for the moving object.
        # if any of the given condition is true then gameOver variable is become false , come out of the game loop
        if lead_x >= display_width  or lead_x < 0 or lead_y >= display_height  or lead_y < 0 :
            gameOver = True
            
        # stop for 1 sec at every iteration
        # time.sleep(1)
        # this is work as coordinates of new block
        # increment the value of lead_x,lead_y by lead_x_change,lead_y_change respectively
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        # fill the pygame surface with white colour
        # this change is done in background
        gameDisplay.fill(white)

        # this line draw a red block at random coordinates within the display area
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,block_size,block_size])

        # this method draw a rectangular shape on the pygame surface object
        # pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])

        # this store coordinate of current block.
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        # this condition help in maintaing the length of snake
        if len(snakeList) > snakeLength :
            del snakeList[0]

        # this three line of code determine the collision. 
        for eachSegment in snakeList[ : -1] :
            if eachSegment == snakeHead :
                gameOver = True
                
        # this also draw a rectangle with colour fill in it.
        #gameDisplay.fill(red,rect = [200,20,10,100] )

        snake(block_size, snakeList)
        
        # update the python surface object
        # update reveals background thing to
        # frontend
        pygame.display.update()
        
        if lead_x == randAppleX and lead_y == randAppleY :
                # for generating block at different location after crossing by moving object
                randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10
                randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10
                snakeLength += 1
                
        # this also draw a rectangle of specified dimensions with specified colour fill in it.
        #gameDisplay.fill(red,rect = [200,20,10,100] )



        # set a no. of frame per second
        clock.tick(FPS)
    """
    message_to_screen("You loose", red)
    pygame.display.update()

    # for stooping the current frame
    time.sleep(2)
    """
    # quit pygame
    # and unitialising all the pygame attributes
    pygame.quit()

    # quit prgm
    quit()

if __name__ == "__main__" :

    # calling the game loop function
    gameLoop()

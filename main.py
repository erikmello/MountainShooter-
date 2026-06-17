import pygame

print("setup start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))   
print ("Setup end")

print("Loop start")
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close the window
            quit() #End pygame
from turtle import window_height
import pygame, sys # import the libraries for pygame and sys at the same time
pygame.init() # activate pygame usefulness
clock = pygame.time.Clock() # set up clock for framerate

BLACK = (0, 0, 0) # setting up the RBG values for black

class Frog(pygame.sprite.Sprite): # sprite class for the frog frames
    def __init__(self, x_position, y_position):
        super().__init__()
        self.frog_frames = []
        self.is_moving = False
        for frame in range(0, 10):
            load_frame = pygame.image.load('./Assets/Images/attack_' + str(frame + 1) + '.png')
            self.frog_frames.append(pygame.transform.scale(load_frame, (300, 150)))
        self.current_frame = 0 # this will increment by 1 for each frame in the loop below
        self.image = self.frog_frames[self.current_frame] # displays the current sprite frame based on list element
        self.rect = self.image.get_rect()
        self.rect.topleft = [x_position, y_position]
    
    def move(self): # gives the below functions permission to activate
        self.is_moving = True
        self.noise = True

    def update(self, speed): # makes sure the animation goes smoothly
        if self.is_moving == True:
            self.current_frame += speed # goes through each frame of animation
            if self.current_frame == 1: # prevents the sound from playing repeatedly if a key is pressed down rapidly
                tongue_sound = pygame.mixer.Sound('./Assets/Sounds/Yoshi_tongue_sound.mp3')
                tongue_sound.play() # play a noise when the frog attacks
            if self.current_frame >= len(self.frog_frames): # resets the animation after each run through
                self.current_frame = 0
                self.is_moving = False # stops a continuous loop to allow a key to be pressed again
            self.image = self.frog_frames[int(self.current_frame)]
        
width_window = 600
height_window = 350
window = pygame.display.set_mode((width_window, height_window)) # dimensions of the window
load_image = pygame.image.load('./Assets/Images/rainforest_image.jpg') # load in an image to be the background
background_image = pygame.transform.scale(load_image, (width_window, height_window)) # resize the image to fit the window
pygame.display.set_caption("Attack Frog") # name of the window

frog_sprites = pygame.sprite.Group() # group that takes in all the frames for animation
frog = Frog(90, 140)
frog_sprites.add(frog)

def main():
    ambience = pygame.mixer.Sound('./Assets/Sounds/BirdsSporadicFrogs CM020101.mp3')
    ambience.play() # play a noise when the frog attacks
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if you close the window, the program closes down pygame and sys
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # press any key to make the frog attack
                frog.move()

        window.blit(background_image, (0, 0)) # puts the background image in the game window, starting from 0 0 xy position
        frog_sprites.draw(window)
        frog_sprites.update(0.2)
        pygame.display.flip()
        clock.tick(60) # framerate

main()
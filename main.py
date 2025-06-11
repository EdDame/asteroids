import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) #define updatable + drawable and add Player class to both
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, all_shots)

    AsteroidField()

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, all_shots)

    dt = 0 #initialize delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        updatable.update(dt)     #update all updatable sprites, passing delta time
        
        for ast in asteroids:
            if ast.collide(player) == True:
                print("Game Over!")
                pygame.quit()
                return
        
        for ast in asteroids:
            for shot in all_shots:
                if ast.collide(shot) == True:
                    ast.split()
                    shot.kill()

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen) #draw all drawable sprites
        
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000.0    #ms to s for delta time, limit to 60 fps
        
                
        
if __name__ == "__main__":
    main()


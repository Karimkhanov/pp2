import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Pythonist')
 
clock = pygame.time.Clock()
 
snake_block = 10 #координата 10 на 10
snake_speed = 10

#шрифты
font_style = pygame.font.SysFont("bahnschrift", 25) #шрифт
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, yellow) #Метод для отображения текста
    dis.blit(value, [dis_width / 6, dis_height / 3+50]) #подставляем на указанные координаты

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])
         #рисуем змейку

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
def gameLoop(): #Описываем всю игровую логику в одной функции.
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = [] #Создаём список, в котором будем хранить показатель текущей длины змейки.
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Round - округлять число
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 #randrange - рандомные цифры

    while not game_over:
        
        while game_close == True:
            
            dis.fill(blue)
            message("You Lost!", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() #перезапускаем игру
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        current_score = Length_of_snake-1
    
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block]) #Рисуем еду

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0] #удаляем голову
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
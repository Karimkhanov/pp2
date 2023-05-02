from config import config
import pygame
import time
import random
import psycopg2
import pygame as pg
import csv

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 620
dis_height = 460

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 10 #координата 10 на 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25) #шрифт
score_font = pygame.font.SysFont("comicsansms", 35)

def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused=False

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
 
def gameLoop(text):
    
    parameters = config()
    connection = psycopg2.connect(**parameters)

    query_create_user = "INSERT INTO snake_game (name, score) VALUES (%s, %s) ;"
    query_update_user = "Update snake_game set score=%s where name =%s ;"
    query_get_user ="select*from snake_game where name='"+text+"';"
    cursor = connection.cursor()
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    point = 1

    get_user=[
        (text)
    ]

    cursor.execute(query_get_user)
    users=cursor.fetchall()
    print(users)
    if users!=[]:
        for user in users:
            point = user[1]
    else:
        textlist =[
        (text,point)
        ]
        cursor.executemany(query_create_user,textlist)

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Round - округлять число
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 #randrange - рандомные цифры

    while not game_over:
        
        while game_close == True:
            
            dis.fill(blue)
            message("You Lost!", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            update_user=[
                (Length_of_snake-1,text)
            ]
            cursor.executemany(query_update_user,update_user)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    connection.commit() #Записать транзакцию
                    cursor.close() #немедленно закрывает курсор
                    connection.close() 
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
                elif event.key == pygame.K_SPACE:
                    pause()
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_over = True #Укажем, что если координаты змейкивыходят за рамки игрового поля, то игра должна закончиться.
                    
 
        x1 += x1_change
        y1 += y1_change
        dis.fill(yellow)
        current_score = Length_of_snake-1
    
        if point % 3 == 0:
            pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block]) #Рисуем еду
        else:
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

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
            Length_of_snake=point
            if point % 3 == 0:
                Length_of_snake += 3
            else:
                Length_of_snake += 1
            point += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()


def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    
    text=''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        gameLoop(text)
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)



if __name__ == '__main__':
    pg.init()
    main()
    pg.quit() 
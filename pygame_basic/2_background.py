import pygame

pygame.init()#초기화(반드시 필요)

#화면 크기 설정
screen_width=480    #가로크기
screen_height=640   #세로크기
screen=pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("PyGame")    #게임 이름

#배경 이미지 불러오기
background=pygame.image.load("C:\\Users\\Home\\Desktop\\VSC_Project\\Python\\나도코딩_파이게임\\pygame_basic\\background.png")

#이벤트 루프가 실행되어야 화면이 꺼지지 않음
running=True    #게임이 진행중인가?
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가?            파이게임을 하기 위해서는 무조건 써야하는 것. #eventloop계속 프로그램이 종료되지 않도록 대기 하는 것.
        if event.type == pygame.QUIT:   #창이 닫히는 이벤트가 발생하였는가?     여러 이벤트 중 QUIT이라면 이 이벤트가 발생
            running = False             #게임이 진행중이 아님                  False로 종료

    #screen.fill((0,30,200))            #배경 색깔로 채우기
    screen.blit(background, (0,0))     #배경 그리기

    pygame.display.update()             #게임 화면을 다시 그리기                매 프레임마다 화면을 계속 그려주는 동작을 해줘야 함
#pygame 종료
pygame.quit()
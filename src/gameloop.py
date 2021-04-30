import sys
import pygame


class GameLoop:
    def __init__(self, level, clock, event_queue, renderer, pace, score_repository):
        self.__level = level
        self.__clock = clock
        self.__event_queue = event_queue
        self.__renderer = renderer
        self.__pace = pace
        self.__score_repository = score_repository
        self.__game_over = False
        self.__player = ""

    def new_game(self):
        self.__give_name()
        self.__start()

    def __give_name(self):
        self.__giving_name = True
        while self.__giving_name:
            self.__check_events()
            self.__render_input()

    def __start(self):
        self.__reset_game()
        while True:
            self.__check_counter()
            self.__check_game_over()
            self.__check_score()
            self.__check_events()
            self.__render_game()
            self.__clock.tick(60)

    def __finished(self):
        while True:
            self.__check_events()
            self.__render_game()

    def __check_game_over(self):
        if self.__level.game_over:
            self.__game_over = True
            self.__save_score()
            self.__finished()

    def __save_score(self):
        score = self.__level.score.score
        self.__score_repository.save_score(self.__player, score)

    def __check_counter(self):
        if self.__pace.check_counter():
            self.__level.lower_block()

    def __check_score(self):
        if self.__level.score.check_score():
            self.__pace.increase_difficulty()

    def __check_events(self):
        for event in self.__event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.__giving_name:
                    if event.key == pygame.K_RETURN:
                        self.__giving_name = False
                    if len(self.__player) < 16:
                        self.__player += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        self.__player = self.__player[:-1]
                elif not self.__game_over:
                    if event.key == pygame.K_LEFT:
                        self.__level.move_block(-1)
                    if event.key == pygame.K_RIGHT:
                        self.__level.move_block(1)
                    if event.key == pygame.K_UP:
                        self.__level.rotate_block()
                    if event.key == pygame.K_DOWN:
                        self.__pace.increase_speed()
                    if event.key == pygame.K_SPACE:
                        self.__level.drop_block()
                #if event.key == pygame.K_RETURN:
                    #self.new_game()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.__pace.decrease_speed()

    def __render_game(self):
        self.__renderer.draw("playing")

    def __render_input(self):
        self.__renderer.draw("input", self.__player)

    def __reset_game(self):
        self.__game_over = False
        self.__level.reset_game_state()
        self.__pace.reset_pace()

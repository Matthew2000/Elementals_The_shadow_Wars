#!/usr/bin/python3
from UniCurses import unicurses as curses

from func import *
from Maps.environment import Environment
from character_classes.player import Player

input_key = -1
current_map = Environment("map1")
DebugLog = open('log.txt', "w")

try:
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()

    viewport = curses.newwin(35, 100, 0, 0)
    update_map(viewport, current_map.get_map())

    player1 = Player("player 1")

    def update_screen():
        curses.clear()
        update_map(viewport, current_map.get_map())
        update_character_location(viewport, player1)
        curses.refresh()
        curses.wrefresh(viewport)

    player1.location = [10, 10]
    spawn_character(viewport, player1)

    curses.refresh()
    curses.wrefresh(viewport)
    while input_key != ord("q"):
        input_key = curses.wgetch(viewport)

        player1.tick(input_key)

        update_screen()
finally:
    curses.endwin()

#!/usr/bin/python3
from UniCurses import unicurses as curses
from Maps.environment import Environment

input_key = -1
main_map = Environment("map1")

try:
    stdscr = curses.initscr()
    curses.noecho()
    curses.curs_set(False)

    viewport = curses.newwin(35, 100, 0, 0)
    curses.waddstr(viewport, main_map.get_map())

    curses.refresh()
    curses.wrefresh(viewport)

    while input_key != ord("q"):
        input_key = curses.getch()

finally:
    curses.endwin()

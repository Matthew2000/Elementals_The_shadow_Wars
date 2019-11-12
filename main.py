#!/usr/bin/python3

from UniCurses import unicurses as curses

input_key = -1

try:
    stdscr = curses.initscr()
    curses.noecho()
    curses.curs_set(False)

    viewport = curses.newwin(35, 100, 0, 0)
    curses.waddstr(viewport, "press 'q' to quit.")

    curses.refresh()
    curses.wrefresh(viewport)

    while input_key != ord("q"):
        input_key = curses.getch()

finally:
    curses.endwin()

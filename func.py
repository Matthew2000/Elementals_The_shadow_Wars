from UniCurses import unicurses as curses


def spawn_character(map_window, character):
    curses.mvwaddstr(map_window, character.location[0], character.location[1], character.symbol)


def update_character_location(map_window, character):
    if character.prev_location != character.location:
        if curses.mvwinch(map_window, character.location[0], character.location[1]) == ord(" "):
            character.prev_location = character.location[:]
        else:
            character.location = character.prev_location[:]
    curses.mvwaddstr(map_window, character.location[0], character.location[1], character.symbol)


def update_map(map_window, map_data):
    curses.mvwaddstr(map_window, 0, 0, map_data)

import pygame as pyg

from Config import config as cfg


def circle_template(play_col):
    surface = pyg.Surface((cfg.b_button_size, cfg.b_button_size))
    surface.fill(pyg.Color(cfg.bg_color))
    pyg.draw.circle(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.b_circle_pos,
        cfg.b_circle_rad,
        cfg.b_width,
    )
    pyg.draw.circle(surface, play_col, cfg.b_circle_pos, cfg.b_circle_rad - cfg.b_width)
    pyg.draw.line(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.b_start_poss[1],
        cfg.b_end_poss[1],
        cfg.b_width,
    )
    pyg.draw.line(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.b_start_poss[2],
        cfg.b_end_poss[2],
        cfg.b_width,
    )
    return surface


def circle_edge(play_col):
    return circle_template(play_col)


def circle_border(play_col):
    surface = circle_edge(play_col)
    pyg.draw.line(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.b_start_poss[3],
        cfg.b_end_poss[3],
        cfg.b_width,
    )
    return surface


def circle_middle(play_col):
    surface = circle_border(play_col)
    pyg.draw.line(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.b_start_poss[0],
        cfg.b_end_poss[0],
        cfg.b_width,
    )
    return surface


def empty_template():
    surface = pyg.Surface((cfg.b_button_size, cfg.b_button_size))
    surface.fill(pyg.Color(cfg.bg_color))
    pyg.draw.line(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.bcr_start_poss[1],
        cfg.bcr_end_poss[1],
        cfg.b_width,
    )
    pyg.draw.line(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.bcr_start_poss[2],
        cfg.bcr_end_poss[2],
        cfg.b_width,
    )
    return surface


def empty_edge():
    return empty_template()


def empty_border():
    surface = empty_edge()
    pyg.draw.line(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.bcr_start_poss[3],
        cfg.bcr_end_poss[3],
        cfg.b_width,
    )
    return surface


def empty_middle():
    surface = empty_border()
    pyg.draw.line(
        surface,
        pyg.Color(cfg.fg_color),
        cfg.bcr_start_poss[0],
        cfg.bcr_end_poss[0],
        cfg.b_width,
    )
    return surface

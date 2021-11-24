def make_text_objs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()

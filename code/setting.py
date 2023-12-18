
# test level map
level_map = [
'                                                                                    ', # 0
'                                                                                    ', # 1
'        C              C            C              C            C              C    ', # 2
' XX    XXX            XX     XX    XXX            XX     XX    XXX            XX    ', # 3
' XX P          C         C   XX            C         C   XX            C         C  ', # 4
' XXXX         XX         XX  XXXX         XX         XX  XXXX         XX         XX ', # 5
' XXXX     C XX     C         XXXX     C XX     C         XXXX     C XX     C        ', # 6
' XX    X  XXXX    XX  XX     XX    X  XXXX    XX  XX     XX    X  XXXX    XX  XX    ', # 7
'    C  X  XXXX    XX  XXX       C  X  XXXX    XX  XXX       C  X  XXXX    XX  XXX   ', # 8
'    XXXX  XXXXXX  XX  XXXX      XXXX  XXXXXX  XX  XXXX      XXXX  XXXXXX  XX  XXXX  ', # 9
'XXXXXXXX  XXXXXX  XX  XXXX  XXXXXXXX  XXXXXX  XX  XXXX  XXXXXXXX  XXXXXX  XX  XXXX  ' # 10
]


# general level settings 
tile_size = 64
half_tile_size = tile_size / 2
screen_width = 1280
screen_height = len(level_map) * tile_size

# font
font_1 = "./images/fonts/my_font.ttf"
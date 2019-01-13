import pyglet
from pyglet.gl import *

# create a pyglet window
win = pyglet.window.Window(fullscreen=True)

# create label
label = pyglet.text.Label('Metro rush',
                          font_name='Times New Roman',
                          font_size=36,
                          x=win.width//2, y=win.height - 30,
                          anchor_x='center', anchor_y='center')


def read_file():
    file_his = open("stations", "r")
    content = file_his.readlines()
    i = 0
    while i < len(content):
        content[i] = content[i].replace("\n", "")
        i = i + 1
    return content


# override the method that draws when the window loads
@win.event
def on_draw():
    win.clear()
    label.draw()
    lis_stations = read_file()
    # len1 = len(lis_stations)
    red_station = []
    blue_station = []
    yellow_stations = []

    glEnable(GL_PROGRAM_POINT_SIZE_EXT)
    glPointSize(10)
    i = 0
    while i < len(lis_stations):
        if lis_stations[i].startswith("#red"):
            while True:
                if lis_stations[i+1].startswith("#"):
                    break
                station = lis_stations[i+1].split(", ")
                red_station.append([int(station[1]), int(station[2])])
                pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (int(station[1]), int(station[2]))),
                ('c3B', (223, 0, 41))
                )
                i = i + 1
            # print(red_station)
            for j in range(len(red_station)-1):
                # create a line context
                glBegin(GL_LINES)
                # create a line, x,y,z
                glVertex3f(red_station[j][0], red_station[j][1], 1)
                glVertex3f(red_station[j+1][0], red_station[j+1][1], -1)
                glEnd()
        # print(i)
        if lis_stations[i].startswith("#yellow"):
            while True:
                if lis_stations[i+1].startswith("#"):
                    break
                station_yellow = lis_stations[i+1].split(", ")
                yellow_stations.append([int(station_yellow[1]), int(station_yellow[2])])
                pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (int(station_yellow[1]), int(station_yellow[2]))),
                ('c3B', (241, 175, 0))
                )
                i = i + 1
            for y in range(len(yellow_stations)-1):
                # create a line context
                glBegin(GL_LINES)
                # create a line, x,y,z
                glVertex3f(yellow_stations[y][0], yellow_stations[y][1], 1)
                glVertex3f(yellow_stations[y+1][0], yellow_stations[y+1][1], -1)
                glEnd()

        if lis_stations[i].startswith("#blue"):
            while True:
                if lis_stations[i+1].startswith("#"):
                    break
                station_blue = lis_stations[i+1].split(", ")
                blue_station.append([int(station_blue[1]), int(station_blue[2])])
                pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (int(station_blue[1]), int(station_blue[2]))),
                ('c3B', (0, 0, 255))
                )
                i = i + 1
            for b in range(len(blue_station)-1):
                # create a line context
                glBegin(GL_LINES)
                # create a line, x,y,z
                glVertex3f(blue_station[b][0], blue_station[b][1], 1)
                glVertex3f(blue_station[b+1][0], blue_station[b+1][1], -1)
                glEnd()
        i = i + 1

# run our pyglet app, and show the window
pyglet.app.run()

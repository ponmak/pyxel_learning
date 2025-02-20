import pyxel

pyxel.init(160, 120)


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    
    # for i in range(10):
    #     rect.x += 1



def draw():
    pyxel.cls(0)
    


pyxel.run(update, draw)
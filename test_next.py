import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
import math
from PIL import Image, ImageDraw
import os
import numpy as np
from matplotlib import pyplot as plt

import pymysql
from pymysql.cursors import DictCursor



connection = pymysql.connect(
    host='213.59.135.187',
    port=3306,
    user='root',
    password='root',
    db='watchman_db',
    charset='utf8mb4',
    cursorclass=DictCursor
)

print(DictCursor)
with connection.cursor() as cursor:
    id_comp = None
    id_team = 2
    buy_lot = 1.5
    sell_lot = 8.0
    floating = -20300.0
    name = 'ZHONG BEN'
    id_terminal = 1
    arg = (id_team, buy_lot, sell_lot, floating, name)
    cursor.execute('''INSERT INTO terminals (ID_Terminal, ID_Team, Lots_buy, Lots_sell, Floating_PL, Name)
                       VALUES (NULL, %s, %s, %s, %s, %s)''',
                   (str(id_team),
                    str(buy_lot),
                    str(sell_lot),
                    str(floating),
                    str(name)
                    )
                   )
    # --------------------------------------------------------------------------------------------------
    cursor.execute('''UPDATE terminals 
                      SET ID_Team = %s
                      WHERE ID_Terminal = %s''',
                   (str(id_team), str(id_terminal))
                   )
    # --------------------------------------------------------------------------------------------------
    cursor.execute('''UPDATE terminals 
                      SET Lots_buy = %s,
                          Lots_sell = %s,
                          Floating_PL = %s,
                      WHERE ID_Terminal = %s''',
                   (str(buy_lot), str(sell_lot), str(floating), str(id_terminal))
                   )
    # --------------------------------------------------------------------------------------------------
    cursor.execute("SELECT ID_Terminal, Name FROM terminals")
    rows = cursor.fetchall()
    for row in rows:
        # tut budet tvoi kod
        pass
    # --------------------------------------------------------------------------------------------------
    cursor.execute("SELECT ID_Team, Name_Team FROM teams")
    rows = cursor.fetchall()
    for row in rows:
        # tut budet tvoi kod
        pass

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        # tut budet tvoi kod
        pass



    #query = "INSERT INTO terminals (ID_Terminal, ID_Team, Lots_buy, Lots_sell, Floating_PL, Name) VALUES (NULL, %d, %f, %f, %f, %s)"
    #cursor.executemany(query, arg)
    # необходимо, т.к. по-умолчанию commit происходит только после выхода
    # из контекстного менеджера иначе мы бы не увидели твиттов
    connection.commit()
with connection.cursor() as cursor:
    query = 'SELECT * FROM terminals'
    cursor.execute(query)
    for row in cursor:
        print(row)

connection.close()
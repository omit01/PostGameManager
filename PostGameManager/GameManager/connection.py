import sqlite3
import time
import uuid

import finishedround
import ongoinground
import group
import post
import os.path

con = sqlite3.connect('gamedb.sqlite3')
cur = con.cursor()


def db_getfinishedrounds():
    global cur
    rounds = []
    for row in cur.execute("SELECT * FROM finishedround"):
        dbround = finishedround.FinishedRound(row[0], row[1], row[2], row[3], row[4], row[5])
        rounds.append(dbround)
    return rounds


def db_addfinishedround(round):
    global cur
    global con
    cur.execute("INSERT INTO finishedround ('UUID', 'Post', 'Groups', 'Scores', 'Starttime', 'Endtime') "
                "VALUES (?, ?, ?, ?, ?, ?)", (
                str(round.uuid), str(round.post), str(round.groups), str(round.scores), round.starttime, round.endtime))
    con.commit()
    return


def db_getongoingrounds():
    global cur
    rounds = []
    for row in cur.execute("SELECT * FROM ongoinground"):
        dbround = ongoinground.OnGoingRound(row[0], row[1], row[2], row[3])
        rounds.append(dbround)
    return rounds


def db_addongoinground(round):
    global cur
    global con
    cur.execute("INSERT INTO ongoinground ('UUID', 'Post', 'Starttime', 'Groups') "
                "VALUES (?, ?, ?, ?)", (str(round.uuid), str(round.post), round.starttime, str(round.groups)))
    con.commit()
    return


def db_getposts():
    global cur
    posts = []
    for row in cur.execute("SELECT * FROM posts"):
        dbpost = post.Post(row[0], row[1], row[2], row[3], row[4])
        posts.append(dbpost)
    return posts


def db_addpost(post):
    global cur
    global con
    cur.execute("INSERT INTO post ('UUID', 'Name', 'Type', 'User', 'Limitgroups', 'Endtime') "
                "VALUES (?, ?, ?, ?, ?, ?)", (
                str(round.uuid), str(round.post), str(round.groups), str(round.scores), round.starttime, round.endtime))
    con.commit()
    return


def db_getgroups():
    global cur
    groups = []
    for row in cur.execute("SELECT * FROM group"):
        dbgroup = group.Group(row[0], row[1], row[2], row[3])
        groups.append(dbgroup)
    return groups


def db_addgroup(group):
    global cur
    global con
    cur.execute("INSERT INTO group ('UUID', 'Name', 'Numberofplayers', 'User',) "
                "VALUES (?, ?, ?, ?)", (str(group.uuid), str(group.name), group.numberofplayers, str(group.user)))
    con.commit()
    return

#!/usr/bin/env python
import random, sys
import cPickle as pickle

matchboxes={}
movehistory=[]

def main():

    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print ""
    print "              _        __     ___    _____  _______    __        __" 
    print "    |        | \    ___) |    \  |  |    /  \     /  __) \    ___) "
    print "    |  |\/|  |  |  (__   |  |\ \ |  |   /    \   |  /     |  (__   "
    print "    |  |  |  |  |   __)  |  | \ \|  |  /  ()  \  | |      |   __)  "
    print "    |  |  |  |  |  (___  |  |  \    | |   __   | |  \__   |  (___  "
    print "    |  |__|  |_/       )_|  |___\   |_|  (__)  |__\    )_/       )_"
    print ""
    print "    Welcome to a MENACE implementation."
    print "    A simulation of the first machine that could learn."
    print "    made by kloki"
    print ""
    print ""
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print ""
    startmenu()



#starting screen
def startmenu():

    print""
    print "    What do you want to do?"
    print "    Pick from play, help, exit."
    print ""
    answer = raw_input()
    
    if answer !="play" and answer!="exit" and answer!="help":
        print ""
        print"    Thats not an option, pick again, wisely."
        print ""
        startmenu()

    if answer == "play":
        play()

    if answer == "help":
        printhelp()
        startmenu()

    if answer == "exit":
        print ""
        print "    Bye."
        print ""
        exit()

#menu before and between games
def play():
    global matchboxes
    global movehistory
    movehistory=[]

    print ""
    print "    Lets play.."
    print "    Choose your action:current, new, load, save, back."
    print ""

    answer=raw_input()

    if answer !="new" and answer!="current" and answer!="load" and answer!="save" and answer!="back" and answer!="" and answer!="beads":
        print ""
        print"    Thats not an option, pick again, wisely."
        print ""
        play()

    if answer == "current" or answer =="":
        menaceturn([" ", " ", " ", " ", " ", " ", " ", " ", " "])

    if answer == "new":
        matchboxes={}
        menaceturn([" ", " ", " ", " ", " ", " ", " ", " ", " "])

    if answer == "load":
        print "    Name of the file?"
        load=raw_input()
        try:
            matchboxes=pickle.load(open(load,"rb"))
            print ""
            print "    beads and matchboxes loaded"
            print ""
        except:
            print""
            print "    No such file."
            print ""
        play()

    if answer == "save":
        print "    Name for the file?"
        save=raw_input()
        pickle.dump(matchboxes,open(save,"wb"))
        print ""
        print "    beads and matchboxes saved."
        print ""
        play()

    if answer == "back":
        startmenu()

    if answer == "beads":
        print matchboxes
        play()
#During game menaceturn and playerturn call eachother
def menaceturn(board):
    board=menacemove(board)#determine move for menace
            
    print""
    print"    MENACE made its move."
    print""
    checkgameend(board)
    printboard(board)
    playerturn(board)

def playerturn(board):
    print""
    print "    What's you action?"
    print""
    move=raw_input()
    checkmovepossible(move,board)
    board[((int(move[1])-1)+ 3*(int(move[0])-1))]="O"#make move for the player
    checkgameend(board)
    print""
    print"    Your move."
    print""

    printboard(board)
    menaceturn(board)

def checkmovepossible(move,board):
    if move!="11" and move!="12" and move!="13" and move!="21" and move!="22" and move!="23" and move!="31" and move!="32" and move!="33":
        print""
        print"    Thats not a valid move."
        print"    Valids move are:11,12,13,21,22,23,31,32,33"
        print""
        playerturn(board)

    if board[((int(move[1])-1)+ 3*(int(move[0])-1))] !=" ":
        print""
        print"    That move is not possible."
        print""
        playerturn(board)


def checkgameend(board):
    
    if (board[0]=="X" and board[1]=="X" and board[2]=="X")or(board[3]=="X" and board[4]=="X" and board[5]=="X")or(board[6]=="X" and board[7]=="X" and board[8]=="X")or(board[0]=="X" and board[3]=="X" and board[6]=="X")or(board[1]=="X" and board[4]=="X" and board[7]=="X")or(board[2]=="X" and board[5]=="X" and board[8]=="X")or(board[0]=="X" and board[4]=="X" and board[8]=="X") or (board[2]=="X" and board[4]=="X" and board[6]=="X"):
        print""
        print"    How sad you lost, but you probably couldn't do anything about it"
        print"    Game end."
        print""
        updatebeads(1)
        printboard(board)
        play()

    if (board[0]=="O" and board[1]=="O" and board[2]=="O")or(board[3]=="O" and board[4]=="O" and board[5]=="O")or(board[6]=="O" and board[7]=="O" and board[8]=="O")or(board[0]=="O" and board[3]=="O" and board[6]=="O")or(board[1]=="O" and board[4]=="O" and board[7]=="O")or(board[2]=="O" and board[5]=="O" and board[8]=="O")or(board[0]=="O" and board[4]=="O" and board[8]=="O") or (board[2]=="O" and board[4]=="O" and board[6]=="O"):
        print""
        print"    Congratulations you won."
        print"    Game end."
        print""
        updatebeads(-1)
        printboard(board)
        play()

    if " " not in board:
        print ""
        print "    Tie, game over"
        print ""
        updatebeads(-1)
        printboard(board)
        play()



def printboard(board):
    print "      1 2 3"
    print "    1|"+board[0]+"|"+board[1]+"|"+board[2]+"|"
    print "    2|"+board[3]+"|"+board[4]+"|"+board[5]+"|"
    print "    3|"+board[6]+"|"+board[7]+"|"+board[8]+"|"


def menacemove(board):
    global movehistory
    global matchboxes
    isomorphlist=findisomorphs(board)#find the isomorph this greatly reduces the amount of matchboxes.
    turn=0
    #finds isomorphs
    for i in isomorphlist:
        if str(i)in isomorphlist:
            break
        turn=turn+1
    if turn==8:#board not in matchboxes
        entry=str(board)
        matchboxes[str(board)]=givebeads(board)
    else:
        entry=str(isomorphlist[turn])

    #decide move
    actions=matchboxes[entry]
    if len(actions)==1:#if theres only one action
        boardnext=actions[0][0]
    else:#randomly choose one action
        beads=0
        for i in actions:
            beads=beads+i[1]
        rollwheel=random.randint(0,beads)
        beads=0
        for i in actions:
            beads=beads+i[1]
            if rollwheel<=beads:
                boardnext=i[0]
                break
    
    #return ismorph to correct original form
    if turn >1 and turn!=8:
        boardnext=t90grid(boardnext)

    if turn >1 and turn!=8 and turn <6:
        boardnext=t90grid(boardnext)

    if turn >1 and turn!=8 and turn <4:
        boardnext=t90grid(boardnext)

    if turn == 1 or turn == 3 or turn ==5: #reverse inverse
        boardnext=[boardnext[6],boardnext[7],boardnext[8],boardnext[3],boardnext[4],boardnext[5],boardnext[0],boardnext[1],boardnext[2]]

    movehistory.append((board,boardnext))#storemove for learning
    return boardnext


def t90grid(board):#turns the game board 90 degrees useful for isomorphs
    t90board=[board[2],board[5],board[8],board[1],board[4],board[7],board[0],board[3],board[6]]
    return t90board                                                                                       
                                                                                           
def findisomorphs(board):
    isomorphlist=[board]
    isomorphlist.append([board[6],board[7],board[8],board[3],board[4],board[5],board[0],board[1],board[2]])
    isomorphlist.append(t90grid(isomorphlist[0]))
    isomorphlist.append(t90grid(isomorphlist[1]))
    isomorphlist.append(t90grid(isomorphlist[2]))
    isomorphlist.append(t90grid(isomorphlist[3]))
    isomorphlist.append(t90grid(isomorphlist[4]))
    isomorphlist.append(t90grid(isomorphlist[5]))
    return isomorphlist

def givebeads(board):#determines all possible action for given board
    options=board.count(" ")
    beadslist=[]
    for i in xrange(len(board)):
        if board[i] == " ":
            entry=board[:]
            entry[i]="X"
            beadslist.append([entry,options])
    return beadslist

def updatebeads(winorlose):#learning part is called at the end of each game
    global matchboxes
    global movehistory

    for i in movehistory:
        update=0
        beads=matchboxes[str(i[0])]
        for n in xrange(len(beads)-1):
            if beads[n][0]==i[1]:
                update=beads[n][1]+winorlose
                beads[n][1]=update
                break
        matchboxes[str(i[0])]=beads


def printhelp():
    print"    "
    print"    This is an implementation of Menace, the first learning machine that"
    print"    learned beating humans in tic-tac-toe using beads and matchboxes."
    print"    url:http://shorttermmemoryloss.com/menace/"
    print"    Yes, there is no wikipedia entry :( "
    print"    "
    print"    The point of the game is to play tic-tac-toe repeatly against Menace."
    print"    In the beginning it will play randomly but eventually it will beat"
    print"    you, always. "
    print"    "
    print"    Controls:"
    print"    To place your circles type two integers corresponding to the location"
    print"    on the board. First vertically than horizantally. Thus for the upper-"
    print"    right corner type: 13"
    print "   "
    print "      1 2 3"
    print "    1| | |O|"
    print "    2| | | |"
    print "    3| | | |"
    print "    "
    print"    Between episodes you have multiple options "
    print"    current:play the game with the current beads and matchboxes"
    print"            (instead of typing current over and over again, press enter)"
    print"    new    :reset the current beads and matchboxes"
    print"    load   :load the beads and matchboxes of a previous game(pickle)"
    print"    save   :save the current beads and matchboxes in a pickle"

#-------------------------------
if __name__ == "__main__":
    main()

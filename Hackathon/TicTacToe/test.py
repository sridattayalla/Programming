class Field:
    __EMPTY_FIELD = "."
    __AVAILABLE_FIELD = "-1"
    __NUM_COLS = 9
    __NUM_ROWS = 9
    __mBoard = []
    __mMacroboard = []
    __myId = "0"
    __opponentId = "1"
    __POSSIBLE_LINES = [[0,1,2],[3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__(self):
        for _ in range(81):
            self.__mBoard.append(self.__EMPTY_FIELD)

        # Macroboard
        for _ in range(9):
            self.__mMacroboard.append(self.__AVAILABLE_FIELD)

    #
    def parseFromString(self, s):
        s = s.replace(";", ",")
        r = s.split(",")
        counter = 0
        for y in range(9):
            for x in range(9):
                self.__mBoard[y*9+x] = r[counter]
                counter += 1

    def parseMacroboardFromString(self, s):
        r = s.split(",")
        counter = 0
        self.__mMacroboard = []
        for _ in range(9):
            self.__mMacroboard.append(r[counter])
            counter += 1

    def getPositionNumber(self, i, pos):
        return 9*(3*(i//3)+pos//3)+3*(i%3)+pos%3

    def returnMove(self, i, pos):
        position_num = self.getPositionNumber(i, pos)
        column = position_num % 9
        row = position_num // 9
        return Move(column, row)

    def getRandomAvailableMove(self, i):
        for pos in range(9):
            if (self.__mBoard[self.getPositionNumber(i, pos)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos)

    def getEmptyCorner(self, i):
        l = [0, 2, 6, 8]
        for pos in l:
            if (self.__mBoard[self.getPositionNumber(i, pos)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos)
        # get random available move
        return self.getRandomAvailableMove(i)

    def getUsefulMove(self, i):
        for line in self.__POSSIBLE_LINES:
            pos_1 = line[0]
            pos_2 = line[1]
            pos_3 = line[2]
            if(self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__EMPTY_FIELD and self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_3)
            elif (self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__EMPTY_FIELD and self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_1)
            elif (self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__EMPTY_FIELD and self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_1)
        # return middle square if available
        if(self.__mBoard[self.getPositionNumber(i,4)]==self.__EMPTY_FIELD):
            return self.returnMove(i, 4)
        # return corner squares if available
        return self.getEmptyCorner(i)

    def getOpponentWinningMove(self, i):
        for line in self.__POSSIBLE_LINES:
            pos_1 = line[0]
            pos_2 = line[1]
            pos_3 = line[2]
            if(self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__opponentId and self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__opponentId and self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_3)
            elif (self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__opponentId and self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__opponentId and self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_2)
            elif (self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__opponentId and self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__opponentId and self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_1)
            # if opponent dont have any chance to win then place our move to win
        return self.getUsefulMove(i)

    def getMyWinningMove(self, i):
        for line in self.__POSSIBLE_LINES:
            pos_1 = line[0]
            pos_2 = line[1]
            pos_3 = line[2]
            print(self.__mBoard[self.getPositionNumber(i, pos_1)], self.__mBoard[self.getPositionNumber(i, pos_2)], self.__mBoard[self.getPositionNumber(i, pos_3)])
            if(self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_3)
            elif (self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_2)
            elif (self.__mBoard[self.getPositionNumber(i, pos_2)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_3)] == self.__myId and self.__mBoard[self.getPositionNumber(i, pos_1)] == self.__EMPTY_FIELD):
                return self.returnMove(i, pos_1)
            # if we dont have any chance to win then block opponent chances to win
        return self.getOpponentWinningMove(i)

    def getAvailableMoves(self):
        for i in range(9):
            if(self.__mMacroboard[i]==self.__AVAILABLE_FIELD):
                return self.getMyWinningMove(i)




    def toString(self):
        r = ""
        counter = 0
        for y in range(self.__NUM_ROWS):
            for x in range(self.__NUM_COLS):
                if (counter > 0):
                    r += ","
                r += self.__mBoard[x][y]
                counter += 1
        return r

    def isFull(self):
        for y in range(self.__NUM_ROWS):
            for x in range(self.__NUM_COLS):
                if (self.__mBoard[x][y] == self.__EMPTY_FIELD):  return False
        return True

    def isEmpty(self):
        for y in range(self.__NUM_ROWS):
            for x in range(self.__NUM_COLS):
                if (self.__mBoard[x][y] != self.__EMPTY_FIELD):  return False
        return True

    def getNrColumns(self):
        return self.__NUM_COLS

    def getNrRows(self):
        return self.__NUM_ROWS

    def getPlayerID(self, x, y):
        return self.__mBoard[x][y]

    def getMyId(self):
        return self.__myId

    def setMyId(self, id):
        self.__myId = id

    def getOpponentId(self):
        return self.__opponentId

    def setOpponentId(self, id):
        self.__opponentId = id


class Move:
    __x = -1
    __y = -1

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def toString(self):
        return "place_move {} {}".format(self.__x, self.__y)

f = Field()
f.parseFromString(".,1,1,.,.,.,0,.,.,1,0,1,.,0,.,.,0,1,1,.,.,.,.,.,.,.,.,.,.,.,0,.,1,0,.,.,.,0,.,.,1,.,.,0,.,.,.,.,1,.,1,.,.,.,0,.,.,.,.,.,.,.,.,.,0,.,.,.,.,.,0,.,.,.,.,.,.,.,1,.,.")
f.parseMacroboardFromString(".,.,.,.,1,.,-1,.,.")
print(f.getAvailableMoves().toString())
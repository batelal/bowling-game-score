
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class round:
    def __init__(self, throw1=0, throw2=0, throw3=0, totalRoundScore=0, isStrike=False, isSpare=False, isFinalScore =False, isLastRound=False):
        self.__throw1 = 0
        self.__throw2 = 0
        self.__throw3 = 0
        self.__totalRoundScore = 0
        self.__isStrike = False
        self.__isSpare = False
        self.__isFinalScore = False
        self.__isLastRound = False


    def __str__(self):
        if(self.__isLastRound):
            return f"(throw1: {self.__throw1}, throw2: {self.__throw2}, throw3: {self.__throw3}, totalScore: {self.__totalRoundScore}, Strike Ind: {self.__isStrike}, Spare Ind: {self.__isSpare}, FinalScore Ind: {self.__isFinalScore}, LastRound Ind: {self.__isLastRound})"
        else:
            return f"(throw1: {self.__throw1}, throw2: {self.__throw2}, totalScore: {self.__totalRoundScore}, Strike Ind: {self.__isStrike}, Spare Ind: {self.__isSpare}, LastRound Ind: {self.__isLastRound})"

    def setThrow1(self, throw1):
        if throw1 <= 10 and throw1 >= 0:
           self.__throw1 = throw1
        else:
            print("Given number is out of range, please enter a number between 0 and 10")
            raise Exception()

    def setThrow2(self, throw2):
        if throw2 <= 10 and throw2 >= 0:
           self.__throw2 = throw2
        else:
            print("Given number is out of range, please enter a number between 0 and 10")
            raise Exception()

    def setThrow3(self, throw3):
        if throw3 <= 10 and throw3 >= 0:
           self.__throw3 = throw3
        else:
            print("Given number is out of range, please enter a number between 0 and 10")
            raise Exception()

    def setStrikeInd(self):
        self.__isStrike = True

    def setSpareInd(self):
        self.__isSpare = True

    def setFinalScoreInd(self):
        self.__isFinalScore = True

    def setLastRoundInd(self):
        self.__isLastRound = True

    def updateTotalRoundScore(self):
        self.__totalRoundScore = int(self.__throw1) + int(self.__throw2) + int(self.__throw3)

    def getStrikeInd(self):
       return self.__isStrike

    def getSpareInd(self):
       return self.__isSpare

    def getFinalScoreInd(self):
       return self.__isFinalScore

    def getLastRoundInd(self):
       return self.__isLastRound

    def getTotalRoundScore(self):
       return self.__totalRoundScore

    def getThrow1(self):
       return self.__throw1

    def getThrow2(self):
       return self.__throw2

    def getThrow3(self):
       return self.__throw3

def bowling_game(name):

    print('Welcome to Bowling game. What is your name?')
    UserName = input()
    print(f'Hi, {UserName}', 'Lets start to Play')


    bowlingRoundsList = []
    totalScoresList = []
    ScoreListPrint = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    TotalScoreListPrint = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " "]


    for i in range(0,10):
        r = round()

        #If Last round
        if i == 9:
            r.setLastRoundInd()
            r.setFinalScoreInd()

        while (True):
            print('Enter your score in  round {} throw 1 '.format(i+1))
            try:
                throw1 = int(input())
                r.setThrow1(throw1)
                break
            except Exception as error:
                print(error)


        #If user did Strike
        if throw1 == 10:
            r.setStrikeInd()
            if r.getLastRoundInd():
                while (True):
                    print('Enter your score in  round {} throw 2 '.format(i + 1))
                    try:
                        throw2 = int(input())
                        r.setThrow2(throw2)
                        break
                    except Exception as error:
                        print(error)

                if throw1 + throw2 == 10:
                    r.setSpareInd()
        else:
            while(True):
                print('Enter your score in  round {} throw 2 '.format(i+1))
                try:
                    throw2 = int(input())
                    r.setThrow2(throw2)
                    break
                except Exception as error:
                    print(error)

            #If user did Spare
            if throw1 + throw2 == 10:
                r.setSpareInd()

        #For the last round if Strike or Spare give Throw 3
        if r.getLastRoundInd() and (r.getSpareInd() or r.getStrikeInd()):
            while (True):
                print('Enter your score in  round {} throw 3 '.format(i + 1))
                try:
                    throw3 = int(input())
                    r.setThrow3(throw3)
                    break
                except Exception as error:
                    print(error)


        if r.getLastRoundInd() == False and r.getStrikeInd() == False:
            if throw1 + throw2 > 10:
                print("Total score of two rounds cannot be great than 10")
                break

        r.updateTotalRoundScore()
        bowlingRoundsList.append(r)


        #Give Bonus for Strike
        if (i==1) and (bowlingRoundsList[i-1].getStrikeInd() == True) :
            strikeBonus = totalScoresList[i-1] + r.getTotalRoundScore()
            totalScoresList[i-1] = strikeBonus
            if (bowlingRoundsList[i].getStrikeInd() == False):
                bowlingRoundsList[i - 1].setFinalScoreInd()

        if (i > 1) and (bowlingRoundsList[i - 1].getStrikeInd() == True) and (bowlingRoundsList[i].getStrikeInd() == False):
            strikeBonus = totalScoresList[i - 1] + r.getTotalRoundScore()
            totalScoresList[i - 1] = strikeBonus
            if (bowlingRoundsList[i].getStrikeInd() == False):
                bowlingRoundsList[i - 1].setFinalScoreInd()

        if (i > 1) and (bowlingRoundsList[i - 1].getStrikeInd() == True) and (bowlingRoundsList[i].getStrikeInd() == True):
            strikeBonus = totalScoresList[i - 1] + r.getTotalRoundScore()
            totalScoresList[i - 1] = strikeBonus


        #Check if 2 strikes in a row
        if (i>1) and (bowlingRoundsList[i-1].getStrikeInd() == True) and (bowlingRoundsList[i-2].getStrikeInd() == True):
            #update for both strikes in a row
            strikeBonus = totalScoresList[i-2] + r.getThrow1()
            totalScoresList[i-2] = strikeBonus
            strikeBonus = totalScoresList[i - 2] + bowlingRoundsList[i-1].getTotalRoundScore() + r.getTotalRoundScore()
            totalScoresList[i - 1] = strikeBonus
            bowlingRoundsList[i - 2].setFinalScoreInd()
            bowlingRoundsList[i - 1].setFinalScoreInd()

        # Give Bonus for Spare
        if (i>0) and (bowlingRoundsList[i-1].getSpareInd()):
            spareBonus = totalScoresList[i-1] + r.getThrow1()
            totalScoresList[i - 1] = spareBonus
            bowlingRoundsList[i - 1].setFinalScoreInd()

        # Update score in the list
        if (i == 0):
            totalScoresList.append(r.getTotalRoundScore())
        else:
            totalScore = totalScoresList[i - 1] + r.getTotalRoundScore()
            totalScoresList.append(totalScore)

        if ((r.getStrikeInd() == False) and (r.getSpareInd() == False)):
            r.setFinalScoreInd()

        #print(bowlingRoundsList[i])
        #print(totalScoresList[i])

        #Print score board
        y=0
        for j in range(0, i+1) :
            if bowlingRoundsList[j].getStrikeInd() == False:
                ScoreListPrint[y] = bowlingRoundsList[j].getThrow1()
            else:
                ScoreListPrint[y] = "/"

            if (bowlingRoundsList[j].getStrikeInd() == False and bowlingRoundsList[j].getSpareInd() == False):
                ScoreListPrint[y+1] = bowlingRoundsList[j].getThrow2()
            else:
                ScoreListPrint[y+1] = "/"

            if bowlingRoundsList[j].getLastRoundInd() == True:
                ScoreListPrint[y] = bowlingRoundsList[j].getThrow1()
                ScoreListPrint[y+1] = bowlingRoundsList[j].getThrow2()
                ScoreListPrint[y+2] = bowlingRoundsList[j].getThrow3()

            if bowlingRoundsList[j].getFinalScoreInd() == True:
                TotalScoreListPrint[j] = totalScoresList[j]

            y=y+2

        print("------------------------------------------------------------------------------------------------------------------------------")
        if bowlingRoundsList[j].getLastRoundInd() == True and (bowlingRoundsList[j].getStrikeInd() == True or bowlingRoundsList[j].getSpareInd() == True):
            print("| Round 1 ||  Round 2  ||  Round 3 || Round 4 || Round 5 || Round 6 || Round 7 || Round 8 || Round 9 ||   Round 10   ||   ")
            print("------------------------------------------------------------------------------------------------------------------------------")
            print(f"|  {ScoreListPrint[0]} | {ScoreListPrint[1]}  ||   {ScoreListPrint[2]} | {ScoreListPrint[3]}    ||  {ScoreListPrint[4]} | {ScoreListPrint[5]}   ||  {ScoreListPrint[6]} | {ScoreListPrint[7]}  ||  {ScoreListPrint[8]} | {ScoreListPrint[9]}  ||  {ScoreListPrint[10]} | {ScoreListPrint[11]}  ||  {ScoreListPrint[12]} | {ScoreListPrint[13]}  ||  {ScoreListPrint[14]} | {ScoreListPrint[15]}  ||  {ScoreListPrint[16]} | {ScoreListPrint[17]}  ||  {ScoreListPrint[18]} | {ScoreListPrint[19]}  | {ScoreListPrint[20]} ||")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"|   {TotalScoreListPrint[0]}     ||     {TotalScoreListPrint[1]}    ||   {TotalScoreListPrint[2]}     ||   {TotalScoreListPrint[3]}    ||   {TotalScoreListPrint[4]}    ||   {TotalScoreListPrint[5]}    ||   {TotalScoreListPrint[6]}    ||   {TotalScoreListPrint[7]}    ||   {TotalScoreListPrint[8]}    ||     {TotalScoreListPrint[9]}       ||   ")
        else:
            print("| Round 1 ||  Round 2  ||  Round 3 || Round 4 || Round 5 || Round 6 || Round 7 || Round 8 || Round 9 || Round 10 ||   ")
            print("------------------------------------------------------------------------------------------------------------------------------")
            print(f"|  {ScoreListPrint[0]} | {ScoreListPrint[1]}  ||   {ScoreListPrint[2]} | {ScoreListPrint[3]}   ||  {ScoreListPrint[4]} | {ScoreListPrint[5]}   ||  {ScoreListPrint[6]} | {ScoreListPrint[7]}  ||  {ScoreListPrint[8]} | {ScoreListPrint[9]}  ||  {ScoreListPrint[10]} | {ScoreListPrint[11]}  ||  {ScoreListPrint[12]} | {ScoreListPrint[13]}  ||  {ScoreListPrint[14]} | {ScoreListPrint[15]}  ||  {ScoreListPrint[16]} | {ScoreListPrint[17]}  ||  {ScoreListPrint[18]} | {ScoreListPrint[19]}   ||")
            print("--------------------------------------------------------------------------------------------------------------------------")
            print(f"|   {TotalScoreListPrint[0]}     ||     {TotalScoreListPrint[1]}    ||   {TotalScoreListPrint[2]}     ||   {TotalScoreListPrint[3]}    ||   {TotalScoreListPrint[4]}    ||   {TotalScoreListPrint[5]}    ||   {TotalScoreListPrint[6]}    ||   {TotalScoreListPrint[7]}    ||   {TotalScoreListPrint[8]}    ||   {TotalScoreListPrint[9]}     ||   ")

    if(i==9):
        print("   ")
        print("----------------------------------------------------")
        print(f'**** Great Game {UserName}. Your Total Score is:  {TotalScoreListPrint[9]} ****')
        print("----------------------------------------------------")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bowling_game('Bat Ela')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

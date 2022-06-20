
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


    def printround(self):
       print(f"(throw1: {self.__throw1}, throw2: {self.__throw2})")

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

    def setThrow2(self, throw2):
        if throw2 <= 10 and throw2 >= 0:
           self.__throw2 = throw2
        else:
            print("Given number is out of range, please enter a number between 0 and 10")

    def setThrow3(self, throw3):
        if throw3 <= 10 and throw3 >= 0:
           self.__throw3 = throw3
        else:
            print("Given number is out of range, please enter a number between 0 and 10")
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

        print('Enter your score in  round {} throw 1 '.format(i+1))
        try:
            throw1 = int(input())
            r.setThrow1(throw1)
        except Exception as error:
            print(error)
            break

        #If user did Strike
        if throw1 == 10:
            r.setStrikeInd()
            if r.getLastRoundInd():
                print('Enter your score in  round {} throw 2 '.format(i + 1))
                try:
                    throw2 = int(input())
                    r.setThrow2(throw2)
                except Exception as error:
                    print(error)
                    break

                if throw1 + throw2 == 10:
                    r.setSpareInd()
        else:
            print('Enter your score in  round {} throw 2 '.format(i+1))
            try:
                throw2 = int(input())
                r.setThrow2(throw2)
            except Exception as error:
                print(error)
                break

            #If user did Spare
            if throw1 + throw2 == 10:
                r.setSpareInd()

        #For the last round if Strike or Spare give Throw 3
        if r.getLastRoundInd() and (r.getSpareInd() or r.getStrikeInd()):
            print('Enter your score in  round {} throw 3 '.format(i + 1))
            try:
                throw3 = int(input())
                r.setThrow3(throw3)
                print(f"(***Throw 3: ", r.getThrow3())
            except Exception as error:
                print(error)
                break

        if r.getLastRoundInd() == False and r.getStrikeInd() == False:
            if throw1 + throw2 > 10:
                print("Total score of two rounds cannot be great than 10")
                break

        r.updateTotalRoundScore()
        bowlingRoundsList.append(r)

        #Give Bonus for Strike or Spare
        if (i>0) and (bowlingRoundsList[i-1].getStrikeInd()) :
            strikeBonus = totalScoresList[i-1] + r.getThrow1() + r.getThrow2()
            totalScoresList[i-1] = strikeBonus
            print(f"(Total Score for Round for strike {i - 1}: ", totalScoresList[i - 1])
            bowlingRoundsList[i - 1].setFinalScoreInd()
            #Check if 2 Strikes in a row
            If (i>1) and (bowlingRoundsList[i-2].getStrikeInd()):
                strikeBonus = totalScoresList[i - 2] + totalScoresList[i - 1] + r.getThrow1()
                totalScoresList[i - 1] = strikeBonus
                print(f"(Total Score for Round for strike {i - 2}: ", totalScoresList[i - 2])
                bowlingRoundsList[i - 2].setFinalScoreInd()

        elif (i>0) and (bowlingRoundsList[i-1].getSpareInd()):
            spareBonus = totalScoresList[i-1] + r.getThrow1()
            totalScoresList[i - 1] = spareBonus
            print(f"(Total Score for Round for spare {i-1}: ", totalScoresList[i-1])
            bowlingRoundsList[i - 1].setFinalScoreInd()

        if (i>0):
            totalScore = totalScoresList[i-1] + r.getTotalRoundScore()
            totalScoresList.append(totalScore)
        else:
            totalScoresList.append(r.getTotalRoundScore())

        if r.getStrikeInd() == False and r.getSpareInd() == False:
            r.setFinalScoreInd()

        print(f"(***FinalScoreInd for Round {i}: ", bowlingRoundsList[i].getFinalScoreInd())
        print(f"(Total Score for Round {i}: ", totalScoresList[i])


        print(bowlingRoundsList[i])
        print(totalScoresList[i])

        y=0
        for j in range(0, i+1) :
            print(f"Total Score for Round {j+1}: ", totalScoresList[j])
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


        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"| {ScoreListPrint[0]} | {ScoreListPrint[1]}  || {ScoreListPrint[2]} | {ScoreListPrint[3]}  || {ScoreListPrint[4]} | {ScoreListPrint[5]}  ||  {ScoreListPrint[6]} | {ScoreListPrint[7]}  ||  {ScoreListPrint[8]} | {ScoreListPrint[9]}  ||  {ScoreListPrint[10]} | {ScoreListPrint[11]}  ||  {ScoreListPrint[12]} | {ScoreListPrint[13]}  ||  {ScoreListPrint[14]} | {ScoreListPrint[15]} ||  {ScoreListPrint[16]} | {ScoreListPrint[17]} ||  {ScoreListPrint[18]} | {ScoreListPrint[19]} | {ScoreListPrint[20]} |")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|   {TotalScoreListPrint[0]}    ||   {TotalScoreListPrint[1]}   ||   {TotalScoreListPrint[2]}    ||   {TotalScoreListPrint[3]}    ||   {TotalScoreListPrint[4]}    ||   {TotalScoreListPrint[5]}    ||   {TotalScoreListPrint[6]}    ||   {TotalScoreListPrint[7]}    ||   {TotalScoreListPrint[8]}    ||   {TotalScoreListPrint[9]}   ||   {TotalScoreListPrint[9]}    ||")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bowling_game('Bat Ela')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

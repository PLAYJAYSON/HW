import random as rnd

class GameItem:
    def __init__(self, name, *power):
        self.name = name
        self.power = list(power)

class handItem:
    def __init__(self, *gameItem):       
        self.gameItem = list(gameItem)
        
    def choise(self, thisPlayer):
        self.thisPlayer = thisPlayer
        if self.thisPlayer == True:
            print()
            print('Сделайте выбор:')
            print()
            for i in range(len(self.gameItem)):
               print(f'{i + 1} {self.gameItem[i].name}')
            __myChoise = int(input())
            print()
            print(f'Игрок выбрал: {self.gameItem[__myChoise -1].name}')

        else:
            __myChoise = rnd.randint(1,len(self.gameItem))
            print()
            print(f'Компьютер выбрал: {self.gameItem[__myChoise -1].name}')

        return self.gameItem[__myChoise -1]

def compareHand(playerHand, PCHand):
    print()
    if playerHand.name == PCHand.name:
        print('Ничья!')
    else:
        winCounter = 0
        for i in range(len(playerHand.power)):
            if playerHand.power[i] > PCHand.power[i]:
                winCounter +=1
        if winCounter > len(playerHand.power) / 2:
            print('Игрок победил!')
        else:
            print('Компьютер победил!')
    print()

stone = GameItem('Камень', 0, 2, 1)
paper = GameItem('Бумага', 1, 0, 2)
scissors = GameItem('Ножницы', 2, 1, 0)

handGame = handItem(stone, scissors, paper)

while True:
    playerTurn = handGame.choise(True)
    PCTurn = handGame.choise(False)
    compareHand(playerTurn, PCTurn)
    print('****')



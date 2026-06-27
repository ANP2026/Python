class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Cricket player :{self.__player} , Score : {self.__score}")
    def play(self):
        print(f"{self.__player} hits a six!")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score >=0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score can't be negative")
class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Football player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} scores a goal!")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score >=0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score can't be negative")
cricket = Cricket("Rohit", 85)
football = Football("Arjun", 2)
print("Scoreboard")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()
print("Direct Change Attempt")
cricket.__score = 999
print(f"{cricket.get_score()}")
print("Updating Score")
cricket.set_score(143)
football.set_score(5)
print(f"Cricket score is now {cricket.get_score()}")
print(f"Football score is now {football.get_score()}")

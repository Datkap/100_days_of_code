class ScoreBoard:
    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score += 1

    def display_score(self):
        print(f"Your score is {self.score}!")
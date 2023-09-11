from random import randint
import math

class Env:
    def __init__(self):
        self.distance = 5  # km
        self.time_spend = 0  # 使用的总共时间 要惩罚时间的
        self.block = 0  # 中立
        self.reset()

    def reset(self):
        self.distance = randint(2, 6)  # km
        self.block = 0
        self.time_spend = 0  # 使用的总共时间 要惩罚时间的

    def is_over(self):
        return abs(self.distance) < 0.01

    def get_state_reword(self, action: int):
        pass

    def step(self, action: int):
        speed = action + self.block + math.tan(action + self.block)


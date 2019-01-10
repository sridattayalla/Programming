#!/usr/bin/env python3


import sys
import random
from util import *


def go():
    bot = BotStarter()
    parser = BotParser(bot)
    parser.run()


class BotStarter:
    def __init__(self):
        random.seed()
        
    def doMove(self, state):
        return state.getField().getAvailableMoves()


if __name__ == '__main__':
    go()

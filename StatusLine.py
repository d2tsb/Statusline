"""
The MIT License (MIT)
Copyright (c) 2024* Tilman Bertram

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import sys
import time
import threading

from enum import Enum


class Efficiency(Enum):
    # prints every <value> seconds
    EFFICIENT = 0.006
    MEDIUM = 0.00001
    PRECISE = 0.0000006


class StatusLine:

    def __init__(self,
                 rangeEnd=100,
                 x_width=12,
                 end_char='>',
                 status_char='=',
                 printEndMessage=True,
                 printPercentage=True,
                 spinWheel=True,
                 eff: Efficiency = Efficiency.EFFICIENT
                 ):

        self.count = 0
        self.end = rangeEnd
        self.x_width = x_width
        self.beg_charBracket = '['
        self.end_charBracket = ']'
        self.printEndMessage = printEndMessage
        self.status_char = status_char
        self.end_char = end_char
        self.spinWheel = spinWheel
        self.killed = False
        self.printPercentage = printPercentage
        self.eff = eff
        self.mutex = threading.Lock()
        self.run_event = threading.Event()
        self.run_event.clear()

    def throwLoop(self, ):
        while self.run_event.is_set():
            # if self.count >= self.end:
            # print (self.run_event.is_set())
            with self.mutex:
                self.printCurrentState()
                # sys.stdout.write("%d" % self.count);
            time.sleep(self.eff.value)
        with self.mutex:
            self.printCurrentState()
        print("") #new line


    def test(self):
        tLoop = threading.Thread(target=self.throwLoop,)
        self.run_event.set()
        tLoop.start()
        for _ in range(0,
                       self.end):
            time.sleep(0.01)
            # time.sleep(0.2)
            # self.incrementCount();
            self.incrementCount()
        tLoop.join()

    def run(self):
        self.run_event.set()
        tLoop = threading.Thread(target=self.throwLoop,)
        tLoop.start()
    def kill(self):
        self.run_event.clear()
        time.sleep(0.1 + Efficiency.EFFICIENT.value)
        # naive way to terminate the thread. sigkill or something else
        # would be a more proper solution.

    def clearLine(self):
        # nice and simple solution
        i = ''
        backspace = chr(8)
        for _ in range(0, self.x_width):
            i += backspace
        print(i, end='')

        """
        i += '\x1b[0;'
        for _ in range(0,self.x_width):
            i += ' '

        i += '\x1b[0;'
        print(i, end='')
        """

    def print(self, value):
        # sys.stdout.write(value + '\n');
        sys.stdout.write(value)
        # print(value, end='');

    def printCurrentState(self, ):
        wing = str('\33[2K\r')
        wing += self.beg_charBracket
        percentage = self.count/self.end  # value  [0;1]
        bla = round(percentage * (self.x_width - 2))  # max x_width - 2
        # fill content
        for _ in range(0, bla):
            wing += self.status_char
        if bla > 0 and self.count < self.end:
            wing = list(wing)
            wing[-1] = self.end_char
            wing = "".join(wing)
        # fill content
        fill_char = ' '
        for _ in range(0, (self.x_width - 2) - bla):
            wing += fill_char
        wing += self.end_charBracket
        if self.printPercentage:
            wing += ' ' + ('%03.1f ' % (percentage * 100)) + '% ' + 2*' '
        wing += ' '

        # wing += ' ' + str(percentage * 100) + '% ' + 20*' '

        if self.count == self.end:
            wing += '\n'
            self.killed = True
        else:
            if self.spinWheel:
                match self.count % 4:
                    case 0:
                        wing += '|'
                    case 1:
                        wing += '/'
                    case 2:
                        wing += '-'
                    case 3:
                        wing += '\\'
                        """
                    case 4: 
                        wing += '-' 
                    case 5: 
                        wing += '/' 
                        """
                wing += '  '

        self.print(wing)

        # print(wing, end='')
        # print(wing, end='')
        # self.clearLine()
        # self.print('\x1b[2K\r')

    def incrementCount(self):
        with self.mutex:
            self.count += 1
        if (self.count == self.end):
            self.kill()

    def reset(self):
        self.count = 0
        self.killed = False

    def incrementCountSync(self):
        # easiest update solution
        if (self.count == self.end):
            self.killed = True

        if (self.killed == False):
            self.count += 1
        self.printCurrentState()

    def testRun(self):
        # Primitive
        self.reset()
        for _ in range(0,
                       self.end):
            self.incrementCount()
            self.printCurrentState()
            time.sleep(0.01)


# loading. loading.. loading...

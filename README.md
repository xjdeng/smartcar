# SmartCar #

SmartCar is a demonstration of the Q-Learning methodology of training a smart car to navigate and find directions to its destination.  At the beginning, the smart car will be placed at a random location on a 8x6 street grid and another random location will be designated as a destination.  The smart car will also be supplied with a waypoint indicating a recommended direction of travel to reach the destination.  However, the car will be required to obey the traffic signals and will incur penalties for trying to violate them.  The goal of this simulation is to get the cab to reach its destination before it runs out of time and to train it to reach its destination as quickly as possible.

## Installation and Usage ##

Requires Python 2.7 and pygame


$ git clone http://github.com/xjdeng/smartcar.git

$ cd smartcar

$ python smartcab/agent.py


## Further Documentation ##

Please see the file [smartcar/smartcab/writeup.pdf](https://github.com/xjdeng/smartcar/blob/master/smartcab/smartcab/writeup.pdf) to understand the reasoning behind the project as well as the intermediate steps taken to achieve the final result.

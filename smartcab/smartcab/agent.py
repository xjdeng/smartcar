import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
from QLearner import QLearner

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        # TODO: Initialize any additional variables here
        self.discount_factor = 0.5
        self.learning_rate = 0.5
        self.default_Q = 2
        self.Q0 = {}
        self.none_count = 0
        self.max_none = 6
        for i in ['forward','left','right']:
            for j in ['green','red']:
                for k in self.env.valid_actions:
                    self.Q0[(i,j),k] = self.default_Q
        self.Q = QLearner(self.env.valid_actions, self.Q0, self.learning_rate, self.discount_factor)

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
        self.Q.reset()
        self.none_count = 0

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # TODO: Update state
        self.state = (self.next_waypoint, inputs['light'])
        
        # TODO: Select action according to your policy
        action = self.Q.pickAction(self.state)
        if action == None:
            self.none_count = self.none_count + 1
        else:
            self.none_count = 0
        if self.none_count > self.max_none:
            action = random.choice(Environment.valid_actions)

        # Execute action and get reward
        reward = self.env.act(self, action)
        

        # TODO: Learn policy based on state, action, reward

        self.Q.updateState(self.state,reward,newAction = action)

        print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # set agent to track

    # Now simulate it
    sim = Simulator(e, update_delay=0.01)  # reduce update_delay to speed up simulation
    sim.run(n_trials=100)  # press Esc or close pygame window to quit


if __name__ == '__main__':
    run()

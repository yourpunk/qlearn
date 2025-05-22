import random
import time
from collections import defaultdict
from blockworld import BlockWorldEnv
 
class QLearning():
    def __init__(self, env: BlockWorldEnv, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.env = env
        self.Q = defaultdict(float)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
 
    def serialize_state(self, state, goal):
        return (tuple(sorted(state.get_state())), tuple(sorted(goal.get_state())))
 
    def choose_action(self, state, goal):
        actions = state.get_actions()
        if not actions:
            return None
        if random.random() < self.epsilon:
            return random.choice(actions)
        s_key = self.serialize_state(state, goal)
        q_vals = [(self.Q[(s_key, a)], a) for a in actions]
        max_q = max(q_vals, key=lambda x: x[0])[0]
        best_actions = [a for q, a in q_vals if q == max_q]
        return random.choice(best_actions)
 
    def train(self):
        start_time = time.time()
        while time.time() - start_time < 30:
            (state, goal), _ = self.env.reset()
            for _ in range(50):
                state_key = self.serialize_state(state, goal)
                actions = state.get_actions()
                if not actions:
                    break
                action = self.choose_action(state, goal)
                (new_state, _), reward, done, _, _ = self.env.step(action)
                new_key = self.serialize_state(new_state, goal)
                future_actions = new_state.get_actions()
                max_future_q = max([self.Q[(new_key, a)] for a in future_actions], default=0.0)
                self.Q[(state_key, action)] += self.alpha * (
                    reward + self.gamma * max_future_q - self.Q[(state_key, action)]
                )
                state = new_state
                if done:
                    break
 
    def act(self, s):
        state, goal = s
        actions = state.get_actions()
        if not actions:
            return None
        s_key = self.serialize_state(state, goal)
        q_vals = [(self.Q[(s_key, a)], a) for a in actions]
        max_q = max(q_vals, key=lambda x: x[0])[0]
        best_actions = [a for q, a in q_vals if q == max_q]
        return random.choice(best_actions)

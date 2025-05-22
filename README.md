# 💻 Q-Learning Agent 
### Overview
This is a small Q-Learning-based reinforcement learning project, created as part of a school assignment. The task was to implement the core logic of a **Q-learning agent** that interacts with a simple environment — the Block World.<br> The code simulates a reinforcement learning scenario where an agent learns to navigate a grid-like environment using the Q-Learning algorithm. The environment and visual logic are handled in ``blockworld.py``, while the main focus of this repository is the core learning logic implemented in ``student.py``.

## 🧠 What I Did
- I implemented the Q-Learning agent in student.py, including:
- Q-table initialization
- Action selection using epsilon-greedy policy
- Q-value updates
- Agent training loop and performance tracking

## 🗂️ Project Structure
``` graphql
qlearn-main/
├── blockworld.py     # Simulation environment
├── student.py        # Q-Learning agent logic (my part 🩷)
└── README.md         # Project overview
```

## 🧪 How to Run
> Make sure you have Python 3 installed.

To run the simulation:  
``` bash
python blockworld.py
```
This will launch the learning process and visualize how the agent learns over time.

## ⚙️ Dependencies
Only standard Python libraries are used (no external dependencies).

## 🐣 Status
✅ Complete – The learning agent is functional and demonstrates basic reinforcement learning behavior.

## 📚 Learnings
This project helped me understand:
- How Q-Learning works in practice
- The importance of exploration vs. exploitation
- How to implement and debug reinforcement learning logic

## 👤 Author
🚀 Created by Aleksandra Kenig (aka [yourpunk](https://github.com/yourpunk)). 


💌 Wanna collab or throw some feedback? You know where to find me.

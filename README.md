# 🤖 Q-Learning Agent: Block World Edition

A reinforcement learning agent that learns to navigate a grid-based environment using the **Q-Learning algorithm**.

This project simulates an agent exploring a discrete environment — balancing exploration vs exploitation, learning through feedback, and improving over time.  
Visualized using a lightweight `blockworld.py` environment.

---

## 🎯 Why This Exists

Most beginner RL agents feel like “proof-of-concept math”.  
I wanted to build something that **actually behaves** like an agent:

- learns smarter paths over time  
- balances randomness and logic  
- uses a minimal, readable Q-table structure

---

## 🧠 What I Built

My implementation lives in `qlearn.py` and covers:

- ✅ Q-table initialization (dictionary-based, sparse-safe)
- 🎲 Action selection via **ε-greedy** strategy
- 🔁 Q-value update rule:  
  `Q(s, a) = Q(s, a) + α [reward + γ * max Q(s', a') - Q(s, a)]`
- 📈 Training loop with episode tracking
- 🧪 Run-time feedback to visualize learning progression

---

## 🗂️ File Structure

```text
qlearn-main/
├── blockworld.py     # Visualization & environment logic
├── qlearn.py        # Q-Learning agent logic (my part 🩷)
└── README.md         # You're here.
```

---

## 🚀 How to Run

> Requires Python 3.<br> No external libraries needed.
```bash
python blockworld.py
```
Agent will begin learning in the visual environment — you’ll see its decisions evolve over time.

---

## ✨ What I Explored
This wasn't just about plugging in a formula. I wanted to:
- understand how RL agents adapt over episodes
- test different ε and α values to see learning speed trade-offs
- visualize why some policies converge while others fail

---

## ⚙️ Tech Notes

- **Environment**: 2D grid world with states and reward conditions
- **State encoding**: stringified coordinates
- **Q-table**: nested Python dict `{state: {action: value}}`
- **Default behavior**: 1000 episodes, ε=0.1, α=0.5, γ=0.9
Can be tweaked easily in `blockworld.py`.

---

## 💡 Takeaway
Reinforcement learning isn’t about big frameworks — it’s about designing logic that improves over time.
This agent may be simple, but it thinks, fails, adapts — and that’s exactly what makes it cool.

---

## 📜 License

**MIT**. Use it, fork it, break it. Just don’t ship it without understanding it.

---

## 👤 Author
🦾 Crafted by Aleksandra Kenig (aka [yourpunk](https://github.com/yourpunk)).<br>
💌 Got questions, ideas, or just want to nerd out about RL? Ping me.

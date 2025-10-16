# 🏎️ The Bot Racing Game

**A fun, AI-powered racing game built with Python and Pygame.**  
Race against a computer-controlled car, navigate challenging tracks, and test your reflexes as you speed to the finish line!  

![🎮 Game Preview](https://github.com/iamghimirebishal/Bot-Racing-Game/blob/main/imgs/bot%20racing.gif)  


---

## 💡 Project Motivation

This project was created by **The Binary Bots** - a team of enthusiastic robotics and programming learners - to explore the fundamentals of **AI motion control**, **path following**, and **game development** using **Python and Pygame**.  

The goal was to simulate a fun yet technical racing environment where players compete against an AI bot that follows a defined racing path, showcasing how simple automation logic can create an engaging gaming experience.

---

## 🎮 Features

- 🧠 **AI Bot Racer** – Compete against an autonomous computer car that follows a defined path.  
- 🎨 **Smooth Graphics & Animation** – Realistic car rotation, acceleration, and visually appealing menu animations.  
- 🚦 **Multiple Levels** – Progress through 10 increasingly challenging levels.  
- 🧩 **Accurate Collision Detection** – Mask-based collisions for walls and finish lines.  
- 🎵 **Interactive Menu** – Animated start menu with scaling and rotation effects.  
- 💨 **Speed & Time Tracking** – Displays player speed and time per level.  

---

## 🗂️ Project Structure

Bot-Racing-Game/

│ ├── imgs/ # Image assets (track, cars, backgrounds)

│ ├── background.png

│ ├── grass.jpg

│ ├── track1.png

│ ├── track1_border.png

│ ├── finish.png

│ ├── red-car.png

│ └── green-car.png

│

├── main.py # Main game logic and loop

├── utils.py # Helper functions for scaling and rendering

└── README.md # Project documentation

---

## ⚙️ Installation & Setup

**1. Clone the repository**

- git clone https://github.com/iamghimirebishal/Bot-Racing-Game.git

- cd Bot-Racing-Game

**2. Install dependencies**

- Make sure you have Python 3.8+ installed, then run:

- pip install pygame

**3. Run the game**

- python main.py

---

## 🎮 How to Play
**Key	Action**
- W	Move Forward
- S	Move Backward
- A	Turn Left
- D	Turn Right
- Enter	Start Game / Next Level
- Esc	Quit Game

🧭 Avoid crashing into the track borders, outsmart the AI car, and race your way to victory!

---

## 🧠 Game Logic Overview

**PlayerCar**: Handles player control, movement, and collision reactions.

**ComputerCar**: Follows a predefined set of path points to simulate AI racing.

**Menu Screen**: Features animated scaling and rotation effects for an engaging intro.

---

## 📸 Screenshots

Main Menu	In-Game View

https://github.com/iamghimirebishal/Bot-Racing-Game/imgs/gameplay.png
https://github.com/iamghimirebishal/Bot-Racing-Game/imgs/losing interface.png
https://github.com/iamghimirebishal/Bot-Racing-Game/imgs/main menu.png

---

## 👨‍💻 Developed By
### The Binary Bots
#### Team Members:

- Bishal Ghimire

- Abhisam Sharma

- Rajan Pandey

- Sagar Bhatta

---

## 🏁 Future Enhancements

- Add multiplayer or Bluetooth-controlled mode

- Add new tracks and obstacle mechanics

- Enhance AI pathfinding with adaptive learning

- Add sound effects and background music

- Implement save progress and leaderboard

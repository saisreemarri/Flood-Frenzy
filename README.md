Flood Frenzy is a web-based implementation of the classic Color Flood game. The objective is to capture the entire board by repeatedly choosing colors that expand your territory.
The project demonstrates the use of fundamental Data Structures and Algorithms in an interactive game.

Features :
-  Randomly generated 11 × 11 game board
-  Five different colors
-  Click-based gameplay
-  Flood Fill algorithm for territory expansion
-  Undo functionality
-  Accessibility (Color-Blind) Mode
-  Animated color highlighting
-  Win popup displaying total moves
-  New Game button



Data Structures & Algorithms Used :
2D Array : Stores the game board 
Breadth-First Search (BFS) : Flood Fill algorithm 
Queue (`deque`) : BFS traversal 
Set : Tracks the player's owned cells 
Stack : Undo functionality 


Tech Stack :
 Frontend 
- HTML
- CSS
- JavaScript

 Backend
- Python
- Flask
- Flask-CORS



Project Structure

Flood-Frenzy/
│
├── backend/
│   ├── app.py
│   ├── game.py
│   ├── floodFill.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── api.js
│       └── script.js
│
└── .gitignore
```



 How to Play

1. The game starts with the top-left region as your territory.
2. Select one of the five colors at the bottom of the board.
3. Your territory changes to the selected color and expands to adjacent cells of the same color.
4. Continue selecting colors until the entire board is captured.
5. Try to win in as few moves as possible!

---

 Accessibility Mode

Enable Accessibility Mode using the toggle switch to display unique symbols on each color, making the game easier to distinguish for color-blind users.

Red : ● 
Yellow : ■ 
Green : ▲ 
Blue : ★ 
Pink : ✚ 



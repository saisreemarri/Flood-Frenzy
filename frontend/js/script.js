
const boardElement = document.getElementById("board");
const moveCounter = document.getElementById("moveCounter");
const colorBlindToggle = document.getElementById("colorBlindToggle");

const undoBtn = document.getElementById("undoBtn");

const winModal = document.getElementById("winModal");
const finalMoves = document.getElementById("finalMoves");
const newGameBtn = document.getElementById("newGameBtn");

const colorMap = {
    0: "red",
    1: "yellow",
    2: "green",
    3: "blue",
    4: "pink"
};

const symbolMap = {
    0: "●",
    1: "■",
    2: "▲",
    3: "★",
    4: "✚"
};

let gameState = {
    board: [],
    owned: [],
    moves: 0,
    won: false
};

let accessibilityMode = false;
let isAnimating = false;


/* -------------------- */
/* Draw Board */
/* -------------------- */

function renderBoard(board) {

    gameState.board = board;

    boardElement.innerHTML = "";

    board.forEach((row, r) => {

        row.forEach((color, c) => {

            const cell = document.createElement("div");

            cell.classList.add("cell");
            cell.classList.add(colorMap[color]);

            cell.dataset.row = r;
            cell.dataset.col = c;
            cell.dataset.color = color;

            if (accessibilityMode) {
                cell.textContent = symbolMap[color];
            }

            boardElement.appendChild(cell);

        });

    });

}


/* -------------------- */
/* Preview */
/* -------------------- */

function previewMove(selectedColor) {

    const preview = gameState.board.map(row => [...row]);

    gameState.owned.forEach(([r, c]) => {

        preview[r][c] = selectedColor;

    });

    renderBoard(preview);

}


/* -------------------- */
/* Highlight */
/* -------------------- */

function highlightColor(color) {

    document.querySelectorAll(".cell").forEach(cell => {

        if (Number(cell.dataset.color) === color) {

            cell.classList.add("highlight");

        }

    });

}


function removeHighlight() {

    document.querySelectorAll(".cell").forEach(cell => {

        cell.classList.remove("highlight");

    });

}


/* -------------------- */
/* Update UI */
/* -------------------- */

function updateUI() {

    moveCounter.textContent = `Moves : ${gameState.moves}`;

    if (gameState.won) {

        finalMoves.textContent =
            `You finished the game in ${gameState.moves} moves!`;

        winModal.classList.remove("hidden");

    } else {

        winModal.classList.add("hidden");

    }

}


/* -------------------- */
/* Load Game */
/* -------------------- */

async function loadGame() {

    const game = await newGame();

    gameState = game;

    renderBoard(game.board);

    updateUI();

    winModal.classList.add("hidden");

}


/* -------------------- */
/* Color Buttons */
/* -------------------- */

document.querySelectorAll(".color-btn").forEach(button => {

    button.addEventListener("click", async () => {

        if (isAnimating)
            return;

        const color = Number(button.dataset.color);

        if (color === gameState.board[0][0])
            return;

        isAnimating = true;

        const backendPromise = makeMove(color);

        previewMove(color);

        highlightColor(color);

        await new Promise(resolve => setTimeout(resolve, 100));

        const game = await backendPromise;

        removeHighlight();

        gameState = game;

        renderBoard(game.board);

        updateUI();

        isAnimating = false;

    });

});


/* -------------------- */
/* Undo */
/* -------------------- */

undoBtn.addEventListener("click", async () => {

    if (isAnimating)
        return;

    const game = await undoMove();

    gameState = game;

    renderBoard(game.board);

    updateUI();

});


/* -------------------- */
/* Accessibility */
/* -------------------- */

colorBlindToggle.addEventListener("change", () => {

    accessibilityMode = colorBlindToggle.checked;

    if (accessibilityMode) {

        document.body.classList.add("color-blind");

    }

    else {

        document.body.classList.remove("color-blind");

    }

    renderBoard(gameState.board);

    document.querySelectorAll(".color-btn").forEach(button => {

        button.textContent = accessibilityMode
            ? button.dataset.symbol
            : "";

    });

});


/* -------------------- */
/* Play Again */
/* -------------------- */

newGameBtn.addEventListener("click", loadGame);


/* -------------------- */
/* Start */
/* -------------------- */

loadGame();
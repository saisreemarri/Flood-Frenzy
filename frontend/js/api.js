
const BASE_URL = "http://127.0.0.1:5000";

/* ------------------------- */
/* Start New Game */
/* ------------------------- */

async function newGame() {

    const response = await fetch(`${BASE_URL}/new-game`);

    return await response.json();

}

/* ------------------------- */
/* Make Move */
/* ------------------------- */

async function makeMove(color) {

    const response = await fetch(`${BASE_URL}/make-move`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            color: color
        })

    });

    return await response.json();

}

/* ------------------------- */
/* Undo */
/* ------------------------- */

async function undoMove() {

    const response = await fetch(`${BASE_URL}/undo`, {

        method: "POST"

    });

    return await response.json();

}
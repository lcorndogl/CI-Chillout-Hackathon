document.addEventListener('DOMContentLoaded', function () {
    const gameArea = document.getElementById('gameArea');
    const gameMessage = document.getElementById('gameMessage');
    let initialClickTime;
    let greenTime;
    let timeoutId;
    let gameStarted = false;

    gameArea.addEventListener('click', function () {
        if (!gameStarted) {
            initialClickTime = performance.now();
            startGame();
        } else {
            const clickTime = performance.now();
            if (clickTime < greenTime) {
                clickedTooSoon();
            } else {
                endGame(clickTime);
            }
        }
    });

    function startGame() {
        gameMessage.innerText = 'Wait for green...';
        const delay = Math.random() * 2000 + 1000; // Random delay between 1 and 3 seconds
        gameStarted = true;
        timeoutId = setTimeout(() => {
            gameArea.style.backgroundColor = 'green';
            gameMessage.innerText = 'Click!';
            greenTime = performance.now();
        }, delay);
    }

    function clickedTooSoon() {
        clearTimeout(timeoutId);
        gameMessage.innerText = 'You clicked too soon! Click anywhere to try again.';
        gameArea.style.backgroundColor = '';
        gameStarted = false;
    }

    function endGame(clickTime) {
        const reactionTime = clickTime - greenTime;
        gameMessage.innerText = `Your reaction time is: ${reactionTime.toFixed(2)} ms. Click anywhere to try again.`;
        gameArea.style.backgroundColor = '';
        gameStarted = false;
    }
});
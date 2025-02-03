document.addEventListener('DOMContentLoaded', function () {
    const gameArea = document.getElementById('gameArea');
    const gameMessage = document.getElementById('gameMessage');
    let initialClickTime;
    let greenTime;
    let timeoutId;
    let gameStarted = false;

    gameArea.addEventListener('click', function () {
        const clickTime = performance.now();
        if (!gameStarted) {
            initialClickTime = clickTime;
            startGame();
        } else {
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
        saveReactionTime(reactionTime);
    }

    function saveReactionTime(reactionTime) {
        fetch('/save-reaction-time/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ score: reactionTime })
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
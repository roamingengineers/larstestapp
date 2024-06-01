document.addEventListener('DOMContentLoaded', () => {
    const stairForm = document.getElementById('stairForm');
    const logClimbButton = document.getElementById('logClimbButton');
    const mainContainer = document.getElementById('mainContainer');
    const logClimbContainer = document.getElementById(
        'logClimbContainer');
    const backButton = document.getElementById('backButton');
    const eiffelTower = document.getElementById('eiffelTower');
    const eiffelInfoContainer = document.getElementById(
        'eiffelInfoContainer');
    const backToMainButton = document.getElementById(
        'backToMainButton');
    const totalFlightsElement = document.getElementById('totalFlights');
    const totalTimeElement = document.getElementById('totalTime');
    const totalSecondsElement = document.getElementById('totalSeconds');
    const progressBar = document.getElementById('progressBar');
    const remainingFlightsElement = document.getElementById(
        'remainingFlights');
    const progressPercent = document.getElementById('progressPercent');
    let totalFlights = 0;
    let totalTime = 0;
    let totalSeconds = 0;
    const goalFlights = 1200;
    logClimbButton.addEventListener('click', () => {
        logClimbContainer.classList.remove('hidden');
    });
    backButton.addEventListener('click', () => {
        logClimbContainer.classList.add('hidden');
    });
    eiffelTower.addEventListener('click', () => {
        eiffelInfoContainer.classList.remove('hidden');
    });
    backToMainButton.addEventListener('click', () => {
        eiffelInfoContainer.classList.add('hidden');
    });
    stairForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const flights = parseInt(document.getElementById(
            'flights').value);
        const time = document.getElementById('time').value
            .split(':');
        const minutes = parseInt(time[0]);
        const seconds = parseInt(time[1]);
        totalFlights += flights;
        totalTime += minutes;
        totalSeconds += seconds;
        if (totalSeconds >= 60) {
            totalTime += Math.floor(totalSeconds / 60);
            totalSeconds = totalSeconds % 60;
        }
        totalFlightsElement.textContent = totalFlights;
        totalTimeElement.textContent = totalTime.toString()
            .padStart(2, '0');
        totalSecondsElement.textContent = totalSeconds
            .toString().padStart(2, '0');
        const progressPercentage = Math.min((totalFlights /
            goalFlights) * 100, 100);
        progressBar.style.width = `${progressPercentage}%`;
        progressPercent.textContent =
            `${progressPercentage.toFixed(2)}%`;
        const remainingFlights = Math.max(goalFlights -
            totalFlights, 0);
        remainingFlightsElement.textContent = remainingFlights;
        stairForm.reset();
        logClimbContainer.classList.add('hidden');
    });
});
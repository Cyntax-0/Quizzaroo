document.addEventListener("DOMContentLoaded", function () {
    const questions = [
        {
            question: "What is the capital city of France?",
            answers: [
                { text: "Paris", correct: true },
                { text: "Madrid", correct: false },
                { text: "Rome", correct: false },
                { text: "Berlin", correct: false },
            ]
        },
        {
            question: "Which planet is known as the Red Planet?",
            answers: [
                { text: "Mars", correct: true },
                { text: "Venus", correct: false },
                { text: "Jupiter", correct: false },
                { text: "Saturn", correct: false },
            ]
        },
        {
            question: "Who painted the Mona Lisa?",
            answers: [
                { text: "Leonardo da Vinci", correct: true },
                { text: "Pablo Picasso", correct: false },
                { text: "Vincent van Gogh", correct: false },
                { text: "Michelangelo", correct: false },
            ]
        },
        {
            question: "What is the largest ocean in the world?",
            answers: [
                { text: "Pacific Ocean", correct: true },
                { text: "Atlantic Ocean", correct: false },
                { text: "Indian Ocean", correct: false },
                { text: "Arctic Ocean", correct: false },
            ]
        },
        {
            question: "What is the tallest living animal on Earth?",
            answers: [
                { text: "Elephant", correct: false },
                { text: "Giraffe", correct: true },
                { text: "Blue whale", correct: false },
                { text: "Shark", correct: false },
            ]
        },
        {
            question: "Which animal has the largest heart?",
            answers: [
                { text: "Elephant", correct: false },
                { text: "Giraffe", correct: false },
                { text: "Blue whale", correct: true },
                { text: "Shark", correct: false },
            ]
        },
        {
            question: "What is the weight of the largest blue whale ever recorded?",
            answers: [
                { text: "100 tons", correct: false },
                { text: "200 tons", correct: false },
                { text: "300 tons", correct: false },
                { text: "400 tons", correct: true },
            ]
        },
        {
            question: "Which animal is considered the largest aquatic animal in the world?",
            answers: [
                { text: "Elephant", correct: false },
                { text: "Giraffe", correct: false },
                { text: "Blue whale", correct: true },
                { text: "Shark", correct: false },
            ]
        },
        {
            question: "What is the weight of the Antarctic blue whale?",
            answers: [
                { text: "100,000 pounds", correct: false },
                { text: "200,000 pounds", correct: false },
                { text: "300,000 pounds", correct: false },
                { text: "400,000 pounds", correct: true },
            ]
        },
        {
            question: "Which animal is the tallest mammal on Earth?",
            answers: [
                { text: "Elephant", correct: false },
                { text: "Giraffe", correct: true },
                { text: "Blue whale", correct: false },
                { text: "Shark", correct: false },
            ]
        }
    ];

    const questionElement = document.getElementById("question");
    const answerButton = document.getElementById("answer-buttons");
    const nextButton = document.getElementById("next-btn");
    const timerElement = document.getElementById("timer");

    let currentQuestionIndex = 0;
    let score = 0;
    let remainingTime = 30;
    let timer;

    function startQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        nextButton.innerHTML = "Next";
        showQuestion();
    }

    function showQuestion() {
        resetState();
        let currentQuestion = questions[currentQuestionIndex];
        let questionNo = currentQuestionIndex + 1;
        questionElement.innerHTML = questionNo + ". " + currentQuestion.question;

        currentQuestion.answers.forEach(answer => {
            const button = document.createElement("button");
            button.innerHTML = answer.text;
            button.classList.add("btn");
            answerButton.appendChild(button);
            if (answer.correct) {
                button.dataset.correct = answer.correct;
            }
            button.addEventListener("click", selectAnswer);
        });

        startTimer();
        updateTimerDisplay();
    }

    function resetState() {
        nextButton.style.display = "none";
        while (answerButton.firstChild) {
            answerButton.removeChild(answerButton.firstChild);
        }
    }

    function selectAnswer(e) {
        const selectedBtn = e.target;
        const isCorrect = selectedBtn.dataset.correct === "true";
        if (isCorrect) {
            selectedBtn.classList.add("correct");
            score++;
        } else {
            selectedBtn.classList.add("incorrect");
        }
        Array.from(answerButton.children).forEach(button => {
            if (button.dataset.correct === "true") {
                button.classList.add("correct");
            }
            button.disabled = true;
        });

        // Delay the next question by 4 seconds
        setTimeout(handleNextButton, 4000);
    }

    function showScore() {
        resetState();
        res = (score/questions.length) * 100;
        questionElement.innerHTML = `Your score ${res}%`;
    
        // Send the score to the Flask endpoint
        fetch('/score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ score: res })
        })
        .then(response => response.text())
        .then(data => {
            // Handle the response from the server
            console.log(data);
        })
        .catch(error => {
            // Handle any errors that occurred during the request
            console.error(error);
        });
    }

    function handleNextButton() {
        remainingTime = 30; // Reset the remaining time for the next question
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            showQuestion();
        } else {
            clearInterval(timer); // Clear the timer when all questions are answered
            showScore(); // Send the score to the Flask endpoint
            setTimeout(function() {
                window.location.href = '/score';
            }, 10000);
        }
    }

    function startTimer() {
        clearInterval(timer); // Clear the previous timer
        timer = setInterval(() => {
            remainingTime--;
            updateTimerDisplay();
            if (remainingTime <= 0) {
                handleNextButton();
            }
        }, 1000);
    }

    function updateTimerDisplay() {
        timerElement.innerHTML = remainingTime;
    }

    nextButton.addEventListener("click", () => {
        handleNextButton();
    });

    startQuiz();
});
document.addEventListener('DOMContentLoaded', function() {
    var quizForm = document.getElementById('quizForm');
    if (quizForm) {
        quizForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting normally

            const submitButton = document.querySelector('button[type="submit"]');
            submitButton.disabled = true; // Disable the submit button immediately on submission

            const userAnswer = document.querySelector('input[name="user_answer"]:checked');
            if (!userAnswer) {
                submitButton.disabled = false; // Re-enable the button if no option was selected
                return; // Exit if no answer is selected
            }

            const userAnswerValue = userAnswer.value;
            const correctAnswer = userAnswer.dataset.correct; // This should be set in your HTML as data attribute

            // Apply styling based on the answer correctness
            document.querySelectorAll('.form-check-input').forEach(input => {
                const parent = input.parentElement;
                parent.classList.remove('correct-answer', 'incorrect-answer');
                if (input.value === correctAnswer) {
                    parent.classList.add('correct-answer');
                }
                if (input.value === userAnswerValue) {
                    if (userAnswerValue !== correctAnswer) {
                        parent.classList.add('incorrect-answer');
                    }
                }
            });

            const feedbackMessage = document.getElementById('feedbackMessage');
            if (userAnswerValue === correctAnswer) {
                feedbackMessage.textContent = "Correct.";
                feedbackMessage.classList.remove('incorrect');
                feedbackMessage.classList.add('correct');

                fetch('/quiz/add_correct', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ increment: 1 })
                }).then(response => {
                    // Handle response if needed
                }).catch(error => {
                    console.error('Error:', error);
                });
            } else {
                feedbackMessage.textContent = "Incorrect.";
                feedbackMessage.classList.add('incorrect');
                feedbackMessage.classList.remove('correct');
            }

            // Show the Next Question button
            nextQuestionButton.style.display = 'block';
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const draggables = document.querySelectorAll('.term');
    const containers = document.querySelectorAll('.term-slot');
    const nextQuestionButton = document.getElementById('nextQuestionButton');
    const feedbackMessage = document.getElementById('feedbackMessage');

    draggables.forEach(draggable => {
        draggable.addEventListener('dragstart', () => {
            draggable.classList.add('dragging');
        });

        draggable.addEventListener('dragend', () => {
            draggable.classList.remove('dragging');
        });
    });

    containers.forEach(container => {
        container.addEventListener('dragover', e => {
            e.preventDefault(); // Allow the drop by preventing the default handling of the element
            container.classList.add('hovered'); // Visual cue for drop target
        });

        container.addEventListener('dragleave', () => {
            container.classList.remove('hovered'); // Remove visual cue when draggable leaves
        });

        container.addEventListener('drop', e => {
            e.preventDefault();
            const draggable = document.querySelector('.dragging');
            if (container.children.length === 0) { // Check if the drop container is empty
                container.appendChild(draggable);
            } else {
                container.replaceChildren(draggable); // Replace existing content with the new draggable
            }
            container.classList.remove('hovered'); // Clean up visual cue
        });
    });

    var quizForm = document.getElementById('quizForm');
    if (quizForm) {
        quizForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting normally

            // Check if it is a multiple-choice question
            if (document.querySelector('input[name="user_answer"]')) {
                handleMultipleChoiceSubmission();
            } else {
                handleMatchTermsSubmission();
            }
        });
    }

    function handleMultipleChoiceSubmission() {
        const userAnswer = document.querySelector('input[name="user_answer"]:checked');
        if (!userAnswer) {
            feedbackMessage.textContent = "Please select an option.";
            feedbackMessage.classList.add('incorrect');
            return; // Exit if no answer is selected
        }
    
        const correctAnswer = userAnswer.dataset.correct; // Correct answer is stored in data-correct attribute
        document.querySelectorAll('.form-check-input').forEach(input => {
            const parent = input.parentElement;
            if (input.value === correctAnswer) {
                parent.classList.add('correct-answer');
            } else {
                parent.classList.remove('correct-answer');
            }
        });
    
        // Disable the submit button after the form is submitted
        document.querySelector('button[type="submit"]').disabled = true;
    
        updateFeedback(userAnswer.value === correctAnswer);
    }

    function handleMultipleChoiceSubmission() {
        const userAnswer = document.querySelector('input[name="user_answer"]:checked');
        if (!userAnswer) {
            feedbackMessage.textContent = "Please select an option.";
            feedbackMessage.classList.add('incorrect');
            return; // Exit if no answer is selected
        }
    
        const correctAnswer = userAnswer.dataset.correct; // Correct answer is stored in data-correct attribute
        document.querySelectorAll('.form-check-input').forEach(input => {
            const parent = input.parentElement;
            if (input.value === correctAnswer) {
                parent.classList.add('correct-answer'); // Highlight correct answer in green
            } else {
                parent.classList.remove('correct-answer');
            }
        
            if (input.value === userAnswer.value && input.value !== correctAnswer) {
                parent.classList.add('incorrect-answer'); // Highlight incorrect answer in red
            } else {
                parent.classList.remove('incorrect-answer');
            }
        
            input.disabled = true; // Disable the radio button to prevent further changes
        });        
    
        // Disable the submit button after the form is submitted
        document.querySelector('button[type="submit"]').disabled = true;
    
        updateFeedback(userAnswer.value === correctAnswer);
    }

    function updateFeedback(isCorrect) {
        if (isCorrect) {
            feedbackMessage.textContent = "Correct!";
            feedbackMessage.classList.remove('incorrect');
            feedbackMessage.classList.add('correct');

            // Edit correct answer count
            fetch('/quiz/add_correct', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question_number: 1 })
            }).then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not ok.');
            }).then(data => {
                console.log('Success:', data);
            }).catch(error => {
                console.error('Error:', error);
            });
        } else {
            feedbackMessage.textContent = "Incorrect!";
            feedbackMessage.classList.add('incorrect');
            feedbackMessage.classList.remove('correct');
        }

        nextQuestionButton.style.display = 'block'; // Show the Next Question button
    }
});

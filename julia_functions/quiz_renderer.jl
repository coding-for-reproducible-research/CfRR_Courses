using JSON

function show_quiz_from_json(path)
    quiz_data = JSON.parsefile(path)

    html = """
    <style>
    .quiz-question {
        background-color: #6c63ff;
        color: white;
        padding: 12px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.2em;
        margin-bottom: 10px;
    }

    .quiz-form {
        margin-bottom: 20px;
    }

    .quiz-answer {
        display: block;
        background-color: #f2f2f2;
        border: none;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        font-size: 1em;
        cursor: pointer;
        text-align: left;
        transition: background-color 0.3s;
        width: 100%;
    }

    .quiz-answer:hover {
        background-color: #e0e0e0;
    }

    .correct {
        background-color: #4CAF50 !important;
        color: white !important;
        border: none;
    }

    .incorrect {
        background-color: #D32F2F !important;
        color: white !important;
        border: none;
    }

    .feedback {
        margin-top: 10px;
        font-weight: bold;
        font-size: 1em;
    }
    </style>

    <script>
    function handleAnswer(qid, aid, feedback, isCorrect) {
        let buttons = document.querySelectorAll(".answer-" + qid);
        buttons.forEach(btn => {
            btn.classList.remove('correct', 'incorrect');
        });

        let selected = document.getElementById(aid);
        selected.classList.add(isCorrect ? 'correct' : 'incorrect');

        let feedbackBox = document.getElementById('feedback_' + qid);
        feedbackBox.innerHTML = feedback;
        feedbackBox.style.color = isCorrect ? 'green' : 'red';
    }
    </script>
    """

    for (i, question) in enumerate(quiz_data)
        qid = "$i"
        html *= """<div class="quiz-question">$(question["question"])</div><form class="quiz-form">"""

        for (j, answer) in enumerate(question["answers"])
            aid = "q$(i)_a$(j)"
            feedback = answer["feedback"]
            correct = startswith(lowercase(feedback), "correct")
            html *= """
            <button type="button" class="quiz-answer answer-$qid" id="$aid"
                onclick="handleAnswer('$qid', '$aid', '$feedback', $(correct))">
                $(answer["answer"])
            </button>
            """
        end

        # ✅ Accessibility-compliant submit button (off-screen but reachable)
        html *= """
        <div class="feedback" id="feedback_$qid"></div>
        <button type="submit" style="position:absolute; left:-9999px; width:1px; height:1px; overflow:hidden;">
            Submit
        </button>
        </form><hr>
        """
    end

    display("text/html", html)
end

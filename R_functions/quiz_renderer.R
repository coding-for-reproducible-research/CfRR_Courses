# quiz_renderer.R

# Load required libraries
library(jsonlite)
library(IRdisplay)
library(uuid)  # For generating unique quiz IDs

show_quiz_from_json <- function(path, quiz_id_prefix = NULL) {
  quiz_data <- fromJSON(path, simplifyVector = FALSE)

  # Generate a unique prefix if one isn't supplied
  if (is.null(quiz_id_prefix)) {
    quiz_id_prefix <- paste0("quiz_", UUIDgenerate(use.time = TRUE))
  }

  html <- '
  <style>
  .quiz-question {
      background-color: #392061;
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
      let buttons = document.querySelectorAll("." + qid);
      buttons.forEach(btn => {
          btn.classList.remove("correct", "incorrect");
      });

      let selected = document.getElementById(aid);
      if (selected) {
        selected.classList.add(isCorrect ? "correct" : "incorrect");
      }

      let feedbackBox = document.getElementById("feedback_" + qid);
      if (feedbackBox) {
        feedbackBox.innerHTML = feedback;
        feedbackBox.style.color = isCorrect ? "green" : "red";
      }
  }
  </script>
  '

  for (i in seq_along(quiz_data)) {
    question <- quiz_data[[i]]
    qid <- sprintf("%s_q%s", quiz_id_prefix, i)
    html <- paste0(html, sprintf('<div class="quiz-question">%s</div><form class="quiz-form">', question$question))

    for (j in seq_along(question$answers)) {
      answer <- question$answers[[j]]
      aid <- sprintf("%s_a%s", qid, j)
      feedback <- gsub("'", "\\'", answer$feedback)
      correct <- tolower(substr(answer$feedback, 1, 7)) == "correct"
      correct_js <- tolower(as.character(correct))

      html <- paste0(html, sprintf(
        '<button type="button" class="quiz-answer %s" id="%s"
         onclick="handleAnswer(\'%s\', \'%s\', \'%s\', %s)">
         %s</button>',
        qid, aid, qid, aid, feedback, correct_js, answer$answer
      ))
    }

    html <- paste0(html, sprintf(
      '<div class="feedback" id="feedback_%s"></div>
       <button type="submit" style="position:absolute; left:-9999px; width:1px; height:1px; overflow:hidden;">
         Submit
       </button>
       </form><hr>', qid))
  }

  display_html(html)
}

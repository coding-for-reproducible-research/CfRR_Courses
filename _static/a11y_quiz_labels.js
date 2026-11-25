"use strict";

// Older saved JupyterQuiz output places each radio immediately before its label
// without associating them. Newer output nests the radio inside the label.
(function () {
  function associateAnswer(label) {
    if (!label.closest('.Quiz') || label.control || label.hasAttribute('for')) return;

    const input = label.previousElementSibling;
    if (input && input.matches('input[type="radio"][id^="quizo"]')) {
      label.htmlFor = input.id;
    }
  }

  function labelAnswers(root) {
    if (root.matches && root.matches('label.MCButton')) associateAnswer(root);
    root.querySelectorAll('label.MCButton').forEach(associateAnswer);
  }

  function init() {
    labelAnswers(document);
    // Quiz answers can appear after DOMContentLoaded or be rendered again.
    const observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(function (node) {
          if (node.nodeType === Node.ELEMENT_NODE) labelAnswers(node);
        });
      });
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();

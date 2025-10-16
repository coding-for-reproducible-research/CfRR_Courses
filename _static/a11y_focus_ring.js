"use strict";

(function () {
  function applyFocusRing() {
    var selectors = [
      "button.btn.dropdown-toggle",
      ".sidebar-toggle.btn",
      ".action-button",
      ".header-article-item button",
      ".bd-sidebar button",
      ".bd-header button"
    ];

    document
      .querySelectorAll(selectors.join(","))
      .forEach(function (button) {
        button.classList.add("js-focus-ring-enhanced");
      });

    if (!document.getElementById("cfrr-focus-ring-style")) {
      var style = document.createElement("style");
      style.id = "cfrr-focus-ring-style";
      style.textContent =
        ".js-focus-ring-enhanced:focus-visible {" +
        "outline: 3px solid #005eb8;" +
        "outline-offset: 2px;" +
        "box-shadow: 0 0 0 3px rgba(0, 94, 184, 0.25);" +
        "}" +
        ".js-focus-ring-enhanced:focus {" +
        "outline: 3px solid #005eb8;" +
        "outline-offset: 2px;" +
        "}";
      document.head.appendChild(style);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyFocusRing);
  } else {
    applyFocusRing();
  }
})();

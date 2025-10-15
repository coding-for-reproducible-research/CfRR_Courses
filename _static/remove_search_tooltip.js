"use strict";

(function () {
  function removeSearchTooltip() {
    document
      .querySelectorAll(
        '.search-button__button[data-bs-toggle="tooltip"], .search-button__button[data-bs-original-title]'
      )
      .forEach(function (button) {
        button.removeAttribute('title');
        button.removeAttribute('data-bs-toggle');
        button.removeAttribute('data-bs-placement');
        button.removeAttribute('data-bs-original-title');
      });

    document
      .querySelectorAll('.tooltip, .tooltip-inner, .tooltip-arrow')
      .forEach(function (tooltip) {
        tooltip.remove();
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", removeSearchTooltip);
  } else {
    removeSearchTooltip();
  }
})();

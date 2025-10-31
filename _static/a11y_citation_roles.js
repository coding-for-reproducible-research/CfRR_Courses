"use strict";

/**
 * Sphinx outputs bibliography blocks as <div class="citation" role="doc-biblioentry">,
 * but doc-biblioentry is intended for list items. Drop the role so native semantics apply.
 */
(function () {
  function cleanCitationRoles(root) {
    (root || document)
      .querySelectorAll('.citation[role="doc-biblioentry"]')
      .forEach(function (node) {
        node.removeAttribute("role");
      });
  }

  function initObserver() {
    var observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(function (node) {
          if (!(node instanceof HTMLElement)) return;
          if (node.classList && node.classList.contains("citation")) {
            cleanCitationRoles(node.parentElement || document);
          } else {
            cleanCitationRoles(node);
          }
        });
      });
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  function init() {
    cleanCitationRoles();
    initObserver();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

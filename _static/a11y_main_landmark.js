"use strict";

/**
 * Guarantee there is exactly one main landmark on standalone pages that are
 * rendered outside the book layout (e.g., embedded network visualisations).
 */
(function () {
  function ensureMainLandmark() {
    if (document.querySelector("main, [role='main']")) {
      return;
    }

    var networkContainer = document.querySelector("#mynetwork");
    if (!networkContainer) {
      networkContainer = document.querySelector(".vis-network");
    }

    if (!networkContainer) return;

    var mainWrapper =
      networkContainer.closest("[data-main-landmark], .card, .card-body") ||
      networkContainer.parentElement;

    if (!mainWrapper) return;

    if (mainWrapper.getAttribute("role") === "region") {
      mainWrapper = mainWrapper.parentElement || document.body;
    }

    if (!mainWrapper || mainWrapper.getAttribute("role") === "main") return;

    mainWrapper.setAttribute("role", "main");
    if (!mainWrapper.getAttribute("aria-label")) {
      var label = document.title ? document.title.trim() : "";
      mainWrapper.setAttribute(
        "aria-label",
        label ? label + " content" : "Main content"
      );
    }
  }

  function init() {
    ensureMainLandmark();

    var observer = new MutationObserver(function () {
      ensureMainLandmark();
      if (document.querySelector("main, [role='main']")) {
        observer.disconnect();
      }
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

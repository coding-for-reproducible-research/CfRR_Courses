"use strict";

/**
 * Give dynamically generated vis-network canvases an accessible landmark.
 * The widgets behave like carousels, so we wrap them in ARIA region semantics
 * with meaningful labelling.
 */
(function () {
  function deriveLabel(element) {
    var label;

    var labelledContainer = element.closest("[data-vis-region-label]");
    if (labelledContainer) {
      label = labelledContainer.getAttribute("data-vis-region-label");
      if (label) return label;
    }

    var nearbyHeading = element.closest("section, article, div, main");
    if (nearbyHeading) {
      var heading = nearbyHeading.querySelector("h1, h2, h3, h4, h5, h6");
      if (heading) {
        var headingText = heading.textContent.trim();
        if (headingText.length > 0) {
          return headingText + " interactive network";
        }
      }
    }

    var docTitle = document.title ? document.title.trim() : "";
    if (docTitle.length > 0) {
      return docTitle + " interactive network";
    }

    return "Interactive course network";
  }

  function labelNetworkElement(element) {
    if (!element || element.getAttribute("role") === "region") return;

    element.setAttribute("role", "region");
    if (!element.getAttribute("aria-label")) {
      element.setAttribute("aria-label", deriveLabel(element));
    }

    if (!element.hasAttribute("tabindex")) {
      element.setAttribute("tabindex", "0");
    }
  }

  function labelExistingNetworks() {
    document
      .querySelectorAll(".vis-network")
      .forEach(function (element) {
        labelNetworkElement(element);
      });
  }

  function initObserver() {
    var observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(function (node) {
          if (!(node instanceof HTMLElement)) return;
          if (node.classList.contains("vis-network")) {
            labelNetworkElement(node);
          } else if (node.querySelector) {
            node.querySelectorAll(".vis-network").forEach(labelNetworkElement);
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
    labelExistingNetworks();
    initObserver();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

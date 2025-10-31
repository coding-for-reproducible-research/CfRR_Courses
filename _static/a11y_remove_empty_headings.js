"use strict";

/**
 * Remove empty heading elements generated at runtime so assistive
 * technologies do not encounter blank headings.
 */
(function () {
  /**
   * @param {Element} heading
   * @returns {boolean}
   */
  function isEffectivelyEmpty(heading) {
    if (!heading) return false;
    if (!/^H[1-6]$/.test(heading.tagName)) return false;
    if (heading.childElementCount === 0) {
      return heading.textContent.trim().length === 0;
    }

    // Allow hidden decorative content (aria-hidden) without text.
    var visibleText = "";
    heading.childNodes.forEach(function (node) {
      if (node.nodeType === Node.TEXT_NODE) {
        visibleText += node.textContent;
        return;
      }
      if (
        node.nodeType === Node.ELEMENT_NODE &&
        node.getAttribute("aria-hidden") === "true"
      ) {
        return;
      }
      visibleText += node.textContent || "";
    });

    return visibleText.trim().length === 0;
  }

  function removeEmptyHeadings(root) {
    (root || document)
      .querySelectorAll("h1, h2, h3, h4, h5, h6")
      .forEach(function (heading) {
        if (isEffectivelyEmpty(heading)) {
          heading.remove();
        }
      });
  }

  function initObserver() {
    var observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(function (node) {
          if (!(node instanceof HTMLElement)) return;
          if (/^H[1-6]$/.test(node.tagName)) {
            removeEmptyHeadings(node.parentElement || document);
          } else {
            removeEmptyHeadings(node);
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
    removeEmptyHeadings();
    initObserver();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

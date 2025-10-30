"use strict";

(function () {
  var LABELS = {
    "vis-zoomIn": "Zoom in",
    "vis-zoomOut": "Zoom out",
    "vis-zoomExtends": "Zoom to fit",
    "vis-fit": "Fit to screen",
    "vis-up": "Pan up",
    "vis-down": "Pan down",
    "vis-left": "Pan left",
    "vis-right": "Pan right"
  };

  var enhancedDocuments = typeof WeakSet === "function" ? new WeakSet() : [];

  function hasKeyboardFlag(element) {
    if (!element) {
      return true;
    }

    if (element.dataset && element.dataset.visA11yKeyboard === "true") {
      return true;
    }

    return element.getAttribute("data-vis-a11y-keyboard") === "true";
  }

  function setKeyboardFlag(element) {
    if (!element) {
      return;
    }

    if (element.dataset) {
      element.dataset.visA11yKeyboard = "true";
    } else {
      element.setAttribute("data-vis-a11y-keyboard", "true");
    }
  }

  function ensureKeyboardSupport(button) {
    if (!button || hasKeyboardFlag(button)) {
      return;
    }

    var handleKeyDown = function (event) {
      var key = event.key || event.code;

      if (key === "Enter") {
        event.preventDefault();
        button.click();
      } else if (key === " " || key === "Spacebar" || key === "Space") {
        event.preventDefault();
      }
    };

    var handleKeyUp = function (event) {
      var key = event.key || event.code;

      if (key === " " || key === "Spacebar" || key === "Space") {
        event.preventDefault();
        button.click();
      }
    };

    button.addEventListener("keydown", handleKeyDown);
    button.addEventListener("keyup", handleKeyUp);
    setKeyboardFlag(button);
  }

  function hasDocumentBeenEnhanced(doc) {
    if (!doc) {
      return true;
    }

    if (enhancedDocuments instanceof WeakSet) {
      return enhancedDocuments.has(doc);
    }

    return enhancedDocuments.indexOf(doc) !== -1;
  }

  function markDocumentEnhanced(doc) {
    if (!doc) {
      return;
    }

    if (enhancedDocuments instanceof WeakSet) {
      enhancedDocuments.add(doc);
    } else if (enhancedDocuments.indexOf(doc) === -1) {
      enhancedDocuments.push(doc);
    }
  }

  function labelButton(button) {
    if (!button || !button.classList) {
      return;
    }

    var label = null;

    Object.keys(LABELS).some(function (className) {
      if (button.classList.contains(className)) {
        label = LABELS[className];
        return true;
      }
      return false;
    });

    if (!label) {
      return;
    }

    button.setAttribute("role", "button");
    if (!button.hasAttribute("tabindex")) {
      button.setAttribute("tabindex", "0");
    }

    var currentLabel = button.getAttribute("aria-label");
    if (!currentLabel || currentLabel.trim() === "") {
      button.setAttribute("aria-label", label);
    }

    if (!button.hasAttribute("title")) {
      button.setAttribute("title", label);
    }

    ensureKeyboardSupport(button);
  }

  function collectButtons(root) {
    if (!root) {
      return [];
    }

    if (root.querySelectorAll) {
      return root.querySelectorAll(".vis-button");
    }

    if (root.classList && root.classList.contains("vis-button")) {
      return [root];
    }

    return [];
  }

  function applyLabels(root) {
    var scope = root || document;
    var buttons = collectButtons(scope);

    if (!buttons.length) {
      return;
    }

    Array.prototype.forEach.call(buttons, function (button) {
      labelButton(button);
    });
  }

  function enhanceDocument(doc) {
    if (!doc || hasDocumentBeenEnhanced(doc)) {
      return;
    }

    markDocumentEnhanced(doc);
    applyLabels(doc);

    var target = doc.body || doc;

    if (!target) {
      return;
    }

    var handleIframe = function (iframe) {
      if (!iframe || iframe.dataset.visA11yHandled === "true") {
        return;
      }

      var warnedCrossOrigin = false;

      var attemptEnhancement = function () {
        try {
          var iframeDoc =
            iframe.contentDocument ||
            (iframe.contentWindow && iframe.contentWindow.document);

          if (!iframeDoc || !iframeDoc.body) {
            return false;
          }

          enhanceDocument(iframeDoc);
          enhanceIframes(iframeDoc);
          return true;
        } catch (error) {
          if (!warnedCrossOrigin) {
            warnedCrossOrigin = true;
            if (typeof console !== "undefined" && console.warn) {
              console.warn(
                "[vis-button-a11y] Unable to enhance iframe buttons because the iframe content is from a different origin.",
                iframe
              );
            }
          }
          return false;
        }
      };

      var onLoad = function () {
        if (attemptEnhancement()) {
          iframe.removeEventListener("load", onLoad);
        }
      };

      iframe.addEventListener("load", onLoad);
      iframe.dataset.visA11yHandled = "true";

      // If the iframe content is already loaded we enhance immediately.
      if (attemptEnhancement()) {
        iframe.removeEventListener("load", onLoad);
      }
    };

    function enhanceIframes(scope) {
      if (!scope || !scope.querySelectorAll) {
        return;
      }

      Array.prototype.forEach.call(
        scope.querySelectorAll("iframe"),
        handleIframe
      );
    }

    enhanceIframes(doc);

    if (typeof MutationObserver !== "undefined") {
      var observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
          mutation.addedNodes.forEach(function (node) {
            var isElement = node instanceof Element;
            var isFragment = node && node.nodeType === 11;

            if (!isElement && !isFragment) {
              return;
            }

            if (
              isElement &&
              node.classList &&
              node.classList.contains("vis-button")
            ) {
              labelButton(node);
              return;
            }

            if (isElement && node.tagName && node.tagName.toLowerCase() === "iframe") {
              handleIframe(node);
              return;
            }

            applyLabels(node);
            enhanceIframes(node);
          });
        });
      });

      observer.observe(target, {
        childList: true,
        subtree: true
      });
    } else {
      setInterval(function () {
        applyLabels(doc);
        enhanceIframes(doc);
      }, 1000);
    }
  }

  function init() {
    enhanceDocument(document);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

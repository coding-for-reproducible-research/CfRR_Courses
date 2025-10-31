"use strict";

/**
 * Promote Sphinx bibliography markup to native list semantics.
 * Converts div.citation-list containers into <ol> elements and child
 * div.citation nodes into <li> entries, dropping deprecated doc-biblioentry roles.
 */
(function () {
  function copyAttributes(from, to) {
    if (!from || !to) return;
    Array.from(from.attributes).forEach(function (attr) {
      if (attr.name === "role") return;
      to.setAttribute(attr.name, attr.value);
    });
  }

  function convertCitationItem(node, targetList) {
    if (!(node instanceof HTMLElement)) return null;
    var li = document.createElement("li");
    copyAttributes(node, li);
    li.classList.add("citation");

    while (node.firstChild) {
      li.appendChild(node.firstChild);
    }

    if (node.parentNode) {
      node.parentNode.removeChild(node);
    }

    if (targetList) {
      targetList.appendChild(li);
    }

    return li;
  }

  function convertCitationList(listNode) {
    if (!(listNode instanceof HTMLElement)) return;
    if (listNode.dataset && listNode.dataset.citationConvertedList) return;

    var isListElement = listNode.tagName === "OL" || listNode.tagName === "UL";
    var targetList = listNode;

    if (!isListElement) {
      targetList = document.createElement("ol");
      copyAttributes(listNode, targetList);
      targetList.dataset.citationConvertedList = "true";
    } else {
      targetList.dataset.citationConvertedList = "true";
      targetList.classList.add("citation-list");
    }

    var processChild = function (child) {
      if (child instanceof HTMLElement && child.classList.contains("citation")) {
        convertCitationItem(child, targetList);
      } else if (child.nodeType === Node.TEXT_NODE && !child.textContent.trim()) {
        child.parentNode && child.parentNode.removeChild(child);
      } else if (targetList !== child.parentNode) {
        targetList.appendChild(child);
      }
    };

    if (!isListElement) {
      while (listNode.firstChild) {
        processChild(listNode.firstChild);
      }

      if (listNode.parentNode) {
        listNode.parentNode.replaceChild(targetList, listNode);
      }
    } else {
      Array.from(Array.from(targetList.children)).forEach(function (child) {
        if (child instanceof HTMLElement && child.classList.contains("citation")) {
          convertCitationItem(child, targetList);
        }
      });
    }
  }

  function upgradeBibliography(root) {
    (root || document)
      .querySelectorAll(".citation-list, [role='list'].citation-list")
      .forEach(function (list) {
        convertCitationList(list);
      });

    (root || document)
      .querySelectorAll(".citation[role='doc-biblioentry']")
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
            upgradeBibliography(node.parentElement || document);
          } else {
            upgradeBibliography(node);
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
    upgradeBibliography();
    initObserver();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

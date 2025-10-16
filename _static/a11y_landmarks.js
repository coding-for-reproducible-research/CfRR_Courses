"use strict";

(function () {
  function enhanceLandmarks() {
    var primarySidebar = document.querySelector(
      ".bd-sidebar-primary .sidebar-primary-items__start"
    );
    if (primarySidebar && primarySidebar.getAttribute("role") !== "banner") {
      primarySidebar.setAttribute("role", "banner");
      if (!primarySidebar.getAttribute("aria-label")) {
        primarySidebar.setAttribute("aria-label", "Site header");
      }
    }

    var searchContainer = document.querySelector(
      ".bd-sidebar-primary .sidebar-primary-item .search-button__button"
    );
    if (searchContainer) {
      var region = searchContainer.closest(".sidebar-primary-item");
      if (region && region.getAttribute("role") !== "search") {
        region.setAttribute("role", "search");
        if (!region.getAttribute("aria-label")) {
          region.setAttribute("aria-label", "Site search");
        }
      }
    }

    var complementaryNav = document.querySelector(".bd-sidebar-primary");
    if (complementaryNav && complementaryNav.getAttribute("role") !== "complementary") {
      complementaryNav.setAttribute("role", "complementary");
      if (!complementaryNav.getAttribute("aria-label")) {
        complementaryNav.setAttribute("aria-label", "Primary navigation");
      }
    }

    return Boolean(primarySidebar || searchContainer || complementaryNav);
  }

  function initLandmarks() {
    if (enhanceLandmarks()) return;

    var observer = new MutationObserver(function () {
      if (enhanceLandmarks()) {
        observer.disconnect();
      }
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initLandmarks);
  } else {
    initLandmarks();
  }
})();

"use strict";

(function () {
  function enhanceLandmarks() {
    var siteHeader = document.querySelector(".bd-header");
    if (siteHeader && siteHeader.getAttribute("role") !== "banner") {
      siteHeader.setAttribute("role", "banner");
      if (!siteHeader.getAttribute("aria-label")) {
        siteHeader.setAttribute("aria-label", "Site header");
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

    var sidebarBanner = document.querySelector(
      ".bd-sidebar-primary .sidebar-primary-items__start[role='banner']"
    );
    if (sidebarBanner) {
      sidebarBanner.removeAttribute("role");
      if (sidebarBanner.getAttribute("aria-label") === "Site header") {
        sidebarBanner.removeAttribute("aria-label");
      }
    }

    return Boolean(siteHeader || searchContainer || complementaryNav);
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

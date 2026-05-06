"use strict";

(function () {
  function updateLogoAlt() {
    document
      .querySelectorAll('img.logo__image')
      .forEach(function (img) {
        img.setAttribute('alt', 'University of Exeter Logo Home');
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", updateLogoAlt);
  } else {
    updateLogoAlt();
  }
})();

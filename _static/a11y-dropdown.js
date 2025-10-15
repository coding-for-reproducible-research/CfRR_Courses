"use strict";

/**
 * Make Sphinx/Jupyter Book toctree dropdowns expose their expanded state.
 * Keeps aria-expanded in sync and hides collapsed submenus so screen readers
 * and keyboard users get consistent feedback.
 */
(function () {
  /**
   * @param {HTMLElement} li
   * @returns {HTMLElement|null}
   */
  function findToggle(li) {
    const detailsToggle = li.querySelector(':scope > details > summary');
    if (detailsToggle) return detailsToggle;

    return li.querySelector(
      ':scope > .toctree-expand, :scope > button, :scope > .toctree-toggle, :scope > a'
    );
  }

  /**
   * @param {HTMLElement} li
   * @param {boolean} expanded
   */
  function setAria(li, expanded) {
    const toggle = findToggle(li);
    if (!toggle) return;

    toggle.setAttribute('aria-haspopup', 'menu');
    toggle.setAttribute('aria-expanded', String(expanded));

    const submenu =
      li.querySelector(':scope > details > ul') ||
      li.querySelector(':scope > ul');
    if (submenu) submenu.hidden = !expanded;

    const details = li.querySelector(':scope > details');
    if (details) details.open = expanded;
  }

  /**
   * @param {HTMLElement} li
   * @returns {boolean}
   */
  function isInitiallyOpen(li) {
    return (
      li.classList.contains('current') ||
      li.classList.contains('open') ||
      li.classList.contains('active')
    );
  }

  document.addEventListener('DOMContentLoaded', function () {
    document
      .querySelectorAll('li[class*="toctree-"].has-children')
      .forEach(function (li) {
        const details = li.querySelector(':scope > details');
        const toggle = findToggle(li);
        const submenu =
          li.querySelector(':scope > details > ul') ||
          li.querySelector(':scope > ul');

        const initialExpanded = details
          ? details.hasAttribute('open')
          : isInitiallyOpen(li);

        // Establish the initial state based on theme-provided classes or attributes.
        setAria(li, initialExpanded);

        if (details && toggle) {
          // Sync aria-expanded/hidden whenever the native <details> toggles.
          details.addEventListener('toggle', function () {
            const expanded = details.open;
            toggle.setAttribute('aria-expanded', String(expanded));
            if (submenu) submenu.hidden = !expanded;
          });

          // No further handler needed because <details>/<summary> manage toggling.
          return;
        }

        if (!toggle) return;

        toggle.addEventListener('click', function (event) {
          const isLink = toggle.tagName === 'A';
          const href = isLink ? toggle.getAttribute('href') : '';

          // Allow links with a real destination to continue navigation.
          if (isLink && href && href !== '#') return;

          const expanded = toggle.getAttribute('aria-expanded') === 'true';
          setAria(li, !expanded);
          event.preventDefault();
        });
      });
  });
})();

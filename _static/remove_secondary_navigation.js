(() => {
  const removeSecondaryNavigation = () => {
    const selectorsToRemove = [
      '.bd-sidebar-secondary',
      '.overlay-secondary',
      'label[for="__secondary"]'
    ];

    selectorsToRemove.forEach((selector) => {
      document.querySelectorAll(selector).forEach((element) => element.remove());
    });

    document.querySelectorAll('.sidebar-toggle[name="__secondary"]').forEach((element) => element.remove());

    if (document.body) {
      document.body.removeAttribute('data-bs-target');
      document.body.removeAttribute('data-bs-spy');
    }

    if (!document.getElementById('cfrr-remove-secondary-nav-style')) {
      const style = document.createElement('style');
      style.id = 'cfrr-remove-secondary-nav-style';
      style.textContent = `
        html {
          --pst-sidebar-secondary: 0 !important;
        }
      `;
      if (document.head) {
        document.head.appendChild(style);
      }
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', removeSecondaryNavigation);
  } else {
    removeSecondaryNavigation();
  }
})();

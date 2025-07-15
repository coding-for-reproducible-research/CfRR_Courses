function fixAccessibility() {
  // Fix overlay <label> elements by replacing them with <div>
  document.querySelectorAll('label.overlay').forEach(function(label) {
    var div = document.createElement('div');
    div.className = label.className;
    for (var i = 0; i < label.attributes.length; i++) {
      var attr = label.attributes[i];
      if (attr.name !== 'for') div.setAttribute(attr.name, attr.value);
    }
    div.setAttribute('aria-hidden', 'true');
    div.innerHTML = label.innerHTML;
    label.parentNode.replaceChild(div, label);
  });

  // For each sidebar checkbox, add an aria-label if missing
  [
    { selector: 'input.sidebar-toggle#\\__primary', label: 'Toggle primary sidebar' },
    { selector: 'input.sidebar-toggle#\\__secondary', label: 'Toggle secondary sidebar' }
  ].forEach(function(cfg) {
    document.querySelectorAll(cfg.selector).forEach(function(input) {
      if (!input.hasAttribute('aria-label')) {
        input.setAttribute('aria-label', cfg.label);
      }
    });
  });

  // Inject CSS for .sr-only (optional, in case you use it elsewhere)
  if (!document.getElementById('sr-only-style')) {
    var style = document.createElement('style');
    style.id = 'sr-only-style';
    style.innerHTML = `
.sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0,0,0,0) !important;
  border: 0 !important;
  white-space: nowrap !important;
}
`;
    document.head.appendChild(style);
  }
}

// Run once at DOMContentLoaded (for static content)
document.addEventListener('DOMContentLoaded', fixAccessibility);

// Also run when new nodes are added (for dynamic content)
const observer = new MutationObserver(function(mutationsList, observer) {
  fixAccessibility();
});
observer.observe(document.body, { childList: true, subtree: true });

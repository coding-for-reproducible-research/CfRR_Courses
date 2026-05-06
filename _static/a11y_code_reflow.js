(()=>{
  const wrapClass = 'a11y-soft-wrap';
  const selectors = [
    '.highlight pre',
    'pre.literal-block',
    'div.nbinput pre',
    'div.nboutput pre'
  ];

  const injectStyles = () => {
    if (document.getElementById('a11y-soft-wrap-style')) {
      return;
    }
    const style = document.createElement('style');
    style.id = 'a11y-soft-wrap-style';
    style.textContent = `
      .${wrapClass} {
        white-space: pre-wrap !important;
        overflow-wrap: anywhere;
        word-break: break-word;
      }
      .${wrapClass} code {
        white-space: inherit !important;
      }
    `;
    document.head.append(style);
  };

  const getTargets = () => document.querySelectorAll(selectors.join(', '));

  const applyWrap = (shouldWrap) => {
    getTargets().forEach((pre) => {
      if (shouldWrap) {
        pre.classList.add(wrapClass);
      } else {
        pre.classList.remove(wrapClass);
      }
    });
  };

  const setup = () => {
    injectStyles();
    const mediaQuery = window.matchMedia('(max-width: 40rem)');
    const update = (e) => applyWrap(e.matches);
    update(mediaQuery);
    if (typeof mediaQuery.addEventListener === 'function') {
      mediaQuery.addEventListener('change', update);
    } else if (typeof mediaQuery.addListener === 'function') {
      mediaQuery.addListener(update);
    }
    window.addEventListener('resize', () => applyWrap(mediaQuery.matches), { passive: true });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setup, { once: true });
  } else {
    setup();
  }
})();

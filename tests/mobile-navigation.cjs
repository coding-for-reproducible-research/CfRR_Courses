const assert = require('node:assert/strict');
const puppeteer = require('puppeteer');

// Run against a served Jupyter Book build, or pass its homepage URL as an argument.
const url = process.argv[2] || 'http://localhost:8000/home_page.html';
const toggle = '.header-article-item .primary-toggle';
const dialog = '#pst-primary-sidebar-modal';

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  try {
    const page = await browser.newPage();
    const waitForToggle = () => page.waitForFunction(selector => {
      const button = document.querySelector(selector);
      const rect = button.getBoundingClientRect();
      return button.contains(document.elementFromPoint(
        rect.x + rect.width / 2, rect.y + rect.height / 2));
    }, {}, toggle);
    for (const width of [375, 768]) {
      await page.setViewport({ width, height: 900, isMobile: true, hasTouch: true });
      await page.goto(url, { waitUntil: 'networkidle0' });
      assert.equal(await page.$$eval('.primary-toggle', nodes => nodes.length), 1,
        'Only the visible article header should provide a primary menu toggle');

      await page.tap(toggle);
      await page.waitForSelector(`${dialog}[open]`);
      const link = `${dialog} .bd-links li:not(.current) > a.reference.internal[href]`;
      await page.waitForSelector(link, { visible: true });

      await page.keyboard.press('Escape');
      await page.waitForSelector(`${dialog}:not([open])`);
      await page.waitForSelector('#pst-primary-sidebar .bd-links');
      await waitForToggle(); // Wait for the closing sidebar animation to clear the button.

      // Keyboard users must also be able to open and dismiss the menu.
      await page.focus(toggle);
      await page.keyboard.press('Enter');
      await page.waitForSelector(`${dialog}[open]`);
      await page.touchscreen.tap(width - 5, 450);
      await page.waitForSelector(`${dialog}:not([open])`);
      await page.waitForSelector('#pst-primary-sidebar .bd-links');
      await waitForToggle();

      await page.tap(toggle);
      await page.waitForSelector(link, { visible: true });
      const destination = await page.$eval(link, node => node.href);
      assert.notEqual(destination, page.url(), 'Choose a different page to test navigation');
      await Promise.all([
        page.waitForNavigation({ waitUntil: 'networkidle0' }),
        page.click(link),
      ]);
      assert.equal(page.url(), destination, 'A primary navigation link must navigate');
      console.log(`PASS: touch, keyboard, Escape, backdrop and navigation at ${width}px`);
    }

    await page.setViewport({ width: 1280, height: 900, isMobile: false, hasTouch: false });
    await page.goto(url, { waitUntil: 'networkidle0' });
    await page.click(toggle);
    assert.equal(await page.$eval(dialog, node => node.open), false,
      'Desktop toggling must not open a mobile dialog');
    assert.equal(await page.$eval('#pst-primary-sidebar', node =>
      node.classList.contains('pst-sidebar-hidden')), true);
    await page.click(toggle);
    assert.equal(await page.$eval('#pst-primary-sidebar', node =>
      node.classList.contains('pst-sidebar-hidden')), false);
    console.log('PASS: desktop sidebar collapses and reopens');
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});

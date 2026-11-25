const assert = require('node:assert/strict');
const puppeteer = require('puppeteer');

const url = process.argv[2] ||
  'http://localhost:8000/individual_modules/introduction_to_python/functions.html';

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });
    await page.waitForSelector('.Quiz input[type="radio"]');
    const answers = await page.$$eval('.Quiz input[type="radio"]', inputs =>
      inputs.map(input => ({
        labels: input.labels.length,
        text: input.labels[0]?.textContent.trim(),
      })));
    assert.equal(answers.length, 12, 'All three questions should render four answers');
    assert(answers.every(answer => answer.labels === 1 && answer.text),
      'Every radio must have an associated answer label with text');

    // Associating labels must preserve the quiz's existing feedback handlers.
    const questions = await page.$$('.Quiz');
    for (const question of questions) {
      const correct = await question.$('label.MCButton[data-correct="true"]');
      await correct.click();
      assert(await question.$('.Feedback.correct'), 'Correct answers should show feedback');
    }

    // Test late-rendered legacy answers and preserve modern implicit/explicit labels.
    await page.evaluate(() => {
      const quiz = document.createElement('div');
      quiz.className = 'Quiz';
      quiz.id = 'quiz-label-test';
      quiz.innerHTML = `
        <input type="radio" id="quizo-late">
        <label class="MCButton"><input type="radio" id="quizo-modern">Modern answer</label>
        <label class="MCButton" for="quizo-explicit">Existing answer</label>
        <input type="radio" id="quizo-explicit">
      `;
      document.body.appendChild(quiz);
    });
    await page.evaluate(() => {
      const answer = document.createElement('label');
      answer.className = 'MCButton';
      answer.textContent = 'Late answer';
      document.querySelector('#quizo-late').after(answer);
    });
    await page.waitForFunction(() => document.querySelector('#quizo-late').labels.length === 1);
    assert.deepEqual(await page.evaluate(() => {
      const modern = document.querySelector('#quizo-modern');
      const explicit = document.querySelector('#quizo-explicit');
      return {
        late: document.querySelector('#quizo-late').labels[0].textContent,
        modernLabelUnchanged: !modern.parentElement.hasAttribute('for'),
        modernLabels: modern.labels.length,
        explicitFor: explicit.labels[0].htmlFor,
      };
    }), {
      late: 'Late answer', modernLabelUnchanged: true, modernLabels: 1,
      explicitFor: 'quizo-explicit',
    });
    console.log('PASS: all 12 answers are labelled and correct-answer feedback works.');
    console.log('PASS: late-rendered answers are labelled; existing labels are preserved.');
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error);
  process.exitCode = 1;
});

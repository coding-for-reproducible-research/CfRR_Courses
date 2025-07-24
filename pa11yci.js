const fs = require('fs');
const path = require('path');

// Get current working directory to prefix file paths
const base = process.env.PA11Y_BASE_DIR || process.cwd();

module.exports = {
  defaults: {
    chromeLaunchConfig: {
      args: ['--no-sandbox']
    }
  },
  urls: JSON.parse(fs.readFileSync('pa11y_targets.json', 'utf-8'))
    .map(rel => 'file://' + path.join(base, rel))
};

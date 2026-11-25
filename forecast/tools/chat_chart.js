// Screenshot of the forecast page's "Cumulative probability" chart, for posting in the daily chat report.
//   node forecast/tools/chat_chart.js <out.png> [port]
// Serve the repo root first:  python3 -m http.server <port> --directory <repo root>
// Reads the page as built by tools/build_page.py; changes nothing.
const { chromium } = require('playwright');
(async () => {
  const out = process.argv[2] || 'prob.png', port = process.argv[3] || '8080';
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 2, colorScheme: 'light' });
  const errs = []; pg.on('pageerror', e => errs.push(String(e)));
  await pg.goto('http://localhost:' + port + '/release-forecast.html', { waitUntil: 'networkidle' });
  // Clip from the chart's own heading to the end of its legend.
  const clip = await pg.evaluate(() => {
    const c = document.getElementById('cdf-chart'); if (!c) return null;
    let head = c.previousElementSibling; while (head && !/^H[2-4]$/.test(head.tagName)) head = head.previousElementSibling;
    let legend = c.nextElementSibling;
    const card = c.closest('section') || c.parentElement;
    const top = (head || c).getBoundingClientRect().top + scrollY - 16;
    const bottom = ((legend || c).getBoundingClientRect().bottom) + scrollY + 20;
    const r = card.getBoundingClientRect();
    return { x: r.left + scrollX, y: top, width: r.width, height: bottom - top };
  });
  if (!clip) { console.error('cdf-chart not found'); process.exit(1); }
  await pg.screenshot({ path: out, clip, fullPage: true });
  console.log('wrote', out, 'page errors', errs.length);
  await b.close();
})();

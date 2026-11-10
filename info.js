/* Disclosures shared by all four pages.
   (i) button: sits at the end of a heading and reveals the explanation below it.
     <h2>Title&nbsp;<button type="button" class="info-btn" aria-expanded="false"
         aria-controls="info-x" aria-label="About Title"><span aria-hidden="true">i</span></button></h2>
     <div class="info-panel" id="info-x" hidden="until-found">…</div>
   Text-labelled button: folds away a secondary block (a table, a registry, a log).
     <button type="button" class="more-btn" aria-expanded="false" aria-controls="more-x">Evidence on file</button>
     <div class="more-panel" id="more-x" hidden="until-found">…</div>
   See DESIGN.md, "Info disclosure". Delegated, so it also covers markup a page renders later.
   Nothing is remembered between visits. */
(function () {
  'use strict';
  var BTN = '.info-btn, .more-btn', PANEL = '.info-panel, .more-panel';
  function set(btn, open) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) panel.removeAttribute('hidden');
    else panel.setAttribute('hidden', 'until-found');
  }
  function buttonFor(panel) {
    return panel && panel.id ? document.querySelector('[aria-controls="' + panel.id + '"]') : null;
  }
  // Every panel that encloses el, innermost first (a panel can sit inside a folded block).
  function enclosing(el, each) {
    for (var p = el && el.closest ? el.closest(PANEL) : null; p; p = p.parentElement && p.parentElement.closest(PANEL)) each(p);
  }
  // A link to a heading with an (i) opens its panel; a link to something inside closed panels opens them.
  function reveal(id) {
    var target = id && document.getElementById(id);
    if (!target) return;
    enclosing(target, function (p) { var b = buttonFor(p); if (b) set(b, true); });
    var own = /^H[1-6]$/.test(target.tagName) && target.querySelector(BTN);
    if (own) set(own, true);
  }
  document.addEventListener('click', function (e) {
    if (!e.target.closest) return;
    var btn = e.target.closest(BTN);
    if (btn) { set(btn, btn.getAttribute('aria-expanded') !== 'true'); return; }
    var link = e.target.closest('a[href^="#"]');
    if (link) reveal(decodeURIComponent(link.getAttribute('href').slice(1)));
  });
  // Find-in-page reveals hidden="until-found" panels by itself; keep the buttons in step.
  document.addEventListener('beforematch', function (e) {
    enclosing(e.target, function (p) { var b = buttonFor(p); if (b) b.setAttribute('aria-expanded', 'true'); });
  });
  function fromHash() {
    var id = decodeURIComponent(location.hash.slice(1)), target = id && document.getElementById(id);
    reveal(id);
    // the browser scrolled before the panels opened, so a target inside one needs a second go
    if (target && target.closest(PANEL)) target.scrollIntoView();
  }
  window.addEventListener('hashchange', fromHash);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fromHash);
  else fromHash();
})();

/* Info disclosures: the (i) button at the end of a heading reveals the explanation below it.
   Markup (see DESIGN.md, "Info disclosure"):
     <h2>Title&nbsp;<button type="button" class="info-btn" aria-expanded="false"
         aria-controls="info-x" aria-label="About Title"><span aria-hidden="true">i</span></button></h2>
     <div class="info-panel" id="info-x" hidden="until-found">…</div>
   Delegated, so it also covers headings a page renders later. Nothing is remembered between visits. */
(function () {
  'use strict';
  function panelOf(btn) { return document.getElementById(btn.getAttribute('aria-controls')); }
  function set(btn, open) {
    var panel = panelOf(btn);
    if (!panel) return;
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) panel.removeAttribute('hidden');
    else panel.setAttribute('hidden', 'until-found');
  }
  function buttonFor(panel) {
    return panel && panel.id ? document.querySelector('.info-btn[aria-controls="' + panel.id + '"]') : null;
  }
  // A link to a heading with an (i), or to something inside a closed panel, opens that panel.
  function reveal(id) {
    var target = id && document.getElementById(id);
    if (!target) return;
    var btn = (target.querySelector && target.querySelector('.info-btn')) || buttonFor(target.closest('.info-panel'));
    if (btn) set(btn, true);
  }
  document.addEventListener('click', function (e) {
    if (!e.target.closest) return;
    var btn = e.target.closest('.info-btn');
    if (btn) { set(btn, btn.getAttribute('aria-expanded') !== 'true'); return; }
    var link = e.target.closest('a[href^="#"]');
    if (link) reveal(decodeURIComponent(link.getAttribute('href').slice(1)));
  });
  // Find-in-page reveals a hidden="until-found" panel by itself; keep the button in step.
  document.addEventListener('beforematch', function (e) {
    var btn = buttonFor(e.target.closest ? e.target.closest('.info-panel') : null);
    if (btn) btn.setAttribute('aria-expanded', 'true');
  });
  function fromHash() { reveal(decodeURIComponent(location.hash.slice(1))); }
  window.addEventListener('hashchange', fromHash);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fromHash);
  else fromHash();
})();

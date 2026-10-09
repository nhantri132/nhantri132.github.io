/* Video facades: load the YouTube player only after a click. */
document.querySelectorAll('.video[data-yt]').forEach(function (box) {
  var btn = box.querySelector('button');
  btn.addEventListener('click', function () {
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + box.dataset.yt + '?autoplay=1&rel=0';
    f.title = box.dataset.title;
    f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    f.allowFullscreen = true;
    box.replaceChildren(f);
  });
});

/* Hero: a five-state enemy. patrol -> chase -> windup (telegraph) -> strike -> recover. */
(function () {
  var cv = document.getElementById('arena');
  if (!cv) return;
  var ctx = cv.getContext('2d'), W = cv.width, H = cv.height;
  var list = document.querySelectorAll('#states li');
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var css = function (n) { return getComputedStyle(document.documentElement).getPropertyValue(n).trim(); };

  var player = { x: W * 0.75, y: H * 0.5 };
  var e = { x: W * 0.3, y: H * 0.5, a: 0, state: 'patrol', t: 0, tx: W * 0.3, ty: H * 0.3, dx: 0, dy: 0 };
  var SIGHT = 190, ATTACK = 78, WIND = 0.8, STRIKE = 0.22, RECOVER = 1.1;

  function set(s) {
    e.state = s; e.t = 0;
    list.forEach(function (li) { li.classList.toggle('on', li.dataset.s === s); });
  }
  function pt(ev) {
    var r = cv.getBoundingClientRect();
    player.x = (ev.clientX - r.left) * W / r.width;
    player.y = (ev.clientY - r.top) * H / r.height;
  }
  cv.addEventListener('pointermove', pt);
  cv.addEventListener('pointerdown', pt);

  function step(dt) {
    var dx = player.x - e.x, dy = player.y - e.y, d = Math.hypot(dx, dy);
    e.t += dt;
    if (e.state === 'patrol') {
      var px = e.tx - e.x, py = e.ty - e.y, pd = Math.hypot(px, py);
      if (pd < 8) { e.tx = 60 + Math.random() * (W - 120); e.ty = 60 + Math.random() * (H - 120); }
      else { e.x += px / pd * 55 * dt; e.y += py / pd * 55 * dt; e.a = Math.atan2(py, px); }
      if (d < SIGHT) set('chase');
    } else if (e.state === 'chase') {
      e.a = Math.atan2(dy, dx);
      e.x += Math.cos(e.a) * 120 * dt; e.y += Math.sin(e.a) * 120 * dt;
      if (d < ATTACK) set('windup');
      else if (d > SIGHT * 1.4) set('patrol');
    } else if (e.state === 'windup') {
      e.a = Math.atan2(dy, dx);           /* tracks the player until the strike commits */
      if (e.t > WIND) { e.dx = Math.cos(e.a); e.dy = Math.sin(e.a); set('strike'); }
    } else if (e.state === 'strike') {
      e.x += e.dx * 520 * dt; e.y += e.dy * 520 * dt;
      if (e.t > STRIKE) set('recover');
    } else if (e.state === 'recover') {
      if (e.t > RECOVER) set(d < SIGHT ? 'chase' : 'patrol');
    }
    e.x = Math.max(20, Math.min(W - 20, e.x)); e.y = Math.max(20, Math.min(H - 20, e.y));
  }

  function draw() {
    var ink = css('--ink'), tell = css('--tell'), blue = css('--blue');
    ctx.clearRect(0, 0, W, H);
    /* sight range */
    ctx.setLineDash([6, 6]); ctx.strokeStyle = ink; ctx.globalAlpha = 0.3; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.arc(e.x, e.y, SIGHT, 0, 7); ctx.stroke(); ctx.setLineDash([]); ctx.globalAlpha = 1;
    /* telegraph: a cone that fills as the hit gets closer */
    if (e.state === 'windup' || e.state === 'strike') {
      var p = e.state === 'windup' ? e.t / WIND : 1;
      ctx.fillStyle = tell; ctx.globalAlpha = 0.12 + 0.3 * p;
      ctx.beginPath(); ctx.moveTo(e.x, e.y); ctx.arc(e.x, e.y, ATTACK + 70, e.a - 0.45, e.a + 0.45); ctx.closePath(); ctx.fill();
      ctx.globalAlpha = 1; ctx.strokeStyle = tell; ctx.lineWidth = 2; ctx.stroke();
    }
    /* enemy body */
    ctx.save(); ctx.translate(e.x, e.y); ctx.rotate(e.a);
    var open = e.state === 'recover';
    ctx.fillStyle = open ? 'transparent' : ink; ctx.strokeStyle = open ? tell : ink; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(22, 0); ctx.lineTo(-14, 16); ctx.lineTo(-8, 0); ctx.lineTo(-14, -16); ctx.closePath();
    ctx.fill(); ctx.stroke(); ctx.restore();
    if (open) { ctx.fillStyle = tell; ctx.font = '600 14px "Bricolage Grotesque",sans-serif'; ctx.textAlign = 'center'; ctx.fillText('open', e.x, e.y - 28); }
    /* player */
    ctx.fillStyle = blue; ctx.beginPath(); ctx.arc(player.x, player.y, 9, 0, 7); ctx.fill();
  }

  var last = performance.now(), running = true;
  function loop(now) {
    var dt = Math.min(0.05, (now - last) / 1000); last = now;
    if (running) { step(dt); draw(); }
    requestAnimationFrame(loop);
  }
  new IntersectionObserver(function (en) { running = en[0].isIntersecting; }).observe(cv);

  set('patrol');
  if (reduce) {            /* no autoplay motion: show a still telegraph frame; the pointer still works */
    e.a = 0.2; set('windup'); e.t = WIND * 0.7; draw();
    cv.addEventListener('pointermove', function () { step(0.016); draw(); });
  } else { requestAnimationFrame(loop); }
})();

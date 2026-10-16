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

/* Frame data demo: a training-mode view of a stick figure punching a dummy. */
(function () {
  var cv = document.getElementById('fd');
  if (!cv) return;
  var ctx = cv.getContext('2d'), W = 500, H = 250, GROUND = 228, PELVIS_Y = GROUND - 95; /* logical units; draw() scales them to the canvas */
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var css = function (n) { return getComputedStyle(document.documentElement).getPropertyValue(n).trim(); };

  /* Illustrative moves. Advantage is computed: stun minus the frames left after the first active frame. */
  var MOVES = {
    jab:   { dmg: 30, st: 8,  ac: 3, re: 12, hitstun: 16, blockstun: 11, wind: 0.8, reach: 1.0, hitLen: 38 },
    heavy: { dmg: 90, st: 20, ac: 4, re: 28, hitstun: 26, blockstun: 18, wind: 1.5, reach: 1.25, hitLen: 52 }
  };
  Object.keys(MOVES).forEach(function (k) {
    var m = MOVES[k], left = (m.ac - 1) + m.re;
    m.total = m.st + m.ac + m.re; m.onBlock = m.blockstun - left; m.onHit = m.hitstun - left;
  });

  /* Poses: joints relative to the pelvis, facing right. y is down. */
  var IDLE = { neck: [2, -52], head: [4, -70], elF: [14, -38], wrF: [26, -56], elB: [-2, -36], wrB: [14, -54], knF: [20, 48], ftF: [30, 95], knB: [-14, 50], ftB: [-30, 95], px: 0 };
  var WIND = { neck: [-6, -50], head: [-8, -68], elF: [-10, -38], wrF: [-14, -46], elB: [4, -34], wrB: [20, -52], knF: [16, 48], ftF: [26, 95], knB: [-18, 50], ftB: [-36, 95], px: -6 };
  var EXT  = { neck: [14, -50], head: [20, -66], elF: [42, -50], wrF: [72, -53], elB: [8, -34], wrB: [22, -52], knF: [32, 46], ftF: [46, 95], knB: [-12, 52], ftB: [-38, 95], px: 14 };

  function mix(a, b, t) {
    var o = {};
    for (var k in a) o[k] = (k === 'px') ? a[k] + (b[k] - a[k]) * t : [a[k][0] + (b[k][0] - a[k][0]) * t, a[k][1] + (b[k][1] - a[k][1]) * t];
    return o;
  }
  var easeOut = function (u) { return 1 - Math.pow(1 - u, 3); }, easeIn = function (u) { return u * u; }, ease = function (u) { return u * u * (3 - 2 * u); };

  function poseAt(f, m) {
    var wind = mix(IDLE, WIND, m.wind), ext = mix(IDLE, EXT, m.reach);
    if (f < m.st) {
      var u = m.st > 1 ? f / (m.st - 1) : 1;
      return u < 0.7 ? mix(IDLE, wind, ease(u / 0.7)) : mix(wind, ext, easeIn((u - 0.7) / 0.3) * 0.85);
    }
    if (f < m.st + m.ac) return ext;
    var r = (f - m.st - m.ac) / Math.max(1, m.re - 1);
    return mix(ext, IDLE, easeOut(Math.min(1, r)));
  }

  function rectOf(pts, pad) {
    var x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    pts.forEach(function (p) { x0 = Math.min(x0, p[0]); y0 = Math.min(y0, p[1]); x1 = Math.max(x1, p[0]); y1 = Math.max(y1, p[1]); });
    return { x: x0 - pad, y: y0 - pad, w: x1 - x0 + 2 * pad, h: y1 - y0 + 2 * pad };
  }

  function boxes(pose, rx, m, active, dir) {
    var P = function (j) { return [rx + pose.px * dir + pose[j][0] * dir, PELVIS_Y + pose[j][1]]; };
    var head = P('head'), neck = P('neck'), wr = P('wrF'), el = P('elF');
    var root = [rx + pose.px * dir, PELVIS_Y];
    var hurt = [
      rectOf([[head[0] - 13, head[1] - 15], [head[0] + 13, head[1] + 15]], 0),
      rectOf([neck, root, [neck[0] - 15, neck[1]], [neck[0] + 15, neck[1]], [root[0] - 15, root[1]], [root[0] + 15, root[1]]], 2),
      rectOf([P('knF'), P('ftF'), P('knB'), P('ftB'), [root[0] - 14, root[1]], [root[0] + 14, root[1]]], 5),
      rectOf([neck, el, wr], 9)
    ];
    var push = { x: root[0] - 13, y: head[1] - 14, w: 26, h: GROUND - (head[1] - 14) };
    var hit = null;
    if (active) {
      var x0 = dir > 0 ? wr[0] - 12 : wr[0] - m.hitLen - 14, w = m.hitLen + 26;
      hit = { x: x0, y: wr[1] - 17, w: w, h: 34 };
    }
    return { hurt: hurt, push: push, hit: hit };
  }
  function overlap(a, b) { return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y; }

  function stick(pose, rx, dir, color, w) {
    var P = function (j) { return [rx + pose.px * dir + pose[j][0] * dir, PELVIS_Y + pose[j][1]]; };
    var pel = [rx + pose.px * dir, PELVIS_Y], neck = P('neck'), head = P('head');
    ctx.strokeStyle = color; ctx.lineWidth = w; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    function line(pts) { ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]); for (var i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]); ctx.stroke(); }
    var sh = [neck[0], neck[1] + 5];
    line([pel, neck]);
    line([pel, P('knB'), P('ftB')]);
    line([pel, P('knF'), P('ftF')]);
    line([sh, P('elB'), P('wrB')]);
    line([sh, P('elF'), P('wrF')]);
    ctx.beginPath(); ctx.arc(head[0], head[1], 12, 0, 7); ctx.fillStyle = css('--white'); ctx.fill(); ctx.stroke();
  }
  function drawRect(r, fill, stroke, lw) { ctx.fillStyle = fill; ctx.fillRect(r.x, r.y, r.w, r.h); ctx.strokeStyle = stroke; ctx.lineWidth = lw || 2; ctx.strokeRect(r.x, r.y, r.w, r.h); }

  var move = 'jab', frame = 0, playing = !reduce, showBoxes = true, acc = 0;
  var DUMMY_X = 300, FPS = 14;
  var els = {
    play: document.getElementById('fd-play'), prev: document.getElementById('fd-prev'), next: document.getElementById('fd-next'),
    hb: document.getElementById('fd-hb'), scrub: document.getElementById('fd-scrub'), num: document.getElementById('fd-frame'), bar: document.getElementById('fd-bar')
  };

  function draw() {
    var m = MOVES[move], active = frame >= m.st && frame < m.st + m.ac;
    var ink = css('--ink'), red = css('--red'), blue = css('--blue');
    ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, cv.width, cv.height); ctx.setTransform(cv.width / W, 0, 0, cv.width / W, 0, 0);
    ctx.strokeStyle = ink; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(0, GROUND + 5); ctx.lineTo(W, GROUND + 5); ctx.stroke();

    var pose = poseAt(frame, m), me = boxes(pose, 165, m, active, 1);
    var dpose = IDLE, dm = boxes(dpose, DUMMY_X, m, false, -1);
    var touching = false;
    if (me.hit) dm.hurt.forEach(function (h) { if (overlap(me.hit, h)) touching = true; });
    var sinceHit = frame - m.st, struck = frame >= m.st && sinceHit < m.ac + 6 && (touching || sinceHit >= m.ac);
    var flash = struck && sinceHit < m.ac + 5;

    stick(dpose, DUMMY_X + (flash ? 6 : 0), -1, flash ? red : '#8A93A6', 5);
    stick(pose, 165, 1, ink, 5);

    if (showBoxes) {
      dm.hurt.forEach(function (r) { drawRect(r, 'rgba(31,163,91,.16)', '#1FA35B', 1.5); });
      me.hurt.forEach(function (r) { drawRect(r, 'rgba(31,163,91,.18)', '#1FA35B', 2); });
      drawRect(me.push, 'rgba(31,79,216,.10)', blue, 2);
      if (me.hit) drawRect(me.hit, 'rgba(217,43,38,.30)', red, 2.5);
    }
    if (touching) {
      var cx = me.hit.x + me.hit.w - 10, cy = me.hit.y + 17;
      ctx.strokeStyle = red; ctx.lineWidth = 3; ctx.lineCap = 'round';
      for (var i = 0; i < 8; i++) { var a = i * Math.PI / 4; ctx.beginPath(); ctx.moveTo(cx + Math.cos(a) * 9, cy + Math.sin(a) * 9); ctx.lineTo(cx + Math.cos(a) * 19, cy + Math.sin(a) * 19); ctx.stroke(); }
    }
    ctx.font = '700 13px "Bricolage Grotesque",sans-serif'; ctx.textAlign = 'left'; ctx.fillStyle = ink;
    var phase = frame < m.st ? 'Startup' : (active ? 'Active' : 'Recovery');
    ctx.fillText(phase, 12, 22);

    els.num.textContent = (frame + 1) + ' / ' + m.total;
    els.scrub.value = frame;
    var cells = els.bar.children;
    for (var c = 0; c < cells.length; c++) cells[c].classList.toggle('cur', c === frame);
  }

  function fmt(el, v, signed) {
    el.textContent = signed && v > 0 ? '+' + v : String(v);
    el.className = signed ? (v < 0 ? 'neg' : (v > 0 ? 'pos' : '')) : '';
  }
  function setMove(k) {
    move = k; var m = MOVES[k]; frame = 0; acc = 0;
    document.querySelectorAll('[data-move]').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.move === k ? 'true' : 'false'); });
    els.scrub.max = m.total - 1;
    els.bar.innerHTML = '';
    for (var i = 0; i < m.total; i++) { var li = document.createElement('li'); li.className = i < m.st ? 's' : (i < m.st + m.ac ? 'a' : 'r'); els.bar.appendChild(li); }
    fmt(document.getElementById('d-dmg'), m.dmg); fmt(document.getElementById('d-st'), m.st); fmt(document.getElementById('d-ac'), m.ac);
    fmt(document.getElementById('d-re'), m.re); fmt(document.getElementById('d-ob'), m.onBlock, true); fmt(document.getElementById('d-oh'), m.onHit, true);
    draw();
  }
  function setPlaying(p) { playing = p; els.play.textContent = p ? 'Pause' : 'Play'; }
  function step(d) { setPlaying(false); var t = MOVES[move].total; frame = (frame + d + t) % t; draw(); }

  els.play.addEventListener('click', function () { setPlaying(!playing); });
  els.prev.addEventListener('click', function () { step(-1); });
  els.next.addEventListener('click', function () { step(1); });
  els.hb.addEventListener('click', function () { showBoxes = !showBoxes; els.hb.setAttribute('aria-pressed', showBoxes ? 'true' : 'false'); els.hb.textContent = showBoxes ? 'Hitboxes on' : 'Hitboxes off'; draw(); });
  els.scrub.addEventListener('input', function () { setPlaying(false); frame = +els.scrub.value; draw(); });
  document.querySelectorAll('[data-move]').forEach(function (b) { b.addEventListener('click', function () { setMove(b.dataset.move); }); });

  var last = performance.now(), visible = false;
  function loop(now) {
    var dt = Math.min(0.1, (now - last) / 1000); last = now;
    if (playing && visible) {
      acc += dt * FPS;
      while (acc >= 1) { acc -= 1; var t = MOVES[move].total; frame = (frame + 1) % t; if (frame === 0) acc -= 6; }
      draw();
    }
    requestAnimationFrame(loop);
  }
  new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(cv);
  setPlaying(playing);
  setMove('jab');
  if (reduce) { frame = MOVES.jab.st; draw(); }
  requestAnimationFrame(loop);
})();

/* Stuff I like: one open row at a time */
(function () {
  var box = document.querySelector('.stuff');
  if (!box) return;
  var rows = box.querySelectorAll('.srow');
  box.classList.add('js');
  rows.forEach(function (r) {
    r.addEventListener('click', function () {
      rows.forEach(function (o) { o.setAttribute('aria-expanded', o === r ? 'true' : 'false'); });
    });
  });
})();

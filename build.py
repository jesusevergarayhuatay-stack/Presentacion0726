import json
data = json.load(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/data.json'))
DATA = json.dumps(data, ensure_ascii=False)

TPL = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Adjuntía para la Prevención de Conflictos Sociales · Informes y Documentos</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#070a18; --bg2:#0c1230; --panel:rgba(255,255,255,.045);
  --stroke:rgba(255,255,255,.09); --stroke2:rgba(255,255,255,.16);
  --txt:#eef1ff; --mut:#9aa3c7; --mut2:#6d76a0;
  --a1:#7c5cff; --a2:#00d4ff; --a3:#ff5ca8; --grn:#2ee6a6; --red:#ff5d73; --amb:#ffb547;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{
  font-family:'Inter',system-ui,sans-serif; color:var(--txt);
  background:var(--bg); overflow:hidden;
}
/* animated aurora background */
.bg{position:fixed;inset:0;z-index:0;overflow:hidden;background:
  radial-gradient(1200px 700px at 12% -8%,rgba(124,92,255,.28),transparent 60%),
  radial-gradient(1000px 700px at 100% 0%,rgba(0,212,255,.18),transparent 55%),
  radial-gradient(1100px 800px at 60% 120%,rgba(255,92,168,.16),transparent 55%),
  linear-gradient(180deg,#070a18,#05060f);}
.bg:before{content:"";position:absolute;inset:-40%;
  background:conic-gradient(from 0deg,transparent,rgba(124,92,255,.10),transparent 40%);
  animation:spin 40s linear infinite;}
.grid{position:fixed;inset:0;z-index:0;opacity:.35;
  background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);
  background-size:44px 44px;mask:radial-gradient(circle at 50% 40%,black,transparent 85%);}
@keyframes spin{to{transform:rotate(360deg)}}

.app{position:relative;z-index:2;height:100vh;display:grid;grid-template-columns:320px 1fr;grid-template-rows:auto 1fr;gap:0;}
/* top bar */
.top{grid-column:1/3;display:flex;align-items:center;gap:18px;padding:18px 30px;border-bottom:1px solid var(--stroke);backdrop-filter:blur(8px);}
.brand{display:flex;align-items:center;gap:14px}
.emblem{width:44px;height:44px;border-radius:13px;display:grid;place-items:center;font-family:'Space Grotesk';font-weight:700;font-size:20px;
  background:linear-gradient(135deg,var(--a1),var(--a3));box-shadow:0 8px 30px rgba(124,92,255,.5);}
.brand h1{font-family:'Sora';font-weight:700;font-size:15px;letter-spacing:.2px}
.brand p{font-size:11.5px;color:var(--mut);letter-spacing:1.5px;text-transform:uppercase;margin-top:2px}
.top .spacer{flex:1}
.kpis{display:flex;gap:26px}
.kpi{text-align:right}
.kpi b{font-family:'Space Grotesk';font-size:22px;background:linear-gradient(120deg,var(--a2),var(--a1));-webkit-background-clip:text;background-clip:text;color:transparent}
.kpi span{display:block;font-size:10px;color:var(--mut2);text-transform:uppercase;letter-spacing:1.4px}

/* navigator rail */
.rail{border-right:1px solid var(--stroke);padding:22px 18px;overflow-y:auto}
.rail h2{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--mut2);margin:2px 6px 16px}
.nav-card{position:relative;display:block;width:100%;text-align:left;cursor:pointer;border:1px solid var(--stroke);
  background:var(--panel);border-radius:16px;padding:15px 16px;margin-bottom:12px;color:var(--txt);
  transition:.35s cubic-bezier(.2,.7,.2,1);overflow:hidden}
.nav-card:hover{border-color:var(--stroke2);transform:translateY(-2px)}
.nav-card .idx{font-family:'Space Grotesk';font-size:12px;color:var(--mut2)}
.nav-card .num{font-family:'Sora';font-weight:700;font-size:14px;margin:3px 0 6px;line-height:1.25}
.nav-card .sub{font-size:11px;color:var(--mut);line-height:1.4;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.nav-card .row{display:flex;align-items:center;gap:8px;margin-top:10px}
.chip-mini{font-size:10px;padding:3px 8px;border-radius:20px;border:1px solid var(--stroke2);color:var(--mut)}
.nav-card.active{border-color:transparent;background:linear-gradient(135deg,rgba(124,92,255,.22),rgba(0,212,255,.12))}
.nav-card.active:before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:linear-gradient(var(--a1),var(--a2))}
.nav-card.active .num{background:linear-gradient(120deg,#fff,var(--a2));-webkit-background-clip:text;background-clip:text;color:transparent}

/* stage */
.stage{overflow-y:auto;padding:30px 40px 60px;scroll-behavior:smooth}
.stage::-webkit-scrollbar,.rail::-webkit-scrollbar{width:9px}
.stage::-webkit-scrollbar-thumb,.rail::-webkit-scrollbar-thumb{background:rgba(255,255,255,.12);border-radius:8px}

.hero{position:relative;border:1px solid var(--stroke);border-radius:26px;padding:34px 38px;overflow:hidden;
  background:linear-gradient(135deg,rgba(124,92,255,.14),rgba(0,212,255,.05));backdrop-filter:blur(10px)}
.hero .bignum{position:absolute;right:24px;top:-30px;font-family:'Space Grotesk';font-weight:700;font-size:190px;line-height:1;
  color:transparent;-webkit-text-stroke:1.5px rgba(255,255,255,.10);pointer-events:none;user-select:none}
.tag{display:inline-flex;align-items:center;gap:8px;font-size:11px;letter-spacing:1.6px;text-transform:uppercase;color:var(--a2);
  border:1px solid rgba(0,212,255,.4);padding:5px 12px;border-radius:20px;background:rgba(0,212,255,.06)}
.doc-num{font-family:'Space Grotesk';font-size:13px;color:var(--mut);margin:16px 0 8px;letter-spacing:.5px}
.title{font-family:'Sora';font-weight:800;font-size:30px;line-height:1.18;max-width:80%}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.chip{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;padding:8px 14px;border-radius:12px;
  border:1px solid var(--stroke2);background:rgba(255,255,255,.04);color:var(--txt)}
.chip .dot{width:7px;height:7px;border-radius:50%}
.badge-state{font-weight:600}
.st-ok{color:var(--grn)} .st-no{color:var(--red)}

.two{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:22px}
.panel{border:1px solid var(--stroke);border-radius:20px;padding:24px 26px;background:var(--panel);backdrop-filter:blur(8px)}
.panel .lbl{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--mut2);margin-bottom:12px;display:flex;align-items:center;gap:9px}
.panel .lbl i{width:26px;height:26px;border-radius:9px;display:grid;place-items:center;font-style:normal;font-size:14px;
  background:linear-gradient(135deg,var(--a1),var(--a3))}
.panel p{font-size:14.5px;line-height:1.65;color:#dfe3ff}

.sec-h{display:flex;align-items:center;gap:14px;margin:34px 4px 18px}
.sec-h h3{font-family:'Sora';font-weight:700;font-size:17px}
.sec-h .line{flex:1;height:1px;background:linear-gradient(90deg,var(--stroke2),transparent)}
.sec-h .cnt{font-size:12px;color:var(--mut2)}

.recs{display:grid;gap:16px}
.rec{border:1px solid var(--stroke);border-radius:20px;padding:22px 24px;background:var(--panel);position:relative;overflow:hidden;
  transition:.3s;animation:rise .5s both}
.rec:hover{border-color:var(--stroke2)}
.rec .head{display:flex;align-items:center;gap:16px;margin-bottom:14px}
.ring{--p:0;width:56px;height:56px;flex:none;border-radius:50%;display:grid;place-items:center;
  background:conic-gradient(var(--a2) calc(var(--p)*1%),rgba(255,255,255,.08) 0);position:relative}
.ring:after{content:"";position:absolute;inset:5px;border-radius:50%;background:#0c1024}
.ring b{position:relative;font-family:'Space Grotesk';font-size:18px;z-index:1}
.rec .inst{flex:1}
.rec .inst .who{font-family:'Sora';font-weight:600;font-size:15.5px}
.rec .inst .meta{font-size:11.5px;color:var(--mut);margin-top:3px}
.pill{font-size:11px;font-weight:600;padding:6px 13px;border-radius:20px;white-space:nowrap}
.pill.ok{color:var(--grn);background:rgba(46,230,166,.12);border:1px solid rgba(46,230,166,.35)}
.pill.no{color:var(--red);background:rgba(255,93,115,.12);border:1px solid rgba(255,93,115,.35)}
.rec ul{list-style:none;display:grid;gap:9px;margin-top:6px}
.rec li{position:relative;padding-left:26px;font-size:13.5px;line-height:1.6;color:#d4d9f5}
.rec li:before{content:"";position:absolute;left:6px;top:9px;width:7px;height:7px;border-radius:2px;transform:rotate(45deg);
  background:linear-gradient(135deg,var(--a1),var(--a2))}
.act{margin-top:16px;padding-top:14px;border-top:1px dashed var(--stroke2);display:flex;gap:11px;align-items:flex-start}
.act .k{font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;color:var(--amb);white-space:nowrap;padding-top:2px}
.act .v{font-size:13px;color:var(--mut);line-height:1.55}

@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.fade{animation:fadein .45s both}
@keyframes fadein{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}

.footnav{display:flex;justify-content:space-between;align-items:center;margin-top:30px;gap:14px}
.btn{display:inline-flex;align-items:center;gap:9px;padding:12px 20px;border-radius:14px;cursor:pointer;font-size:13px;font-weight:600;
  border:1px solid var(--stroke2);background:var(--panel);color:var(--txt);transition:.25s}
.btn:hover{background:rgba(255,255,255,.09);transform:translateY(-1px)}
.btn:disabled{opacity:.3;cursor:default;transform:none}
.dots{display:flex;gap:8px}
.dots span{width:9px;height:9px;border-radius:50%;background:rgba(255,255,255,.18);cursor:pointer;transition:.3s}
.dots span.on{background:linear-gradient(120deg,var(--a1),var(--a2));width:26px;border-radius:8px}
.hint{position:fixed;bottom:16px;right:22px;z-index:5;font-size:11px;color:var(--mut2);letter-spacing:.5px}
kbd{font-family:'Space Grotesk';border:1px solid var(--stroke2);border-radius:6px;padding:1px 6px;font-size:11px;color:var(--mut)}
@media(max-width:980px){.app{grid-template-columns:1fr}.rail{display:none}.two{grid-template-columns:1fr}.title{max-width:100%}.hero .bignum{font-size:120px}}
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>

<div class="app">
  <div class="top">
    <div class="brand">
      <div class="emblem">DP</div>
      <div>
        <h1>Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad</h1>
        <p>Informes y Documentos · Conflictos Sociales</p>
      </div>
    </div>
    <div class="spacer"></div>
    <div class="kpis">
      <div class="kpi"><b id="k-docs">0</b><span>Documentos</span></div>
      <div class="kpi"><b id="k-inst">0</b><span>Instituciones</span></div>
      <div class="kpi"><b id="k-recs">0</b><span>Recomendaciones</span></div>
    </div>
  </div>

  <aside class="rail">
    <h2>Navegador de documentos</h2>
    <div id="nav"></div>
  </aside>

  <main class="stage" id="stage"></main>
</div>
<div class="hint">Navega con <kbd>←</kbd> <kbd>→</kbd></div>

<script>
const DOCS = __DATA__;

function stateClass(s){ return (s||'').toLowerCase().includes('no') ? 'no' : 'ok'; }
function splitRecs(t){
  if(!t) return [];
  let parts = t.split(/\n+/).map(x=>x.trim()).filter(x=>x.length>2);
  return parts;
}
const totalInst = new Set();
DOCS.forEach(d=>d.recs.forEach(r=>totalInst.add((r.institucion||'').trim())));
const totalRecs = DOCS.reduce((a,d)=>a+d.recs.reduce((s,r)=>s+(Number(r.total)||0),0),0);

// KPI count-up
function countUp(el,to){let n=0;const step=Math.max(1,Math.ceil(to/28));const t=setInterval(()=>{n+=step;if(n>=to){n=to;clearInterval(t)}el.textContent=n;},28);}
countUp(document.getElementById('k-docs'),DOCS.length);
countUp(document.getElementById('k-inst'),totalInst.size);
countUp(document.getElementById('k-recs'),totalRecs);

// build navigator
const nav=document.getElementById('nav');
DOCS.forEach((d,i)=>{
  const b=document.createElement('button');
  b.className='nav-card';b.dataset.i=i;
  b.innerHTML=`<div class="idx">DOCUMENTO ${String(i+1).padStart(2,'0')}</div>
    <div class="num">${d.numero}</div>
    <div class="sub">${d.titulo.replace(/\n/g,' ')}</div>
    <div class="row"><span class="chip-mini">${d.anio}</span><span class="chip-mini">${d.linea}</span></div>`;
  b.onclick=()=>show(i);
  nav.appendChild(b);
});

let cur=-1;
const stage=document.getElementById('stage');
function maxTotal(d){return Math.max(...d.recs.map(r=>Number(r.total)||0),1);}

function show(i){
  if(i<0||i>=DOCS.length)return;
  cur=i;const d=DOCS[i];const mx=maxTotal(d);
  document.querySelectorAll('.nav-card').forEach(c=>c.classList.toggle('active',+c.dataset.i===i));
  const sc=stateClass(d.estado_rec);
  let recsHtml=d.recs.map((r,ri)=>{
    const items=splitRecs(r.texto).map(x=>`<li>${x.replace(/^[IVX0-9]+[\.\)]\s*/,'')}</li>`).join('');
    const p=Math.round((Number(r.total)||0)/mx*100);
    const cls=stateClass(r.estado_rec);
    const act=r.acciones?`<div class="act"><div class="k">Acciones futuras</div><div class="v">${r.acciones}</div></div>`:'';
    return `<div class="rec" style="animation-delay:${ri*70}ms">
      <div class="head">
        <div class="ring" style="--p:${p}"><b>${r.total||'–'}</b></div>
        <div class="inst"><div class="who">${r.institucion||'—'}</div>
          <div class="meta">${r.total||0} recomendación(es) dirigidas</div></div>
        <div class="pill ${cls}">${r.estado_rec||'—'}</div>
      </div>
      <ul>${items}</ul>${act}</div>`;
  }).join('');

  stage.innerHTML=`<div class="fade">
    <section class="hero">
      <div class="bignum">${String(i+1).padStart(2,'0')}</div>
      <span class="tag">◆ ${d.tipo} · ${d.estado}</span>
      <div class="doc-num">N° ${d.numero}</div>
      <div class="title">${d.titulo.replace(/\n/g,' ')}</div>
      <div class="chips">
        <span class="chip"><span class="dot" style="background:var(--a2)"></span>Año ${d.anio}</span>
        <span class="chip"><span class="dot" style="background:var(--a1)"></span>Publicado ${d.fecha||'—'}</span>
        <span class="chip"><span class="dot" style="background:var(--a3)"></span>${d.linea}</span>
        <span class="chip badge-state ${sc==='ok'?'st-ok':'st-no'}"><span class="dot" style="background:${sc==='ok'?'var(--grn)':'var(--red)'}"></span>${d.estado_rec}</span>
      </div>
    </section>

    <div class="two">
      <div class="panel"><div class="lbl"><i>◎</i>Objetivo del documento</div><p>${d.objetivo}</p></div>
      <div class="panel"><div class="lbl"><i>❖</i>Público beneficiario</div><p>${d.publico}</p>
        <div class="lbl" style="margin-top:22px"><i>∑</i>Alcance</div>
        <p><b style="font-family:'Space Grotesk';font-size:26px;color:#fff">${d.recs.length}</b> institución(es) recomendadas ·
        <b style="font-family:'Space Grotesk';font-size:26px;color:#fff">${d.recs.reduce((s,r)=>s+(Number(r.total)||0),0)}</b> recomendaciones</p>
      </div>
    </div>

    <div class="sec-h"><h3>Recomendaciones por institución</h3><div class="line"></div>
      <div class="cnt">${d.recs.length} entidad(es)</div></div>
    <div class="recs">${recsHtml}</div>

    <div class="footnav">
      <button class="btn" id="prev">← Anterior</button>
      <div class="dots" id="dots"></div>
      <button class="btn" id="next">Siguiente →</button>
    </div>
  </div>`;
  const dots=document.getElementById('dots');
  DOCS.forEach((_,j)=>{const s=document.createElement('span');if(j===i)s.className='on';s.onclick=()=>show(j);dots.appendChild(s);});
  const pv=document.getElementById('prev'),nx=document.getElementById('next');
  pv.disabled=i===0;nx.disabled=i===DOCS.length-1;
  pv.onclick=()=>show(i-1);nx.onclick=()=>show(i+1);
  stage.scrollTop=0;
}
document.addEventListener('keydown',e=>{if(e.key==='ArrowRight')show(Math.min(cur+1,DOCS.length-1));if(e.key==='ArrowLeft')show(Math.max(cur-1,0));});
show(0);
</script>
</body>
</html>'''

html = TPL.replace('__DATA__', DATA)
open('/sessions/wonderful-relaxed-feynman/mnt/outputs/Informes_Adjuntia_Conflictos_Sociales.html','w',encoding='utf-8').write(html)
print('OK bytes:', len(html))

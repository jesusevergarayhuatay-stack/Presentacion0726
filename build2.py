import json, base64
data = json.load(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/data.json'))
DATA = json.dumps(data, ensure_ascii=False)
logo_b64 = base64.b64encode(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/Defensoría_del_Pueblo.png','rb').read()).decode()
LOGO = 'data:image/png;base64,'+logo_b64

TPL = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Defensoría del Pueblo · Informes y Documentos — Conflictos Sociales</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
<style>
:root{
  --blue:#0a56a8; --blue-d:#083b73; --blue-l:#e8f1fb; --red:#e1251b; --red-l:#fdecea;
  --ink:#12161c; --mut:#5c6675; --mut2:#9aa4b2; --line:#e7ebf1; --soft:#f6f8fc;
  --grn:#1f9d57; --grn-l:#e7f6ee; --amb:#c47d00;
  --sh:0 10px 40px rgba(16,42,80,.10); --sh2:0 18px 60px rgba(16,42,80,.16);
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:#fff;overflow:hidden}
/* dynamic soft background */
.bg{position:fixed;inset:0;z-index:0;background:#fff;overflow:hidden}
.orb{position:absolute;border-radius:50%;filter:blur(70px);opacity:.5;animation:float 20s ease-in-out infinite}
.o1{width:460px;height:460px;background:radial-gradient(circle,#cfe2f7,transparent 70%);top:-140px;left:-100px}
.o2{width:400px;height:400px;background:radial-gradient(circle,#fbd6d2,transparent 70%);bottom:-160px;right:8%;animation-delay:-7s}
.o3{width:360px;height:360px;background:radial-gradient(circle,#dbe9fb,transparent 70%);bottom:20%;left:30%;animation-delay:-13s}
@keyframes float{0%,100%{transform:translate(0,0)}33%{transform:translate(40px,-30px)}66%{transform:translate(-30px,25px)}}
.grid{position:fixed;inset:0;z-index:0;opacity:.5;
  background-image:linear-gradient(rgba(10,86,168,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(10,86,168,.05) 1px,transparent 1px);
  background-size:46px 46px;mask:radial-gradient(circle at 50% 30%,#000,transparent 80%)}

.app{position:relative;z-index:2;height:100vh;display:grid;grid-template-columns:330px 1fr;grid-template-rows:auto 1fr}
/* top progress */
#prog{position:fixed;top:0;left:0;height:3px;width:0;z-index:9;background:linear-gradient(90deg,var(--blue),var(--red));transition:width .1s}

/* top bar */
.top{grid-column:1/3;display:flex;align-items:center;gap:20px;padding:16px 34px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.85);backdrop-filter:blur(10px)}
.top img.logo{height:52px;width:auto}
.top .divider{width:1px;height:40px;background:var(--line)}
.top .ctx h1{font-family:'Sora';font-weight:700;font-size:14px;line-height:1.25}
.top .ctx p{font-size:11px;color:var(--mut);letter-spacing:1.4px;text-transform:uppercase;margin-top:3px}
.top .spacer{flex:1}
.anniv{height:60px;width:auto}
.anniv text.script{font-family:'Dancing Script',cursive}

/* navigator */
.rail{border-right:1px solid var(--line);padding:22px 18px;overflow-y:auto;background:rgba(255,255,255,.6)}
.rail h2{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--mut2);margin:2px 8px 16px;font-weight:700}
.nav-card{position:relative;display:block;width:100%;text-align:left;cursor:pointer;border:1px solid var(--line);
  background:#fff;border-radius:16px;padding:15px 16px 15px 18px;margin-bottom:12px;color:var(--ink);
  box-shadow:0 4px 18px rgba(16,42,80,.05);transition:.34s cubic-bezier(.2,.7,.2,1);overflow:hidden}
.nav-card:hover{transform:translateY(-3px);box-shadow:var(--sh)}
.nav-card .idx{font-family:'Space Grotesk';font-size:11px;color:var(--mut2);letter-spacing:1px}
.nav-card .num{font-family:'Sora';font-weight:700;font-size:14px;margin:4px 0 6px;line-height:1.25;color:var(--blue-d)}
.nav-card .sub{font-size:11.5px;color:var(--mut);line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.nav-card .row{display:flex;gap:7px;margin-top:11px;flex-wrap:wrap}
.chip-mini{font-size:10px;padding:3px 9px;border-radius:20px;background:var(--soft);border:1px solid var(--line);color:var(--mut)}
.nav-card:before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:transparent;transition:.3s}
.nav-card.active{border-color:#cfe0f4;background:linear-gradient(180deg,#fff,var(--blue-l))}
.nav-card.active:before{background:linear-gradient(var(--blue),var(--red))}
.nav-card.active .num{color:var(--blue)}

/* stage */
.stage{overflow-y:auto;padding:28px 42px 70px;scroll-behavior:smooth}
.stage::-webkit-scrollbar,.rail::-webkit-scrollbar{width:9px}
.stage::-webkit-scrollbar-thumb,.rail::-webkit-scrollbar-thumb{background:#d5dce6;border-radius:8px}

/* kpi strip */
.kpis{display:flex;gap:14px;margin-bottom:24px}
.kcard{flex:1;border:1px solid var(--line);border-radius:18px;padding:18px 20px;background:#fff;box-shadow:var(--sh);position:relative;overflow:hidden}
.kcard:before{content:"";position:absolute;left:0;top:0;height:100%;width:4px}
.kcard.k1:before{background:var(--blue)} .kcard.k2:before{background:var(--red)} .kcard.k3:before{background:var(--grn)} .kcard.k4:before{background:var(--amb)}
.kcard b{font-family:'Space Grotesk';font-size:30px;display:block;line-height:1}
.kcard.k1 b{color:var(--blue)} .kcard.k2 b{color:var(--red)} .kcard.k3 b{color:var(--grn)} .kcard.k4 b{color:var(--amb)}
.kcard span{font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:1.2px;margin-top:6px;display:block}

.hero{position:relative;border:1px solid var(--line);border-radius:26px;padding:34px 40px;overflow:hidden;background:#fff;box-shadow:var(--sh)}
.hero:before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:linear-gradient(var(--blue),var(--red))}
.hero .bignum{position:absolute;right:26px;top:-26px;font-family:'Space Grotesk';font-weight:700;font-size:190px;line-height:1;
  color:transparent;-webkit-text-stroke:2px #e6eefa;pointer-events:none;user-select:none}
.tag{display:inline-flex;align-items:center;gap:8px;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--blue);font-weight:600;
  border:1px solid #cfe0f4;padding:6px 13px;border-radius:20px;background:var(--blue-l)}
.doc-num{font-family:'Space Grotesk';font-size:13px;color:var(--mut);margin:16px 0 8px;letter-spacing:.4px}
.title{font-family:'Sora';font-weight:800;font-size:29px;line-height:1.2;max-width:82%;color:var(--ink)}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.chip{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;padding:8px 14px;border-radius:12px;border:1px solid var(--line);background:var(--soft);color:var(--ink);font-weight:500}
.chip .dot{width:8px;height:8px;border-radius:50%}
.st-ok{color:var(--grn)} .st-no{color:var(--red)}

.two{display:grid;grid-template-columns:1.05fr 1fr;gap:18px;margin-top:20px}
.panel{border:1px solid var(--line);border-radius:20px;padding:24px 26px;background:#fff;box-shadow:var(--sh)}
.panel .lbl{font-size:11px;letter-spacing:1.6px;text-transform:uppercase;color:var(--mut);margin-bottom:12px;display:flex;align-items:center;gap:10px;font-weight:700}
.panel .lbl i{width:28px;height:28px;border-radius:9px;display:grid;place-items:center;font-style:normal;font-size:14px;color:#fff;background:linear-gradient(135deg,var(--blue),var(--blue-d))}
.panel .lbl.r i{background:linear-gradient(135deg,var(--red),#b41b13)}
.panel p{font-size:14.5px;line-height:1.65;color:#2a3340}
.stat-inline b{font-family:'Space Grotesk';font-size:28px;color:var(--ink)}

.sec-h{display:flex;align-items:center;gap:14px;margin:32px 4px 16px}
.sec-h h3{font-family:'Sora';font-weight:700;font-size:17px}
.sec-h .line{flex:1;height:1px;background:linear-gradient(90deg,var(--line),transparent)}
.sec-h .cnt{font-size:12px;color:var(--mut2);font-weight:600}

.recs{display:grid;gap:15px}
.rec{border:1px solid var(--line);border-left:5px solid var(--mut2);border-radius:18px;padding:22px 24px;background:#fff;box-shadow:var(--sh);position:relative;transition:.3s}
.rec.ok{border-left-color:var(--grn)} .rec.no{border-left-color:var(--red)}
.rec:hover{transform:translateY(-3px);box-shadow:var(--sh2)}
.rec .head{display:flex;align-items:center;gap:16px;margin-bottom:14px}
.ring{--p:0;width:56px;height:56px;flex:none;border-radius:50%;display:grid;place-items:center;
  background:conic-gradient(var(--blue) calc(var(--p)*1%),#eaf0f8 0);position:relative}
.ring:after{content:"";position:absolute;inset:5px;border-radius:50%;background:#fff}
.ring b{position:relative;font-family:'Space Grotesk';font-size:18px;z-index:1;color:var(--blue-d)}
.rec .inst{flex:1}
.rec .inst .who{font-family:'Sora';font-weight:700;font-size:15.5px;color:var(--ink)}
.rec .inst .meta{font-size:11.5px;color:var(--mut);margin-top:3px}
.pill{font-size:11px;font-weight:700;padding:6px 13px;border-radius:20px;white-space:nowrap}
.pill.ok{color:var(--grn);background:var(--grn-l);border:1px solid #b8e6cb}
.pill.no{color:var(--red);background:var(--red-l);border:1px solid #f6c9c4}
.rec ul{list-style:none;display:grid;gap:9px;margin-top:4px}
.rec li{position:relative;padding-left:26px;font-size:13.5px;line-height:1.6;color:#2f3947}
.rec li:before{content:"";position:absolute;left:6px;top:8px;width:7px;height:7px;border-radius:2px;transform:rotate(45deg);background:linear-gradient(135deg,var(--blue),var(--red))}
.act{margin-top:16px;padding-top:14px;border-top:1px dashed var(--line);display:flex;gap:12px;align-items:flex-start}
.act .k{font-size:10.5px;letter-spacing:1.3px;text-transform:uppercase;color:var(--amb);white-space:nowrap;padding-top:2px;font-weight:700}
.act .v{font-size:13px;color:var(--mut);line-height:1.55}

.reveal{opacity:0;transform:translateY(18px)}
.reveal.in{animation:rise .55s forwards cubic-bezier(.2,.7,.2,1)}
@keyframes rise{to{opacity:1;transform:none}}
.fade{animation:fadein .4s both}
@keyframes fadein{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

.footnav{display:flex;justify-content:space-between;align-items:center;margin-top:30px;gap:14px}
.btn{display:inline-flex;align-items:center;gap:9px;padding:12px 20px;border-radius:14px;cursor:pointer;font-size:13px;font-weight:600;border:1px solid var(--line);background:#fff;color:var(--ink);box-shadow:var(--sh);transition:.25s}
.btn:hover{background:var(--blue);color:#fff;border-color:var(--blue);transform:translateY(-2px)}
.btn:disabled{opacity:.35;cursor:default;transform:none;background:#fff;color:var(--ink);border-color:var(--line)}
.dots{display:flex;gap:8px}
.dots span{width:9px;height:9px;border-radius:50%;background:#d3dbe6;cursor:pointer;transition:.3s}
.dots span.on{background:linear-gradient(120deg,var(--blue),var(--red));width:28px;border-radius:8px}
.hint{position:fixed;bottom:14px;right:20px;z-index:5;font-size:11px;color:var(--mut2)}
kbd{font-family:'Space Grotesk';border:1px solid var(--line);border-radius:6px;padding:1px 6px;font-size:11px;color:var(--mut);background:#fff}
@media(max-width:980px){.app{grid-template-columns:1fr}.rail{display:none}.two{grid-template-columns:1fr}.title{max-width:100%}.hero .bignum{font-size:120px}.kpis{flex-wrap:wrap}.kcard{min-width:44%}}
</style>
</head>
<body>
<div id="prog"></div>
<div class="bg"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div></div>
<div class="grid"></div>

<div class="app">
  <div class="top">
    <img class="logo" src="__LOGO__" alt="Defensoría del Pueblo">
    <div class="divider"></div>
    <div class="ctx">
      <h1>Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad</h1>
      <p>Informes y Documentos · Conflictos Sociales</p>
    </div>
    <div class="spacer"></div>
    __ANNIV__
  </div>

  <aside class="rail">
    <h2>Navegador de documentos</h2>
    <div id="nav"></div>
  </aside>

  <main class="stage" id="stage"></main>
</div>
<div class="hint">Navega con <kbd>&larr;</kbd> <kbd>&rarr;</kbd></div>

<script>
const DOCS = __DATA__;
function stateClass(s){return (s||'').toLowerCase().includes('no')?'no':'ok';}
function splitRecs(t){if(!t)return[];return t.split(/\n+/).map(x=>x.trim()).filter(x=>x.length>2);}
const totalInst=new Set();DOCS.forEach(d=>d.recs.forEach(r=>totalInst.add((r.institucion||'').trim())));
const totalRecs=DOCS.reduce((a,d)=>a+d.recs.reduce((s,r)=>s+(Number(r.total)||0),0),0);
const yrs=[...new Set(DOCS.map(d=>d.anio))].sort();

const nav=document.getElementById('nav');
DOCS.forEach((d,i)=>{
  const b=document.createElement('button');b.className='nav-card';b.dataset.i=i;
  b.innerHTML=`<div class="idx">DOCUMENTO ${String(i+1).padStart(2,'0')}</div>
    <div class="num">${d.numero}</div>
    <div class="sub">${d.titulo.replace(/\n/g,' ')}</div>
    <div class="row"><span class="chip-mini">${d.anio}</span><span class="chip-mini">${d.linea}</span></div>`;
  b.onclick=()=>show(i);nav.appendChild(b);
});

let cur=-1;const stage=document.getElementById('stage');
const maxTotal=d=>Math.max(...d.recs.map(r=>Number(r.total)||0),1);

function countUp(el,to){let n=0;const step=Math.max(1,Math.ceil(to/26));const t=setInterval(()=>{n+=step;if(n>=to){n=to;clearInterval(t)}el.textContent=n;},26);}

function show(i){
  if(i<0||i>=DOCS.length)return;cur=i;const d=DOCS[i];const mx=maxTotal(d);
  document.querySelectorAll('.nav-card').forEach(c=>c.classList.toggle('active',+c.dataset.i===i));
  const sc=stateClass(d.estado_rec);
  const docRecs=d.recs.reduce((s,r)=>s+(Number(r.total)||0),0);
  const acog=d.recs.filter(r=>stateClass(r.estado_rec)==='ok').length;
  let recsHtml=d.recs.map((r,ri)=>{
    const items=splitRecs(r.texto).map(x=>`<li>${x.replace(/^[IVX0-9]+[\.\)]\s*/,'')}</li>`).join('');
    const p=Math.round((Number(r.total)||0)/mx*100);const cls=stateClass(r.estado_rec);
    const act=r.acciones?`<div class="act"><div class="k">Acciones futuras</div><div class="v">${r.acciones}</div></div>`:'';
    return `<div class="rec ${cls} reveal">
      <div class="head">
        <div class="ring" style="--p:${p}"><b>${r.total||'–'}</b></div>
        <div class="inst"><div class="who">${r.institucion||'—'}</div><div class="meta">${r.total||0} recomendación(es) dirigidas</div></div>
        <div class="pill ${cls}">${r.estado_rec||'—'}</div>
      </div><ul>${items}</ul>${act}</div>`;
  }).join('');

  stage.innerHTML=`<div class="fade">
    <div class="kpis">
      <div class="kcard k1"><b id="c1">0</b><span>Instituciones</span></div>
      <div class="kcard k2"><b id="c2">0</b><span>Recomendaciones</span></div>
      <div class="kcard k3"><b id="c3">0</b><span>Acogidas</span></div>
      <div class="kcard k4"><b id="c4">0</b><span>Año</span></div>
    </div>
    <section class="hero reveal">
      <div class="bignum">${String(i+1).padStart(2,'0')}</div>
      <span class="tag">&#9670; ${d.tipo} &middot; ${d.estado}</span>
      <div class="doc-num">N&deg; ${d.numero}</div>
      <div class="title">${d.titulo.replace(/\n/g,' ')}</div>
      <div class="chips">
        <span class="chip"><span class="dot" style="background:var(--blue)"></span>Año ${d.anio}</span>
        <span class="chip"><span class="dot" style="background:var(--blue-d)"></span>Publicado ${d.fecha||'—'}</span>
        <span class="chip"><span class="dot" style="background:var(--red)"></span>${d.linea}</span>
        <span class="chip ${sc==='ok'?'st-ok':'st-no'}"><span class="dot" style="background:${sc==='ok'?'var(--grn)':'var(--red)'}"></span>${d.estado_rec}</span>
      </div>
    </section>
    <div class="two">
      <div class="panel reveal"><div class="lbl"><i>&#9673;</i>Objetivo del documento</div><p>${d.objetivo}</p></div>
      <div class="panel reveal"><div class="lbl r"><i>&#10070;</i>Público beneficiario</div><p>${d.publico}</p>
        <div class="lbl" style="margin-top:22px"><i>&#8721;</i>Alcance</div>
        <p class="stat-inline"><b>${d.recs.length}</b> institución(es) &middot; <b>${docRecs}</b> recomendaciones</p></div>
    </div>
    <div class="sec-h"><h3>Recomendaciones por institución</h3><div class="line"></div><div class="cnt">${d.recs.length} entidad(es)</div></div>
    <div class="recs">${recsHtml}</div>
    <div class="footnav">
      <button class="btn" id="prev">&larr; Anterior</button>
      <div class="dots" id="dots"></div>
      <button class="btn" id="next">Siguiente &rarr;</button>
    </div></div>`;

  countUp(document.getElementById('c1'),d.recs.length);
  countUp(document.getElementById('c2'),docRecs);
  countUp(document.getElementById('c3'),acog);
  document.getElementById('c4').textContent=d.anio;
  const dots=document.getElementById('dots');
  DOCS.forEach((_,j)=>{const s=document.createElement('span');if(j===i)s.className='on';s.onclick=()=>show(j);dots.appendChild(s);});
  const pv=document.getElementById('prev'),nx=document.getElementById('next');
  pv.disabled=i===0;nx.disabled=i===DOCS.length-1;pv.onclick=()=>show(i-1);nx.onclick=()=>show(i+1);
  stage.scrollTop=0;
  // reveal on scroll
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{root:stage,threshold:.12});
  stage.querySelectorAll('.reveal').forEach(el=>io.observe(el));
}
stage.addEventListener('scroll',()=>{const p=stage.scrollTop/(stage.scrollHeight-stage.clientHeight||1);document.getElementById('prog').style.width=(p*100)+'%';});
document.addEventListener('keydown',e=>{if(e.key==='ArrowRight')show(Math.min(cur+1,DOCS.length-1));if(e.key==='ArrowLeft')show(Math.max(cur-1,0));});
show(0);
</script>
</body>
</html>'''

ANNIV = r'''<svg class="anniv" viewBox="0 0 480 185" xmlns="http://www.w3.org/2000/svg">
<text x="12" y="128" font-family="'Space Grotesk',Arial,sans-serif" font-size="132" font-weight="700" fill="#0a56a8" font-style="italic" letter-spacing="-8">30</text>
<g fill="#e1251b">
<path d="M300 12 L275 78 L296 73 L278 128 L330 52 L307 57 L326 16 Z"/>
<path d="M258 80 L236 128 L253 124 L241 160 L276 108 L259 112 L273 78 Z"/>
</g>
<text x="205" y="120" font-family="Arial" font-size="34" font-weight="800" fill="#0a56a8" font-style="italic">años</text>
<text class="script" x="240" y="178" font-size="34" fill="#0a56a8" text-anchor="middle">Defendiendo tus derechos</text>
<path d="M300 183 Q345 176 400 182" stroke="#0a56a8" stroke-width="3" fill="none" stroke-linecap="round"/>
</svg>'''

html = TPL.replace('__DATA__', DATA).replace('__LOGO__', LOGO).replace('__ANNIV__', ANNIV)
open('/sessions/wonderful-relaxed-feynman/mnt/outputs/Informes_Adjuntia_Conflictos_Sociales.html','w',encoding='utf-8').write(html)
print('OK bytes:', len(html))

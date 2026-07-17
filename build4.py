import json, base64
data = json.load(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/data.json'))
labels = {1:"Informe Defensorial N°001-2023-DP/ACSGO",2:"Informe Defensorial N°273",3:"Informe Defensorial 278",4:"Informe Defensorial 284",5:"Informe Defensorial 279"}
shorts = {1:"N°001-2023",2:"N°273",3:"N°278",4:"N°284",5:"N°279"}
for d in data:
    d['label']=labels[d['n']]; d['short']=shorts[d['n']]
DATA = json.dumps(data, ensure_ascii=False)
LOGO='data:image/png;base64,'+base64.b64encode(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/Defensoría_del_Pueblo.png','rb').read()).decode()
ANNIV='data:image/png;base64,'+base64.b64encode(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/Logo30anos_web.png','rb').read()).decode()

TPL = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Defensoría del Pueblo · Informes y Documentos — Conflictos Sociales</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --blue:#0a56a8; --blue-d:#083b73; --blue-l:#e8f1fb; --red:#e1251b; --red-l:#fdecea;
  --ink:#0f1319; --mut:#5c6675; --mut2:#9aa4b2; --line:#e7ebf1; --soft:#f6f8fc;
  --grn:#1f9d57; --grn-l:#e7f6ee; --amb:#c47d00;
  --sh:0 10px 40px rgba(16,42,80,.10); --sh2:0 22px 70px rgba(16,42,80,.18);
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:#fff}
.bg{position:fixed;inset:0;z-index:0;background:#fff;overflow:hidden}
.orb{position:absolute;border-radius:50%;filter:blur(80px);opacity:.55;animation:float 22s ease-in-out infinite}
.o1{width:520px;height:520px;background:radial-gradient(circle,#cfe2f7,transparent 70%);top:-160px;left:-120px}
.o2{width:460px;height:460px;background:radial-gradient(circle,#fbd6d2,transparent 70%);bottom:-180px;right:6%;animation-delay:-8s}
.o3{width:420px;height:420px;background:radial-gradient(circle,#dbe9fb,transparent 70%);bottom:12%;left:34%;animation-delay:-15s}
@keyframes float{0%,100%{transform:translate(0,0)}33%{transform:translate(50px,-34px)}66%{transform:translate(-34px,28px)}}
.grid-bg{position:fixed;inset:0;z-index:0;opacity:.5;background-image:linear-gradient(rgba(10,86,168,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(10,86,168,.05) 1px,transparent 1px);background-size:48px 48px;mask:radial-gradient(circle at 50% 20%,#000,transparent 82%)}
#prog{position:fixed;top:0;left:0;height:3px;width:0;z-index:60;background:linear-gradient(90deg,var(--blue),var(--red));transition:width .1s}

.topbar{position:relative;z-index:5;display:flex;align-items:center;gap:20px;padding:16px 44px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.82);backdrop-filter:blur(12px)}
.topbar img.logo{height:54px}
.topbar .divider{width:1px;height:42px;background:var(--line)}
.topbar .ctx h1{font-family:'Sora';font-weight:700;font-size:14px;line-height:1.25}
.topbar .ctx p{font-size:11px;color:var(--mut);letter-spacing:1.4px;text-transform:uppercase;margin-top:3px}
.topbar .spacer{flex:1}
.topbar img.anniv{height:70px;border-radius:10px}

/* ===== HOME ===== */
.home{position:relative;z-index:2;max-width:1280px;margin:0 auto;padding:40px 44px 80px}
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-size:11.5px;font-weight:700;letter-spacing:1.8px;text-transform:uppercase;color:var(--blue);background:var(--blue-l);border:1px solid #cfe0f4;padding:7px 15px;border-radius:30px}
.eyebrow .pulse{width:8px;height:8px;border-radius:50%;background:var(--red);box-shadow:0 0 0 0 rgba(225,37,27,.5);animation:pulse 2s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(225,37,27,.5)}70%{box-shadow:0 0 0 10px rgba(225,37,27,0)}100%{box-shadow:0 0 0 0 rgba(225,37,27,0)}}
.hometitle{font-family:'Sora';font-weight:800;font-size:46px;line-height:1.08;margin:20px 0 12px;letter-spacing:-1px}
.hometitle .g{background:linear-gradient(100deg,var(--blue),var(--red));-webkit-background-clip:text;background-clip:text;color:transparent}
.homesub{font-size:16px;color:var(--mut);max-width:640px;line-height:1.6}

.overview{display:grid;grid-template-columns:1.15fr .85fr;gap:24px;margin-top:34px;align-items:stretch}
.kpis{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.kcard{border:1px solid var(--line);border-radius:20px;padding:22px 24px;background:#fff;box-shadow:var(--sh);position:relative;overflow:hidden;transition:.3s}
.kcard:hover{transform:translateY(-4px);box-shadow:var(--sh2)}
.kcard:before{content:"";position:absolute;left:0;top:0;height:100%;width:5px}
.kcard.k1:before{background:var(--blue)}.kcard.k2:before{background:var(--red)}.kcard.k3:before{background:var(--grn)}.kcard.k4:before{background:var(--amb)}
.kcard b{font-family:'Space Grotesk';font-size:40px;line-height:1;display:block}
.kcard.k1 b{color:var(--blue)}.kcard.k2 b{color:var(--red)}.kcard.k3 b{color:var(--grn)}.kcard.k4 b{color:var(--amb)}
.kcard span{font-size:12px;color:var(--mut);text-transform:uppercase;letter-spacing:1.2px;margin-top:8px;display:block}

.panorama{border:1px solid var(--line);border-radius:22px;padding:24px 26px;background:#fff;box-shadow:var(--sh)}
.panorama h3{font-family:'Sora';font-size:14px;font-weight:700;margin-bottom:6px}
.panorama .psub{font-size:11.5px;color:var(--mut2);margin-bottom:18px}
.prow{display:flex;align-items:center;gap:12px;margin-bottom:13px;cursor:pointer}
.prow .pl{font-family:'Space Grotesk';font-size:12px;font-weight:600;color:var(--blue-d);width:78px;flex:none}
.ptrack{flex:1;height:12px;background:var(--soft);border-radius:8px;overflow:hidden}
.pfill{height:100%;width:0;border-radius:8px;transition:width 1.1s cubic-bezier(.2,.8,.2,1)}
.pfill.ok{background:linear-gradient(90deg,#3bbd77,var(--grn))}
.pfill.no{background:linear-gradient(90deg,#ef5a4f,var(--red))}
.prow .pv{font-family:'Space Grotesk';font-size:13px;font-weight:700;width:26px;text-align:right;flex:none}
.prow:hover .pl{color:var(--red)}
.plegend{display:flex;gap:16px;margin-top:6px;font-size:11px;color:var(--mut)}
.plegend i{width:9px;height:9px;border-radius:3px;display:inline-block;margin-right:5px;vertical-align:middle}

.sec-title{display:flex;align-items:center;gap:14px;margin:52px 2px 22px}
.sec-title h2{font-family:'Sora';font-weight:700;font-size:22px}
.sec-title .ln{flex:1;height:1px;background:linear-gradient(90deg,var(--line),transparent)}
.sec-title .hintc{font-size:12px;color:var(--mut2);font-weight:600}

.mosaic{display:grid;grid-template-columns:repeat(12,1fr);gap:20px;grid-auto-rows:minmax(168px,1fr)}
.tile{position:relative;grid-column:span 6;border:1px solid var(--line);border-radius:24px;background:#fff;box-shadow:var(--sh);padding:26px 28px;cursor:pointer;overflow:hidden;display:flex;flex-direction:column;transition:.4s cubic-bezier(.2,.7,.2,1);opacity:0;transform:translateY(24px)}
.tile.in{opacity:1;transform:none}
.tile.feat{grid-column:span 6;grid-row:span 2}
.tile:hover{transform:translateY(-6px);box-shadow:var(--sh2);border-color:#cfe0f4}
.tile .ghost{position:absolute;right:-6px;top:-30px;font-family:'Space Grotesk';font-weight:700;font-size:130px;line-height:1;color:transparent;-webkit-text-stroke:2px #eef3fb;pointer-events:none;transition:.4s}
.tile.feat .ghost{font-size:210px;top:-46px}
.tile:hover .ghost{-webkit-text-stroke-color:#dbe7f7;transform:scale(1.05)}
.tile .accent{position:absolute;left:0;top:0;bottom:0;width:5px;background:linear-gradient(var(--blue),var(--red));transform:scaleY(0);transform-origin:top;transition:.45s}
.tile:hover .accent{transform:scaleY(1)}
.tile .tstate{position:absolute;top:20px;right:22px;font-size:10.5px;font-weight:700;padding:5px 11px;border-radius:20px}
.tstate.ok{color:var(--grn);background:var(--grn-l);border:1px solid #b8e6cb}
.tstate.no{color:var(--red);background:var(--red-l);border:1px solid #f6c9c4}
.tile .tlabel{font-family:'Space Grotesk';font-size:12.5px;font-weight:600;color:var(--blue);letter-spacing:.4px;position:relative;z-index:1}
.tile .ttitle{font-family:'Sora';font-weight:700;font-size:17px;line-height:1.32;margin-top:10px;position:relative;z-index:1;max-width:88%}
.tile.feat .ttitle{font-size:25px;line-height:1.24;margin-top:14px}
.tile .tmeta{margin-top:auto;padding-top:18px;display:flex;align-items:center;gap:9px;flex-wrap:wrap;position:relative;z-index:1}
.tchip{font-size:11px;padding:5px 11px;border-radius:20px;background:var(--soft);border:1px solid var(--line);color:var(--mut);font-weight:500}
.tchip.b{background:var(--blue-l);border-color:#cfe0f4;color:var(--blue);font-weight:600}
.tile .tgo{position:relative;z-index:1;margin-top:16px;display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;color:var(--red);opacity:0;transform:translateX(-8px);transition:.35s}
.tile:hover .tgo{opacity:1;transform:none}
.tile.feat .tdesc{font-size:13px;color:var(--mut);line-height:1.55;margin-top:14px;position:relative;z-index:1;max-width:92%;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}

/* ===== DETAIL ===== */
.detail{position:fixed;inset:0;z-index:40;background:#fff;overflow-y:auto;opacity:0;transform:scale(.98) translateY(14px);pointer-events:none;transition:.5s cubic-bezier(.2,.7,.2,1)}
.detail.open{opacity:1;transform:none;pointer-events:auto}
.dtop{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:16px;padding:14px 40px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.9);backdrop-filter:blur(12px)}
.back{display:inline-flex;align-items:center;gap:9px;padding:10px 18px;border-radius:12px;border:1px solid var(--line);background:#fff;cursor:pointer;font-size:13px;font-weight:600;color:var(--ink);box-shadow:var(--sh);transition:.25s}
.back:hover{background:var(--blue);color:#fff;border-color:var(--blue);transform:translateX(-3px)}
.dtop img.logo{height:40px}
.dtop .dcount{font-family:'Space Grotesk';font-size:12.5px;color:var(--mut);font-weight:600}
.dtop .spacer{flex:1}
.dnav{display:flex;gap:8px}
.dnav button{width:40px;height:40px;border-radius:11px;border:1px solid var(--line);background:#fff;cursor:pointer;font-size:16px;color:var(--ink);box-shadow:var(--sh);transition:.25s}
.dnav button:hover:not(:disabled){background:var(--blue);color:#fff;border-color:var(--blue)}
.dnav button:disabled{opacity:.3;cursor:default}
.dbody{max-width:1120px;margin:0 auto;padding:30px 40px 80px}

.hero{position:relative;border:1px solid var(--line);border-radius:26px;padding:36px 42px;overflow:hidden;background:#fff;box-shadow:var(--sh)}
.hero:before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:linear-gradient(var(--blue),var(--red))}
.hero .bignum{position:absolute;right:28px;top:-30px;font-family:'Space Grotesk';font-weight:700;font-size:200px;line-height:1;color:transparent;-webkit-text-stroke:2px #e6eefa;pointer-events:none}
.tag{display:inline-flex;align-items:center;gap:8px;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--blue);font-weight:600;border:1px solid #cfe0f4;padding:6px 13px;border-radius:20px;background:var(--blue-l)}
.doc-num{font-family:'Space Grotesk';font-size:16px;color:var(--blue-d);font-weight:700;margin:16px 0 8px}
.title{font-family:'Sora';font-weight:800;font-size:30px;line-height:1.2;max-width:82%}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.chip{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;padding:8px 14px;border-radius:12px;border:1px solid var(--line);background:var(--soft);font-weight:500}
.chip .dot{width:8px;height:8px;border-radius:50%}
.st-ok{color:var(--grn)}.st-no{color:var(--red)}
.kstrip{display:flex;gap:14px;margin:20px 0}
.ks{flex:1;border:1px solid var(--line);border-radius:16px;padding:16px 18px;background:#fff;box-shadow:var(--sh);position:relative;overflow:hidden}
.ks:before{content:"";position:absolute;left:0;top:0;height:100%;width:4px}
.ks.k1:before{background:var(--blue)}.ks.k2:before{background:var(--red)}.ks.k3:before{background:var(--grn)}.ks.k4:before{background:var(--amb)}
.ks b{font-family:'Space Grotesk';font-size:26px;display:block;line-height:1}
.ks.k1 b{color:var(--blue)}.ks.k2 b{color:var(--red)}.ks.k3 b{color:var(--grn)}.ks.k4 b{color:var(--amb)}
.ks span{font-size:10.5px;color:var(--mut);text-transform:uppercase;letter-spacing:1px;margin-top:5px;display:block}
.two{display:grid;grid-template-columns:1.05fr 1fr;gap:18px;margin-top:6px}
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
.rec{border:1px solid var(--line);border-left:5px solid var(--mut2);border-radius:18px;padding:22px 24px;background:#fff;box-shadow:var(--sh);transition:.3s}
.rec.ok{border-left-color:var(--grn)}.rec.no{border-left-color:var(--red)}
.rec:hover{transform:translateY(-3px);box-shadow:var(--sh2)}
.rec .head{display:flex;align-items:center;gap:16px;margin-bottom:14px}
.ring{--p:0;width:56px;height:56px;flex:none;border-radius:50%;display:grid;place-items:center;background:conic-gradient(var(--blue) calc(var(--p)*1%),#eaf0f8 0);position:relative}
.ring:after{content:"";position:absolute;inset:5px;border-radius:50%;background:#fff}
.ring b{position:relative;font-family:'Space Grotesk';font-size:18px;z-index:1;color:var(--blue-d)}
.rec .inst{flex:1}.rec .inst .who{font-family:'Sora';font-weight:700;font-size:15.5px}
.rec .inst .meta{font-size:11.5px;color:var(--mut);margin-top:3px}
.pill{font-size:11px;font-weight:700;padding:6px 13px;border-radius:20px;white-space:nowrap}
.pill.ok{color:var(--grn);background:var(--grn-l);border:1px solid #b8e6cb}
.pill.no{color:var(--red);background:var(--red-l);border:1px solid #f6c9c4}
.rec ul{list-style:none;display:grid;gap:9px;margin-top:4px}
.rec li{position:relative;padding-left:26px;font-size:13.5px;line-height:1.6;color:#2f3947}
.rec li:before{content:"";position:absolute;left:6px;top:8px;width:7px;height:7px;border-radius:2px;transform:rotate(45deg);background:linear-gradient(135deg,var(--blue),var(--red))}
.act{margin-top:16px;padding-top:14px;border-top:1px dashed var(--line);display:flex;gap:12px}
.act .k{font-size:10.5px;letter-spacing:1.3px;text-transform:uppercase;color:var(--amb);white-space:nowrap;padding-top:2px;font-weight:700}
.act .v{font-size:13px;color:var(--mut);line-height:1.55}
.reveal{opacity:0;transform:translateY(18px)}
.reveal.in{animation:rise .55s forwards cubic-bezier(.2,.7,.2,1)}
@keyframes rise{to{opacity:1;transform:none}}
.hint{position:fixed;bottom:14px;right:20px;z-index:50;font-size:11px;color:var(--mut2)}
kbd{font-family:'Space Grotesk';border:1px solid var(--line);border-radius:6px;padding:1px 6px;font-size:11px;color:var(--mut);background:#fff}
@media(max-width:900px){.overview{grid-template-columns:1fr}.mosaic{grid-template-columns:1fr}.tile,.tile.feat{grid-column:span 1;grid-row:auto}.two{grid-template-columns:1fr}.title{max-width:100%}.hometitle{font-size:34px}.kstrip{flex-wrap:wrap}.ks{min-width:44%}}
</style>
</head>
<body>
<div id="prog"></div>
<div class="bg"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div></div>
<div class="grid-bg"></div>

<div class="topbar">
  <img class="logo" src="__LOGO__" alt="Defensoría del Pueblo">
  <div class="divider"></div>
  <div class="ctx"><h1>Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad</h1>
    <p>Informes y Documentos · Conflictos Sociales</p></div>
  <div class="spacer"></div>
  <img class="anniv" src="__ANNIV__" alt="30 años Defendiendo tus derechos">
</div>

<div class="home" id="home">
  <span class="eyebrow"><span class="pulse"></span>Defendiendo tus derechos · 2023–2026</span>
  <div class="hometitle">Informes que <span class="g">transforman</span><br>la gestión de conflictos</div>
  <p class="homesub">Un recorrido interactivo por los informes defensoriales de la Adjuntía: objetivos, público beneficiario y las recomendaciones dirigidas a cada institución del Estado.</p>

  <div class="overview">
    <div class="kpis">
      <div class="kcard k1"><b id="ov1">0</b><span>Informes defensoriales</span></div>
      <div class="kcard k2"><b id="ov2">0</b><span>Recomendaciones</span></div>
      <div class="kcard k3"><b id="ov3">0</b><span>Instituciones alcanzadas</span></div>
      <div class="kcard k4"><b id="ov4">0</b><span>Recomendaciones acogidas</span></div>
    </div>
    <div class="panorama">
      <h3>Panorama de recomendaciones</h3>
      <div class="psub">Total de recomendaciones por informe · color según estado general</div>
      <div id="prows"></div>
      <div class="plegend"><span><i style="background:var(--grn)"></i>Acogida</span><span><i style="background:var(--red)"></i>No acogida</span></div>
    </div>
  </div>

  <div class="sec-title"><h2>Explora los informes</h2><div class="ln"></div><div class="hintc">Haz clic en una tarjeta para ver el detalle</div></div>
  <div class="mosaic" id="mosaic"></div>
</div>

<div class="detail" id="detail"><div id="detailInner"></div></div>
<div class="hint">Detalle: <kbd>&larr;</kbd> <kbd>&rarr;</kbd> &middot; <kbd>Esc</kbd> volver</div>

<script>
const DOCS = __DATA__;
const sc=s=>(s||'').toLowerCase().includes('no')?'no':'ok';
const splitRecs=t=>!t?[]:t.split(/\n+/).map(x=>x.trim()).filter(x=>x.length>2);
const recSum=d=>d.recs.reduce((s,r)=>s+(Number(r.total)||0),0);
const acogInst=d=>d.recs.filter(r=>sc(r.estado_rec)==='ok').length;

const T_INST=new Set();DOCS.forEach(d=>d.recs.forEach(r=>T_INST.add((r.institucion||'').trim())));
const T_RECS=DOCS.reduce((a,d)=>a+recSum(d),0);
const T_ACOG=DOCS.reduce((a,d)=>a+d.recs.reduce((s,r)=>s+(sc(r.estado_rec)==='ok'?(Number(r.total)||0):0),0),0);

function countUp(el,to,ms){let n=0;const step=Math.max(1,Math.ceil(to/(ms/24)));const t=setInterval(()=>{n+=step;if(n>=to){n=to;clearInterval(t)}el.textContent=n;},24);}

// panorama
const maxRecs=Math.max(...DOCS.map(recSum));
const prows=document.getElementById('prows');
DOCS.forEach((d,i)=>{
  const v=recSum(d);const st=sc(d.estado_rec);
  const row=document.createElement('div');row.className='prow';
  row.innerHTML=`<span class="pl">${d.short}</span><div class="ptrack"><div class="pfill ${st}" data-w="${Math.round(v/maxRecs*100)}"></div></div><span class="pv">${v}</span>`;
  row.onclick=()=>openDetail(i);prows.appendChild(row);
});

// mosaic
const mosaic=document.getElementById('mosaic');
DOCS.forEach((d,i)=>{
  const st=sc(d.estado_rec);const feat=i===0;
  const t=document.createElement('div');t.className='tile'+(feat?' feat':'');t.dataset.i=i;t.style.transitionDelay=(i*90)+'ms';
  t.innerHTML=`<div class="accent"></div><div class="ghost">${String(i+1).padStart(2,'0')}</div>
    <div class="tstate ${st}">${d.estado_rec}</div>
    <div class="tlabel">${d.label}</div>
    <div class="ttitle">${d.titulo.replace(/\n/g,' ')}</div>
    ${feat?`<div class="tdesc">${d.objetivo}</div>`:''}
    <div class="tmeta"><span class="tchip b">${d.anio}</span><span class="tchip">${d.linea}</span><span class="tchip">${d.recs.length} instituciones · ${recSum(d)} recom.</span></div>
    <span class="tgo">Ver informe &rarr;</span>`;
  t.onclick=()=>openDetail(i);mosaic.appendChild(t);
});

// intro animations
window.addEventListener('load',()=>{
  countUp(document.getElementById('ov1'),DOCS.length,700);
  countUp(document.getElementById('ov2'),T_RECS,1100);
  countUp(document.getElementById('ov3'),T_INST.size,1000);
  countUp(document.getElementById('ov4'),T_ACOG,900);
  setTimeout(()=>document.querySelectorAll('.pfill').forEach(f=>f.style.width=f.dataset.w+'%'),300);
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1});
  document.querySelectorAll('.tile').forEach(el=>io.observe(el));
});

// DETAIL
const detail=document.getElementById('detail');const dInner=document.getElementById('detailInner');
let cur=-1;
function detailHTML(i){
  const d=DOCS[i];const mx=Math.max(...d.recs.map(r=>Number(r.total)||0),1);
  const recsHtml=d.recs.map(r=>{
    const items=splitRecs(r.texto).map(x=>`<li>${x.replace(/^[IVX0-9]+[\.\)]\s*/,'')}</li>`).join('');
    const p=Math.round((Number(r.total)||0)/mx*100);const cls=sc(r.estado_rec);
    const act=r.acciones?`<div class="act"><div class="k">Acciones futuras</div><div class="v">${r.acciones}</div></div>`:'';
    return `<div class="rec ${cls} reveal"><div class="head"><div class="ring" style="--p:${p}"><b>${r.total||'–'}</b></div>
      <div class="inst"><div class="who">${r.institucion||'—'}</div><div class="meta">${r.total||0} recomendación(es) dirigidas</div></div>
      <div class="pill ${cls}">${r.estado_rec||'—'}</div></div><ul>${items}</ul>${act}</div>`;
  }).join('');
  const st=sc(d.estado_rec);
  return `<div class="dtop">
      <button class="back" onclick="closeDetail()">&larr; Volver al mosaico</button>
      <img class="logo" src="__LOGO__">
      <span class="dcount">Informe ${String(i+1).padStart(2,'0')} / ${String(DOCS.length).padStart(2,'0')}</span>
      <div class="spacer"></div>
      <div class="dnav"><button id="dp">&larr;</button><button id="dn">&rarr;</button></div>
    </div>
    <div class="dbody"><div class="fade">
      <section class="hero reveal"><div class="bignum">${String(i+1).padStart(2,'0')}</div>
        <span class="tag">&#9670; ${d.tipo} &middot; ${d.estado}</span>
        <div class="doc-num">${d.label}</div>
        <div class="title">${d.titulo.replace(/\n/g,' ')}</div>
        <div class="chips">
          <span class="chip"><span class="dot" style="background:var(--blue)"></span>Año ${d.anio}</span>
          <span class="chip"><span class="dot" style="background:var(--blue-d)"></span>Publicado ${d.fecha||'—'}</span>
          <span class="chip"><span class="dot" style="background:var(--red)"></span>${d.linea}</span>
          <span class="chip ${st==='ok'?'st-ok':'st-no'}"><span class="dot" style="background:${st==='ok'?'var(--grn)':'var(--red)'}"></span>${d.estado_rec}</span>
        </div></section>
      <div class="kstrip">
        <div class="ks k1"><b>${d.recs.length}</b><span>Instituciones</span></div>
        <div class="ks k2"><b>${recSum(d)}</b><span>Recomendaciones</span></div>
        <div class="ks k3"><b>${acogInst(d)}</b><span>Entidades con acogida</span></div>
        <div class="ks k4"><b>${d.anio}</b><span>Año de publicación</span></div>
      </div>
      <div class="two">
        <div class="panel reveal"><div class="lbl"><i>&#9673;</i>Objetivo del documento</div><p>${d.objetivo}</p></div>
        <div class="panel reveal"><div class="lbl r"><i>&#10070;</i>Público beneficiario</div><p>${d.publico}</p></div>
      </div>
      <div class="sec-h"><h3>Recomendaciones por institución</h3><div class="line"></div><div class="cnt">${d.recs.length} entidad(es)</div></div>
      <div class="recs">${recsHtml}</div>
    </div></div>`;
}
function openDetail(i){
  cur=i;dInner.innerHTML=detailHTML(i);
  detail.classList.add('open');detail.scrollTop=0;document.body.style.overflow='hidden';
  const dp=document.getElementById('dp'),dn=document.getElementById('dn');
  dp.disabled=i===0;dn.disabled=i===DOCS.length-1;
  dp.onclick=()=>openDetail(i-1);dn.onclick=()=>openDetail(i+1);
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{root:detail,threshold:.1});
  detail.querySelectorAll('.reveal').forEach(el=>io.observe(el));
}
function closeDetail(){detail.classList.remove('open');document.body.style.overflow='';cur=-1;}
detail.addEventListener('scroll',()=>{const p=detail.scrollTop/(detail.scrollHeight-detail.clientHeight||1);document.getElementById('prog').style.width=(p*100)+'%';});
document.addEventListener('keydown',e=>{
  if(!detail.classList.contains('open'))return;
  if(e.key==='Escape')closeDetail();
  if(e.key==='ArrowRight'&&cur<DOCS.length-1)openDetail(cur+1);
  if(e.key==='ArrowLeft'&&cur>0)openDetail(cur-1);
});
</script>
</body>
</html>'''

html=TPL.replace('__DATA__',DATA).replace('__LOGO__',LOGO).replace('__ANNIV__',ANNIV)
open('/sessions/wonderful-relaxed-feynman/mnt/outputs/Informes_Adjuntia_Conflictos_Sociales.html','w',encoding='utf-8').write(html)
print('OK bytes:',len(html))

import json, base64
data = json.load(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/data.json'))
labels = {1:"Informe Defensorial N°001-2023-DP/ACSGO",2:"Informe Defensorial N°273",3:"Informe Defensorial 278",4:"Informe Defensorial 284",5:"Informe Defensorial 279",6:"Informe Jurídico Defensorial N°001-2025-DP/ACSGO",7:"Informe Técnico Legal N°003-2025-DP/ACSGO",8:"Informe Técnico Legal N°004-2025-DP/ACSGO"}
shorts = {1:"N°001-2023",2:"N°273",3:"N°278",4:"N°284",5:"N°279",6:"N°001-2025",7:"N°003-2025",8:"N°004-2025"}
for d in data:
    d['label']=labels[d['n']]; d['short']=shorts[d['n']]
DATA = json.dumps(data, ensure_ascii=False)
LOGO='data:image/png;base64,'+base64.b64encode(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/Defensoría_del_Pueblo.png','rb').read()).decode()
ANNIV='data:image/png;base64,'+base64.b64encode(open('/sessions/wonderful-relaxed-feynman/mnt/outputs/Logo30anos_web.png','rb').read()).decode()

TPL = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Defensoría del Pueblo · Panel Ejecutivo — Informes de Conflictos Sociales</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
@property --p{syntax:'<number>';inherits:true;initial-value:0}
:root{
  --blue:#0a56a8; --blue-d:#083b73; --blue-l:#e8f1fb; --red:#e1251b; --red-l:#fdecea;
  --ink:#0f1319; --mut:#5c6675; --mut2:#98a2b3; --line:#e7ebf1; --soft:#f6f8fc;
  --grn:#12a45a; --grn-l:#e7f6ee; --amb:#c47d00;
  --glass:rgba(255,255,255,.60); --glass-2:rgba(255,255,255,.78); --gbrd:rgba(255,255,255,.85);
  --sh:0 10px 34px rgba(16,42,80,.10); --sh2:0 30px 70px rgba(16,42,80,.20);
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:#eef2f8}
/* rich mesh background so glass reads premium */
.bg{position:fixed;inset:0;z-index:0;overflow:hidden;background:
  radial-gradient(60% 50% at 12% 6%,#dbe8fb,transparent 60%),
  radial-gradient(55% 55% at 92% 8%,#fbe0dc,transparent 60%),
  radial-gradient(70% 60% at 50% 100%,#e3ecfb,transparent 60%),
  linear-gradient(180deg,#f3f6fb,#eaf0f8)}
.orb{position:absolute;border-radius:50%;filter:blur(70px);opacity:.6;animation:float 24s ease-in-out infinite}
.o1{width:520px;height:520px;background:radial-gradient(circle,#bcd6f6,transparent 70%);top:-150px;left:-120px}
.o2{width:480px;height:480px;background:radial-gradient(circle,#f9cec8,transparent 70%);top:8%;right:-120px;animation-delay:-8s}
.o3{width:460px;height:460px;background:radial-gradient(circle,#c9def8,transparent 70%);bottom:-160px;left:36%;animation-delay:-15s}
@keyframes float{0%,100%{transform:translate(0,0)}33%{transform:translate(46px,-30px)}66%{transform:translate(-32px,26px)}}
.gridlines{position:fixed;inset:0;z-index:0;opacity:.4;background-image:linear-gradient(rgba(10,86,168,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(10,86,168,.06) 1px,transparent 1px);background-size:52px 52px;mask:radial-gradient(circle at 50% 20%,#000,transparent 82%)}
#prog{position:fixed;top:0;left:0;height:3px;width:0;z-index:60;background:linear-gradient(90deg,var(--blue),var(--red));transition:width .12s}

.topbar{position:sticky;top:0;z-index:30;display:flex;align-items:center;gap:20px;padding:14px 44px;border-bottom:1px solid var(--gbrd);background:var(--glass-2);backdrop-filter:blur(18px) saturate(140%)}
.topbar img.logo{height:52px}
.topbar .divider{width:1px;height:40px;background:var(--line)}
.topbar .ctx h1{font-family:'Sora';font-weight:700;font-size:14px;line-height:1.25}
.topbar .ctx p{font-size:11px;color:var(--mut);letter-spacing:1.4px;text-transform:uppercase;margin-top:3px}
.topbar .spacer{flex:1}
.topbar img.anniv{height:70px;border-radius:10px}

.home{position:relative;z-index:2;max-width:1300px;margin:0 auto;padding:40px 44px 90px}
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-size:11.5px;font-weight:700;letter-spacing:1.8px;text-transform:uppercase;color:var(--blue);background:var(--glass);border:1px solid var(--gbrd);backdrop-filter:blur(10px);padding:7px 15px;border-radius:30px;box-shadow:var(--sh)}
.eyebrow .pulse{width:8px;height:8px;border-radius:50%;background:var(--red);animation:pulse 2s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(225,37,27,.5)}70%{box-shadow:0 0 0 10px rgba(225,37,27,0)}100%{box-shadow:0 0 0 0 rgba(225,37,27,0)}}
.hometitle{font-family:'Sora';font-weight:800;font-size:48px;line-height:1.06;margin:20px 0 12px;letter-spacing:-1.2px}
.hometitle .g{background:linear-gradient(100deg,var(--blue),var(--red));-webkit-background-clip:text;background-clip:text;color:transparent}
.homesub{font-size:16px;color:var(--mut);max-width:660px;line-height:1.6}

.rise{opacity:0;transform:translateY(26px);animation:riseIn .7s forwards cubic-bezier(.2,.75,.2,1)}
@keyframes riseIn{to{opacity:1;transform:none}}

.overview{display:grid;grid-template-columns:1.1fr .9fr;gap:22px;margin-top:34px}
.scene{perspective:1400px}
.kpis{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.kcard{transform-style:preserve-3d;border:1px solid var(--gbrd);border-radius:22px;padding:24px 26px;background:var(--glass);backdrop-filter:blur(18px) saturate(150%);box-shadow:var(--sh);position:relative;overflow:hidden;transition:transform .4s cubic-bezier(.2,.7,.2,1),box-shadow .4s}
.kcard:hover{transform:translateY(-8px) translateZ(40px) rotateX(3deg);box-shadow:var(--sh2)}
.kcard:before{content:"";position:absolute;left:0;top:0;height:100%;width:5px}
.kcard.k1:before{background:var(--blue)}.kcard.k2:before{background:var(--red)}.kcard.k3:before{background:var(--grn)}.kcard.k4:before{background:var(--amb)}
.kcard .ico{font-size:16px;opacity:.5;position:absolute;top:20px;right:22px}
.kcard b{font-family:'Space Grotesk';font-size:42px;line-height:1;display:block;transform:translateZ(30px)}
.kcard.k1 b{color:var(--blue)}.kcard.k2 b{color:var(--red)}.kcard.k3 b{color:var(--grn)}.kcard.k4 b{color:var(--amb)}
.kcard span{font-size:12px;color:var(--mut);text-transform:uppercase;letter-spacing:1.1px;margin-top:9px;display:block}

.panorama{border:1px solid var(--gbrd);border-radius:24px;padding:26px 28px;background:var(--glass);backdrop-filter:blur(18px) saturate(150%);box-shadow:var(--sh)}
.panorama h3{font-family:'Sora';font-size:15px;font-weight:700}
.panorama .psub{font-size:11.5px;color:var(--mut2);margin:4px 0 18px}
.donutwrap{display:flex;align-items:center;gap:22px;margin-bottom:20px}
.donut{--p:0;width:132px;height:132px;flex:none;border-radius:50%;position:relative;
  background:conic-gradient(var(--grn) calc(var(--p)*1%), #f0c9c5 0);transition:--p 1.5s cubic-bezier(.2,.8,.2,1);
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.6),0 12px 30px rgba(16,42,80,.14)}
.donut:after{content:"";position:absolute;inset:16px;border-radius:50%;background:var(--glass-2);backdrop-filter:blur(6px);box-shadow:inset 0 2px 8px rgba(16,42,80,.08)}
.donut .dc{position:absolute;inset:0;display:grid;place-items:center;text-align:center;z-index:1}
.donut .dc b{font-family:'Space Grotesk';font-size:30px;color:var(--grn);line-height:1}
.donut .dc small{font-size:9.5px;color:var(--mut);text-transform:uppercase;letter-spacing:1px;display:block;margin-top:2px}
.dside{flex:1}
.dstat{display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid var(--line)}
.dstat:last-child{border-bottom:0}
.dstat .sw{width:12px;height:12px;border-radius:4px;flex:none}
.dstat .nm{font-size:12.5px;color:var(--mut);flex:1}
.dstat .vl{font-family:'Space Grotesk';font-weight:700;font-size:16px}
.pbars{margin-top:6px}
.pbtitle{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:var(--mut2);font-weight:700;margin-bottom:12px}
.prow{display:flex;align-items:center;gap:12px;margin-bottom:12px;cursor:pointer}
.prow .pl{font-family:'Space Grotesk';font-size:12px;font-weight:600;color:var(--blue-d);width:76px;flex:none}
.ptrack{flex:1;height:14px;background:rgba(16,42,80,.06);border-radius:8px;overflow:hidden;display:flex}
.seg{height:100%;width:0;transition:width 1.1s cubic-bezier(.2,.8,.2,1)}
.seg.ok{background:linear-gradient(90deg,#28c274,var(--grn))}
.seg.no{background:linear-gradient(90deg,#ef5a4f,var(--red))}
.prow .pv{font-family:'Space Grotesk';font-size:13px;font-weight:700;width:26px;text-align:right;flex:none}
.prow:hover .pl{color:var(--red)}

.sec-title{display:flex;align-items:center;gap:14px;margin:54px 2px 22px}
.sec-title h2{font-family:'Sora';font-weight:700;font-size:23px}
.sec-title .ln{flex:1;height:1px;background:linear-gradient(90deg,var(--line),transparent)}
.sec-title .hintc{font-size:12px;color:var(--mut2);font-weight:600}

.mosaic{display:grid;grid-template-columns:repeat(12,1fr);gap:22px;grid-auto-rows:minmax(172px,1fr)}
.tile{transform-style:preserve-3d;position:relative;grid-column:span 6;border:1px solid var(--gbrd);border-radius:26px;background:var(--glass);backdrop-filter:blur(18px) saturate(150%);box-shadow:var(--sh);padding:28px 30px;cursor:pointer;overflow:hidden;display:flex;flex-direction:column;transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s,border-color .35s;will-change:transform}
.tile.feat{grid-column:span 12;min-height:230px}
.tile.wide{grid-column:span 12}
.tstate.mix{color:var(--amb);background:#fdf3e0;border:1px solid #f0d8a8}
.st-mix{color:var(--amb)}
.tile:hover{box-shadow:var(--sh2);border-color:#cfe0f4}
.tile>*{transform:translateZ(0)}
.tile .ghost{position:absolute;right:-4px;top:-30px;font-family:'Space Grotesk';font-weight:700;font-size:132px;line-height:1;color:transparent;-webkit-text-stroke:2px rgba(10,86,168,.10);pointer-events:none;transition:.4s;transform:translateZ(10px)}
.tile.feat .ghost{font-size:190px;top:-40px}
.tile:hover .ghost{-webkit-text-stroke-color:rgba(10,86,168,.20)}
.tile .accent{position:absolute;left:0;top:0;bottom:0;width:5px;background:linear-gradient(var(--blue),var(--red));transform:scaleY(0);transform-origin:top;transition:.45s}
.tile:hover .accent{transform:scaleY(1)}
.tile .tstate{position:absolute;top:22px;right:24px;font-size:10.5px;font-weight:700;padding:5px 11px;border-radius:20px;transform:translateZ(40px)}
.tstate.ok{color:var(--grn);background:var(--grn-l);border:1px solid #b8e6cb}
.tstate.no{color:var(--red);background:var(--red-l);border:1px solid #f6c9c4}
.tile .tlabel{font-family:'Space Grotesk';font-size:12.5px;font-weight:600;color:var(--blue);letter-spacing:.4px;position:relative;z-index:1;transform:translateZ(45px)}
.tile .ttitle{font-family:'Sora';font-weight:700;font-size:17.5px;line-height:1.32;margin-top:10px;position:relative;z-index:1;max-width:88%;transform:translateZ(30px)}
.tile.feat .ttitle{font-size:25px;line-height:1.24;margin-top:12px;max-width:74%}
.tile .tmeta{margin-top:auto;padding-top:18px;display:flex;align-items:center;gap:9px;flex-wrap:wrap;position:relative;z-index:1;transform:translateZ(24px)}
.tchip{font-size:11px;padding:5px 11px;border-radius:20px;background:rgba(255,255,255,.55);border:1px solid var(--line);color:var(--mut);font-weight:500}
.tchip.b{background:var(--blue-l);border-color:#cfe0f4;color:var(--blue);font-weight:600}
.tile .tgo{position:relative;z-index:1;margin-top:16px;display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;color:var(--red);opacity:0;transform:translateX(-8px) translateZ(40px);transition:.35s}
.tile:hover .tgo{opacity:1;transform:translateZ(40px)}
.tile.feat .tdesc{font-size:13px;color:var(--mut);line-height:1.55;margin-top:12px;position:relative;z-index:1;max-width:70%;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;transform:translateZ(20px)}

/* OFFCANVAS */
.scrim{position:fixed;inset:0;z-index:39;background:rgba(9,16,32,.55);backdrop-filter:blur(7px);opacity:0;pointer-events:none;transition:.45s}
.scrim.open{opacity:1;pointer-events:auto}
.off{position:fixed;top:0;right:0;height:100vh;width:min(750px,95vw);z-index:41;background:var(--glass-2);backdrop-filter:blur(24px) saturate(150%);border-left:1px solid var(--gbrd);box-shadow:-34px 0 90px rgba(9,16,32,.34);transform:translateX(102%);transition:transform .55s cubic-bezier(.3,.85,.2,1);overflow-y:auto}
.off.open{transform:none}
.offtop{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:14px;padding:16px 26px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.72);backdrop-filter:blur(16px)}
.close{width:40px;height:40px;border-radius:12px;border:1px solid var(--line);background:#fff;cursor:pointer;font-size:17px;color:var(--ink);box-shadow:var(--sh);transition:.25s}
.close:hover{background:var(--red);color:#fff;border-color:var(--red);transform:rotate(90deg)}
.offtop .dcount{font-family:'Space Grotesk';font-size:12.5px;color:var(--mut);font-weight:600}
.offtop .spacer{flex:1}
.dnav{display:flex;gap:8px}
.dnav button{width:40px;height:40px;border-radius:12px;border:1px solid var(--line);background:#fff;cursor:pointer;font-size:16px;color:var(--ink);box-shadow:var(--sh);transition:.25s}
.dnav button:hover:not(:disabled){background:var(--blue);color:#fff;border-color:var(--blue)}
.dnav button:disabled{opacity:.3;cursor:default}
.offbody{padding:26px 30px 70px}

.hero{position:relative;border:1px solid var(--gbrd);border-radius:24px;padding:30px 32px;overflow:hidden;background:var(--glass);box-shadow:var(--sh)}
.hero:before{content:"";position:absolute;left:0;top:0;bottom:0;width:6px;background:linear-gradient(var(--blue),var(--red))}
.hero .bignum{position:absolute;right:20px;top:-26px;font-family:'Space Grotesk';font-weight:700;font-size:150px;line-height:1;color:transparent;-webkit-text-stroke:2px rgba(10,86,168,.09);pointer-events:none}
.tag{display:inline-flex;align-items:center;gap:8px;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--blue);font-weight:600;border:1px solid #cfe0f4;padding:6px 13px;border-radius:20px;background:var(--blue-l)}
.doc-num{font-family:'Space Grotesk';font-size:15px;color:var(--blue-d);font-weight:700;margin:15px 0 8px}
.title{font-family:'Sora';font-weight:800;font-size:24px;line-height:1.22;max-width:94%}
.chips{display:flex;flex-wrap:wrap;gap:9px;margin-top:20px}
.chip{display:inline-flex;align-items:center;gap:8px;font-size:12px;padding:7px 13px;border-radius:12px;border:1px solid var(--line);background:rgba(255,255,255,.6);font-weight:500}
.chip .dot{width:8px;height:8px;border-radius:50%}
.st-ok{color:var(--grn)}.st-no{color:var(--red)}
.kstrip{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin:18px 0}
.ks{border:1px solid var(--gbrd);border-radius:16px;padding:16px 18px;background:var(--glass);box-shadow:var(--sh);position:relative;overflow:hidden}
.ks:before{content:"";position:absolute;left:0;top:0;height:100%;width:4px}
.ks.k1:before{background:var(--blue)}.ks.k2:before{background:var(--red)}.ks.k3:before{background:var(--grn)}.ks.k4:before{background:var(--amb)}
.ks b{font-family:'Space Grotesk';font-size:26px;display:block;line-height:1}
.ks.k1 b{color:var(--blue)}.ks.k2 b{color:var(--red)}.ks.k3 b{color:var(--grn)}.ks.k4 b{color:var(--amb)}
.ks span{font-size:10.5px;color:var(--mut);text-transform:uppercase;letter-spacing:1px;margin-top:5px;display:block}
.panel{border:1px solid var(--gbrd);border-radius:18px;padding:22px 24px;background:var(--glass);box-shadow:var(--sh);margin-top:14px}
.panel .lbl{font-size:11px;letter-spacing:1.6px;text-transform:uppercase;color:var(--mut);margin-bottom:12px;display:flex;align-items:center;gap:10px;font-weight:700}
.panel .lbl i{width:28px;height:28px;border-radius:9px;display:grid;place-items:center;font-style:normal;font-size:14px;color:#fff;background:linear-gradient(135deg,var(--blue),var(--blue-d))}
.panel .lbl.r i{background:linear-gradient(135deg,var(--red),#b41b13)}
.panel p{font-size:14px;line-height:1.65;color:#2a3340}
.sec-h{display:flex;align-items:center;gap:14px;margin:28px 2px 14px}
.sec-h h3{font-family:'Sora';font-weight:700;font-size:16px}
.sec-h .line{flex:1;height:1px;background:linear-gradient(90deg,var(--line),transparent)}
.sec-h .cnt{font-size:12px;color:var(--mut2);font-weight:600}
.recs{display:grid;gap:14px}
.rec{border:1px solid var(--gbrd);border-left:5px solid var(--mut2);border-radius:18px;padding:20px 22px;background:var(--glass);box-shadow:var(--sh);transition:.3s}
.rec.ok{border-left-color:var(--grn)}.rec.no{border-left-color:var(--red)}
.rec:hover{transform:translateY(-3px);box-shadow:var(--sh2)}
.rec .head{display:flex;align-items:center;gap:14px;margin-bottom:12px}
.ring{--q:0;width:52px;height:52px;flex:none;border-radius:50%;display:grid;place-items:center;background:conic-gradient(var(--blue) calc(var(--q)*1%),#e2e9f3 0);position:relative}
.ring:after{content:"";position:absolute;inset:5px;border-radius:50%;background:#fff}
.ring b{position:relative;font-family:'Space Grotesk';font-size:17px;z-index:1;color:var(--blue-d)}
.rec .inst{flex:1}.rec .inst .who{font-family:'Sora';font-weight:700;font-size:14.5px}
.rec .inst .meta{font-size:11px;color:var(--mut);margin-top:3px}
.pill{font-size:10.5px;font-weight:700;padding:6px 12px;border-radius:20px;white-space:nowrap}
.pill.ok{color:var(--grn);background:var(--grn-l);border:1px solid #b8e6cb}
.pill.no{color:var(--red);background:var(--red-l);border:1px solid #f6c9c4}
.rec ul{list-style:none;display:grid;gap:8px;margin-top:4px}
.rec li{position:relative;padding-left:24px;font-size:13px;line-height:1.58;color:#2f3947}
.rec li:before{content:"";position:absolute;left:5px;top:8px;width:7px;height:7px;border-radius:2px;transform:rotate(45deg);background:linear-gradient(135deg,var(--blue),var(--red))}
.act{margin-top:14px;padding-top:12px;border-top:1px dashed var(--line);display:flex;gap:11px}
.act .k{font-size:10px;letter-spacing:1.2px;text-transform:uppercase;color:var(--amb);white-space:nowrap;padding-top:2px;font-weight:700}
.act .v{font-size:12.5px;color:var(--mut);line-height:1.55}
.reveal{opacity:0;transform:translateY(16px)}
.reveal.in{animation:riseIn .55s forwards cubic-bezier(.2,.7,.2,1)}
.hint{position:fixed;bottom:14px;right:20px;z-index:38;font-size:11px;color:var(--mut2)}
kbd{font-family:'Space Grotesk';border:1px solid var(--line);border-radius:6px;padding:1px 6px;font-size:11px;color:var(--mut);background:#fff}
@media(max-width:900px){.overview{grid-template-columns:1fr}.mosaic{grid-template-columns:1fr}.tile,.tile.feat{grid-column:span 1;grid-row:auto}.hometitle{font-size:34px}.off{width:100vw}}
</style>
</head>
<body>
<div id="prog"></div>
<div class="bg"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div></div>
<div class="gridlines"></div>

<div class="topbar">
  <img class="logo" src="__LOGO__" alt="Defensoría del Pueblo">
  <div class="divider"></div>
  <div class="ctx"><h1>Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad</h1>
    <p>Panel Ejecutivo · Informes y Documentos</p></div>
  <div class="spacer"></div>
  <img class="anniv" src="__ANNIV__" alt="30 años Defendiendo tus derechos">
</div>

<div class="home">
  <span class="eyebrow rise"><span class="pulse"></span>Defendiendo tus derechos · 2023–2026</span>
  <div class="hometitle rise" style="animation-delay:.06s">Informes que <span class="g">transforman</span><br>la gestión de conflictos</div>
  <p class="homesub rise" style="animation-delay:.12s">Panel interactivo de los informes defensoriales de la Adjuntía: objetivos, público beneficiario y las recomendaciones dirigidas a cada institución del Estado, con su nivel de acogida.</p>

  <div class="overview">
    <div class="kpis scene">
      <div class="kcard k1 rise" style="animation-delay:.18s"><div class="ico">▤</div><b id="ov1">0</b><span>Informes defensoriales</span></div>
      <div class="kcard k2 rise" style="animation-delay:.26s"><div class="ico">◆</div><b id="ov2">0</b><span>Recomendaciones</span></div>
      <div class="kcard k3 rise" style="animation-delay:.34s"><div class="ico">◎</div><b id="ov3">0</b><span>Instituciones alcanzadas</span></div>
      <div class="kcard k4 rise" style="animation-delay:.42s"><div class="ico">✓</div><b id="ov4">0</b><span>Recomendaciones acogidas</span></div>
    </div>
    <div class="panorama rise" style="animation-delay:.5s">
      <h3>Panorama de recomendaciones</h3>
      <div class="psub">Nivel de acogida del Estado y distribución por informe</div>
      <div class="donutwrap">
        <div class="donut" id="donut"><div class="dc"><b id="dpct">0%</b><small>Acogidas</small></div></div>
        <div class="dside">
          <div class="dstat"><span class="sw" style="background:var(--grn)"></span><span class="nm">Acogidas</span><span class="vl" id="dok" style="color:var(--grn)">0</span></div>
          <div class="dstat"><span class="sw" style="background:var(--red)"></span><span class="nm">No acogidas</span><span class="vl" id="dno" style="color:var(--red)">0</span></div>
          <div class="dstat"><span class="sw" style="background:var(--blue)"></span><span class="nm">Total emitidas</span><span class="vl" id="dtot" style="color:var(--blue)">0</span></div>
        </div>
      </div>
      <div class="pbars"><div class="pbtitle">Recomendaciones por informe</div><div id="prows"></div></div>
    </div>
  </div>

  <div class="sec-title rise" style="animation-delay:.58s"><h2>Explora los informes</h2><div class="ln"></div><div class="hintc">Haz clic en una tarjeta para abrir el detalle →</div></div>
  <div class="mosaic scene" id="mosaic"></div>
</div>

<div class="scrim" id="scrim" onclick="closeDetail()"></div>
<aside class="off" id="off"><div id="offInner"></div></aside>
<div class="hint">Panel: <kbd>&larr;</kbd> <kbd>&rarr;</kbd> &middot; <kbd>Esc</kbd> cerrar</div>

<script>
const DOCS = __DATA__;
const sc=s=>(s||'').toLowerCase().includes('no')?'no':'ok';
const splitRecs=t=>!t?[]:t.split(/\n+/).map(x=>x.trim()).filter(x=>x.length>2);
const recSum=d=>d.recs.reduce((s,r)=>s+(Number(r.total)||0),0);
const okRecs=d=>d.recs.reduce((s,r)=>s+(sc(r.estado_rec)==='ok'?(Number(r.total)||0):0),0);
const noRecs=d=>d.recs.reduce((s,r)=>s+(sc(r.estado_rec)==='no'?(Number(r.total)||0):0),0);
const acogInst=d=>d.recs.filter(r=>sc(r.estado_rec)==='ok').length;
const docState=d=>{const okc=acogInst(d),n=d.recs.length;if(okc===0)return{cls:'no',text:'No acogida'};if(okc===n)return{cls:'ok',text:'Acogida'};return{cls:'mix',text:okc+' de '+n+' acogidas'};};

const T_INST=new Set();DOCS.forEach(d=>d.recs.forEach(r=>T_INST.add((r.institucion||'').trim())));
const T_RECS=DOCS.reduce((a,d)=>a+recSum(d),0);
const T_OK=DOCS.reduce((a,d)=>a+okRecs(d),0);
const T_NO=T_RECS-T_OK;
const PCT=Math.round(T_OK/T_RECS*100);

function countUp(el,to,ms,suf){let n=0;const step=Math.max(1,Math.ceil(to/(ms/24)));const t=setInterval(()=>{n+=step;if(n>=to){n=to;clearInterval(t)}el.textContent=n+(suf||'');},24);}

const maxRecs=Math.max(...DOCS.map(recSum));
const prows=document.getElementById('prows');
DOCS.forEach((d,i)=>{
  const ok=okRecs(d),no=noRecs(d),v=recSum(d);
  const row=document.createElement('div');row.className='prow';
  row.innerHTML=`<span class="pl">${d.short}</span><div class="ptrack">
    <span class="seg ok" data-w="${ok/maxRecs*100}"></span><span class="seg no" data-w="${no/maxRecs*100}"></span></div>
    <span class="pv">${v}</span>`;
  row.onclick=()=>openDetail(i);prows.appendChild(row);
});

const mosaic=document.getElementById('mosaic');
DOCS.forEach((d,i)=>{
  const ds=docState(d);const feat=i===0;
  const wide=(DOCS.length%2===0)&&(i===DOCS.length-1);
  const t=document.createElement('div');
  t.className='tile'+(feat?' feat':'')+(wide?' wide':'')+' rise';t.dataset.i=i;t.style.animationDelay=(.62+i*.08)+'s';
  t.innerHTML=`<div class="accent"></div><div class="ghost">${String(i+1).padStart(2,'0')}</div>
    <div class="tstate ${ds.cls}">${ds.text}</div>
    <div class="tlabel">${d.label}</div>
    <div class="ttitle">${d.titulo.replace(/\n/g,' ')}</div>
    ${feat?`<div class="tdesc">${d.objetivo}</div>`:''}
    <div class="tmeta"><span class="tchip b">${d.anio}</span><span class="tchip">${d.linea}</span><span class="tchip">${d.recs.length} instituciones · ${recSum(d)} recom.</span></div>
    <span class="tgo">Ver informe &rarr;</span>`;
  t.onclick=()=>openDetail(i);
  // 3D tilt
  t.addEventListener('mousemove',e=>{const r=t.getBoundingClientRect();const px=(e.clientX-r.left)/r.width-.5;const py=(e.clientY-r.top)/r.height-.5;t.style.transform=`translateY(-8px) rotateX(${-py*5}deg) rotateY(${px*6}deg) translateZ(20px)`;});
  t.addEventListener('mouseleave',()=>{t.style.transform='';});
  mosaic.appendChild(t);
});

window.addEventListener('load',()=>{
  countUp(document.getElementById('ov1'),DOCS.length,700);
  countUp(document.getElementById('ov2'),T_RECS,1100);
  countUp(document.getElementById('ov3'),T_INST.size,1000);
  countUp(document.getElementById('ov4'),T_OK,1200);
  setTimeout(()=>{
    document.getElementById('donut').style.setProperty('--p',PCT);
    countUp(document.getElementById('dpct'),PCT,1400,'%');
    countUp(document.getElementById('dok'),T_OK,1400);
    countUp(document.getElementById('dno'),T_NO,1400);
    countUp(document.getElementById('dtot'),T_RECS,1400);
    document.querySelectorAll('.seg').forEach(s=>s.style.width=parseFloat(s.dataset.w)+'%');
  },500);
});

const scrim=document.getElementById('scrim'),off=document.getElementById('off'),offInner=document.getElementById('offInner');
let cur=-1;
function detailHTML(i){
  const d=DOCS[i];const mx=Math.max(...d.recs.map(r=>Number(r.total)||0),1);
  const recsHtml=d.recs.map(r=>{
    const items=splitRecs(r.texto).map(x=>`<li>${x.replace(/^[IVX0-9]+[\.\)]\s*/,'')}</li>`).join('');
    const q=Math.round((Number(r.total)||0)/mx*100);const cls=sc(r.estado_rec);
    const act=r.acciones?`<div class="act"><div class="k">Acciones futuras</div><div class="v">${r.acciones}</div></div>`:'';
    return `<div class="rec ${cls} reveal"><div class="head"><div class="ring" style="--q:${q}"><b>${r.total||'–'}</b></div>
      <div class="inst"><div class="who">${r.institucion||'—'}</div><div class="meta">${r.total||0} recomendación(es) dirigidas</div></div>
      <div class="pill ${cls}">${r.estado_rec||'—'}</div></div><ul>${items}</ul>${act}</div>`;
  }).join('');
  const ds=docState(d);
  return `<div class="offtop">
      <button class="close" onclick="closeDetail()">✕</button>
      <span class="dcount">Informe ${String(i+1).padStart(2,'0')} / ${String(DOCS.length).padStart(2,'0')}</span>
      <div class="spacer"></div>
      <div class="dnav"><button id="dp">&larr;</button><button id="dn">&rarr;</button></div>
    </div>
    <div class="offbody">
      <section class="hero reveal"><div class="bignum">${String(i+1).padStart(2,'0')}</div>
        <span class="tag">&#9670; ${d.tipo} &middot; ${d.estado}</span>
        <div class="doc-num">${d.label}</div>
        <div class="title">${d.titulo.replace(/\n/g,' ')}</div>
        <div class="chips">
          <span class="chip"><span class="dot" style="background:var(--blue)"></span>Año ${d.anio}</span>
          <span class="chip"><span class="dot" style="background:var(--blue-d)"></span>Publicado ${d.fecha||'—'}</span>
          <span class="chip"><span class="dot" style="background:var(--red)"></span>${d.linea}</span>
          <span class="chip ${ds.cls==='ok'?'st-ok':ds.cls==='no'?'st-no':'st-mix'}"><span class="dot" style="background:${ds.cls==='ok'?'var(--grn)':ds.cls==='no'?'var(--red)':'var(--amb)'}"></span>${ds.text}</span>
        </div></section>
      <div class="kstrip">
        <div class="ks k1"><b>${d.recs.length}</b><span>Instituciones</span></div>
        <div class="ks k2"><b>${recSum(d)}</b><span>Recomendaciones</span></div>
        <div class="ks k3"><b>${acogInst(d)}</b><span>Entidades con acogida</span></div>
        <div class="ks k4"><b>${d.anio}</b><span>Año de publicación</span></div>
      </div>
      <div class="panel reveal"><div class="lbl"><i>&#9673;</i>Objetivo del documento</div><p>${d.objetivo}</p></div>
      <div class="panel reveal"><div class="lbl r"><i>&#10070;</i>Público beneficiario</div><p>${d.publico}</p></div>
      <div class="sec-h"><h3>Recomendaciones por institución</h3><div class="line"></div><div class="cnt">${d.recs.length} entidad(es)</div></div>
      <div class="recs">${recsHtml}</div>
    </div>`;
}
function openDetail(i){
  cur=i;offInner.innerHTML=detailHTML(i);
  scrim.classList.add('open');off.classList.add('open');off.scrollTop=0;document.body.style.overflow='hidden';
  const dp=document.getElementById('dp'),dn=document.getElementById('dn');
  dp.disabled=i===0;dn.disabled=i===DOCS.length-1;
  dp.onclick=()=>openDetail(i-1);dn.onclick=()=>openDetail(i+1);
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{root:off,threshold:.08});
  off.querySelectorAll('.reveal').forEach(el=>io.observe(el));
  requestAnimationFrame(()=>off.querySelectorAll('.reveal').forEach((el,k)=>{if(el.getBoundingClientRect().top<window.innerHeight)el.classList.add('in')}));
}
function closeDetail(){scrim.classList.remove('open');off.classList.remove('open');document.body.style.overflow='';cur=-1;}
off.addEventListener('scroll',()=>{const p=off.scrollTop/(off.scrollHeight-off.clientHeight||1);document.getElementById('prog').style.width=(p*100)+'%';});
document.addEventListener('keydown',e=>{
  if(!off.classList.contains('open'))return;
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

t=open('template.html',encoding='utf-8').read()

# ---------- A) sidebar + stage + section1 + section2 open (replace topbar+home-open) ----------
old_a='''<div class="topbar">
  <img class="logo" src="__LOGO__" alt="Defensoría del Pueblo">
  <div class="divider"></div>
  <div class="ctx"><h1>Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad</h1>
    <p>Panel Ejecutivo · Informes y Documentos</p></div>
  <div class="spacer"></div>
  <img class="anniv" src="__ANNIV__" alt="30 años Defendiendo tus derechos">
</div>

<div class="home">'''

ph1='''<section id="s-antecedentes" class="slide">
  <div class="slidebox">
    <div class="slidehead">
      <span class="eyebrow2"><span class="pulse"></span>01 · Antecedentes</span>
      <h1 class="slidetitle">Antecedentes de la <span class="g">Adjuntía</span></h1>
      <p class="slidesub">Origen, evolución institucional y casos emblemáticos que enmarcan la labor de prevención y gestión de conflictos sociales.</p>
    </div>
    <div class="phgrid">
      <div class="phcard"><span class="ph-n">1.1</span><h3>Objetivo de la Adjuntía</h3><p class="ph-ph">Contenido estratégico en construcción…</p></div>
      <div class="phcard"><span class="ph-n">1.2</span><h3>Evolución institucional</h3><p class="ph-ph">Contenido estratégico en construcción…</p></div>
      <div class="phcard"><span class="ph-n">1.3</span><h3>Supervisiones</h3><p class="ph-ph">Contenido estratégico en construcción…</p></div>
      <div class="phcard"><span class="ph-n">1.4</span><h3>Casos emblemáticos de intervención</h3><p class="ph-ph">Contenido estratégico en construcción…</p></div>
    </div>
  </div>
</section>

<section id="s-balance" class="slide active">
<div class="home">'''

new_a='''<aside class="sidebar">
  <div class="brand"><img src="__LOGO__" alt="Defensoría del Pueblo"></div>
  <div class="navttl">Exposición · Alta Dirección</div>
  <nav class="menu">
    <button class="mitem" data-s="s-antecedentes"><span class="mi-n">01</span><span class="mi-l">Antecedentes</span></button>
    <button class="mitem active" data-s="s-balance"><span class="mi-n">02</span><span class="mi-l">Balance de Informes</span></button>
    <button class="mitem" data-s="s-fortalecimiento"><span class="mi-n">03</span><span class="mi-l">Fortalecimiento Institucional</span></button>
    <button class="mitem" data-s="s-prospectiva"><span class="mi-n">04</span><span class="mi-l">Prospectiva Gubernamental</span></button>
  </nav>
  <div class="side-foot"><img src="__ANNIV__" alt="30 años Defendiendo tus derechos"><p>Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad</p></div>
</aside>

<main class="stage">

'''+ph1
assert old_a in t, 'A missing'
t=t.replace(old_a,new_a)

# ---------- B) close section2 + section3 + section4 + close stage ----------
old_b='''  <div class="mosaic scene" id="mosaic"></div>
</div>

<div class="scrim" id="scrim" onclick="closeDetail()"></div>'''

ph34='''  <div class="mosaic scene" id="mosaic"></div>
</div>
</section>

<section id="s-fortalecimiento" class="slide">
  <div class="slidebox">
    <div class="slidehead">
      <span class="eyebrow2"><span class="pulse"></span>03 · Fortalecimiento Institucional</span>
      <h1 class="slidetitle">Fortalecimiento para la <span class="g">prevención y gestión</span> de conflictos</h1>
      <p class="slidesub">Propuestas para consolidar la institucionalidad del Estado en el abordaje temprano y articulado de la conflictividad social.</p>
    </div>
    <div class="phgrid">
      <div class="phcard"><span class="ph-n">3.1</span><h3>Observatorio de conflictividad social</h3><p class="ph-ph">Contenido estratégico en construcción…</p></div>
      <div class="phcard"><span class="ph-n">3.2</span><h3>Sistema Nacional de Prevención y Gestión de Conflictos Sociales</h3><p class="ph-ph">Contenido estratégico en construcción…</p></div>
    </div>
  </div>
</section>

<section id="s-prospectiva" class="slide">
  <div class="slidebox">
    <div class="slidehead">
      <span class="eyebrow2"><span class="pulse"></span>04 · Prospectiva Gubernamental</span>
      <h1 class="slidetitle">Prospectiva de la <span class="g">conflictividad social</span> para el gobierno entrante</h1>
      <p class="slidesub">Escenarios de riesgo y factores de escalamiento proyectados hacia la transición gubernamental 2026.</p>
    </div>
    <div class="phgrid">
      <div class="phcard"><span class="ph-n">4.1</span><h3>Escenario actual de la conflictividad · junio 2026</h3><p class="ph-ph">Contenido estratégico en construcción…</p></div>
      <div class="phcard"><span class="ph-n">4.2</span><h3>Escenarios con nivel de riesgo para el nuevo gobierno</h3><p class="ph-ph">Contenido estratégico en construcción…</p></div>
    </div>
  </div>
</section>

</main>

<div class="scrim" id="scrim" onclick="closeDetail()"></div>'''
assert old_b in t, 'B missing'
t=t.replace(old_b,ph34)

# ---------- C) CSS ----------
css='''
/* ===== SPA layout ===== */
.sidebar{position:fixed;left:0;top:0;bottom:0;width:266px;z-index:35;display:flex;flex-direction:column;padding:24px 18px;
  background:linear-gradient(180deg,rgba(16,24,42,.93),rgba(10,16,30,.95));backdrop-filter:blur(22px) saturate(140%);
  border-right:1px solid rgba(255,255,255,.08);box-shadow:16px 0 50px rgba(9,16,32,.20)}
.sidebar .brand{background:#fff;border-radius:16px;padding:13px 14px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 26px rgba(0,0,0,.28)}
.sidebar .brand img{height:46px;width:auto}
.navttl{color:rgba(255,255,255,.42);font-size:10px;letter-spacing:1.8px;text-transform:uppercase;font-weight:700;margin:26px 10px 12px}
.menu{display:flex;flex-direction:column;gap:8px}
.mitem{display:flex;align-items:center;gap:13px;padding:14px 15px;border-radius:14px;border:1px solid transparent;background:transparent;color:rgba(255,255,255,.72);cursor:pointer;transition:.25s;text-align:left;font-family:'Sora';font-weight:600;font-size:13px;width:100%}
.mitem .mi-n{font-family:'Space Grotesk';font-size:12px;color:rgba(255,255,255,.34);font-weight:700}
.mitem:hover{background:rgba(255,255,255,.07);color:#fff;transform:translateX(3px)}
.mitem.active{background:linear-gradient(120deg,rgba(10,86,168,.92),rgba(8,59,115,.92));color:#fff;border-color:rgba(255,255,255,.14);box-shadow:0 12px 28px rgba(10,86,168,.42)}
.mitem.active .mi-n{color:#8fbcff}
.side-foot{margin-top:auto;text-align:center;padding-top:20px}
.side-foot img{width:100%;max-width:158px;background:#fff;border-radius:12px;padding:9px;box-shadow:0 10px 26px rgba(0,0,0,.28)}
.side-foot p{color:rgba(255,255,255,.42);font-size:9.5px;line-height:1.45;margin-top:12px}
.stage{margin-left:266px;position:relative;z-index:2;min-height:100vh}
.slide{display:none}
.slide.active{display:block;animation:slideIn .55s cubic-bezier(.2,.75,.2,1)}
@keyframes slideIn{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:none}}
.slidebox{max-width:1120px;margin:0 auto;padding:52px 46px 80px}
.slidehead{margin-bottom:36px}
.eyebrow2{display:inline-flex;align-items:center;gap:9px;font-size:11.5px;font-weight:700;letter-spacing:1.8px;text-transform:uppercase;color:var(--blue);background:var(--glass);border:1px solid var(--gbrd);backdrop-filter:blur(10px);padding:7px 15px;border-radius:30px;box-shadow:var(--sh)}
.eyebrow2 .pulse{width:8px;height:8px;border-radius:50%;background:var(--red);animation:pulse 2s infinite}
.slidetitle{font-family:'Sora';font-weight:800;font-size:44px;line-height:1.08;letter-spacing:-1.1px;margin:20px 0 12px}
.slidetitle .g{background:linear-gradient(100deg,var(--blue),var(--red));-webkit-background-clip:text;background-clip:text;color:transparent}
.slidesub{font-size:16px;color:var(--mut);max-width:660px;line-height:1.6}
.phgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
.phcard{position:relative;border:1.5px dashed #cdd6e2;border-radius:22px;padding:30px 30px;background:var(--glass);backdrop-filter:blur(12px) saturate(150%);min-height:172px;display:flex;flex-direction:column;box-shadow:var(--sh);transition:.3s;overflow:hidden}
.phcard:hover{border-color:var(--blue);transform:translateY(-5px);box-shadow:var(--sh2)}
.phcard .ph-n{font-family:'Space Grotesk';font-weight:700;font-size:13px;color:var(--blue)}
.phcard h3{font-family:'Sora';font-weight:700;font-size:19px;line-height:1.28;margin:9px 0 auto;max-width:92%}
.phcard .ph-ph{font-size:13px;color:var(--mut2);font-style:italic;margin-top:18px;display:flex;align-items:center;gap:9px}
.phcard .ph-ph:before{content:'';width:9px;height:9px;border-radius:50%;background:var(--amb);box-shadow:0 0 0 4px rgba(196,125,0,.15)}
.home{max-width:1200px;margin:0 auto;padding:44px 46px 90px}
@media(max-width:980px){.sidebar{position:static;width:auto;flex-direction:row;align-items:center;gap:12px;padding:12px 14px}.sidebar .brand{padding:7px 9px}.sidebar .brand img{height:30px}.navttl,.side-foot{display:none}.menu{flex-direction:row;overflow-x:auto;flex:1}.mitem{white-space:nowrap;padding:11px 13px}.stage{margin-left:0}.slidebox{padding:32px 22px}.phgrid{grid-template-columns:1fr}.slidetitle{font-size:30px}}
</style>'''
t=t.replace('</style>',css)

# ---------- D) JS nav + VIS tracking ----------
t=t.replace("function applyFilter(k,btn){",
            "let VIS=DOCS.slice();\nfunction applyFilter(k,btn){")
t=t.replace("  recompute(vis.length?vis:DOCS);\n}",
            "  VIS=vis.length?vis:DOCS;recompute(VIS);\n}")

nav_js='''/* ===== SPA navigation ===== */
const MENU=document.querySelectorAll('.mitem');
function navTo(id){
  document.querySelectorAll('.slide').forEach(s=>s.classList.toggle('active',s.id===id));
  MENU.forEach(m=>m.classList.toggle('active',m.dataset.s===id));
  if(id==='s-balance'){recompute(VIS);}
  window.scrollTo({top:0,behavior:'smooth'});
}
MENU.forEach(m=>m.onclick=()=>navTo(m.dataset.s));

/* ===== init ===== */'''
t=t.replace("/* ===== init ===== */",nav_js)

open('template.html','w',encoding='utf-8').write(t)
print('SPA patch applied')

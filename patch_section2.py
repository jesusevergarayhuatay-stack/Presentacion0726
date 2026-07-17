t=open('template.html',encoding='utf-8').read()

# ===== A) replace whole section 2 markup (index slice) =====
i=t.find('<section id="s-balance" class="slide active">')
j=t.find('<section id="s-fortalecimiento"')
assert i!=-1 and j!=-1
new_sec2='''<section id="s-balance" class="slide active">
  <div class="subhead">
    <div class="slidehead">
      <span class="eyebrow2"><span class="pulse"></span>02 · Balance de Informes</span>
      <h1 class="slidetitle">Balance de los <span class="g">informes defensoriales</span></h1>
      <p class="slidesub">Los ocho informes registrados por la Adjuntía, con las recomendaciones formuladas a cada institución y su nivel de acogida.</p>
    </div>
    <div class="subtabs">
      <button class="subtab active" data-t="b1"><span class="st-n">2.1</span>Informes y recomendaciones</button>
      <button class="subtab" data-t="b2"><span class="st-n">2.2</span>Balance general</button>
    </div>
  </div>
  <div class="subpanel active" data-t="b1"><div class="subbox">
    <div class="mosaic scene" id="mosaic"></div>
  </div></div>
  <div class="subpanel" data-t="b2"><div class="subbox">
    <p class="blocklead">Resumen agregado de los 8 informes (2023–2026): 165 recomendaciones a 45 instituciones, con 8% de acogida global. Filtra por año para recalcular los indicadores.</p>
    <div class="filters" id="filters" style="margin-top:16px"></div>
    <div class="overview" style="margin-top:6px">
      <div class="kpis scene">
        <div class="kcard k1"><div class="ico">▤</div><b id="ov1">0</b><span>Informes defensoriales</span></div>
        <div class="kcard k2"><div class="ico">◆</div><b id="ov2">0</b><span>Recomendaciones</span></div>
        <div class="kcard k3"><div class="ico">◎</div><b id="ov3">0</b><span>Instituciones alcanzadas</span></div>
        <div class="kcard k4"><div class="ico">✓</div><b id="ov4">0</b><span>Recomendaciones acogidas</span></div>
      </div>
      <div class="panorama">
        <h3>Panorama de recomendaciones</h3>
        <div class="psub">Nivel de acogida del Estado y distribución por informe · pasa el cursor sobre las barras</div>
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
  </div></div>
</section>

'''
t=t[:i]+new_sec2+t[j:]

# ===== B) tiles: no feat/wide, no objetivo desc =====
t=t.replace(
"  const ds=docState(d);const feat=i===0;const wide=(DOCS.length%2===0)&&(i===DOCS.length-1);",
"  const ds=docState(d);const feat=false;const wide=false;")
t=t.replace(
"    ${feat?`<div class=\"tdesc\">${d.objetivo}</div>`:''}\n",
"")

# ===== C) subtab recompute on b2 =====
t=t.replace("  if(k==='b1')recompute(VIS);","  if(k==='b2')recompute(VIS);")

# ===== D) applyFilter: recompute summary only =====
old_af='''function applyFilter(k,btn){
  filtersEl.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('active'));btn.classList.add('active');
  const vis=[];
  document.querySelectorAll('.tile').forEach(t=>{
    const d=DOCS[+t.dataset.i];const ok=matchF(d,k);
    if(ok){vis.push(d);t.classList.remove('hidden');requestAnimationFrame(()=>t.classList.remove('hiding'));}
    else{t.classList.add('hiding');setTimeout(()=>t.classList.add('hidden'),380);}
  });
  VIS=vis.length?vis:DOCS;recompute(VIS);
}'''
new_af='''function applyFilter(k,btn){
  filtersEl.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('active'));btn.classList.add('active');
  const vis=DOCS.filter(d=>matchF(d,k));
  VIS=vis.length?vis:DOCS;recompute(VIS);
}'''
assert old_af in t,'applyFilter anchor missing'
t=t.replace(old_af,new_af)

# ===== E) detailHTML offbody -> two columns =====
t=t.replace('    <div class="offbody">\n      <section class="hero reveal">',
            '    <div class="offbody"><div class="dgrid"><div class="dcol">\n      <section class="hero reveal">')
t=t.replace('      <div class="sec-h"><h3>Recomendaciones por institución</h3>',
            '      </div><div class="dcol"><div class="sec-h"><h3>Recomendaciones por institución</h3>')
t=t.replace('      <div class="recs">${recsHtml}</div>\n    </div>`;',
            '      <div class="recs">${recsHtml}</div></div></div>\n    </div>`;')

# ===== F) openDetail: attach offbody scroll to progress =====
t=t.replace(
"  off.querySelectorAll('.reveal').forEach(el=>el.classList.add('in'):null);",
"  ")  # noop safety
t=t.replace(
"  requestAnimationFrame(()=>off.querySelectorAll('.reveal').forEach(el=>{if(el.getBoundingClientRect().top<innerHeight)el.classList.add('in')}));",
"  requestAnimationFrame(()=>off.querySelectorAll('.reveal').forEach(el=>{if(el.getBoundingClientRect().top<innerHeight)el.classList.add('in')}));\n  const ob=off.querySelector('.offbody');if(ob)ob.addEventListener('scroll',()=>{const p=ob.scrollTop/(ob.scrollHeight-ob.clientHeight||1);document.getElementById('prog').style.width=(p*100)+'%';});")

# ===== G) CSS: mosaic/tiles compact, off modal, dgrid =====
t=t.replace(
".mosaic{display:grid;grid-template-columns:repeat(12,1fr);gap:22px;grid-auto-rows:minmax(172px,1fr)}",
".mosaic{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;grid-auto-rows:minmax(120px,auto)}")
t=t.replace(
"box-shadow:var(--sh);padding:28px 30px;cursor:pointer;overflow:hidden;display:flex;flex-direction:column;transition:transform .2s cubic-bezier(.2,.7,.2,1),box-shadow .35s,border-color .35s,opacity .4s;will-change:transform}",
"box-shadow:var(--sh);padding:20px 22px;cursor:pointer;overflow:hidden;display:flex;flex-direction:column;transition:transform .2s cubic-bezier(.2,.7,.2,1),box-shadow .35s,border-color .35s,opacity .4s;will-change:transform}")
t=t.replace(
".tile .tmeta{margin-top:auto;padding-top:18px;display:flex;align-items:center;gap:9px;flex-wrap:wrap;position:relative;z-index:2;transform:translateZ(24px)}",
".tile .tmeta{margin-top:14px;padding-top:0;display:flex;align-items:center;gap:9px;flex-wrap:wrap;position:relative;z-index:2;transform:translateZ(24px)}")
t=t.replace(
".tile .ghost{position:absolute;right:-4px;top:-30px;font-family:'Space Grotesk';font-weight:700;font-size:132px;line-height:1;",
".tile .ghost{position:absolute;right:-2px;top:-20px;font-family:'Space Grotesk';font-weight:700;font-size:100px;line-height:1;")

# off modal
t=t.replace(
".off{position:fixed;top:0;right:0;height:100vh;width:min(760px,96vw);z-index:41;background:var(--glass-2);backdrop-filter:blur(24px) saturate(150%);border-left:1px solid var(--gbrd);box-shadow:-34px 0 90px rgba(9,16,32,.34);transform:translateX(102%);transition:transform .55s cubic-bezier(.3,.85,.2,1);overflow-y:auto}\n.off.open{transform:none}",
""".off{position:fixed;top:50%;left:50%;transform:translate(-50%,-46%) scale(.97);width:min(1200px,93vw);height:88vh;z-index:41;background:var(--glass-2);backdrop-filter:blur(24px) saturate(150%);border:1px solid var(--gbrd);border-radius:24px;box-shadow:0 40px 120px rgba(9,16,32,.5);overflow:hidden;opacity:0;pointer-events:none;transition:.42s cubic-bezier(.2,.8,.2,1);display:flex;flex-direction:column}
.off.open{transform:translate(-50%,-50%) scale(1);opacity:1;pointer-events:auto}
.off #offInner{display:flex;flex-direction:column;height:100%;min-height:0;width:100%}
.dgrid{display:grid;grid-template-columns:1fr 1.05fr;gap:22px;align-items:start}
.dcol{min-width:0}
@media(max-width:900px){.dgrid{grid-template-columns:1fr}}""")
t=t.replace(
".offtop{position:sticky;top:0;z-index:5;display:flex;align-items:center;gap:14px;padding:16px 26px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.72);backdrop-filter:blur(16px)}",
".offtop{flex:none;display:flex;align-items:center;gap:14px;padding:15px 24px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.55)}")
t=t.replace(
".offbody{padding:26px 30px 70px}",
".offbody{flex:1;min-height:0;overflow-y:auto;padding:22px 26px}\n.offbody::-webkit-scrollbar{width:9px}.offbody::-webkit-scrollbar-thumb{background:rgba(16,42,80,.18);border-radius:8px}")

open('template.html','w',encoding='utf-8').write(t)
print('section 2 restructure applied')

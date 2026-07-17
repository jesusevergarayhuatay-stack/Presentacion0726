t=open('template.html',encoding='utf-8').read()

sec4_old='''<section id="s-prospectiva" class="slide">
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
</section>'''

sec4_new='''<section id="s-prospectiva" class="slide">
  <div class="subhead">
    <div class="slidehead">
      <span class="eyebrow2"><span class="pulse"></span>04 · Prospectiva Gubernamental</span>
      <h1 class="slidetitle">Prospectiva de la <span class="g">conflictividad social</span> para el gobierno entrante</h1>
      <p class="slidesub">Fotografía de la conflictividad a junio de 2026 y escenarios de riesgo proyectados para la transición gubernamental.</p>
    </div>
    <div class="subtabs">
      <button class="subtab active" data-t="d1"><span class="st-n">4.1</span>Escenario actual · junio 2026</button>
      <button class="subtab" data-t="d2"><span class="st-n">4.2</span>Escenarios de riesgo</button>
    </div>
  </div>

  <div class="subpanel active" data-t="d1"><div class="subbox">
    <p class="blocklead">La conflictividad mantiene un carácter estructural, pero se encuentra temporalmente contenida gracias a un despliegue preventivo sostenido. Al cierre de junio de 2026 se registran 197 conflictos, y durante el mes <b>no se registró ninguna persona fallecida ni herida</b>.</p>
    <div class="metrics">
      <div class="metric"><b>197</b><span>Conflictos sociales · 151 activos (76.6%) y 46 latentes</span></div>
      <div class="metric a"><b>211</b><span>Acciones de protesta en un solo mes (sin víctimas)</span></div>
      <div class="metric g"><b>95.6%</b><span>Presencia garante en las 90 mesas de diálogo activas</span></div>
      <div class="metric g"><b>57.4%</b><span>Conflictos con violencia (baja vs. 59.9% de 2025)</span></div>
      <div class="metric"><b>274</b><span>Actuaciones defensoriales en junio (~73% preventivas)</span></div>
      <div class="metric"><b>6</b><span>Conflictos nuevos aparecidos en el mes</span></div>
    </div>
    <div class="ch"><span class="cn">Tipo</span>Composición de la conflictividad</div>
    <div class="grid3">
      <div class="gcard"><h4><span class="ic">◈</span>Socioambiental · 48.7%</h4><p>96 casos; el 63.5% vinculado a minería y el 18.8% a hidrocarburos. Sector determinante para la paz social y la inversión.</p></div>
      <div class="gcard"><h4><span class="ic">▤</span>Demandas de gobierno · 35%</h4><p>Nacional (19.3%), regional (8.6%) y local (7.1%): expectativas insatisfechas por obras, servicios e incumplimientos.</p></div>
      <div class="gcard r"><h4><span class="ic">◆</span>Frente educativo emergente</h4><p>Universidades públicas (San Marcos, Ucayali, Cajamarca, Del Santa) por infraestructura, cobros y gobernanza.</p></div>
    </div>
    <div class="ch"><span class="cn">Competencias</span>Responsabilidad resolutiva y geografía</div>
    <div class="grid2">
      <div class="gcard"><h4><span class="ic">◉</span>Responsabilidad resolutiva</h4><p>Casi <b>2 de cada 3 conflictos (64.5%, 127 casos)</b> son competencia directa del Gobierno Nacional; el resto se reparte entre gobiernos regionales (24.9%), locales (8.1%) y organismos autónomos (2.0%).</p></div>
      <div class="gcard"><h4><span class="ic">◎</span>Concentración territorial</h4><p>Cinco regiones concentran el <b>45.7% (90 casos)</b>: <b>Loreto, Puno, Áncash, Piura y Cusco</b>.</p></div>
    </div>
  </div></div>

  <div class="subpanel" data-t="d2"><div class="subbox">
    <p class="blocklead">Al cruzar las series históricas con la data actual: la violencia disminuye progresivamente, pero el ritmo de aparición de nuevos conflictos se acelera (de 28 anuales en 2023 a 81 en 2025).</p>
    <div class="metrics">
      <div class="metric g"><span class="fl">71.9% → 57.4%</span><span>Conflictos con violencia: caída ininterrumpida</span></div>
      <div class="metric a"><span class="fl"><span class="arrow up">▲</span> 28 → 81</span><span>Conflictos nuevos por año (del 11% al 29% del total)</span></div>
    </div>
    <div class="ch"><span class="cn">Escenarios</span>Proyección a 12 meses</div>
    <div class="csub">Del más probable al de mayor impacto.</div>
    <div class="grid3">
      <div class="scen a"><div class="sh"><h4>A · Contención</h4><span class="prob a">Media-alta</span></div><p>Conflictividad alta en número pero contenida en violencia. Las protestas continúan (~2 500–3 000/año) sin víctimas masivas. Requiere mantener el diálogo y dar señales tempranas en el REINFO y cumplimiento de acuerdos. <b>El desafío es de gestión, no de crisis.</b></p></div>
      <div class="scen b"><div class="sh"><h4>B · Repunte sectorial</h4><span class="prob b">Media</span></div><p>Uno o dos frentes escalan localizadamente (minería informal + corredor minero del sur o descontento urbano). Bloqueos prolongados y paros regionales, sin crisis nacional. Impacto económico y de gobernabilidad regional, <b>manejable con intervención oportuna</b>.</p></div>
      <div class="scen c"><div class="sh"><h4>C · Crisis nacional</h4><span class="prob c">Baja · alto impacto</span></div><p>Converge un detonante político-nacional con el malestar socioeconómico y la minería informal: ola de protestas simultáneas, bloqueos masivos y riesgo de víctimas (al estilo de dic. 2022 y oct. 2025). <b>Exige un protocolo de respuesta preparado de antemano.</b></p></div>
    </div>
  </div></div>
</section>'''
assert sec4_old in t,'sec4 anchor missing'
t=t.replace(sec4_old,sec4_new)

# ============ JS : subtab handler ============
navjs='''MENU.forEach(m=>m.onclick=()=>navTo(m.dataset.s));'''
subjs='''MENU.forEach(m=>m.onclick=()=>navTo(m.dataset.s));
document.querySelectorAll('.subtab').forEach(tb=>tb.onclick=()=>{
  const sec=tb.closest('.slide');const k=tb.dataset.t;
  sec.querySelectorAll('.subtab').forEach(x=>x.classList.toggle('active',x===tb));
  sec.querySelectorAll('.subpanel').forEach(p=>p.classList.toggle('active',p.dataset.t===k));
  if(k==='b1')recompute(VIS);
});'''
assert navjs in t
t=t.replace(navjs,subjs)

open('template.html','w',encoding='utf-8').write(t)
print('section 4 + subtab JS done')

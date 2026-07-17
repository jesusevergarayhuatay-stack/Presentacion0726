t=open('template.html',encoding='utf-8').read()

# ---- CSS ----
css='''
/* ===== master-detail explorer (inspired by projection deck) ===== */
.explorer{display:grid;grid-template-columns:310px 1fr;border:1px solid var(--gbrd);border-radius:22px;overflow:hidden;background:var(--glass);backdrop-filter:blur(14px) saturate(150%);box-shadow:var(--sh);margin-top:10px}
.exp-list{display:flex;flex-direction:column;padding:12px;gap:6px;border-right:1px solid var(--line);max-height:540px;overflow:auto}
.exp-tile{display:flex;align-items:center;gap:13px;padding:13px 14px;border-radius:13px;cursor:pointer;border-left:3px solid transparent;transition:.2s;user-select:none}
.exp-tile:hover{background:rgba(10,86,168,.05)}
.exp-tile.active{background:rgba(10,86,168,.08);border-left-color:var(--blue)}
.exp-tile .ei{font-size:23px;flex:none;line-height:1}
.exp-tile .en{font-family:'Sora';font-weight:600;font-size:13px;color:var(--ink);line-height:1.3}
.exp-tile.active .en{color:var(--blue)}
.exp-tile .em{font-size:11px;color:var(--mut2);margin-top:2px}
.exp-detail{padding:32px 36px;display:flex;flex-direction:column;justify-content:center;min-height:320px}
.exp-detail .dtop{display:flex;align-items:center;gap:16px;margin-bottom:14px}
.exp-detail .dic{font-size:46px;line-height:1}
.exp-tag{display:inline-block;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.6px;padding:6px 13px;border-radius:20px}
.exp-tag.green{color:var(--grn);background:var(--grn-l);border:1px solid #b8e6cb}
.exp-tag.red{color:var(--red);background:var(--red-l);border:1px solid #f6c9c4}
.exp-tag.amber{color:var(--amb);background:#fdf3e0;border:1px solid #f0d8a8}
.exp-tag.navy{color:var(--blue-d);background:var(--blue-l);border:1px solid #cfe0f4}
.exp-detail .dt{font-family:'Sora';font-weight:800;font-size:22px;line-height:1.3;margin-bottom:11px;color:var(--ink)}
.exp-detail .db{font-size:15px;line-height:1.78;color:#334155}
.exp-detail .db b{color:var(--ink)}
.fadeswap{animation:fadeswap .32s ease}
@keyframes fadeswap{from{opacity:0;transform:translateY(9px)}to{opacity:1;transform:none}}
@media(max-width:860px){.explorer{grid-template-columns:1fr}.exp-list{flex-direction:row;overflow-x:auto;max-height:none}.exp-tile{min-width:220px}.exp-detail{padding:24px}}
</style>'''
t=t.replace('</style>',css)

# ---- replace section 1.4 casos with explorer ----
a4_old='''  <div class="subpanel" data-t="a4"><div class="subbox">
    <p class="blocklead">La eficacia de la Adjuntía se materializa en la gestión directa de crisis de alta complejidad, ejerciendo la persuasión para garantizar derechos, evitar la escalada de la violencia y reconducir las demandas hacia la vía institucional.</p>
    <div class="tag2">● Periodo 2023</div>
    <div class="grid2">
      <div class="gcard"><h4><span class="ic">◈</span>Derrame Repsol — Ventanilla (Callao/Lima)</h4><p>Rol garante en los procesos de compensación económica: se contuvo el reinicio de protestas y se concretaron negociaciones que garantizaron un trato justo para más de <b>1 900 afectados</b>, exhortando al MINEM a modificar el marco normativo.</p></div>
      <div class="gcard"><h4><span class="ic">◈</span>Lote 95 Bretaña — Petrotal (Loreto)</h4><p>Reactivación de la Mesa Técnica y supervisión in situ que permitió deponer medidas de fuerza. Derivó en el reglamento del <b>Fondo de Desarrollo de Puinahua</b> (2.5% de la producción fiscalizada) para 18 localidades.</p></div>
    </div>
    <div class="tag2">● Periodo 2025</div>
    <div class="grid3">
      <div class="gcard"><h4><span class="ic">◆</span>REINFO — Formalización minera</h4><p>Ante el bloqueo de la Panamericana Sur por la exclusión de +50 000 mineros: supervisión del uso proporcional de la fuerza, corredores humanitarios y mesas de trabajo con la PCM.</p></div>
      <div class="gcard"><h4><span class="ic">◆</span>Toma de la UNMSM (Lima)</h4><p>Rol mediador en la mesa del 13 de septiembre: liberación pacífica del campus, salvaguarda de la integridad de las partes y ratificación de la anulación de cobros irregulares.</p></div>
      <div class="gcard"><h4><span class="ic">◆</span>Ruta Hiram Bingham — Consettur (Cusco)</h4><p>Mediación ante el riesgo de paralización del servicio a Machu Picchu: dos treguas estratégicas con la comunidad de San Antonio de Torontoy, desescalando una zona económica sensible.</p></div>
    </div>
  </div></div>'''
a4_new='''  <div class="subpanel" data-t="a4"><div class="subbox">
    <p class="blocklead">La eficacia de la Adjuntía se materializa en la gestión directa de crisis de alta complejidad, ejerciendo la persuasión para garantizar derechos, evitar la escalada de la violencia y reconducir las demandas hacia la vía institucional. Selecciona un caso para ver el detalle.</p>
    <div class="explorer" id="exp-casos"></div>
  </div></div>'''
assert a4_old in t,'a4 anchor missing'
t=t.replace(a4_old,a4_new)

# ---- replace section 4.2 scenarios with explorer ----
scen_old='''    <div class="grid3">
      <div class="scen a"><div class="sh"><h4>A · Contención</h4><span class="prob a">Media-alta</span></div><p>Conflictividad alta en número pero contenida en violencia. Las protestas continúan (~2 500–3 000/año) sin víctimas masivas. Requiere mantener el diálogo y dar señales tempranas en el REINFO y cumplimiento de acuerdos. <b>El desafío es de gestión, no de crisis.</b></p></div>
      <div class="scen b"><div class="sh"><h4>B · Repunte sectorial</h4><span class="prob b">Media</span></div><p>Uno o dos frentes escalan localizadamente (minería informal + corredor minero del sur o descontento urbano). Bloqueos prolongados y paros regionales, sin crisis nacional. Impacto económico y de gobernabilidad regional, <b>manejable con intervención oportuna</b>.</p></div>
      <div class="scen c"><div class="sh"><h4>C · Crisis nacional</h4><span class="prob c">Baja · alto impacto</span></div><p>Converge un detonante político-nacional con el malestar socioeconómico y la minería informal: ola de protestas simultáneas, bloqueos masivos y riesgo de víctimas (al estilo de dic. 2022 y oct. 2025). <b>Exige un protocolo de respuesta preparado de antemano.</b></p></div>
    </div>'''
scen_new='''    <div class="csub">Del más probable al de mayor impacto. Selecciona un escenario para ver el análisis completo.</div>
    <div class="explorer" id="exp-escenarios"></div>'''
assert scen_old in t,'scen anchor missing'
t=t.replace(scen_old,scen_new)

# ---- JS: explorer engine + data ----
engine_anchor='function activateDynamics(root){const R=root||document;'
engine='''const EXPLORERS={
 'exp-casos':[
   {ico:'🛢️',name:'Derrame Repsol — Ventanilla',meta:'2023 · Callao / Lima',tag:{t:'Compensación',c:'navy'},title:'Trato justo para más de 1 900 afectados',body:'Rol garante en los procesos de compensación económica. Entre setiembre y noviembre de 2023 se contuvo el reinicio de protestas y se concretaron reuniones de negociación decisivas que garantizaron un trato justo para asociaciones que representaban a más de <b>1 900 afectados</b>. Se oficializó la participación defensorial en la mesa de diálogo y se exhortó al MINEM a modificar el marco normativo para asegurar reparaciones integrales con participación del Estado.'},
   {ico:'🌳',name:'Lote 95 Bretaña — Petrotal',meta:'2023 · Loreto',tag:{t:'Mediación',c:'navy'},title:'Reactivación de la Mesa Técnica y paz social',body:'Ante la paralización del diálogo y medidas de fuerza en la Amazonía, la institución intercedió para reactivar la Mesa Técnica. Frente a un nuevo pico de tensiones en junio de 2023, un rápido despliegue de supervisión in situ permitió deponer las medidas de fuerza. El acompañamiento garante restableció la paz social y derivó, en agosto de 2023, en el reglamento del «Fondo de Desarrollo para el Distrito de Puinahua», que asegura financiamiento para <b>18 localidades</b> mediante el 2.5% del valor de la producción fiscalizada.'},
   {ico:'⛏️',name:'REINFO — Formalización minera',meta:'2025 · Nacional / Arequipa',tag:{t:'Orden público',c:'red'},title:'Corredores humanitarios y uso proporcional de la fuerza',body:'Ante el bloqueo de la Panamericana Sur por la exclusión de más de <b>50 000 mineros</b> del REINFO, los comisionados se desplegaron directamente en los puntos de conflicto. Se supervisó el uso estrictamente proporcional de la fuerza por parte de la Policía Nacional del Perú, se gestionaron corredores humanitarios y se encauzó la crisis mediante la instalación de mesas de trabajo con dirigentes y la PCM.'},
   {ico:'🎓',name:'Toma del campus UNMSM',meta:'2025 · Lima Metropolitana',tag:{t:'Mediación',c:'navy'},title:'Liberación pacífica del recinto universitario',body:'Frente a la radicalización de la protesta estudiantil, la institución ejerció un rol mediador decisivo en la mesa de diálogo del 13 de septiembre. La intervención garantizó la <b>liberación pacífica</b> del recinto universitario, salvaguardó la integridad física de todas las partes durante la entrega de las instalaciones y logró que se ratificara la anulación de cobros irregulares para segundas carreras.'},
   {ico:'🚠',name:'Ruta Hiram Bingham — Consettur',meta:'2025 · Cusco',tag:{t:'Mediación',c:'amber'},title:'Dos treguas para el servicio a Machu Picchu',body:'Ante el riesgo inminente de paralización del servicio turístico hacia Machu Picchu por incertidumbre jurídica, la Defensoría lideró un complejo proceso de mediación. La actuación consolidó <b>dos treguas estratégicas</b> con la comunidad de San Antonio de Torontoy, desescalando la conflictividad social en una de las zonas económicas más sensibles del país.'}
 ],
 'exp-escenarios':[
   {ico:'🕊️',name:'A · Contención',meta:'Probabilidad media-alta',tag:{t:'Base / más probable',c:'green'},title:'La tendencia de desescalamiento se prolonga',body:'La conflictividad se mantiene alta en número pero <b>contenida en violencia</b>, prolongando la tendencia de desescalamiento. Las protestas continúan (~2 500–3 000 al año) sin derivar en víctimas masivas. El sistema de alerta temprana y el acompañamiento defensorial —con presencia garante en el 95.6% de las mesas activas— actúa como amortiguador. Requiere que el gobierno mantenga canales de diálogo abiertos y dé señales tempranas en el REINFO y en el cumplimiento de acuerdos. <b>El principal desafío es de gestión, no de contención de crisis.</b>'},
   {ico:'⚠️',name:'B · Repunte sectorial',meta:'Probabilidad media',tag:{t:'Intermedio',c:'amber'},title:'Uno o dos frentes escalan de forma localizada',body:'Típicamente la minería informal combinada con el corredor minero del sur andino o con el descontento urbano por seguridad. Se producen bloqueos prolongados de vías, paros regionales y un número acotado de heridos, <b>sin llegar a una crisis nacional</b>. Se activa si el cierre o la prórroga del REINFO se maneja sin diálogo previo, o si un incumplimiento de acuerdos de alto perfil reactiva conflictos latentes. El impacto es económico y de gobernabilidad regional, pero <b>manejable con intervención oportuna</b>.'},
   {ico:'🔥',name:'C · Crisis nacional',meta:'Probabilidad baja · impacto muy alto',tag:{t:'Crítico',c:'red'},title:'Ola de protestas simultáneas a nivel nacional',body:'Convergen un detonante político-nacional (cuestionamiento a la legitimidad del gobierno, tensión entre poderes o el ciclo electoral) con el malestar socioeconómico y la minería informal. El resultado es una ola de protestas simultáneas, con bloqueos masivos y riesgo de víctimas, al estilo de diciembre de 2022 y octubre de 2025. La violencia letal en el Perú no proviene de la conflictividad socioambiental ordinaria, sino de estas crisis políticas. <b>Es de baja frecuencia pero de consecuencias severas, y exige un protocolo de respuesta preparado de antemano.</b>'}
 ]
};
function showExp(el,it){
 const d=el.querySelector('.exp-detail');
 d.querySelector('.dic').textContent=it.ico;
 const tag=d.querySelector('.exp-tag');tag.className='exp-tag '+it.tag.c;tag.textContent=it.tag.t;
 d.querySelector('.dt').innerHTML=it.title;
 d.querySelector('.db').innerHTML=it.body;
 d.classList.remove('fadeswap');void d.offsetWidth;d.classList.add('fadeswap');
}
function buildExplorer(el){
 const items=EXPLORERS[el.id];if(!items)return;
 el.innerHTML='<div class="exp-list"></div><div class="exp-detail"><div class="dtop"><div class="dic"></div><span class="exp-tag"></span></div><div class="dt"></div><div class="db"></div></div>';
 const list=el.querySelector('.exp-list');
 items.forEach((it,i)=>{const tl=document.createElement('div');tl.className='exp-tile'+(i===0?' active':'');
   tl.innerHTML='<span class="ei">'+it.ico+'</span><div><div class="en">'+it.name+'</div><div class="em">'+it.meta+'</div></div>';
   tl.onclick=()=>{el.querySelectorAll('.exp-tile').forEach(x=>x.classList.remove('active'));tl.classList.add('active');showExp(el,it);};
   list.appendChild(tl);});
 showExp(el,items[0]);
}
function activateDynamics(root){const R=root||document;
 R.querySelectorAll('.explorer').forEach(el=>{if(el.dataset.drawn||el.offsetParent===null)return;buildExplorer(el);el.dataset.drawn='1';});'''
assert engine_anchor in t
t=t.replace(engine_anchor,engine)

open('template.html','w',encoding='utf-8').write(t)
print('explorer patch applied')

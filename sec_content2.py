t=open('template.html',encoding='utf-8').read()

# ============ SECTION 2 : wrap with subtabs ============
s2_open_old='<section id="s-balance" class="slide active">\n<div class="home">'
s2_open_new='''<section id="s-balance" class="slide active">
  <div class="subhead">
    <div class="subtabs">
      <button class="subtab active" data-t="b1"><span class="st-n">2.1</span>Informes y recomendaciones</button>
      <button class="subtab" data-t="b2"><span class="st-n">2.2</span>Balance general</button>
    </div>
  </div>
  <div class="subpanel active" data-t="b1">
<div class="home">'''
assert s2_open_old in t,'s2 open missing'
t=t.replace(s2_open_old,s2_open_new)

s2_close_old='''  <div class="mosaic scene" id="mosaic"></div>
</div>
</section>

<section id="s-fortalecimiento" class="slide">'''
s2_close_new='''  <div class="mosaic scene" id="mosaic"></div>
</div>
  </div>
  <div class="subpanel" data-t="b2"><div class="subbox">
    <p class="blocklead">Balance agregado de los 8 informes emitidos entre 2023 y 2026: una producción documental amplia y diversa que formula 165 recomendaciones a 45 instituciones distintas, con una tasa de acogida global del 8%.</p>
    <div class="ch"><span class="cn">2.2.1</span>Indicadores agregados</div>
    <div class="metrics">
      <div class="metric"><b>8</b><span>Informes y documentos (todos publicados)</span></div>
      <div class="metric"><b>45</b><span>Instituciones destinatarias distintas (incl. 25 gobiernos regionales)</span></div>
      <div class="metric"><b>165</b><span>Recomendaciones formuladas</span></div>
      <div class="metric g"><b>14 · 8%</b><span>Recomendaciones acogidas</span></div>
      <div class="metric r"><b>151 · 92%</b><span>Recomendaciones no acogidas</span></div>
      <div class="metric r"><b>5 de 8</b><span>Informes con 0% de acogida (1, 5, 6, 7 y 8)</span></div>
      <div class="metric g"><b>1 de 8</b><span>Informe con acogida total (Informe 3 — Minam)</span></div>
    </div>
    <div class="ch"><span class="cn">2.2.4</span>Análisis general del cumplimiento</div>
    <div class="grid2">
      <div class="gcard"><h4><span class="ic">◆</span>El peso del Informe 5</h4><p>La baja tasa global se explica en gran medida por el Informe 5: sus <b>130 recomendaciones (79% del total)</b> no fueron acogidas por ninguna de las 30 instituciones supervisadas (Congreso, PCM, Ceplan, 10 ministerios y 25 gobiernos regionales).</p></div>
      <div class="gcard g"><h4><span class="ic">✓</span>Un panorama más matizado</h4><p>Al excluir el efecto de escala del Informe 5: el Informe 3 mantiene acogida total, el Informe 4 mejoró de 40% a <b>70%</b> (la PCM aceptó transición de gobierno) y el Informe 2 pasó de 0% a <b>33%</b> (el INDECI acogió su recomendación técnica).</p></div>
      <div class="gcard r"><h4><span class="ic">◈</span>Brechas persistentes</h4><p>La Policía Nacional no acogió ninguna de sus 5 recomendaciones (Informes 1 y 4); el <b>Ministerio de Energía y Minas</b> acumula 3 informes consecutivos (2, 7 y 8) sin acoger ninguna; y ni los 25 gobiernos regionales ni los 10 ministerios del Informe 5 acogieron sus recomendaciones.</p></div>
      <div class="gcard"><h4><span class="ic">▤</span>Comportamiento mixto y seguimiento</h4><p>La PCM acogió el Informe 4 (coyuntura) pero no el 5 (reforma estructural). Frente a la no acogida, la Adjuntía mantiene oficios de insistencia y escala hacia un <b>proyecto de ley propio</b> para crear el Sistema Nacional de Prevención y Gestión de Conflictos Sociales.</p></div>
    </div>
  </div></div>
</section>

<section id="s-fortalecimiento" class="slide">'''
assert s2_close_old in t,'s2 close missing'
t=t.replace(s2_close_old,s2_close_new)

open('template.html','w',encoding='utf-8').write(t)
print('section 2 wrapped')

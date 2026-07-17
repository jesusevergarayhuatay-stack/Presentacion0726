t=open('template.html',encoding='utf-8').read()

# 1) full name in section-1 title
t=t.replace(
'<h1 class="slidetitle">Antecedentes de la <span class="g">Adjuntía</span></h1>',
'<h1 class="slidetitle">Antecedentes de la <span class="g">Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad</span></h1>')

# 2) restructure a1: chart directly under each indicator
old='''    <div class="ch"><span class="cn">1.1.1</span>Salvaguarda de la vida y desescalamiento</div>
    <div class="metrics">
      <div class="metric g"><span class="fl"><span class="arrow dn">▼</span> 39 → 4</span><span>Víctimas fatales en conflictos (2023 → 2025)</span></div>
      <div class="metric g"><span class="fl"><span class="arrow dn">▼</span> 1365 → 201</span><span>Personas heridas (2023 → 2025)</span></div>
      <div class="metric g"><span class="fl">71.9% → 59.9%</span><span>Conflictos con hechos de violencia (baja sostenida)</span></div>
      <div class="metric"><b>89.8%</b><span>Presencia defensorial en mesas de diálogo</span></div>
    </div>
    <div class="ch"><span class="cn">1.1.2</span>Capacidad operativa y preventiva</div>
    <div class="metrics">
      <div class="metric"><b>2 933</b><span>Intervenciones defensoriales en 2025 · <b class="arrow up">+14%</b> vs. 2023 (récord desde 2018)</span></div>
      <div class="metric"><span class="fl"><span class="arrow up">+22%</span> 1936 → 2362</span><span>Supervisión preventiva</span></div>
      <div class="metric"><span class="fl"><span class="arrow up">+64%</span> 323 → 529</span><span>Intermediación y mediación</span></div>
    </div>
    <div class="ch"><span class="cn">1.1.3</span>Composición de la conflictividad</div>
    <div class="metrics">
      <div class="metric a"><b>249–277</b><span>Casos registrados por año (volumen estable)</span></div>
      <div class="metric a"><span class="fl">60.6% → 46.2%</span><span>Peso de conflictos socioambientales (2023 → 2025); mayor preponderancia de demandas a los niveles de gobierno</span></div>
    </div>
    <div class="ch"><span class="cn">▧</span>Tendencias en gráficos · 2023–2025</div>
    <div class="grid2">
      <div class="gcard"><h4>Personas fallecidas en conflictos</h4><div class="chart" id="ch-fall"></div></div>
      <div class="gcard"><h4>Personas heridas en conflictos</h4><div class="chart" id="ch-her"></div></div>
      <div class="gcard"><h4>Conflictos con hechos de violencia (%)</h4><div class="chart" id="ch-viol"></div></div>
      <div class="gcard"><h4>Presencia de la Defensoría en mesas de diálogo (%)</h4><div class="chart" id="ch-pres"></div></div>
      <div class="gcard"><h4>Actuaciones defensoriales por año</h4><div class="chart" id="ch-act"></div></div>
      <div class="gcard"><h4>Peso de conflictos socioambientales (%)</h4><div class="chart" id="ch-socio"></div></div>
    </div>'''

new='''    <div class="ch"><span class="cn">1.1.1</span>Salvaguarda de la vida y desescalamiento</div>
    <div class="metrics">
      <div class="metric g"><span class="fl"><span class="arrow dn">▼</span> 39 → 4</span><span>Víctimas fatales en conflictos (2023 → 2025)</span></div>
      <div class="metric g"><span class="fl"><span class="arrow dn">▼</span> 1365 → 201</span><span>Personas heridas (2023 → 2025)</span></div>
      <div class="metric g"><span class="fl">71.9% → 59.9%</span><span>Conflictos con hechos de violencia (baja sostenida)</span></div>
      <div class="metric"><b>89.8%</b><span>Presencia defensorial en mesas de diálogo</span></div>
    </div>
    <div class="grid2" style="margin-top:14px">
      <div class="gcard"><h4>Víctimas fatales en conflictos</h4><div class="chart" id="ch-fall"></div></div>
      <div class="gcard"><h4>Personas heridas en conflictos</h4><div class="chart" id="ch-her"></div></div>
      <div class="gcard"><h4>Conflictos con hechos de violencia (%)</h4><div class="chart" id="ch-viol"></div></div>
      <div class="gcard"><h4>Presencia de la Defensoría en mesas de diálogo (%)</h4><div class="chart" id="ch-pres"></div></div>
    </div>
    <div class="ch"><span class="cn">1.1.2</span>Capacidad operativa y preventiva</div>
    <div class="metrics">
      <div class="metric"><b>2 933</b><span>Intervenciones defensoriales en 2025 · <b class="arrow up">+14%</b> vs. 2023 (récord desde 2018)</span></div>
      <div class="metric"><span class="fl"><span class="arrow up">+22%</span> 1936 → 2362</span><span>Supervisión preventiva</span></div>
      <div class="metric"><span class="fl"><span class="arrow up">+64%</span> 323 → 529</span><span>Intermediación y mediación</span></div>
    </div>
    <div class="gcard" style="margin-top:14px"><h4>Actuaciones defensoriales por año · preventiva vs. mediación</h4><div class="chart" id="ch-act"></div></div>
    <div class="ch"><span class="cn">1.1.3</span>Composición de la conflictividad</div>
    <div class="metrics">
      <div class="metric a"><b>249–277</b><span>Casos registrados por año (volumen estable)</span></div>
      <div class="metric a"><span class="fl">60.6% → 46.2%</span><span>Peso de conflictos socioambientales (2023 → 2025); mayor preponderancia de demandas a los niveles de gobierno</span></div>
    </div>
    <div class="gcard" style="margin-top:14px"><h4>Peso de conflictos socioambientales (%)</h4><div class="chart" id="ch-socio"></div></div>'''

assert old in t,'a1 block anchor missing'
t=t.replace(old,new)

open('template.html','w',encoding='utf-8').write(t)
print('a1 relayout done')

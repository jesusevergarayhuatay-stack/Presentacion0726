t=open('template.html',encoding='utf-8').read()

# ============ SECTION 3 : FORTALECIMIENTO ============
sec3_old='''<section id="s-fortalecimiento" class="slide">
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
</section>'''

sec3_new='''<section id="s-fortalecimiento" class="slide">
  <div class="subhead">
    <div class="slidehead">
      <span class="eyebrow2"><span class="pulse"></span>03 · Fortalecimiento Institucional</span>
      <h1 class="slidetitle">Fortalecimiento para la <span class="g">prevención y gestión</span> de conflictos</h1>
      <p class="slidesub">Dos apuestas estratégicas para consolidar la institucionalidad: el Observatorio de Conflictividad Social y un Sistema Nacional articulado.</p>
    </div>
    <div class="subtabs">
      <button class="subtab active" data-t="c1"><span class="st-n">3.1</span>Observatorio de conflictividad</button>
      <button class="subtab" data-t="c2"><span class="st-n">3.2</span>Sistema Nacional (SINAGECOS)</button>
    </div>
  </div>

  <div class="subpanel active" data-t="c1"><div class="subbox">
    <div class="quote">Transformar la gestión de crisis en una cultura de inteligencia preventiva mediante el uso estratégico de la tecnología.</div>
    <div class="ch"><span class="cn">3.1.1</span>Evolución de la gestión en la Defensoría del Pueblo</div>
    <div class="timeline">
      <div class="tev"><div class="ty">1996 · Atención general</div><ul><li>Herramientas tradicionales de investigación sobre violaciones a derechos humanos (quejas, petitorios y consultas).</li></ul></div>
      <div class="tev"><div class="ty">2004 · Monitoreo especializado</div><ul><li>Primer Reporte Mensual de Conflictos Sociales. Desde entonces, <b>268 reportes</b> publicados de forma ininterrumpida.</li></ul></div>
      <div class="tev"><div class="ty">2016–2023 · Digitalización</div><ul><li>Bases de datos sólidas, dashboards y mapas interactivos: lectura geoespacial de los focos de tensión.</li></ul></div>
      <div class="tev"><div class="ty">2024–2026 · IA y prospectiva en tiempo real</div><ul><li>El Observatorio se proyecta como plataforma <b>predictiva</b>: patrones ocultos, alertas tempranas automatizadas y proyección de escenarios de riesgo.</li></ul></div>
    </div>
    <div class="ch"><span class="cn">3.1.2</span>Inteligencia artificial en tres frentes</div>
    <div class="grid3">
      <div class="gcard"><h4><span class="ic">◈</span>Análisis de patrones</h4><p>Algoritmos que identifican causas raíz y tendencias históricas de las protestas.</p></div>
      <div class="gcard"><h4><span class="ic">◇</span>Redacción asistida</h4><p>Generación automatizada de borradores de reportes mensuales y boletines de prensa.</p></div>
      <div class="gcard"><h4><span class="ic">◎</span>Escucha social</h4><p>Evaluación del sentimiento en redes digitales para comprender la percepción y demandas ciudadanas.</p></div>
    </div>
    <div class="ch"><span class="cn">3.1.3</span>Alineamiento a instrumentos</div>
    <div class="chipset">
      <span>Ley de Fortalecimiento · Política General DP</span><span>PEDN al 2050</span><span>Acuerdo Nacional · Política N.° 4</span><span>ODS 16 · ONU</span>
    </div>
    <div class="ch"><span class="cn">3.1.4</span>Metas de impacto proyectadas</div>
    <div class="metrics">
      <div class="metric"><b>85%</b><span>Precisión en alertas tempranas</span></div>
      <div class="metric g"><b>40%</b><span>Reducción del escalamiento de conflictos</span></div>
      <div class="metric"><b>100%</b><span>Trazabilidad en el cumplimiento de acuerdos</span></div>
    </div>
    <div class="ch"><span class="cn">3.1.5</span>Avances en la implementación</div>
    <div class="grid2">
      <div class="gcard"><h4><span class="ic">▤</span>8 fases de despliegue</h4><p>Infraestructura y seguridad, procesos clave, análisis y visualización, automatización, difusión y evaluación, y cierre y sostenibilidad.</p></div>
      <div class="gcard g"><h4><span class="ic">✓</span>Estado actual</h4><p>Con apoyo del <b>PNUD</b>, entre agosto y diciembre de 2025 se desarrollaron las 3 primeras fases (en prueba). En <b>febrero de 2026</b> inició un piloto en 11 oficinas defensoriales, previo al despliegue nacional.</p></div>
    </div>
  </div></div>

  <div class="subpanel" data-t="c2"><div class="subbox">
    <p class="blocklead">La Defensoría del Pueblo se proyecta a presentar ante el Congreso un proyecto de ley para crear el <b>Sistema Nacional de Prevención y Gestión de Conflictos Sociales (SINAGECOS)</b>, articulando en los tres niveles de gobierno la alerta preventiva, la mediación, la promoción del diálogo y el seguimiento de acuerdos.</p>
    <div class="ch"><span class="cn">Arquitectura</span>Diseño institucional del Sistema</div>
    <div class="arch">
      <div class="alvl rector"><div class="lv">Rector</div><div><h4>Defensoría del Pueblo · Ente Rector</h4><p>Rectoría reconocida por la Ley N.° 32028 en prevención, monitoreo y mediación.</p></div></div>
      <div class="aconn"></div>
      <div class="alvl"><div class="lv">01</div><div><h4>CONAGECOS · Consejo Nacional</h4><p>Máximo nivel de coordinación, presidido por el Defensor del Pueblo (PCM, Interior, Ministerio Público, PNP, ANGR y AMPE).</p></div></div>
      <div class="aconn"></div>
      <div class="alvl"><div class="lv">02</div><div><h4>COREGECOS · Consejos Regionales</h4><p>En cada región, el Callao y Lima Metropolitana, presididos por las Oficinas Defensoriales.</p></div></div>
      <div class="aconn"></div>
      <div class="alvl"><div class="lv">03</div><div><h4>Unidades de Gestión + SIRICS</h4><p>Fortalecimiento de las UGCS en ministerios, gobiernos regionales y locales, y creación del Sistema Integrado de Registro e Información (SIRICS).</p></div></div>
    </div>
    <div class="ch"><span class="cn">Diagnóstico</span>Institucionalidad fragmentada (Informe N.° 279)</div>
    <div class="metrics">
      <div class="metric r"><b>52%</b><span>Gobiernos regionales con unidad formal de gestión de conflictos</span></div>
      <div class="metric r"><b>53%</b><span>Ministerios analizados con unidad formalmente establecida</span></div>
      <div class="metric a"><b>90 días</b><span>Plazo para instalar el CONAGECOS tras la vigencia de la norma</span></div>
    </div>
    <p class="blocklead" style="margin-top:18px">La propuesta recoge experiencias previas (Sistema Nacional de Seguridad Ciudadana y de Justicia en Flagrancia) y representa un paso decisivo para superar la dispersión institucional, dotando al Estado de un sistema articulado, preventivo y con enfoque de derechos humanos.</p>
  </div></div>
</section>'''
assert sec3_old in t,'sec3 anchor missing'
t=t.replace(sec3_old,sec3_new)

open('template.html','w',encoding='utf-8').write(t)
print('section 3 done')

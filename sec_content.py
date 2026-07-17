t=open('template.html',encoding='utf-8').read()

# ============ SECTION 1 : ANTECEDENTES ============
sec1_old='''<section id="s-antecedentes" class="slide">
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
</section>'''

sec1_new='''<section id="s-antecedentes" class="slide">
  <div class="subhead">
    <div class="slidehead">
      <span class="eyebrow2"><span class="pulse"></span>01 · Antecedentes</span>
      <h1 class="slidetitle">Antecedentes de la <span class="g">Adjuntía</span></h1>
      <p class="slidesub">Consolidación de la labor defensorial 2023–2025: mandato, evolución institucional, supervisiones y casos emblemáticos de intervención.</p>
    </div>
    <div class="subtabs">
      <button class="subtab active" data-t="a1"><span class="st-n">1.1</span>Objetivo</button>
      <button class="subtab" data-t="a2"><span class="st-n">1.2</span>Evolución institucional</button>
      <button class="subtab" data-t="a3"><span class="st-n">1.3</span>Supervisiones</button>
      <button class="subtab" data-t="a4"><span class="st-n">1.4</span>Casos emblemáticos</button>
    </div>
  </div>

  <div class="subpanel active" data-t="a1"><div class="subbox">
    <p class="blocklead">La Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad (ACSGO) ejerce el mandato constitucional de defender los derechos fundamentales en escenarios de conflictividad social, promoviendo el diálogo como mecanismo democrático y pacífico de resolución de controversias, con respaldo de la Ley N.° 32028.</p>
    <div class="grid3" style="margin-top:22px">
      <div class="gcard"><h4><span class="ic">◈</span>Alerta preventiva</h4><p>Anticipación temprana de escenarios de riesgo mediante monitoreo permanente de la conflictividad social a nivel nacional.</p></div>
      <div class="gcard"><h4><span class="ic">◇</span>Mediación</h4><p>Facilitación del diálogo en espacios entre el Estado, la sociedad civil y las empresas para reconducir demandas a la vía institucional.</p></div>
      <div class="gcard"><h4><span class="ic">✓</span>Supervisión y cumplimiento</h4><p>Seguimiento del cumplimiento de acuerdos y de las obligaciones del Estado, operado por tres unidades funcionales especializadas.</p></div>
    </div>
    <div class="ch"><span class="cn">1.1.1</span>Salvaguarda de la vida y desescalamiento</div>
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
  </div></div>

  <div class="subpanel" data-t="a2"><div class="subbox">
    <p class="blocklead">Tres años de consolidación estratégica: del liderazgo regional y el monitoreo de crisis (2023), al hito normativo de la Ley N.° 32028 y la reestructuración operativa (2024), hasta la estandarización defensorial y la transformación tecnológica (2025).</p>
    <div class="timeline">
      <div class="tev"><div class="ty">2023 · Cimientos y liderazgo estratégico</div><ul>
        <li><b>Liderazgo Iberoamericano:</b> coordinación del Grupo Temático de Conflictividad Social de la FIO, consolidando al Perú como referente regional.</li>
        <li><b>Monitoreo ininterrumpido:</b> 372 reportes diarios durante la crisis política y 12 reportes mensuales para la toma de decisiones del Estado.</li>
      </ul></div>
      <div class="tev"><div class="ty">2024 · Hito normativo y reestructuración</div><ul>
        <li><b>Mandato legal histórico:</b> Ley N.° 32028 incorpora expresamente las atribuciones de prevención, monitoreo y mediación.</li>
        <li><b>Especialización:</b> creación de tres unidades funcionales (Prevención y Alertas; Mediación; Cumplimiento de Acuerdos).</li>
        <li><b>Estandarización:</b> dos protocolos pioneros de seguimiento a acuerdos; inicio de la supervisión nacional a las unidades de gestión de conflictos.</li>
      </ul></div>
      <div class="tev"><div class="ty">2025 · Estandarización y transformación tecnológica</div><ul>
        <li><b>Lineamientos rectores</b> para intervención en protestas, mediación y alertas tempranas.</li>
        <li><b>Observatorio de Conflictividad Social</b> (octubre 2025): dashboards en tiempo real e inteligencia artificial.</li>
        <li><b>Supervisión Nacional a 1 935 entidades</b> (19 ministerios, 25 gobiernos regionales y 1 891 municipalidades) con apoyo del PNUD.</li>
        <li><b>Despliegue en campo:</b> 58 actividades descentralizadas con impacto en más de 8 000 ciudadanos.</li>
      </ul></div>
    </div>
  </div></div>

  <div class="subpanel" data-t="a3"><div class="subbox">
    <p class="blocklead">La supervisión es la vía principal de actuación de la Adjuntía para garantizar el cumplimiento de las obligaciones del Estado. En el trienio 2023–2025 se ejerció mediante dos enfoques complementarios de alto impacto.</p>
    <div class="grid2" style="margin-top:22px">
      <div class="gcard"><h4><span class="ic">◉</span>Control in situ en crisis</h4><p>Supervisión directa de la actuación gubernamental durante coyunturas de crisis, verificando el respeto de los derechos fundamentales en el terreno.</p></div>
      <div class="gcard"><h4><span class="ic">▤</span>Evaluación de capacidades</h4><p>Diagnóstico de la capacidad institucional del Estado para gestionar la conflictividad social en los tres niveles de gobierno.</p></div>
    </div>
    <div class="ch"><span class="cn">Caso</span>Informe Defensorial N.° 001-2023-DP/APCSG</div>
    <div class="gcard"><p>A pocas semanas del inicio de la actual gestión, la institución enfrentó su primera prueba operativa con las movilizaciones del <b>19 de julio de 2023</b>. Se desplegó un operativo de gran escala movilizando a cerca de <b>300 comisionados</b> en todo el país, reflejando la capacidad de reacción inmediata ante riesgos críticos para los derechos ciudadanos.</p></div>
  </div></div>

  <div class="subpanel" data-t="a4"><div class="subbox">
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
  </div></div>
</section>'''
assert sec1_old in t,'sec1 anchor missing'
t=t.replace(sec1_old,sec1_new)

open('template.html','w',encoding='utf-8').write(t)
print('section 1 done')

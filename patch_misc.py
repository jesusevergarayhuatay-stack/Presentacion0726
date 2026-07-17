t=open('template.html',encoding='utf-8').read()

# ---- 1) sidebar logos: remove white chips ----
t=t.replace(
".sidebar .brand{background:#fff;border-radius:16px;padding:13px 14px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 26px rgba(0,0,0,.28)}",
".sidebar .brand{padding:8px 4px;display:flex;align-items:center;justify-content:center}")
t=t.replace(".sidebar .brand img{height:46px;width:auto}",".sidebar .brand img{height:52px;width:auto}")
t=t.replace(
".side-foot img{width:100%;max-width:158px;background:#fff;border-radius:12px;padding:9px;box-shadow:0 10px 26px rgba(0,0,0,.28)}",
".side-foot img{width:100%;max-width:180px;padding:2px}")

# ---- 2) section 1.1 eje cards -> Unidades Funcionales (names only) ----
old_ejes='''    <div class="grid3" style="margin-top:22px">
      <div class="gcard"><h4><span class="ic">◈</span>Alerta preventiva</h4><p>Anticipación temprana de escenarios de riesgo mediante monitoreo permanente de la conflictividad social a nivel nacional.</p></div>
      <div class="gcard"><h4><span class="ic">◇</span>Mediación</h4><p>Facilitación del diálogo en espacios entre el Estado, la sociedad civil y las empresas para reconducir demandas a la vía institucional.</p></div>
      <div class="gcard"><h4><span class="ic">✓</span>Supervisión y cumplimiento</h4><p>Seguimiento del cumplimiento de acuerdos y de las obligaciones del Estado, operado por tres unidades funcionales especializadas.</p></div>
    </div>'''
new_ejes='''    <p class="blocklead" style="margin-top:8px">Su accionar se operativiza a través de tres unidades funcionales especializadas (creadas mediante Resolución de Secretaría General N.° 0236-2024-DP/SG):</p>
    <div class="grid3" style="margin-top:16px">
      <div class="gcard"><h4><span class="ic">◈</span>Unidad Funcional de Prevención y Alertas</h4></div>
      <div class="gcard"><h4><span class="ic">◇</span>Unidad Funcional de Mediación y Gestión de Conflictos</h4></div>
      <div class="gcard"><h4><span class="ic">✓</span>Unidad Funcional de Gestión de Cumplimiento de Acuerdos</h4></div>
    </div>'''
assert old_ejes in t,'ejes anchor missing'
t=t.replace(old_ejes,new_ejes)

# ---- 3) escenarios 4.2: remove duplicate csub ----
t=t.replace(
'''    <div class="csub">Del más probable al de mayor impacto.</div>
    <div class="csub">Del más probable al de mayor impacto. Selecciona un escenario para ver el análisis completo.</div>''',
'''    <div class="csub">Del más probable al de mayor impacto. Selecciona un escenario para ver el análisis completo.</div>''')

# ---- 3b) escenarios data: A prob alta + body edit, remove C ----
t=t.replace("meta:'Probabilidad media-alta',tag:{t:'Base / más probable',c:'green'}","meta:'Probabilidad alta',tag:{t:'Base / más probable',c:'green'}")
t=t.replace("Las protestas continúan (~2 500–3 000 al año) sin derivar en víctimas masivas.","Las protestas continúan (~2 500–3 000 al año) sin derivar en una gran cantidad de heridos y fallecidos.")
# remove scenario C item (the third object in exp-escenarios array)
cItem=""",
   {ico:'🔥',name:'C · Crisis nacional',meta:'Probabilidad baja · impacto muy alto',tag:{t:'Crítico',c:'red'},title:'Ola de protestas simultáneas a nivel nacional',body:'Convergen un detonante político-nacional (cuestionamiento a la legitimidad del gobierno, tensión entre poderes o el ciclo electoral) con el malestar socioeconómico y la minería informal. El resultado es una ola de protestas simultáneas, con bloqueos masivos y riesgo de víctimas, al estilo de diciembre de 2022 y octubre de 2025. La violencia letal en el Perú no proviene de la conflictividad socioambiental ordinaria, sino de estas crisis políticas. <b>Es de baja frecuencia pero de consecuencias severas, y exige un protocolo de respuesta preparado de antemano.</b>'}"""
assert cItem in t,'C item anchor missing'
t=t.replace(cItem,"")

open('template.html','w',encoding='utf-8').write(t)
print('misc patch applied')

t=open('template.html',encoding='utf-8').read()

# 1) update ch-act + add new CHARTS entries
t=t.replace(
"'ch-act':{type:'bars',labels:['Prevención','Mediación'],max:2600,series:[{name:'2023',color:'#a9c3dd',data:[1936,323]},{name:'2025',color:'#0a56a8',data:[2362,529]}]},",
"'ch-act':{type:'bars',labels:['2023','2024','2025'],max:2600,series:[{name:'Supervisión preventiva',color:'#0a56a8',data:[1936,1958,2362]},{name:'Intermediación / mediación',color:'#12a45a',data:[323,479,529]}]},")

t=t.replace(
" 'ch-nuevos':{type:'bars',labels:['2023','2025'],max:90,series:[{name:'Conflictos nuevos',color:'#0a56a8',data:[28,81]}]}\n};",
""" 'ch-nuevos':{type:'bars',labels:['2023','2025'],max:90,series:[{name:'Conflictos nuevos',color:'#0a56a8',data:[28,81]}]},
 'ch-fall':{type:'bars',labels:['2023','2024','2025'],max:45,series:[{name:'Fallecidos',color:'#e1251b',data:[39,1,4]}]},
 'ch-her':{type:'bars',labels:['2023','2024','2025'],max:1400,series:[{name:'Heridos',color:'#c47d00',data:[1365,34,201]}]},
 'ch-pres':{type:'line',labels:['2023','2024','2025'],ymax:100,suffix:'%',series:[{name:'Presencia en diálogo',color:'#12a45a',data:[81.9,80.0,89.8]}]},
 'ch-socio':{type:'line',labels:['2023','2024','2025'],ymax:70,suffix:'%',series:[{name:'Socioambiental',color:'#12a45a',data:[60.6,55.1,46.2]}]},
 'ch-ugcs':{type:'hbars',suffix:'%',max:100,items:[{label:'Ministerios',value:53,color:'#0a56a8'},{label:'Gob. regionales',value:52,color:'#12a45a'},{label:'Municipalidades*',value:1,color:'#e1251b'}]},
 'ch-ugcsreg':{type:'bars',labels:['2022','2025'],max:25,series:[{name:'GR con unidad',color:'#12a45a',data:[8,13]}]}
};""")

# 2) expand section 1.1 charts grid
old_ch1='''    <div class="ch"><span class="cn">▧</span>Tendencias en gráficos</div>
    <div class="grid2">
      <div class="gcard"><h4>Conflictos con hechos de violencia (%)</h4><div class="chart" id="ch-viol"></div></div>
      <div class="gcard"><h4>Actuaciones defensoriales · 2023 vs 2025</h4><div class="chart" id="ch-act"></div></div>
    </div>'''
new_ch1='''    <div class="ch"><span class="cn">▧</span>Tendencias en gráficos · 2023–2025</div>
    <div class="grid2">
      <div class="gcard"><h4>Personas fallecidas en conflictos</h4><div class="chart" id="ch-fall"></div></div>
      <div class="gcard"><h4>Personas heridas en conflictos</h4><div class="chart" id="ch-her"></div></div>
      <div class="gcard"><h4>Conflictos con hechos de violencia (%)</h4><div class="chart" id="ch-viol"></div></div>
      <div class="gcard"><h4>Presencia de la Defensoría en mesas de diálogo (%)</h4><div class="chart" id="ch-pres"></div></div>
      <div class="gcard"><h4>Actuaciones defensoriales por año</h4><div class="chart" id="ch-act"></div></div>
      <div class="gcard"><h4>Peso de conflictos socioambientales (%)</h4><div class="chart" id="ch-socio"></div></div>
    </div>'''
assert old_ch1 in t,'ch1 anchor missing'
t=t.replace(old_ch1,new_ch1)

# 3) add charts to 3.2 after diagnosis metrics
old_diag='''      <div class="metric a"><b>90 días</b><span>Plazo para instalar el CONAGECOS tras la vigencia de la norma</span></div>
    </div>'''
new_diag='''      <div class="metric a"><b>90 días</b><span>Plazo para instalar el CONAGECOS tras la vigencia de la norma</span></div>
    </div>
    <div class="grid2">
      <div class="gcard"><h4>Entidades con unidad de gestión de conflictos (%)</h4><div class="chart" id="ch-ugcs"></div></div>
      <div class="gcard"><h4>Gobiernos regionales con unidad · 2022 → 2025</h4><div class="chart" id="ch-ugcsreg"></div></div>
    </div>
    <p class="csub" style="margin-top:10px">* Supervisión Nacional 2025 (con apoyo del PNUD) a 1 935 entidades: 19 ministerios, 25 gobiernos regionales y 1 891 municipalidades.</p>'''
assert old_diag in t,'diag anchor missing'
t=t.replace(old_diag,new_diag)

open('template.html','w',encoding='utf-8').write(t)
print('dashboard charts integrated')

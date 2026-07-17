t=open('template.html',encoding='utf-8').read()

# ---- E1: charts in 1.1 ----
e1a='''      <div class="metric a"><span class="fl">60.6% → 46.2%</span><span>Peso de conflictos socioambientales (2023 → 2025); mayor preponderancia de demandas a los niveles de gobierno</span></div>
    </div>
  </div></div>'''
e1b='''      <div class="metric a"><span class="fl">60.6% → 46.2%</span><span>Peso de conflictos socioambientales (2023 → 2025); mayor preponderancia de demandas a los niveles de gobierno</span></div>
    </div>
    <div class="ch"><span class="cn">▧</span>Tendencias en gráficos</div>
    <div class="grid2">
      <div class="gcard"><h4>Conflictos con hechos de violencia (%)</h4><div class="chart" id="ch-viol"></div></div>
      <div class="gcard"><h4>Actuaciones defensoriales · 2023 vs 2025</h4><div class="chart" id="ch-act"></div></div>
    </div>
  </div></div>'''
assert e1a in t; t=t.replace(e1a,e1b)

# ---- E2: gauges in 3.1.4 ----
e2a='''    <div class="ch"><span class="cn">3.1.4</span>Metas de impacto proyectadas</div>
    <div class="metrics">
      <div class="metric"><b>85%</b><span>Precisión en alertas tempranas</span></div>
      <div class="metric g"><b>40%</b><span>Reducción del escalamiento de conflictos</span></div>
      <div class="metric"><b>100%</b><span>Trazabilidad en el cumplimiento de acuerdos</span></div>
    </div>'''
e2b='''    <div class="ch"><span class="cn">3.1.4</span>Metas de impacto proyectadas</div>
    <div class="grid3">
      <div class="gcard center"><div class="gauge" id="g1"></div><p class="glbl">Precisión en alertas tempranas</p></div>
      <div class="gcard center"><div class="gauge" id="g2"></div><p class="glbl">Reducción del escalamiento de conflictos</p></div>
      <div class="gcard center"><div class="gauge" id="g3"></div><p class="glbl">Trazabilidad en el cumplimiento de acuerdos</p></div>
    </div>'''
assert e2a in t; t=t.replace(e2a,e2b)

# ---- E3: charts in 4.1 ----
e3a='''      <div class="gcard"><h4><span class="ic">◎</span>Concentración territorial</h4><p>Cinco regiones concentran el <b>45.7% (90 casos)</b>: <b>Loreto, Puno, Áncash, Piura y Cusco</b>.</p></div>
    </div>
  </div></div>'''
e3b='''      <div class="gcard"><h4><span class="ic">◎</span>Concentración territorial</h4><p>Cinco regiones concentran el <b>45.7% (90 casos)</b>: <b>Loreto, Puno, Áncash, Piura y Cusco</b>.</p></div>
    </div>
    <div class="ch"><span class="cn">▧</span>Distribución en gráficos</div>
    <div class="grid2">
      <div class="gcard"><h4>Composición por tipo de conflicto (%)</h4><div class="chart" id="ch-tipo"></div></div>
      <div class="gcard"><h4>Responsabilidad resolutiva por nivel (%)</h4><div class="chart" id="ch-comp"></div></div>
    </div>
  </div></div>'''
assert e3a in t; t=t.replace(e3a,e3b)

# ---- E4: charts in 4.2 ----
e4a='''    <div class="metrics">
      <div class="metric g"><span class="fl">71.9% → 57.4%</span><span>Conflictos con violencia: caída ininterrumpida</span></div>
      <div class="metric a"><span class="fl"><span class="arrow up">▲</span> 28 → 81</span><span>Conflictos nuevos por año (del 11% al 29% del total)</span></div>
    </div>
    <div class="ch"><span class="cn">Escenarios</span>Proyección a 12 meses</div>'''
e4b='''    <div class="metrics">
      <div class="metric g"><span class="fl">71.9% → 57.4%</span><span>Conflictos con violencia: caída ininterrumpida</span></div>
      <div class="metric a"><span class="fl"><span class="arrow up">▲</span> 28 → 81</span><span>Conflictos nuevos por año (del 11% al 29% del total)</span></div>
    </div>
    <div class="grid2">
      <div class="gcard"><h4>Conflictos con violencia (%) · 2023–2026</h4><div class="chart" id="ch-viol2"></div></div>
      <div class="gcard"><h4>Conflictos nuevos por año</h4><div class="chart" id="ch-nuevos"></div></div>
    </div>
    <div class="ch"><span class="cn">Escenarios</span>Proyección a 12 meses</div>'''
assert e4a in t; t=t.replace(e4a,e4b)

# ---- CSS ----
css='''
/* ===== charts & dynamic timeline ===== */
.chart{width:100%;height:198px;margin-top:8px}
.csvg{width:100%;height:100%;overflow:visible}
.gcard.center{text-align:center;align-items:center}
.gauge{width:122px;height:122px;margin:0 auto}
.gsvg{width:122px;height:122px}
.glbl{font-size:12px;color:var(--mut);margin-top:12px;font-weight:600;line-height:1.35}
.timeline:before{transform:scaleY(0);transform-origin:top}
.timeline.run:before{animation:tlgrow .9s ease forwards}
@keyframes tlgrow{to{transform:scaleY(1)}}
.timeline .tev{opacity:0;transform:translateX(-14px)}
.timeline.run .tev{animation:tevin .55s forwards cubic-bezier(.2,.75,.2,1)}
@keyframes tevin{to{opacity:1;transform:none}}
</style>'''
t=t.replace('</style>',css)

# ---- JS: chart engine ----
engine='''/* ===== charts & dynamic timelines ===== */
const CHARTS={
 'ch-viol':{type:'line',labels:['2023','2024','2025'],ymax:80,suffix:'%',series:[{name:'% con violencia',color:'#e1251b',data:[71.9,64.3,59.9]}]},
 'ch-act':{type:'bars',labels:['Prevención','Mediación'],max:2600,series:[{name:'2023',color:'#a9c3dd',data:[1936,323]},{name:'2025',color:'#0a56a8',data:[2362,529]}]},
 'ch-tipo':{type:'hbars',suffix:'%',max:60,items:[{label:'Socioambiental',value:48.7,color:'#0a56a8'},{label:'Demandas de gobierno',value:35,color:'#e1251b'},{label:'Otros',value:16.3,color:'#c47d00'}]},
 'ch-comp':{type:'hbars',suffix:'%',max:70,items:[{label:'Gobierno nacional',value:64.5,color:'#0a56a8'},{label:'Gob. regionales',value:24.9,color:'#12a45a'},{label:'Gob. locales',value:8.1,color:'#c47d00'},{label:'Org. autónomos',value:2.0,color:'#98a2b3'}]},
 'ch-viol2':{type:'line',labels:['2023','2024','2025','2026*'],ymax:80,suffix:'%',series:[{name:'% con violencia',color:'#e1251b',data:[71.9,64.3,59.9,57.4]}]},
 'ch-nuevos':{type:'bars',labels:['2023','2025'],max:90,series:[{name:'Conflictos nuevos',color:'#0a56a8',data:[28,81]}]}
};
const GAUGES={g1:{v:85,color:'#0a56a8'},g2:{v:40,color:'#12a45a'},g3:{v:100,color:'#0a56a8'}};
const enc=s=>encodeURIComponent(s);
function svgLine(cfg){
 const W=340,H=196,pl=36,pr=14,pt=18,pb=26,iw=W-pl-pr,ih=H-pt-pb,n=cfg.labels.length;
 const xs=i=>pl+(n===1?iw/2:iw*i/(n-1)),ys=v=>pt+ih-(v/cfg.ymax)*ih;
 let g='';for(let k=0;k<=4;k++){const y=pt+ih*k/4;g+=`<line x1="${pl}" y1="${y}" x2="${W-pr}" y2="${y}" stroke="#e7ebf1"/><text x="${pl-6}" y="${y+3}" text-anchor="end" font-size="9" fill="#98a2b3">${Math.round(cfg.ymax*(1-k/4))}</text>`;}
 let xl='';cfg.labels.forEach((l,i)=>xl+=`<text x="${xs(i)}" y="${H-8}" text-anchor="middle" font-size="9.5" fill="#5c6675">${l}</text>`);
 let body='';cfg.series.forEach(s=>{
   const ppts=s.data.map((v,i)=>`${xs(i)},${ys(v)}`).join(' ');
   body+=`<polygon points="${pl},${pt+ih} ${ppts} ${xs(n-1)},${pt+ih}" fill="${s.color}" opacity="0" class="c-area"/>`;
   body+=`<polyline points="${ppts}" fill="none" stroke="${s.color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" class="c-line"/>`;
   s.data.forEach((v,i)=>body+=`<circle cx="${xs(i)}" cy="${ys(v)}" r="0" fill="#fff" stroke="${s.color}" stroke-width="2.6" class="c-pt" data-tip="${enc(cfg.labels[i]+' · '+v+(cfg.suffix||''))}"/>`);
 });
 return `<svg viewBox="0 0 ${W} ${H}" class="csvg">${g}${xl}${body}</svg>`;
}
function svgBars(cfg){
 const W=340,H=196,pl=36,pr=14,pt=22,pb=26,iw=W-pl-pr,ih=H-pt-pb,ng=cfg.labels.length,ns=cfg.series.length;
 const gw=iw/ng,bw=Math.min(30,(gw*0.62)/ns);
 let g='';for(let k=0;k<=4;k++){const y=pt+ih*k/4;g+=`<line x1="${pl}" y1="${y}" x2="${W-pr}" y2="${y}" stroke="#e7ebf1"/><text x="${pl-6}" y="${y+3}" text-anchor="end" font-size="9" fill="#98a2b3">${Math.round(cfg.max*(1-k/4))}</text>`;}
 let bars='',xl='';
 cfg.labels.forEach((l,gi)=>{const cx=pl+gw*gi+gw/2;xl+=`<text x="${cx}" y="${H-8}" text-anchor="middle" font-size="9.5" fill="#5c6675">${l}</text>`;
   cfg.series.forEach((s,si)=>{const v=s.data[gi],bh=(v/cfg.max)*ih,x=cx-(ns*bw+(ns-1)*5)/2+si*(bw+5),y=pt+ih-bh;
     bars+=`<rect x="${x}" y="${y}" width="${bw}" height="${bh}" rx="3" fill="${s.color}" class="c-bar" style="transform-box:fill-box;transform-origin:bottom;transform:scaleY(0)" data-tip="${enc(l+' · '+s.name+': '+v)}"/>`;});});
 let leg='';cfg.series.forEach((s,i)=>leg+=`<rect x="${pl+i*92}" y="4" width="11" height="11" rx="3" fill="${s.color}"/><text x="${pl+i*92+16}" y="13.5" font-size="10" fill="#5c6675">${s.name}</text>`);
 return `<svg viewBox="0 0 ${W} ${H}" class="csvg">${leg}${g}${xl}${bars}</svg>`;
}
function svgHBars(cfg){
 const W=340,rh=36,H=cfg.items.length*rh+6;let rows='';
 cfg.items.forEach((it,i)=>{const y=6+i*rh,bw=(it.value/cfg.max)*(W-150);
   rows+=`<text x="0" y="${y+15}" font-size="11" fill="#39424f" font-weight="600">${it.label}</text>`;
   rows+=`<rect x="120" y="${y+4}" width="${W-128}" height="15" rx="7.5" fill="#eef2f8"/>`;
   rows+=`<rect x="120" y="${y+4}" width="${bw}" height="15" rx="7.5" fill="${it.color}" class="c-hbar" style="transform-box:fill-box;transform-origin:left;transform:scaleX(0)" data-tip="${enc(it.label+': '+it.value+(cfg.suffix||''))}"/>`;
   rows+=`<text x="${W-4}" y="${y+16}" text-anchor="end" font-size="12" font-weight="700" fill="${it.color}" style="font-family:Space Grotesk,monospace">${it.value}${cfg.suffix||''}</text>`;});
 return `<svg viewBox="0 0 ${W} ${H}" class="csvg" style="height:${H}px;max-height:${H}px">${rows}</svg>`;
}
function svgGauge(cfg){const r=48,c=2*Math.PI*r;
 return `<svg viewBox="0 0 120 120" class="gsvg"><circle cx="60" cy="60" r="${r}" fill="none" stroke="#e7ebf1" stroke-width="11"/>`
  +`<circle cx="60" cy="60" r="${r}" fill="none" stroke="${cfg.color}" stroke-width="11" stroke-linecap="round" transform="rotate(-90 60 60)" stroke-dasharray="${c}" stroke-dashoffset="${c}" class="g-arc" data-off="${c*(1-cfg.v/100)}"/>`
  +`<text x="60" y="68" text-anchor="middle" font-weight="700" font-size="27" fill="${cfg.color}" class="g-num" data-v="${cfg.v}" style="font-family:Space Grotesk,monospace">0%</text></svg>`;
}
function chartTips(el){el.querySelectorAll('[data-tip]').forEach(node=>{
  node.addEventListener('mousemove',e=>{tip.innerHTML='<div class="tt">'+decodeURIComponent(node.dataset.tip)+'</div>';let x=e.clientX+16,y=e.clientY+16;if(x+280>innerWidth)x=e.clientX-296;tip.style.left=x+'px';tip.style.top=y+'px';tip.classList.add('on');});
  node.addEventListener('mouseleave',()=>tip.classList.remove('on'));});}
function buildChart(el){const cfg=CHARTS[el.id];if(!cfg)return;
 el.innerHTML=cfg.type==='line'?svgLine(cfg):cfg.type==='bars'?svgBars(cfg):svgHBars(cfg);
 requestAnimationFrame(()=>{
   el.querySelectorAll('.c-line').forEach(p=>{const L=p.getTotalLength();p.style.strokeDasharray=L;p.style.strokeDashoffset=L;p.getBoundingClientRect();p.style.transition='stroke-dashoffset 1.3s ease';p.style.strokeDashoffset=0;});
   el.querySelectorAll('.c-area').forEach(a=>{a.style.transition='opacity 1s ease .35s';a.style.opacity='.12';});
   el.querySelectorAll('.c-pt').forEach((c,i)=>{c.style.transition='r .35s ease';setTimeout(()=>c.setAttribute('r','4'),420+i*110);});
   el.querySelectorAll('.c-bar').forEach((b,i)=>{b.style.transition='transform .85s cubic-bezier(.2,.8,.2,1) '+(i*90)+'ms';b.style.transform='scaleY(1)';});
   el.querySelectorAll('.c-hbar').forEach((b,i)=>{b.style.transition='transform .95s cubic-bezier(.2,.8,.2,1) '+(i*100)+'ms';b.style.transform='scaleX(1)';});
 });
 chartTips(el);
}
function buildGauge(el){const cfg=GAUGES[el.id];if(!cfg)return;el.innerHTML=svgGauge(cfg);
 requestAnimationFrame(()=>{const a=el.querySelector('.g-arc');a.style.transition='stroke-dashoffset 1.4s cubic-bezier(.2,.8,.2,1)';a.style.strokeDashoffset=a.dataset.off;
   const num=el.querySelector('.g-num');let v=+num.dataset.v,n=0,st=Math.max(1,Math.ceil(v/40));const tt=setInterval(()=>{n+=st;if(n>=v){n=v;clearInterval(tt)}num.textContent=n+'%';},28);});}
function activateDynamics(root){const R=root||document;
 R.querySelectorAll('.chart').forEach(el=>{if(el.dataset.drawn||el.offsetParent===null)return;buildChart(el);el.dataset.drawn='1';});
 R.querySelectorAll('.gauge').forEach(el=>{if(el.dataset.drawn||el.offsetParent===null)return;buildGauge(el);el.dataset.drawn='1';});
 R.querySelectorAll('.timeline').forEach(tl=>{if(tl.dataset.run||tl.offsetParent===null)return;tl.classList.add('run');[...tl.querySelectorAll('.tev')].forEach((e,i)=>e.style.animationDelay=(i*0.16)+'s');tl.dataset.run='1';});
}

/* ===== init ===== */'''
t=t.replace("/* ===== init ===== */",engine,1)

# hooks
t=t.replace("  if(id==='s-balance'){recompute(VIS);}\n  window.scrollTo({top:0,behavior:'smooth'});",
            "  if(id==='s-balance'){recompute(VIS);}\n  activateDynamics(document.getElementById(id));\n  window.scrollTo({top:0,behavior:'smooth'});")
t=t.replace("  if(k==='b1')recompute(VIS);\n});",
            "  if(k==='b1')recompute(VIS);\n  activateDynamics(sec);\n});")
t=t.replace("window.addEventListener('load',()=>{ setTimeout(()=>recompute(DOCS),400); });",
            "window.addEventListener('load',()=>{ setTimeout(()=>{recompute(DOCS);activateDynamics(document);},400); });")

open('template.html','w',encoding='utf-8').write(t)
print('charts patch applied')

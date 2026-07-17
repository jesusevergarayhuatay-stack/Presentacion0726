t=open('template.html',encoding='utf-8').read()

# ---- 1) panorama bars: fill by acogida percentage ----
old_pano='''function renderPanorama(list){
  const maxRecs=Math.max(1,...list.map(recSum));
  prowsEl.innerHTML=list.map((d)=>{
    const ok=okRecs(d),no=noRecs(d),v=recSum(d);const i=DOCS.indexOf(d);
    const tip=`<div class="tt">${d.short} · ${d.tipo}</div><div class="tk"><span class="ok">Acogidas</span><b class="ok">${ok}</b></div><div class="tk"><span class="no">No acogidas</span><b class="no">${no}</b></div><div class="tk"><span class="tot">Total</span><b class="tot">${v}</b></div>`;
    return `<div class="prow" data-i="${i}" data-tip="${encodeURIComponent(tip)}"><span class="pl">${d.short}</span><div class="ptrack">
      <span class="seg ok" data-w="${ok/maxRecs*100}"></span><span class="seg no" data-w="${no/maxRecs*100}"></span></div><span class="pv">${v}</span></div>`;
  }).join('');
  requestAnimationFrame(()=>prowsEl.querySelectorAll('.seg').forEach(s=>s.style.width=parseFloat(s.dataset.w)+'%'));
}'''
new_pano='''function renderPanorama(list){
  prowsEl.innerHTML=list.map((d)=>{
    const ok=okRecs(d),no=noRecs(d),v=recSum(d);const i=DOCS.indexOf(d);
    const pct=v?Math.round(ok/v*100):0;
    const tip=`<div class="tt">${d.short} · ${d.tipo}</div><div class="tk"><span class="ok">Acogidas</span><b class="ok">${ok} · ${pct}%</b></div><div class="tk"><span class="no">No acogidas</span><b class="no">${no}</b></div><div class="tk"><span class="tot">Total</span><b class="tot">${v}</b></div>`;
    return `<div class="prow" data-i="${i}" data-tip="${encodeURIComponent(tip)}"><span class="pl">${d.short}</span><div class="ptrack"><span class="seg ok" data-w="${pct}"></span></div><span class="pv">${v}</span></div>`;
  }).join('');
  requestAnimationFrame(()=>prowsEl.querySelectorAll('.seg').forEach(s=>s.style.width=parseFloat(s.dataset.w)+'%'));
}'''
assert old_pano in t,'renderPanorama anchor missing'
t=t.replace(old_pano,new_pano)

# ---- 2) sober "back to cover" button in sidebar ----
t=t.replace('  </nav>\n  <div class="side-foot">',
            '  </nav>\n  <button class="cover-btn" id="toCover"><span>&#8617;</span> Volver a la portada</button>\n  <div class="side-foot">')

# CSS for the button
t=t.replace('.side-foot{margin-top:auto;text-align:center;padding-top:20px}',
'''.cover-btn{margin-top:16px;width:100%;padding:11px 14px;border-radius:12px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);color:rgba(255,255,255,.6);font-family:'Sora';font-weight:600;font-size:12px;cursor:pointer;transition:.2s;display:flex;align-items:center;gap:8px;justify-content:center}
.cover-btn:hover{background:rgba(255,255,255,.09);color:#fff;border-color:rgba(255,255,255,.22)}
.cover-btn span{font-size:14px}
.side-foot{margin-top:auto;text-align:center;padding-top:20px}''')

# ---- 3) wire button in cover IIFE ----
t=t.replace(
"var b=document.getElementById('startBtn');if(b)b.addEventListener('click',start);",
"""function showCover(){cover.style.display='flex';requestAnimationFrame(function(){cover.classList.remove('hide');});}
var b=document.getElementById('startBtn');if(b)b.addEventListener('click',start);
var tc=document.getElementById('toCover');if(tc)tc.addEventListener('click',showCover);""")

open('template.html','w',encoding='utf-8').write(t)
print('cover2 patch applied')

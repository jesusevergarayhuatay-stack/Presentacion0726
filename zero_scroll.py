t=open('template.html',encoding='utf-8').read()

# --- body: fixed viewport ---
t=t.replace(
"body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:#eef2f8}",
"body{font-family:'Inter',system-ui,sans-serif;color:var(--ink);background:#eef2f8;height:100vh;overflow:hidden}")

# --- stage: fixed height, no scroll ---
t=t.replace(
".stage{margin-left:266px;position:relative;z-index:2;min-height:100vh}",
".stage{margin-left:266px;position:relative;z-index:2;height:100vh;overflow:hidden}")

# --- slide: flex column filling viewport ---
t=t.replace(
".slide{display:none}\n.slide.active{display:block;animation:slideIn .55s cubic-bezier(.2,.75,.2,1)}",
".slide{display:none}\n.slide.active{display:flex;flex-direction:column;height:100%;animation:slideIn .5s cubic-bezier(.2,.75,.2,1)}")

# --- subhead fixed header ---
t=t.replace(
".subhead{max-width:1200px;margin:0 auto;padding:26px 46px 0}",
".subhead{flex:none;width:100%;max-width:1200px;margin:0 auto;padding:22px 46px 0}")

# --- subpanel: internal scroll + styled scrollbar ---
t=t.replace(
".subpanel{display:none}\n.subpanel.active{display:block;animation:slideIn .45s cubic-bezier(.2,.75,.2,1)}",
""".subpanel{display:none}
.subpanel.active{display:block;flex:1 1 auto;min-height:0;overflow-y:auto;overflow-x:hidden;animation:slideIn .45s cubic-bezier(.2,.75,.2,1)}
.subpanel::-webkit-scrollbar{width:9px}
.subpanel::-webkit-scrollbar-thumb{background:rgba(16,42,80,.18);border-radius:8px}
.subpanel::-webkit-scrollbar-thumb:hover{background:rgba(16,42,80,.34)}
.subpanel::-webkit-scrollbar-track{background:transparent}""")

# --- re-animate charts/gauges/timelines on every activation ---
t=t.replace(
'''function activateDynamics(root){const R=root||document;
 R.querySelectorAll('.explorer').forEach(el=>{if(el.dataset.drawn||el.offsetParent===null)return;buildExplorer(el);el.dataset.drawn='1';});
 R.querySelectorAll('.chart').forEach(el=>{if(el.dataset.drawn||el.offsetParent===null)return;buildChart(el);el.dataset.drawn='1';});
 R.querySelectorAll('.gauge').forEach(el=>{if(el.dataset.drawn||el.offsetParent===null)return;buildGauge(el);el.dataset.drawn='1';});
 R.querySelectorAll('.timeline').forEach(tl=>{if(tl.dataset.run||tl.offsetParent===null)return;tl.classList.add('run');[...tl.querySelectorAll('.tev')].forEach((e,i)=>e.style.animationDelay=(i*0.16)+'s');tl.dataset.run='1';});
}''',
'''function activateDynamics(root){const R=root||document;
 R.querySelectorAll('.explorer').forEach(el=>{if(el.dataset.drawn||el.offsetParent===null)return;buildExplorer(el);el.dataset.drawn='1';});
 R.querySelectorAll('.chart').forEach(el=>{if(el.offsetParent===null)return;buildChart(el);});
 R.querySelectorAll('.gauge').forEach(el=>{if(el.offsetParent===null)return;buildGauge(el);});
 R.querySelectorAll('.timeline').forEach(tl=>{if(tl.offsetParent===null)return;tl.classList.remove('run');void tl.offsetWidth;tl.classList.add('run');[...tl.querySelectorAll('.tev')].forEach((e,i)=>e.style.animationDelay=(i*0.16)+'s');});
}''')

# --- init: attach subpanel scroll -> progress bar ---
t=t.replace(
"window.addEventListener('load',()=>{ setTimeout(()=>{recompute(DOCS);activateDynamics(document);},400); });",
"""document.querySelectorAll('.subpanel').forEach(sp=>sp.addEventListener('scroll',()=>{const p=sp.scrollTop/(sp.scrollHeight-sp.clientHeight||1);document.getElementById('prog').style.width=(p*100)+'%';}));
window.addEventListener('load',()=>{ setTimeout(()=>{recompute(DOCS);activateDynamics(document);},400); });""")

open('template.html','w',encoding='utf-8').write(t)
print('zero-scroll applied')

t=open('template.html',encoding='utf-8').read()

# --- markup: insert cover after #prog ---
cover_html='''<div id="cover">
  <div class="cv-aurora"></div>
  <div class="cv-grid"></div>
  <div class="cv-inner">
    <img class="cv-logo" src="__LOGO__" alt="Defensoría del Pueblo">
    <div class="cv-adj">Defensoría del Pueblo · Adjuntía para la Prevención de Conflictos Sociales y la Gobernabilidad</div>
    <h1 class="cv-title">BALANCE Y PROSPECTIVA<span class="cv-title-sub">en materia de prevención y gestión de conflictos sociales</span></h1>
    <div class="cv-phases">
      <span class="cv-ph">Contexto</span><span class="cv-arw">→</span>
      <span class="cv-ph">Mejoras</span><span class="cv-arw">→</span>
      <span class="cv-ph">Prospección</span>
    </div>
    <div class="cv-meta"><span>Julio 2026</span><i></i><span>Período del informe · 2023 – 2026</span></div>
    <button id="startBtn" class="cv-btn">Iniciar presentación <span>&rarr;</span></button>
  </div>
  <img class="cv-anniv" src="__ANNIV__" alt="30 años Defendiendo tus derechos">
  <div class="cv-hint">Presiona <b>Iniciar</b> o <b>Enter</b> para comenzar</div>
</div>
'''
t=t.replace('<div id="prog"></div>','<div id="prog"></div>\n'+cover_html)

# --- CSS ---
css='''
/* ===== cover / portada ===== */
#cover{position:fixed;inset:0;z-index:200;overflow:hidden;background:radial-gradient(120% 120% at 50% -10%,#13233f,#0a1120 58%,#070c16);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:5vh 6vw;color:#eaf0ff;transition:opacity .7s ease,transform .7s ease}
#cover.hide{opacity:0;transform:scale(1.05);pointer-events:none}
.cv-aurora{position:absolute;inset:-25%;z-index:0;background:radial-gradient(closest-side at 18% 22%,rgba(46,134,255,.55),transparent 70%),radial-gradient(closest-side at 82% 18%,rgba(225,37,27,.42),transparent 70%),radial-gradient(closest-side at 68% 88%,rgba(18,164,90,.34),transparent 70%),radial-gradient(closest-side at 28% 82%,rgba(124,92,255,.36),transparent 70%);filter:blur(52px);animation:cvfloat 20s ease-in-out infinite}
@keyframes cvfloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(3%,-2%) scale(1.05)}66%{transform:translate(-3%,2%) scale(1.02)}}
.cv-grid{position:absolute;inset:0;z-index:0;opacity:.22;background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);background-size:54px 54px;mask:radial-gradient(circle at 50% 45%,#000,transparent 78%)}
.cv-inner{position:relative;z-index:2;max-width:1000px;display:flex;flex-direction:column;align-items:center;gap:22px}
.cv-inner>*{opacity:0;transform:translateY(22px);animation:cvUp .85s forwards cubic-bezier(.2,.75,.2,1)}
.cv-inner>*:nth-child(1){animation-delay:.15s}.cv-inner>*:nth-child(2){animation-delay:.3s}.cv-inner>*:nth-child(3){animation-delay:.45s}.cv-inner>*:nth-child(4){animation-delay:.6s}.cv-inner>*:nth-child(5){animation-delay:.75s}.cv-inner>*:nth-child(6){animation-delay:.9s}
@keyframes cvUp{to{opacity:1;transform:none}}
.cv-logo{height:74px;width:auto}
.cv-adj{font-size:13px;letter-spacing:2.4px;text-transform:uppercase;color:#9fb4d6;font-weight:600;max-width:680px;line-height:1.55}
.cv-title{font-family:'Sora';font-weight:800;font-size:clamp(30px,5.2vw,60px);line-height:1.04;letter-spacing:-1px;background:linear-gradient(100deg,#eaf2ff,#8fbcff 55%,#ff8f86);-webkit-background-clip:text;background-clip:text;color:transparent;display:flex;flex-direction:column;align-items:center}
.cv-title-sub{font-family:'Sora';font-weight:600;font-size:clamp(13px,1.7vw,20px);letter-spacing:.4px;color:#c3d3ee;-webkit-text-fill-color:#c3d3ee;margin-top:14px;text-transform:none;max-width:760px}
.cv-phases{display:flex;align-items:center;gap:14px;flex-wrap:wrap;justify-content:center}
.cv-ph{font-family:'Sora';font-weight:700;font-size:14px;padding:9px 18px;border-radius:30px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.06);backdrop-filter:blur(6px);color:#eaf0ff}
.cv-arw{color:#7f9cc9;font-size:16px}
.cv-meta{display:flex;align-items:center;gap:16px;color:#b9c8e4;font-size:14.5px;font-weight:500;flex-wrap:wrap;justify-content:center}
.cv-meta i{width:6px;height:6px;border-radius:50%;background:#e1251b;display:inline-block}
.cv-btn{margin-top:6px;display:inline-flex;align-items:center;gap:12px;font-family:'Sora';font-weight:700;font-size:16px;color:#fff;border:0;cursor:pointer;padding:16px 36px;border-radius:16px;background:linear-gradient(120deg,#0a56a8,#2e86ff);box-shadow:0 14px 40px rgba(46,134,255,.5);transition:.25s;position:relative;overflow:hidden}
.cv-btn:hover{transform:translateY(-3px);box-shadow:0 20px 56px rgba(46,134,255,.66)}
.cv-btn>span{transition:.25s}.cv-btn:hover>span{transform:translateX(5px)}
.cv-btn:before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;background:linear-gradient(120deg,transparent,rgba(255,255,255,.35),transparent);transform:translateX(-100%);animation:cvshine 3.2s infinite}
@keyframes cvshine{0%{transform:translateX(-100%)}55%,100%{transform:translateX(100%)}}
.cv-anniv{position:absolute;bottom:34px;right:42px;z-index:2;height:66px;opacity:0;animation:cvUp 1s .95s forwards}
.cv-hint{position:absolute;bottom:40px;left:42px;z-index:2;color:#6f86ad;font-size:12px;letter-spacing:1px;opacity:0;animation:cvUp 1s 1.1s forwards}
.cv-hint b{color:#9fb4d6;font-weight:700}
@media(max-width:720px){.cv-anniv{height:46px;bottom:18px;right:18px}.cv-hint{display:none}.cv-logo{height:56px}}
</style>'''
t=t.replace('</style>',css)

# --- JS: start button ---
js='''<script>
(function(){var cover=document.getElementById('cover');if(!cover)return;
function start(){cover.classList.add('hide');try{navTo('s-antecedentes');}catch(e){}setTimeout(function(){cover.style.display='none';},760);}
var b=document.getElementById('startBtn');if(b)b.addEventListener('click',start);
document.addEventListener('keydown',function(e){if(cover.style.display!=='none'&&!cover.classList.contains('hide')&&(e.key==='Enter'||e.key===' ')){e.preventDefault();start();}});
})();
</script>
</body>'''
t=t.replace('</body>',js)

open('template.html','w',encoding='utf-8').write(t)
print('cover added')

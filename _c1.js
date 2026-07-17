
(function(){var cover=document.getElementById('cover');if(!cover)return;
function start(){cover.classList.add('hide');try{navTo('s-antecedentes');}catch(e){}setTimeout(function(){cover.style.display='none';},760);}
function showCover(){cover.style.display='flex';requestAnimationFrame(function(){cover.classList.remove('hide');});}
var b=document.getElementById('startBtn');if(b)b.addEventListener('click',start);
var tc=document.getElementById('toCover');if(tc)tc.addEventListener('click',showCover);
document.addEventListener('keydown',function(e){if(cover.style.display!=='none'&&!cover.classList.contains('hide')&&(e.key==='Enter'||e.key===' ')){e.preventDefault();start();}});
})();

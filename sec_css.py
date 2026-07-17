t=open('template.html',encoding='utf-8').read()
CSS='''
/* ===== sub-tabs & content ===== */
.subhead{max-width:1200px;margin:0 auto;padding:26px 46px 0}
.subtabs{display:flex;gap:6px;flex-wrap:wrap;border-bottom:1px solid var(--line)}
.subtab{position:relative;font-family:'Sora';font-weight:600;font-size:13px;color:var(--mut);background:transparent;border:0;padding:13px 16px;cursor:pointer;transition:.2s;border-bottom:2.5px solid transparent}
.subtab .st-n{font-family:'Space Grotesk';font-size:11px;color:var(--mut2);margin-right:7px;font-weight:700}
.subtab:hover{color:var(--ink)}
.subtab.active{color:var(--blue)}
.subtab.active .st-n{color:var(--blue)}
.subtab.active:after{content:"";position:absolute;left:6px;right:6px;bottom:-1.5px;height:2.5px;background:linear-gradient(90deg,var(--blue),var(--red));border-radius:2px}
.subpanel{display:none}
.subpanel.active{display:block;animation:slideIn .45s cubic-bezier(.2,.75,.2,1)}
.subbox{max-width:1120px;margin:0 auto;padding:34px 46px 80px}
.blocklead{font-size:15px;line-height:1.72;color:#2a3340;max-width:940px}
.ch{font-family:'Sora';font-weight:700;font-size:17px;margin:34px 0 4px;display:flex;align-items:center;gap:11px}
.ch .cn{font-family:'Space Grotesk';font-size:12px;color:#fff;background:linear-gradient(135deg,var(--blue),var(--blue-d));padding:4px 9px;border-radius:8px}
.csub{font-size:12.5px;color:var(--mut2);margin:2px 0 14px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.gcard{border:1px solid var(--gbrd);border-radius:20px;padding:22px 24px;background:var(--glass);backdrop-filter:blur(14px) saturate(150%);box-shadow:var(--sh);transition:.3s}
.gcard:hover{transform:translateY(-4px);box-shadow:var(--sh2)}
.gcard h4{font-family:'Sora';font-weight:700;font-size:14.5px;margin-bottom:9px;display:flex;align-items:center;gap:9px}
.gcard h4 .ic{width:30px;height:30px;border-radius:9px;display:grid;place-items:center;color:#fff;font-size:14px;background:linear-gradient(135deg,var(--blue),var(--blue-d));flex:none}
.gcard.r h4 .ic{background:linear-gradient(135deg,var(--red),#b41b13)}
.gcard.g h4 .ic{background:linear-gradient(135deg,var(--grn),#0c7a41)}
.gcard p{font-size:13px;line-height:1.6;color:#39424f}
.metrics{display:flex;gap:12px;flex-wrap:wrap;margin-top:14px}
.metric{flex:1;min-width:130px;border:1px solid var(--line);border-left:4px solid var(--blue);background:rgba(255,255,255,.55);border-radius:13px;padding:14px 16px}
.metric.g{border-left-color:var(--grn)}.metric.r{border-left-color:var(--red)}.metric.a{border-left-color:var(--amb)}
.metric b{font-family:'Space Grotesk';font-size:24px;display:block;color:var(--ink);line-height:1}
.metric .fl{font-family:'Space Grotesk';font-size:13px;font-weight:700}
.metric span{font-size:11px;color:var(--mut);line-height:1.4;display:block;margin-top:6px}
.arrow{font-weight:700}.arrow.dn{color:var(--grn)}.arrow.up{color:var(--blue)}
.timeline{position:relative;margin-top:22px;padding-left:28px}
.timeline:before{content:"";position:absolute;left:7px;top:8px;bottom:8px;width:2px;background:linear-gradient(var(--blue),var(--red))}
.tev{position:relative;margin-bottom:24px}
.tev:before{content:"";position:absolute;left:-28px;top:3px;width:15px;height:15px;border-radius:50%;background:#fff;border:3px solid var(--blue);box-shadow:0 0 0 4px rgba(10,86,168,.12)}
.tev .ty{font-family:'Space Grotesk';font-weight:700;color:var(--blue);font-size:15px}
.tev h4{font-family:'Sora';font-size:14.5px;margin:5px 0 8px}
.tev ul{list-style:none;display:grid;gap:7px}
.tev li{font-size:13px;line-height:1.55;color:#39424f;padding-left:17px;position:relative}
.tev li:before{content:"";position:absolute;left:2px;top:7px;width:6px;height:6px;border-radius:2px;transform:rotate(45deg);background:var(--red)}
.tev li b{color:var(--ink)}
.tag2{display:inline-flex;align-items:center;gap:7px;font-size:11px;font-weight:700;letter-spacing:.4px;text-transform:uppercase;color:var(--amb);background:#fdf3e0;border:1px solid #f0d8a8;padding:5px 12px;border-radius:20px;margin:8px 0}
.chipset{display:flex;flex-wrap:wrap;gap:9px;margin-top:14px}
.chipset span{font-size:12px;padding:8px 14px;border-radius:12px;background:var(--blue-l);border:1px solid #cfe0f4;color:var(--blue-d);font-weight:600}
.arch{display:grid;gap:12px;margin-top:20px}
.alvl{display:flex;align-items:center;gap:16px;border:1px solid var(--gbrd);border-radius:16px;padding:16px 20px;background:var(--glass);box-shadow:var(--sh);position:relative}
.alvl .lv{font-family:'Space Grotesk';font-weight:700;font-size:12px;color:#fff;background:var(--blue);width:38px;height:38px;border-radius:11px;display:grid;place-items:center;flex:none}
.alvl.rector .lv{background:linear-gradient(135deg,var(--red),#b41b13)}
.alvl h4{font-family:'Sora';font-size:14px;margin-bottom:3px}
.alvl p{font-size:12px;color:var(--mut);line-height:1.5}
.aconn{height:14px;width:2px;background:var(--line);margin:-6px 0 -6px 39px}
.scen{border:1px solid var(--gbrd);border-top:5px solid var(--mut2);border-radius:20px;padding:24px 26px;background:var(--glass);box-shadow:var(--sh);transition:.3s}
.scen:hover{transform:translateY(-4px);box-shadow:var(--sh2)}
.scen.a{border-top-color:var(--grn)}.scen.b{border-top-color:var(--amb)}.scen.c{border-top-color:var(--red)}
.scen .sh{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:10px}
.scen .sh h4{font-family:'Sora';font-size:16px}
.prob{font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.6px;padding:5px 11px;border-radius:20px}
.prob.a{color:var(--grn);background:var(--grn-l);border:1px solid #b8e6cb}
.prob.b{color:var(--amb);background:#fdf3e0;border:1px solid #f0d8a8}
.prob.c{color:var(--red);background:var(--red-l);border:1px solid #f6c9c4}
.scen p{font-size:13px;line-height:1.6;color:#39424f;margin-top:6px}
.quote{border-left:4px solid var(--blue);background:rgba(10,86,168,.045);border-radius:12px;padding:16px 20px;font-size:14.5px;line-height:1.6;color:#26303c;font-style:italic;margin-top:4px}
@media(max-width:980px){.grid2,.grid3{grid-template-columns:1fr}.subbox{padding:26px 22px 60px}.subhead{padding:20px 22px 0}}
</style>'''
t=t.replace('</style>',CSS)
open('template.html','w',encoding='utf-8').write(t)
print('css added')

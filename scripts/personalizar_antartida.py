#!/usr/bin/env python3
"""Personalización única de la copia AR de ANTÁRTIDA. Ejecútese solo al importar la base."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
site = ROOT / "public"
css = """
<style id="antartida-theme">
:root{font-family:'Trebuchet MS',Inter,system-ui,sans-serif!important;background:#061827!important;color:#f3fdff!important;color-scheme:dark}
body{background:linear-gradient(140deg,#051521 0%,#09263c 52%,#051521 100%) fixed!important}
header{height:auto!important;min-height:86px;padding:18px 28px!important;border-bottom:1px solid #237ba0!important;background:linear-gradient(105deg,#061726,#0a3854 68%,#07506e)!important;box-shadow:0 9px 35px #020c16a8;position:relative;z-index:4}
.brand{font-weight:900!important;letter-spacing:.045em!important;color:#fff!important;font-size:22px!important}
.brand em{font-style:normal!important;color:#75e6ff!important}
.brand small{display:block!important;margin-top:6px;font-size:11px!important;letter-spacing:.08em!important;text-transform:uppercase;color:#bcf2ff!important}
.brand .antarctica-mark{display:inline-grid;place-items:center;width:42px;height:42px;border-radius:13px;background:linear-gradient(145deg,#fff,#abebf8);color:#05618b;margin-right:8px;font-size:26px;vertical-align:middle;box-shadow:0 7px 23px #0005}
.brand .antarctica-submark{font-size:10px;text-transform:uppercase;color:#b5effd;letter-spacing:.16em}
.wrap{max-width:1750px!important;grid-template-columns:285px minmax(340px,1fr) 325px!important;gap:18px!important;padding:22px!important}
.panel{border:1px solid #24536a!important;background:linear-gradient(155deg,#0c2b41,#0a2134 80%)!important;box-shadow:0 10px 36px #0003!important;border-radius:21px!important}
aside.panel{border-top:3px solid #57dcff!important}
.panel h1,.panel h2{color:#edfcff!important;letter-spacing:.01em}
.muted,.group-label{color:#a7d5e5!important}
.group-label{letter-spacing:.15em!important}
button{background:linear-gradient(115deg,#45c8ed,#9beafa)!important;color:#06283e!important;border-radius:12px!important;box-shadow:0 5px 15px #0315215c;font-weight:800!important;transition:filter .15s,transform .15s}
button:hover:not(:disabled){filter:brightness(1.08);transform:translateY(-1px)}
button.subtle,.editor-link,.view-button{background:#10384f!important;color:#daf7ff!important;border:1px solid #33718b!important;box-shadow:none!important}
button.danger{background:#532b3d!important;color:#ffdde4!important;border-color:#845367!important}
.artentry,.layer{background:#082235!important;border:1px solid #275872!important;color:#f1fbff!important}
.artentry.active,.layer.active,.view-button.active{background:#145879!important;border-color:#75e5ff!important;box-shadow:0 0 0 1px #64e9ff66!important}
.artentry small,.layerdepth{color:#9dcadb!important}
.canvas-wrap{background:radial-gradient(ellipse at 50% 40%,#25678b 0%,#0b304b 44%,#061524 83%)!important;border-color:#3b819d!important;position:relative}
.canvas-wrap:before{content:'❄  EXPERIENCIA POLAR  ❄';position:absolute;left:20px;top:14px;font-size:10px;font-weight:800;letter-spacing:.21em;color:#b5efff9e;pointer-events:none}
.artboard{border-color:#a3ebfa!important;box-shadow:0 25px 80px #020a15de!important}
.spacing-toolbar,.notice{background:#082a41!important;border:1px solid #29617b!important}
input[type=text],input[type=number],select{background:#051d30!important;color:#fff!important;border:1px solid #33718b!important}
input[type=range]{accent-color:#71e4ff!important}
.field label{color:#c9f1fa!important}
.field output,.eye{color:#78e8ff!important}
.flag{background:#0d465f!important;color:#b6f0ff!important;border-color:#418ba7!important}
dialog{background:#092b42!important;color:#eafdff!important;border-color:#5aadc9!important}
#qrLink{color:#84e8ff!important}
#status,.status{color:#bdedfc!important}
.antarctica-ribbon{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:14px;padding:11px 15px;border:1px solid #2f7794;border-radius:14px;background:linear-gradient(95deg,#0c3f5f,#0d2b43)}
.antarctica-ribbon b{color:#dbfaff;font-size:12px;letter-spacing:.035em}
.antarctica-ribbon span{color:#9bd2e5;font-size:11px}
@media(max-width:1200px){.wrap{grid-template-columns:235px minmax(290px,1fr)!important}.right{grid-column:1/-1}}
@media(max-width:720px){header{padding:17px!important}.brand{font-size:18px!important}.wrap{display:block!important;padding:10px!important}.wrap>.panel,.wrap>.center{margin-bottom:14px}.right{display:flex!important}.antarctica-ribbon{margin:0 0 14px}}
</style>
"""

def replace_once(s, a, b, label):
    if a not in s:
        raise ValueError(f"No se encontró el marcador de {label}")
    return s.replace(a,b,1)

p=site/"editor.html"
editor=p.read_text(encoding="utf-8")
editor=replace_once(editor,"<title>Visor-222 | Editor visual de capas</title>",
    "<title>ANTÁRTIDA | Estudio de Realidad Aumentada</title>","título editor")
editor=replace_once(editor,"</head>",css+"\n</head>","tema")
editor=replace_once(editor,'<div class="brand">VISOR<em>·222</em> <small>Editor visual · Prototipo</small></div>',
    '<div class="brand"><span class="antarctica-mark" aria-hidden="true">❄</span>ANTÁRTIDA <em>STUDIO</em><small>Heladería & Café · Editor de experiencias AR</small></div>',
    "marca editor")
editor=replace_once(editor,'<div class="wrap">','<div class="wrap">',"envoltura")
editor=replace_once(editor,'<main class="center">','<main class="center"><div class="antarctica-ribbon"><b>❄ LABORATORIO DE EXPERIENCIAS</b><span>Convierte tus diseños en momentos mágicos con capas, profundidad y movimiento.</span></div>',"banda")
editor=editor.replace("Mis cuadros</h1>","Experiencias de Antártida</h1>")
editor=editor.replace("Composición del cuadro · Lienzo 3D","Escenario polar · Editor 3D")
editor=editor.replace("Propiedades de la capa","Personaliza tu capa")
editor=editor.replace("Probar en mi celular","Vista AR en mi celular")
editor=editor.replace("visor222-editor-visual-v1","antartida-editor-visual-v1")
editor=editor.replace("Visor-222", "ANTÁRTIDA AR")
p.write_text(editor,encoding="utf-8")

p=site/"index.html"
viewer=p.read_text(encoding="utf-8")
viewer=viewer.replace("Visor-222 · Escanear cuadros","ANTÁRTIDA · Realidad Aumentada")
viewer=viewer.replace('<meta name="theme-color" content="#050b1c">','<meta name="theme-color" content="#062338">')
viewer=viewer.replace("La magia está frente a ti","La magia del hielo cobra vida")
viewer=viewer.replace("Activa tu cámara y observa cómo las imágenes cobran vida ante tus ojos.",
"¡Bienvenido a ANTÁRTIDA! Activa tu cámara, descubre nuestras experiencias y deja que la magia polar cobre vida.")
viewer=viewer.replace('VISOR<span style="color:#5dd4ff">·222</span>','❄ ANTÁRTIDA<span style="color:#5dd4ff"> AR</span>')
viewer=viewer.replace("Prepara el cuadro frente a la cámara.","Apunta tu cámara a una imagen de Antártida.")
viewer=viewer.replace("#050b1c","#061827").replace("#122f54","#0b4262").replace("#5dd4ff","#6ddffa")
p.write_text(viewer,encoding="utf-8")

print("ANTÁRTIDA: editor y visor personalizados; archivos originales de seguimiento AR conservados.")

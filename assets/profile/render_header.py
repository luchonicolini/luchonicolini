"""Render README artwork. Requires Pillow and DejaVu Sans fonts.

Run from any directory: python assets/profile/render_header.py
Only the interface illustration moves; the name and role stay readable.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = Path("/usr/share/fonts/truetype/dejavu")
W, H, SCALE = 1200, 420, 2


def font(size, bold=False, mono=False):
    name = "DejaVuSansMono.ttf" if mono else (
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    return ImageFont.truetype(str(FONTS / name), size * SCALE)


def render(theme, phase):
    dark = theme == "dark"
    bg = "#101815" if dark else "#f7f7f0"
    ink = "#f2f1e8" if dark else "#17271f"
    muted = "#a5b6ac" if dark else "#52685b"
    line = "#2c4035" if dark else "#d7e0d7"
    panel = "#17251e" if dark else "#edf1e8"
    accent = "#b9f0cb" if dark else "#176447"
    soft = "#355b44" if dark else "#bed5c0"
    image = Image.new("RGB", (W*SCALE, H*SCALE), bg)
    d = ImageDraw.Draw(image)

    def rect(box, fill=None, outline=None, radius=0, width=1):
        b = tuple(round(v*SCALE) for v in box)
        if radius:
            d.rounded_rectangle(b, radius=radius*SCALE, fill=fill,
                                outline=outline, width=width*SCALE)
        else:
            d.rectangle(b, fill=fill, outline=outline, width=width*SCALE)

    def ln(points, color=line, width=1):
        d.line([(round(x*SCALE), round(y*SCALE)) for x, y in points],
               fill=color, width=width*SCALE)

    def txt(x, y, text, size, color=ink, bold=False, mono=False):
        d.text((x*SCALE, y*SCALE), text, font=font(size,bold,mono), fill=color)

    def dot(x,y,r,color):
        d.ellipse(((x-r)*SCALE,(y-r)*SCALE,(x+r)*SCALE,(y+r)*SCALE),fill=color)

    txt(46,30,"LUCIANO NICOLINI",13,muted,mono=True)
    txt(972,30,"BUENOS AIRES",13,muted,mono=True)
    ln([(46,65),(1154,65)])
    txt(40,83,"Luciano",86,bold=True)
    txt(40,178,"Nicolini",86,bold=True)
    dot(416,256,6,accent)
    txt(46,300,"iOS Developer",23,accent,bold=True)
    txt(46,339,"Swift / SwiftUI",16,muted,mono=True)
    ln([(46,388),(1154,388)])
    txt(46,398,"MOBILE + FULL STACK",10,muted,mono=True)
    txt(949,398,"luchonicolini",10,muted,mono=True)

    # A browser and a phone: one visual system spanning mobile and web.
    offset = math.sin(phase*2*math.pi)*6
    x, y = 836, 115-offset
    rect((x,y,x+300,y+210),panel,line,12)
    ln([(x,y+32),(x+300,y+32)])
    for i in range(3):
        dot(x+18+i*14,y+16,3,soft)
    rect((x+18,y+52,x+71,y+185),bg,None,6)
    for k,ww in enumerate([32,26,30,22]):
        rect((x+28,y+69+k*25,x+28+ww,y+73+k*25),soft,None,2)
    rect((x+87,y+52,x+279,y+104),bg,None,6)
    txt(x+101,y+63,"{ web }",19,accent,mono=True)
    for k, ww in enumerate([173,133,155]):
        rect((x+88,y+121+k*22,x+88+ww,y+126+k*22),soft,None,2)
    # A small highlight moves along the shared component rails.
    t = (math.sin(phase*2*math.pi)+1)/2
    rect((x+88,y+185,x+88+90+t*70,y+188),accent,None,1)

    x, y = 734, 82+offset
    rect((x,y,x+174,y+279),bg,soft,25,2)
    rect((x+9,y+9,x+165,y+270),panel,None,18)
    rect((x+63,y+16,x+111,y+21),soft,None,3)
    txt(x+24,y+48,"{ app }",19,accent,mono=True)
    for k in range(3):
        yy = y+96+k*45
        rect((x+19,yy,x+155,yy+34),bg,None,7)
        dot(x+35,yy+17,5,accent if k==0 else soft)
        rect((x+50,yy+11,x+125,yy+14),soft,None,1)
        rect((x+50,yy+21,x+98,yy+23),line,None,1)
    rect((x+31,y+240,x+143,y+244),accent,None,2)
    # Dashed construction marks stay quiet behind the UI illustration.
    for xx,yy in [(687,105),(1134,355),(989,85)]:
        ln([(xx-5,yy),(xx+5,yy)],soft)
        ln([(xx,yy-5),(xx,yy+5)],soft)

    return image.resize((W,H),Image.Resampling.LANCZOS)


def main():
    for theme in ("dark","light"):
        frames = [render(theme, i/48) for i in range(48)]
        frames[0].save(ROOT/f"header-{theme}.png",optimize=True)
        palette = frames[0].quantize(colors=96,method=Image.Quantize.MEDIANCUT)
        indexed = [frame.quantize(palette=palette,dither=Image.Dither.NONE)
                   for frame in frames]
        indexed[0].save(ROOT/f"header-{theme}.gif",save_all=True,
                        append_images=indexed[1:],duration=100,loop=0,
                        optimize=True,disposal=1)
        print(theme, (ROOT/f"header-{theme}.gif").stat().st_size, "bytes")


if __name__ == "__main__":
    main()

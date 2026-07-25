from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
import re, html

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "documentation"
OUT = DOCS / "pdf"
OUT.mkdir(parents=True, exist_ok=True)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="DocTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=18, leading=22, spaceAfter=14))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=13, leading=16, spaceBefore=10, spaceAfter=6))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=13, spaceAfter=5))
styles.add(ParagraphStyle(name="Bulletx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=13, leftIndent=14, firstLineIndent=-8, bulletIndent=4, spaceAfter=3))
styles.add(ParagraphStyle(name="Metax", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.5, leading=11, textColor=colors.HexColor("#333333"), spaceAfter=3))

def inline(s):
    s=html.escape(s)
    s=re.sub(r"\*\*(.*?)\*\*",r"<b>\1</b>",s)
    s=re.sub(r"`(.*?)`",r"<font name='Courier'>\1</font>",s)
    s=re.sub(r"\[(.*?)\]\((.*?)\)",r"\1",s)
    return s

def parse(text):
    story=[]; lines=text.splitlines(); i=0
    while i<len(lines):
        line=lines[i].rstrip()
        if not line: story.append(Spacer(1,4))
        elif line.startswith("# "): story.append(Paragraph(inline(line[2:]),styles["DocTitle"]))
        elif line.startswith("## "): story.append(Paragraph(inline(line[3:]),styles["H1x"]))
        elif line.startswith("- [ ] "): story.append(Paragraph("☐ "+inline(line[6:]),styles["Bulletx"]))
        elif line.startswith("- "): story.append(Paragraph("• "+inline(line[2:]),styles["Bulletx"]))
        elif line.startswith("|"):
            block=[]
            while i<len(lines) and lines[i].startswith("|"): block.append(lines[i]); i+=1
            i-=1; rows=[]
            for n,b in enumerate(block):
                cells=[c.strip() for c in b.strip("|").split("|")]
                if n==1 and all(set(c)<=set("-: ") for c in cells): continue
                rows.append([Paragraph(inline(c),styles["Metax"]) for c in cells])
            if rows:
                w=[7.1*inch/len(rows[0])]*len(rows[0])
                t=Table(rows,colWidths=w,repeatRows=1)
                t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E8EEF5")),("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#AAB4C0")),("VALIGN",(0,0),(-1,-1),"TOP"),("PADDING",(0,0),(-1,-1),4)]))
                story += [t,Spacer(1,6)]
        elif line.startswith("**"): story.append(Paragraph(inline(line.replace("  ","")),styles["Metax"]))
        else: story.append(Paragraph(inline(line),styles["Bodyx"]))
        i+=1
    return story

def footer(canvas,doc):
    canvas.saveState(); canvas.setFont("Helvetica",7); canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawString(0.65*inch,0.42*inch,"ERIS Distributor Documentation Repository")
    canvas.drawRightString(7.85*inch,0.42*inch,f"Page {doc.page}"); canvas.restoreState()

for md in sorted(DOCS.glob("DOC-*.md")):
    out=OUT/(md.stem+".pdf")
    pdf=SimpleDocTemplate(str(out),pagesize=letter,rightMargin=.65*inch,leftMargin=.65*inch,topMargin=.6*inch,bottomMargin=.65*inch)
    pdf.build(parse(md.read_text(encoding="utf-8")),onFirstPage=footer,onLaterPages=footer)

print(f"Generated PDFs in {OUT}")

from docx.shared import Pt
from docx.oxml.ns import qn


def add_line_to_document(d, language, line_str, bold):
    p = d.add_paragraph()

    # 设置段落行间距，1.5倍行间距大致为22.5磅
    p.paragraph_format.line_spacing = Pt(22.5)

    # 添加文本内容
    run = p.add_run(line_str)

    # 设置字号，小四字号大致为12磅
    run.font.size = Pt(12)

    if language == "zh":  # 中文
        run.font.name = "宋体"
        r = run._r
        r.rPr.rFonts.set(qn("w:eastAsia"), "SimSun")
    elif language == "en":  # 英文
        run.font.name = "Times New Roman"
    else:
        raise Exception("Unexpected language in add_line_to_document")

    # 加粗
    run.bold = bold

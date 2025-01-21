from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from send_user_email import send_email
from docx.oxml.ns import qn


def add_line_to_document(d, language, line_str, bold):
    p = d.add_paragraph()

    # 设置段落行间距
    p.paragraph_format.line_spacing = Pt(22.5)  # 1.5 倍行间距大致为 22.5 磅

    # 添加文本内容
    run = p.add_run(line_str)
    run.font.size = Pt(12)  # 小四字号大致为 12 磅

    # 根据语言设置字体
    if language == "zh":
        run.font.name = "宋体"
        r = run._r
        r.rPr.rFonts.set(qn("w:eastAsia"), "SimSun")  # 指定中文字体
    elif language == "en":
        run.font.name = "Times New Roman"
    else:
        raise Exception("Unexpected language in add_line_to_document")

    # 根据 `bold` 参数来设置是否加粗
    run.bold = bold


# 创建一个新的 Document 对象
document = Document()

# 添加内容
add_line_to_document(document, "en", "Computer-Aided Civil and Infrastructure Engineering", True)
add_line_to_document(document, "en", "Most recent:", True)
add_line_to_document(document, "en",
                     "A structure-oriented loss function for automated semantic segmentation of bridge point clouds",
                     False)
add_line_to_document(document, "en", "https://doi.org/10.1111/mice.13422", False)
add_line_to_document(document, "zh", "【用于桥点云自动语义分割的面向结构的损失函数】", False)

# 保存文档
document.save("test.docx")

send_email("test.docx")

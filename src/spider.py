import os
from docx import Document
from get_data_ubuntu import Spider
from datetime import datetime
from send_user_email import send_email
import sys
from document_format import add_line_to_document


def trigger_spider_task(wiley_paper, sciencedirect_paper1, sciencedirect_paper2, sciencedirect_volume1,
                        sciencedirect_volume2):
    # 创建 Word 文档对象
    document = Document()
    handle_wiley_task(wiley_paper, document)
    handle_sciencedirect_task("automation-in-construction", sciencedirect_paper1, sciencedirect_volume1, document)
    handle_sciencedirect_task("journal-of-building-engineering", sciencedirect_paper2, sciencedirect_volume2, document)

    current_time = datetime.now()

    folder_path = '../data'
    # 保证文件夹存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # word文档名称为当前时间，精确到秒
    file_name = "../data/" + current_time.strftime('%Y-%m-%d %H:%M:%S') + ".docx"
    # 保存word文档
    document.save(file_name)
    # 发送邮件
    send_email(file_name)


def handle_wiley_task(latest_paper, document):
    add_line_to_document(document, "en", "Computer-Aided Civil and Infrastructure Engineering", True)
    add_line_to_document(document, "en", "Most recent:", True)

    search_end = False
    page_index = 0

    while not search_end:
        spider = Spider()
        search_end = spider.get_wiley_single_page(latest_paper, page_index, document)
        spider.close()
        page_index += 1


def handle_sciencedirect_task(journal, latest_paper, start_volume, document):
    global sciencedirect_dict
    global sciencedirect_name_dict

    sciencedirect_dict[journal] = 1

    add_line_to_document(document, "en", sciencedirect_name_dict[journal], True)
    add_line_to_document(document, "en", "Most recent:", True)

    search_end = False
    volume_index = int(start_volume)

    while not search_end:
        spider = Spider()
        search_end = spider.get_sciencedirect_single_volume(journal, volume_index, latest_paper, document)
        spider.close()
        volume_index -= 1


if __name__ == "__main__":
    wiley_paper = sys.argv[1]
    sciencedirect_paper1 = sys.argv[2]
    sciencedirect_paper2 = sys.argv[3]
    sciencedirect_volume1 = sys.argv[4]
    sciencedirect_volume2 = sys.argv[5]

    trigger_spider_task(wiley_paper, sciencedirect_paper1, sciencedirect_paper2, sciencedirect_volume1,
                        sciencedirect_volume2)

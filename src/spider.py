from docx import Document
from get_data_ubuntu import Spider
from datetime import datetime
from send_user_email import send_email
import sys


def trigger_spider_task(wiley_paper, sciencedirect_paper1, sciencedirect_paper2, sciencedirect_volume1,
                        sciencedirect_volume2):
    # 创建 Word 文档对象
    document = Document()
    handle_wiley_task(wiley_paper, document)
    handle_sciencedirect_task("automation-in-construction", sciencedirect_paper1, sciencedirect_volume1, document)
    handle_sciencedirect_task("journal-of-building-engineering", sciencedirect_paper2, sciencedirect_volume2, document)

    # 获取当前时间
    current_time = datetime.now()

    # 格式化为精确到秒的字符串
    file_name = "../data/" + current_time.strftime('%Y-%m-%d %H:%M:%S') + ".docx"
    # 保存文档到文件
    document.save(file_name)

    send_email(file_name)


def handle_wiley_task(latest_paper, document):
    search_end = False
    page_index = 0

    while not search_end:
        spider = Spider()
        search_end = spider.get_wiley_single_page(latest_paper, page_index, document)
        spider.close()
        page_index += 1


def handle_sciencedirect_task(journal, latest_paper, start_volume, document):
    search_end = False
    volume_index = int(start_volume)

    while not search_end:
        spider = Spider()
        search_end = spider.get_sciencedirect_single_volume(journal, volume_index, latest_paper, document)
        spider.close()
        volume_index -= 1


if __name__ == "__main__":


    # 检查传递给脚本的参数是否正确
    if len(sys.argv) != 6:
        print(
            "Usage: python spider.py <wiley_paper> <sciencedirect_paper1> <sciencedirect_paper2> <sciencedirect_volume1> <sciencedirect_volume2>")
        sys.exit(1)

    # 获取命令行参数
    wiley_paper = sys.argv[1]
    sciencedirect_paper1 = sys.argv[2]
    sciencedirect_paper2 = sys.argv[3]
    sciencedirect_volume1 = sys.argv[4]
    sciencedirect_volume2 = sys.argv[5]

    # 打印接收到的参数
    print("Received parameters:")
    print("wiley_paper:", wiley_paper)
    print("sciencedirect_paper1:", sciencedirect_paper1)
    print("sciencedirect_paper2:", sciencedirect_paper2)
    print("sciencedirect_volume1:", sciencedirect_volume1)
    print("sciencedirect_volume2:", sciencedirect_volume2)

    trigger_spider_task(wiley_paper, sciencedirect_paper1, sciencedirect_paper2, sciencedirect_volume1,
                        sciencedirect_volume2)

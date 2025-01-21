from flask import Flask, request, send_from_directory
import subprocess

app = Flask(__name__)

# 假设 docx 文件存储在 "output" 目录
OUTPUT_DIR = "/path/to/output/directory"


@app.route('/spider', methods=['GET'])
def start_spider():
    # 获取请求参数
    wiley_paper = request.args.get('wiley_paper')
    sciencedirect_paper1 = request.args.get('sciencedirect_paper1')
    sciencedirect_paper2 = request.args.get('sciencedirect_paper2')
    sciencedirect_volume1 = request.args.get('sciencedirect_volume1')
    sciencedirect_volume2 = request.args.get('sciencedirect_volume2')

    # 打印所有获取到的参数
    print("wiley_paper:", wiley_paper)
    print("sciencedirect_paper1:", sciencedirect_paper1)
    print("sciencedirect_paper2:", sciencedirect_paper2)
    print("sciencedirect_volume1:", sciencedirect_volume1)
    print("sciencedirect_volume2:", sciencedirect_volume2)

    # 这里可以根据获取的参数做进一步的操作，假设进行爬虫的启动
    if not wiley_paper or not sciencedirect_paper1 or not sciencedirect_paper2 or not sciencedirect_volume1 or not sciencedirect_volume2:
        return "All parameters are required!", 400

    # 触发爬虫程序（假设爬虫程序在 Docker 容器内的路径是 /app/spider.py）
    try:
        # 在 Docker 中运行爬虫程序并传递参数
        subprocess.run(
            ["python", "spider.py", wiley_paper, sciencedirect_paper1, sciencedirect_paper2, sciencedirect_volume1,
             sciencedirect_volume2], check=True)
        return "Spider started successfully!", 200
    except Exception as e:
        return f"Error starting spider: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 启动 Web 服务

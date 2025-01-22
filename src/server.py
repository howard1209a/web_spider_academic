from flask import Flask, request, send_from_directory
import subprocess

app = Flask(__name__)


@app.route('/spider', methods=['GET'])
def start_spider():
    # 获取请求参数
    wiley_paper = request.args.get('wiley_paper')
    sciencedirect_paper1 = request.args.get('sciencedirect_paper1')
    sciencedirect_paper2 = request.args.get('sciencedirect_paper2')
    sciencedirect_volume1 = request.args.get('sciencedirect_volume1')
    sciencedirect_volume2 = request.args.get('sciencedirect_volume2')

    if not wiley_paper or not sciencedirect_paper1 or not sciencedirect_paper2 or not sciencedirect_volume1 or not sciencedirect_volume2:
        return "All parameters are required!", 400

    try:
        # 启动子进程，执行spider.py
        subprocess.run(
            ["python", "src/spider.py", wiley_paper, sciencedirect_paper1, sciencedirect_paper2, sciencedirect_volume1,
             sciencedirect_volume2], check=True)
        return "Spider started successfully!", 200
    except Exception as e:
        return f"Error starting spider: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

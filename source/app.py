from flask import Flask

# Flask 애플리케이션을 생성합니다.
app = Flask(__name__)

# '/' 경로로 들어오는 요청을 처리합니다.
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # 개발 서버를 실행합니다.
    app.run()

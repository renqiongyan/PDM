# 入口函数启动文件

from application import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run()
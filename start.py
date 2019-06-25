# 启动文件12345678


from application import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run()


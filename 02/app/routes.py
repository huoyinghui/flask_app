# -*- coding:utf-8 -*-
from app import app


@app.route('/')
@app.route('/index')
def index():
    app.logger.debug('this is debug message')
    app.logger.error('this is error message')
    app.logger.critical('this is critical message')
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from config import DevelopementConfig, ProductionConfig
from info import db, create_app

app = create_app(DevelopementConfig)
# 启动项目app
manager = Manager(app)
# 迁移数据库
Migrate(app, db)
manager.add_command('db', MigrateCommand)





@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()

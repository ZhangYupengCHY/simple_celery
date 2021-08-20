简单实现celery:异步和定时任务

[window]

1.首先进入目录启动celery任务模块

$ celery -A  celery_app worker -l info -P eventlet

2.启动定时任务

$ celery beat -A celery_app

3.启动任务

run test_celery.py

4.观察Worker 窗口,观察异步和定时任务正在执行,同时观察redis数据库中有任务和定时结果生成。

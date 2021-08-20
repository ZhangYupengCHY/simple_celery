from celery_app import task1,task2


# 异步任务
task1.add.apply_async(args=[20, 80]) # 也可以使用delay(2,8)2,8是位置参数，传给add函数
task2.multiply.apply_async(args=[40, 80]) # 也可以使用delay(3,8)

print('hello world')
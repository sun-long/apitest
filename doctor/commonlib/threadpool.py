import concurrent.futures

def task_function(param):
    # 执行任务逻辑，这里用一个简单的示例
    return param * 2

pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)

# 提交任务
future = pool.submit(task_function, 10)

# 获取任务结果
result = future.result()
print("Result:", result)

# 关闭线程池
pool.shutdown()

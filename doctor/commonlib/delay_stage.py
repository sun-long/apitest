import requests
import time

url = "https://api.stage.sensenova.cn/v1/llm/chat-completions"

payload = {
    "stream": True,
    "model": "nova-ptc-xl-v1",
    "messages": [
        {
            "role": "user",
            "content": "大脚趾淤血怎么办"
        }
    ],
    "know_ids": [],
    "max_new_tokens": 2048,
    "repetition_penalty": 1.05,
    "user": "test",
    "temperature": 0.8
}
headers = {
    # "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyUzZrN1JQaThlNWdvWndOQkN1M3N1MlVlWW0iLCJleHAiOjE2OTMxNDE3Mzl9.GZZt_2YVkIDR7X-bqXS5fMOlE6SiRaTP3NLxkonqppg",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyUzZrSzRWQklVRXJ6UlRsVFZ5SWJnMTUxOU4iLCJleHAiOjE2OTMxNDIxMzB9.nlVCiCycE3faYKJ9YUu1qHuBckCgCux4rGupCKIZEYI",
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "Accept": "text/event-stream",
    "Connection": "keep-alive",
}

for i in range(1, 101):
    start = time.time()
    with requests.post(url, json=payload, headers=headers, stream=True) as resp:

        # print(time.time()-start)
        for line in resp.iter_content(chunk_size=None):
            print(time.time() - start)
            # print(line)
            break


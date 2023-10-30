import requests
import time

url = "https://api.sensenova.cn/v1/llm/chat-completions"

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
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyUm9hbFo3NDRpdjNQZzZpS1Z0dnBSaWMxWkoiLCJleHAiOjE2OTMxNDAwOTV9.aZmUIlT9YNOmMX2TTdv8vtjfTNgQjuZ3ipsPgEhJqvA",
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


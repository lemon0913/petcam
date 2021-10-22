import requests as req
import os
url= 'http://localhost:8000/api/video/'
file_name = 'PETCAM 2021-10-21 19_26_45.mp4'
file_path = os.path.join('', file_name)

data = {
    'username': 'park',
    'size': os.path.getsize(file_name),
    'filename': file_name,
    'content_type': 'video/mp4'
}
res = req.post(url, data=data, files={'video_file': open(file_path, 'br')})
if res.status_code == 200:
    print(res.json())
else:
    print(res.text)
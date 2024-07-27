import os
import tempfile
from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, APIRouter, Body, File
import uvicorn
from starlette.responses import FileResponse
import requests
from typing import List
import subprocess

app = FastAPI()
router = APIRouter()


@app.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)):
	"""
	上传本地文件
	curl --location --request POST 'http://127.0.0.1:7861/upload' \
	--header 'multipart/form-data; boundary=<在发送请求时计算>' \
	--form 'files=@"C:\\Users\\Administrator\\Desktop\\0df431adcbef7609ca41e7b6292b02cb7dd99e4a.jpg"'

	:return: ["C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\tmpgc6loewr\\0df431adcbef7609ca41e7b6292b02cb7dd99e4a.jpg"]
	"""
	uploaded_files = []
	for file in files:
		tmp_file_path = os.path.join(tempfile.mkdtemp(), file.filename)
		with open(tmp_file_path, 'wb') as tmp_file:
			shutil.copyfileobj(file.file, tmp_file)
		print(f"upload file success save to {tmp_file_path}")
		uploaded_files.append(tmp_file_path)
	return uploaded_files


@router.post("/load")
def update(file_urls: List[str]):
	"""
	请求示例
	curl --location --request POST '127.0.0.1:7861/load' \
	--header 'Content-Type: application/json' \
	--data-raw '["https://i1.hdslb.com/bfs/archive/9435dad4ccefc1672afdb723799d1a1810df37d5.jpg",
	"https://i1.hdslb.com/bfs/archive/9435dad4ccefc1672afdb723799d1a1810df37d5.jpg"]'

	:param file_urls:  ["https://i1.hdslb.com/bfs/archive/9435dad4ccefc1672afdb723799d1a1810df37d5.jpg"]
	:return: ["C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\tmp2ecn7i18\\9435dad4ccefc1672afdb723799d1a1810df37d5.jpg"]
	"""
	local_files = []
	for file_url in file_urls:
		with requests.get(file_url, stream=True) as r:
			r.raise_for_status()
			file_path = os.path.join(tempfile.mkdtemp(), Path(file_url).name)
			with open(file_path, 'wb') as f:
				for chunk in r.iter_content(chunk_size=8192):
					f.write(chunk)
			print(f"load network file success save to {file_path}")
			local_files.append(file_path)
	return local_files


@router.post("/process")
async def process_frames(params=Body(...)) -> FileResponse:
	"""
curl --location --request POST '127.0.0.1:7861/process' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sources": [
        "C:\\Users\\Administrator\\Desktop\\0df431adcbef7609ca41e7b6292b02cb7dd99e4a.jpg",
        "C:\\Users\\Administrator\\Desktop\\005JErWoly4gkzi4c7oq9j30lx0dmdnd.png"
    ],
    "target": "C:\\Users\\Administrator\\Desktop\\target.jpg"
}'


	:param params:
	:return:
	"""
	sources = params['sources']
	target = params['target']
	file_path = Path(target)

	output_file_name = os.path.basename(f'output{file_path.suffix}')
	output_file_path = os.path.join(tempfile.mkdtemp(), output_file_name)
	command = [
		'python', 'run.py',
		'--headless',
		'--execution-providers', 'cpu','cuda',
		'-t', target,
		'-o', output_file_path
	]
	# command = [
	# 	'E:\\miniconda3\\envs\\facefusion3\\python', 'run.py',
	# 	'--headless',
	# 	'--execution-providers', 'cpu','cuda',
	# 	'-t', target,
	# 	'-o', output_file_path
	# ]

	for source in sources:
		command.append('-s')
		command.append(source)
	print("command: ", command)
	try:
		result = subprocess.run(command, check=True)
		print(f"命令执行成功，返回码：{result.returncode}")
	except subprocess.CalledProcessError as e:
		print(f"命令执行失败，返回码：{e.returncode}")
	return FileResponse(output_file_path,  filename=output_file_name)


def launch():
	app.include_router(router)
	uvicorn.run(app, host="0.0.0.0", port=7861)


if __name__ == '__main__':
	launch()

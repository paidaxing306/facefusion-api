import os
import tempfile
import base64
from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, APIRouter, Body
import uvicorn
from starlette.responses import FileResponse
import requests
from typing import List

app = FastAPI()
router = APIRouter()


@router.post("/upload")
def update(files: List[UploadFile]):
	file_paths = []
	for file in files:
		tmp_file_path = os.path.join(tempfile.mkdtemp(), file.filename)
		print(tmp_file_path)
		with open(tmp_file_path, 'wb') as tmp_file:
			shutil.copyfileobj(file.file, tmp_file)
		file_paths.append(tmp_file_path)
	return file_paths


@router.post("/load")
def update(file_urls: List[str]):
	local_files = []
	for file_url in file_urls:
		with requests.get(file_url, stream=True) as r:
			r.raise_for_status()
			file_path = os.path.join(tempfile.mkdtemp(), Path(file_url).name)
			with open(file_path, 'wb') as f:
				for chunk in r.iter_content(chunk_size=8192):
					f.write(chunk)
			local_files.append(file_path)
	return local_files


@router.post("/process")
def process_frames(params=Body(...)) -> FileResponse:
	target = params['target']
	file_path = Path(target)
	globals.source_paths = params['sources']
	response_file_name = os.path.basename(f'output{file_path.suffix}')
	return FileResponse(globals.output_path, media_type="application/octet-stream", filename=response_file_name)


def launch():
	app.include_router(router)
	uvicorn.run(app, host="0.0.0.0", port=7861)


if __name__ == '__main__':
    launch()

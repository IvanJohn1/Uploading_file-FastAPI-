from fastapi import FastAPI, UploadFile, File
from secrets import token_hex
import uvicorn

app = FastAPI(title='Uploading files with FastAPI')


@app.post('/upload')
async def upload(file: UploadFile = File(...)):
    file_ext = file.filename.split('.').pop()
    file_start = token_hex(10)
    file_path = f'{file_ext}.{file_start}'
    with open(file_path, 'wb') as f:
        content = await file.read()
        f.write(content)
        return {'success': True, 'file_path': file_path, 'message': 'Uploaded successful'}

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

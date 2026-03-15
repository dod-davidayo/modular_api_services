# File Storage Services

from fastapi import APIRouter, UploadFile, File
from app.services.file_services import save_file

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """UPLOAD FILE ENDPOINT"""
    
    result  = await save_file(file)

    return result 
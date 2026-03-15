
from fastapi import APIRouter,  HTTPException
import os
from fastapi import UploadFile
import shutil
import uuid

UPLOAD_DIR = "app/storage/uploads"

# Ensure directory exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter(prefix="/media", tags=["media"])

async def save_file(file: UploadFile):
    """
    Save Uploaded file to disk
    """

    file_id = str(uuid.uuid4())

    file_path = f"{UPLOAD_DIR}/{file_id}_{file.filename}"

    # Stream file to disk(efficient for large files)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_id": file_id, "filename": file.filename}


@router.get("/files")
def list_files():
    files = os.listdir(UPLOAD_DIR)
    return {"files":files}

@router.get("/files/{filename}")
def get_file(filename: str):
    path = f"{UPLOAD_DIR}/{filename}"
    return {"path": path}

@router.delete("/files/{filename}")
def delete_file(filename: str):
    # Step 1: build the file path
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Step 2: check if the file exists
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # Step 3: delete the file
    os.remove(file_path)

    return {"message": f"{filename} deleted successfully"}
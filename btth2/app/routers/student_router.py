from fastapi import APIRouter, Depends
from app.services.student_service import get_all, get_by_id, create_student_service, update_student_service, delete_student_service
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas import StudentCreate, StudentUpdate

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("")
def get_students(db: Session = Depends(get_db)):
    students = get_all(db)
    return {"message": "Lấy toàn bộ danh sách học sinh thành công", "data": students}


@router.get("/{student_id}")
def get_student(student_id: int, db: Session=Depends(get_db)):
    student = get_by_id(student_id, db)
    return {"message": "Lất thông tin sinh viên thành công", "data": student}


@router.post("")
def create_student(student: StudentCreate, db: Session=Depends(get_db)):
    new_student = create_student_service(student, db)
    return {"message": "Thêm mới sv thành công", "data": new_student}


@router.put("/{student_id}")
def update_student(student_id: int, update_student: StudentUpdate, db: Session=Depends(get_db)):
    student = update_student_service(student_id, update_student, db)
    return {"message": "Cập nhật thành công", "data": student}


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session=Depends(get_db)):
    deleted_student = delete_student_service(student_id, db)
    return {"message": "Xóa thành công", "data": deleted_student}
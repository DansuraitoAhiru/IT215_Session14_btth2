from app.models.models import StudentModel
from app.schemas.schemas import StudentCreate, StudentUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def get_all(db: Session):
    return db.query(StudentModel).all()


def get_by_id(id: int, db: Session):
    student = db.query(StudentModel).filter(StudentModel.id == id).first()
    if not student:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Không tìm thấy sinh viên")
    return student


def create_student_service(student: StudentCreate, db: Session):
    try: 
        new_student = StudentModel(**student.model_dump())
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))


def update_student_service(id: int, update_student: StudentUpdate, db: Session):
    try:
        student = get_by_id(id, db)
        for key, value in update_student.model_dump().items():
            setattr(student, key, value)
        db.commit()
        db.refresh(student)
        return student
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
    

def delete_student_service(id: int, db: Session):
    try:
        student = get_by_id(id, db)
        deleted_student = student
        db.delete(student)
        db.commit()
        return deleted_student
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
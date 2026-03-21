from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date
from typing import List, Optional
import enum
import re
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hrms.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enum for attendance status
class AttendanceStatus(str, enum.Enum):
    PRESENT = "Present"
    ABSENT = "Absent"

# SQLAlchemy Models
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=False)

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, nullable=False, index=True)
    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatus), nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Models
class EmployeeCreate(BaseModel):
    employee_id: str = Field(..., min_length=1, max_length=50)
    full_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    department: str = Field(..., min_length=1, max_length=100)

    @field_validator('employee_id')
    @classmethod
    def validate_employee_id(cls, v):
        if not v or not v.strip():
            raise ValueError('Employee ID cannot be empty or whitespace only')
        if len(v.strip()) < 1 or len(v.strip()) > 50:
            raise ValueError('Employee ID must be between 1-50 characters')
        if not re.match(r'^[a-zA-Z0-9_-]+$', v.strip()):
            raise ValueError('Employee ID can only contain letters, numbers, hyphens, and underscores')
        return v.strip()

    @field_validator('full_name')
    @classmethod
    def validate_full_name(cls, v):
        if not v or not v.strip():
            raise ValueError('Full Name cannot be empty')
        if len(v.strip()) < 2:
            raise ValueError('Full Name must be at least 2 characters long')
        if not re.match(r'^[a-zA-Z\s\'-]+$', v.strip()):
            raise ValueError('Full Name can only contain letters, spaces, hyphens, and apostrophes')
        return v.strip()

    @field_validator('department')
    @classmethod
    def validate_department(cls, v):
        if not v or not v.strip():
            raise ValueError('Department cannot be empty')
        if not re.match(r'^[a-zA-Z\s&-]+$', v.strip()):
            raise ValueError('Department contains invalid characters. Use letters, spaces, hyphens, or ampersands')
        return v.strip()

class EmployeeUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    department: Optional[str] = Field(None, min_length=1, max_length=100)

    @field_validator('full_name')
    @classmethod
    def validate_full_name(cls, v):
        if v is not None:
            if not v or not v.strip():
                raise ValueError('Full Name cannot be empty')
            if len(v.strip()) < 2:
                raise ValueError('Full Name must be at least 2 characters long')
            if not re.match(r'^[a-zA-Z\s\'-]+$', v.strip()):
                raise ValueError('Full Name can only contain letters, spaces, hyphens, and apostrophes')
            return v.strip()
        return v

class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    full_name: str
    email: str
    department: str

    class Config:
        from_attributes = True

class AttendanceCreate(BaseModel):
    employee_id: str = Field(..., min_length=1, max_length=50)
    date: date
    status: AttendanceStatus

    @field_validator('employee_id')
    @classmethod
    def validate_employee_id(cls, v):
        if not v or not v.strip():
            raise ValueError('Employee ID cannot be empty')
        return v.strip()

class AttendanceResponse(BaseModel):
    id: int
    employee_id: str
    date: date
    status: AttendanceStatus

    class Config:
        from_attributes = True

# FastAPI app
app = FastAPI(title="HRMS Lite API", version="1.0.0")

# Configure CORS
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
allow_origins = [
    FRONTEND_URL,
    "http://localhost:3000",
    "http://localhost:5173",  # Vite dev server
    "https://hrm1-seven.vercel.app",  # Old Vercel frontend
    "https://hrm20.vercel.app",  # New Vercel frontend (production)
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Employee Routes
@app.post("/api/employees", response_model=EmployeeResponse, status_code=201)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new employee with comprehensive validation"""
    try:
        # Normalize the input
        emp_id_normalized = employee.employee_id.strip()
        email_normalized = employee.email.lower().strip()
        
        # Check if employee_id already exists
        existing_emp_id = db.query(Employee).filter(
            Employee.employee_id == emp_id_normalized
        ).first()
        if existing_emp_id:
            raise HTTPException(
                status_code=400, 
                detail=f"❌ Employee ID '{emp_id_normalized}' already exists in the system. Please use a unique Employee ID."
            )
        
        # Check if email already exists
        existing_email = db.query(Employee).filter(
            Employee.email == email_normalized
        ).first()
        if existing_email:
            raise HTTPException(
                status_code=400, 
                detail=f"❌ Email '{email_normalized}' is already registered. Each employee must have a unique email address."
            )
        
        # Create employee with normalized data
        db_employee = Employee(
            employee_id=emp_id_normalized,
            full_name=employee.full_name.strip(),
            email=email_normalized,
            department=employee.department.strip()
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except HTTPException:
        db.rollback()
        raise
    except ValueError as ve:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"❌ Validation Error: {str(ve)}")
    except Exception as err:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"❌ Failed to create employee: {str(err)}")

@app.get("/api/employees", response_model=List[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    """Get all employees"""
    employees = db.query(Employee).all()
    return employees

@app.get("/api/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """Get a specific employee by ID"""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.delete("/api/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """Delete an employee"""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Delete all attendance records for this employee
    db.query(Attendance).filter(Attendance.employee_id == employee.employee_id).delete()
    
    db.delete(employee)
    db.commit()
    return None

# Attendance Routes
@app.post("/api/attendance", response_model=AttendanceResponse, status_code=201)
def mark_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    """Mark attendance for an employee"""
    try:
        emp_id_normalized = attendance.employee_id.strip()
        
        # Check if employee exists
        employee = db.query(Employee).filter(
            Employee.employee_id == emp_id_normalized
        ).first()
        if not employee:
            raise HTTPException(
                status_code=404, 
                detail=f"❌ Employee with ID '{emp_id_normalized}' not found. Please verify the Employee ID is correct."
            )
        
        # Check if attendance already marked for this date
        existing = db.query(Attendance).filter(
            Attendance.employee_id == emp_id_normalized,
            Attendance.date == attendance.date
        ).first()
        
        if existing:
            # Update existing attendance
            existing.status = attendance.status
            db.commit()
            db.refresh(existing)
            return existing
        
        # Create new attendance record
        db_attendance = Attendance(
            employee_id=emp_id_normalized,
            date=attendance.date,
            status=attendance.status
        )
        db.add(db_attendance)
        db.commit()
        db.refresh(db_attendance)
        return db_attendance
    except HTTPException:
        db.rollback()
        raise
    except Exception as err:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"❌ Failed to mark attendance: {str(err)}"
        )

@app.get("/api/attendance", response_model=List[AttendanceResponse])
def get_attendance(employee_id: Optional[str] = None, db: Session = Depends(get_db)):
    """Get attendance records, optionally filtered by employee_id"""
    query = db.query(Attendance)
    if employee_id:
        query = query.filter(Attendance.employee_id == employee_id)
    return query.all()

@app.get("/api/attendance/{attendance_id}", response_model=AttendanceResponse)
def get_attendance_record(attendance_id: int, db: Session = Depends(get_db)):
    """Get a specific attendance record"""
    attendance = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance

@app.get("/api/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

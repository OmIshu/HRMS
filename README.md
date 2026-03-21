# HRMS Lite - Human Resource Management System

A lightweight, full-stack Human Resource Management System built with React, FastAPI, and SQLite. This application allows administrators to manage employee records and track daily attendance with a clean, professional interface.

## 🎯 Overview

HRMS Lite is a production-ready web application designed for small to medium-sized organizations to manage:
- **Employee Management**: Add, view, and delete employee records
- **Attendance Tracking**: Mark and monitor daily attendance with present/absent status
- **Dashboard & Analytics**: View summary statistics for attendance

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Validation**: Pydantic for request/response validation
- **Server**: Uvicorn ASGI server

### Frontend
- **UI Framework**: React 18
- **HTTP Client**: Axios
- **Styling**: CSS3 with modern-responsive design
- **Build Tool**: Create React App

## ✨ Features

### Core Features
- ✅ Employee Management
  - Add new employees with unique ID, name, email, and department
  - View complete list of all employees
  - Delete employee records with cascading attendance deletion
  - Email validation and duplicate prevention

- ✅ Attendance Management
  - Mark attendance for employees (Present/Absent)
  - View all attendance records
  - Filter attendance by date
  - Update attendance status
  - Automatic duplicate prevention (one entry per employee per date)

### Bonus Features
- ✅ Dashboard Statistics
  - Total present/absent days per employee
  - Summary view for quick insights

### UI/UX Features
- ✅ Professional, responsive design
- ✅ Loading states with animations
- ✅ Empty states with helpful messages
- ✅ Error handling with meaningful messages
- ✅ Form validation with field-level feedback
- ✅ Mobile-responsive layout
- ✅ Intuitive navigation

## 📋 Project Structure

```
HRMS/
├── backend/                          # FastAPI Backend
│   ├── main.py                      # Main application & API routes
│   ├── requirements.txt             # Python dependencies
│   └── .env                         # Environment configuration
│
├── frontend/                         # React Frontend
│   ├── public/
│   │   └── index.html              # HTML entry point
│   ├── src/
│   │   ├── components/
│   │   │   ├── EmployeeManagement.js    # Employee management component
│   │   │   ├── EmployeeManagement.css   # Employee styles
│   │   │   ├── AttendanceManagement.js  # Attendance component
│   │   │   └── AttendanceManagement.css # Attendance styles
│   │   ├── api.js                      # API service & handlers
│   │   ├── App.js                      # Main app component
│   │   ├── App.css                     # App styles
│   │   ├── index.js                    # React entry point
│   │   └── index.css                   # Global styles
│   ├── package.json                # Node dependencies
│   ├── .env                        # Environment configuration
│   └── .gitignore                  # Git ignore patterns
│
└── README.md                       # This file
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** with pip
- **Node.js 14+** with npm
- Git

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**:
   ```bash
   python main.py
   ```
   The backend will be available at `http://localhost:8000`
   API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory** (in a new terminal):
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure API URL** (optional):
   - Edit `.env` file and update `REACT_APP_API_URL` if needed
   - Default: `http://localhost:8000/api`

4. **Run the application**:
   ```bash
   npm start
   ```
   The application will open at `http://localhost:3000`

## 📚 API Documentation

The backend provides a complete RESTful API with auto-generated Swagger documentation available at `http://localhost:8000/docs` when the server is running.

### Employee Endpoints
- `POST /api/employees` - Create new employee
- `GET /api/employees` - List all employees
- `GET /api/employees/{id}` - Get employee details
- `DELETE /api/employees/{id}` - Delete employee

### Attendance Endpoints
- `POST /api/attendance` - Mark attendance
- `GET /api/attendance` - List all attendance records
- `GET /api/attendance?employee_id={id}` - Filter by employee
- `GET /api/attendance/{id}` - Get specific record

### Health Check
- `GET /api/health` - Server health status

## 🗄️ Database Schema

### Employees Table
```sql
CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  employee_id VARCHAR UNIQUE NOT NULL,
  full_name VARCHAR NOT NULL,
  email VARCHAR UNIQUE NOT NULL,
  department VARCHAR NOT NULL
);
```

### Attendance Table
```sql
CREATE TABLE attendance (
  id INTEGER PRIMARY KEY,
  employee_id VARCHAR NOT NULL,
  date DATE NOT NULL,
  status ENUM(Present, Absent) NOT NULL
);
```

## 🔒 Validation & Error Handling

### Input Validation
- **Employee ID**: Unique, required field
- **Email**: Valid email format, unique
- **Full Name**: Required, non-empty
- **Department**: Required, non-empty
- **Attendance Date**: Cannot be future date
- **Status**: Only "Present" or "Absent" allowed

### Error Responses
- `400 Bad Request`: Invalid input or duplicate employee
- `404 Not Found`: Resource doesn't exist
- `500 Internal Server Error`: Server-side error

## 📝 Assumptions & Limitations

### Assumptions
- Single admin user (no authentication/authorization)
- SQLite database (suitable for development/small deployments)
- Same employee can only have one attendance entry per day
- All email addresses are unique across employees

### Limitations
- No user authentication system
- No advanced permission levels
- Leave management not included
- Payroll system not included
- No reporting/export features
- Single-database instance (no replication)
- SQLite not suitable for high-traffic production (use PostgreSQL instead)

### Future Enhancements
- User authentication and role-based access control
- Advanced reporting and export (PDF, Excel)
- Leave management system
- Email notifications
- Payroll integration
- Mobile application
- Real-time notifications
- Multi-language support

## 🧪 Testing

### Manual Testing Workflow

1. **Employee Management**:
   - Add employee with valid data → Success ✓
   - Try duplicate Employee ID → Error message ✓
   - Try invalid email → Validation error ✓
   - View all employees → List displayed ✓
   - Delete employee → Attendance records cascade delete ✓

2. **Attendance Management**:
   - Mark present for valid employee → Success ✓
   - Update status for same employee/date → Override previous ✓
   - Filter by date → Results filtered ✓
   - View statistics → Calculation correct ✓

## 🐛 Troubleshooting

### "Connection refused" error
- Ensure backend is running: `python main.py`
- Check if port 8000 is available
- Verify firewall settings

### CORS errors
- Backend CORS is enabled for all origins
- Check browser console for specific errors
- Ensure API URL in frontend .env matches backend URL

### Database locked error
- Close other instances accessing the database
- Delete `backend/hrms.db` to reset (WARNING: data loss)
- Consider moving to PostgreSQL for production

### Module not found errors
- Reinstall dependencies: `pip install -r requirements.txt`
- Ensure virtual environment is activated
- Check Python version compatibility

## 🌐 Deployment

### Quick Deployment to Vercel & Render

For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md).

**Backend (Render)**:
- Python 3.11+ runtime
- FastAPI application
- SQLite database (or PostgreSQL for production)
- Free tier available

**Frontend (Vercel)**:
- React application
- Automatic deployments from GitHub
- Environment variables configuration
- Free tier available

**Quick Steps**:
1. Push code to GitHub
2. Connect repository to Render for backend
3. Connect repository to Vercel for frontend
4. Set environment variables on both platforms
5. Deploy and monitor

## 📞 Support

For issues and feature requests, please:
1. Check existing documentation
2. Review the troubleshooting section
3. Check browser console for error details
4. Create an issue in the repository

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💼 Author

Created as a Full-Stack HRMS Lite implementation demonstrating professional development practices, clean code, and production-ready features.

---

**Last Updated**: March 14, 2026

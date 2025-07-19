# Imaro Backend - Developer Setup Guide

> Complete setup guide for developers wanting to collaborate on the Imaro Phase 1 backend project

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.11+** ([Download here](https://www.python.org/downloads/))
- **PostgreSQL 15+** ([Download here](https://www.postgresql.org/download/))
- **Git** ([Download here](https://git-scm.com/downloads))
- **Code Editor** (VS Code, PyCharm, etc.)

## 🚀 Quick Setup (5 minutes)

### 1. Clone and Navigate
```bash
# If you don't have the project yet
git clone <repository-url>
cd Imaro/backend

# If you already have it
cd /path/to/Imaro/backend
```

### 2. Python Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup
```bash
# Start PostgreSQL (if not running)
# On macOS with Homebrew:
brew services start postgresql@14
# On Ubuntu/Linux:
sudo systemctl start postgresql
# On Windows: Start PostgreSQL service

# Create database and user
psql -U postgres -c "CREATE DATABASE imarodb;"
psql -U postgres -c "CREATE USER imaro_user WITH PASSWORD 'imaro_pass';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE imarodb TO imaro_user;"
psql -U postgres -d imarodb -c "GRANT ALL ON SCHEMA public TO imaro_user;"
```

### 4. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your settings (see configuration section below)
```

### 5. Database Migration
```bash
# Run database migrations
alembic upgrade head
```

### 6. Start Development Server
```bash
# Make sure you're in the backend directory and venv is activated
cd backend  # if not already there
source venv/bin/activate  # if not already activated
python -m uvicorn app.main:app --reload --port 8000
```

### 7. Verify Setup
```bash
# Test API health
curl http://localhost:8000/api/v1/health/

# Open Swagger documentation
open http://localhost:8000/docs
```

---

## 📁 Project Structure

```
Imaro/
├── backend/                     # Backend API (FastAPI)
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py      # Authentication endpoints
│   │   │   │   ├── users.py     # User management
│   │   │   │   └── health.py    # Health checks
│   │   │   └── router.py        # Main API router
│   │   ├── core/
│   │   │   ├── config.py        # App configuration
│   │   │   ├── database.py      # Database connection
│   │   │   └── security.py      # JWT & security
│   │   ├── models/
│   │   │   ├── base.py          # SQLAlchemy base
│   │   │   └── user.py          # User model
│   │   ├── schemas/
│   │   │   ├── auth.py          # Auth Pydantic models
│   │   │   └── user.py          # User Pydantic models
│   │   ├── services/
│   │   │   ├── auth_service.py  # Auth business logic
│   │   │   ├── firebase_service.py # Firebase integration
│   │   │   └── user_service.py  # User management logic
│   │   ├── utils/
│   │   │   ├── constants.py     # App constants
│   │   │   └── validators.py    # Validation helpers
│   │   ├── dependencies.py      # FastAPI dependencies
│   │   └── main.py              # FastAPI app entry point
│   ├── alembic/                 # Database migrations
│   ├── tests/                   # Test files
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example             # Environment template
│   ├── .env                     # Your local environment (not in git)
│   ├── alembic.ini             # Alembic configuration
│   └── README.md               # Main documentation
└── Documentations/
    └── phase1_backend_auth.md   # Detailed Phase 1 specs
```

---

## ⚙️ Configuration

### Environment Variables (.env)

Create `.env` file in the backend directory:

```bash
# Database Configuration
DATABASE_URL=postgresql://imaro_user:imaro_pass@localhost:5432/imarodb

# Twilio Configuration (SMS/OTP)
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_MESSAGING_SERVICE_SID=your-messaging-service-sid

# Firebase Configuration (Google OAuth & Push Notifications)
FIREBASE_CREDENTIALS_PATH=firebase-admin-sdk.json
FIREBASE_PROJECT_ID=your-firebase-project-id

# JWT Security
SECRET_KEY=imaro-super-secret-jwt-key-change-in-production-2025
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Application Settings
DEBUG=True
ENVIRONMENT=development
APP_NAME=Imaro Phase 1 API
VERSION=1.0.0
```

### Database Configuration Options

**Option 1: Use provided defaults (recommended for development)**
```bash
Database: imarodb
Username: imaro_user
Password: imaro_pass
Host: localhost
Port: 5432
```

**Option 2: Use your own PostgreSQL setup**
```bash
# Update DATABASE_URL in .env file
DATABASE_URL=postgresql://your_user:your_password@localhost:5432/your_database
```

---

## 🗄️ Database Management

### Important Commands

```bash
# Check database status
psql -U imaro_user -d imarodb -c "SELECT COUNT(*) FROM users;"

# View database tables
psql -U imaro_user -d imarodb -c "\dt"

# Reset database (CAUTION: Deletes all data)
alembic downgrade base
alembic upgrade head

# Create new migration after model changes
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# View migration history
alembic history

# Check current migration version
alembic current
```

### Database Schema

The main table is `users` with the following key fields:
- `id` (UUID) - Primary key
- `firebase_uid` (String) - Firebase user identifier
- `auth_method` (String) - 'phone' or 'google'
- `phone_number` (String) - For phone authentication
- `email` (String) - For Google authentication
- `first_name`, `last_name` - User names
- `age`, `gender`, `country` - Profile information
- Various boolean flags for verification and privacy
- Timestamps for created_at and updated_at

---

## 🧪 Development Workflow

### Starting Development Session
```bash
# 1. Navigate to backend
cd backend

# 2. Activate virtual environment
source venv/bin/activate

# 3. Start development server
python -m uvicorn app.main:app --reload --port 8000

# 4. Open another terminal for database operations, testing, etc.
```

### Testing the API

#### Using Swagger UI (Recommended)
1. Open http://localhost:8000/docs
2. Use the interactive documentation to test endpoints
3. All endpoints are documented with examples

#### Using curl
```bash
# Health check
curl http://localhost:8000/api/v1/health/

# Root endpoint
curl http://localhost:8000/

# Send OTP (demo mode)
curl -X POST "http://localhost:8000/api/v1/auth/phone/send-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890"}'

# Verify OTP (use demo code: 123456)
curl -X POST "http://localhost:8000/api/v1/auth/phone/verify-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890", "otp_code": "123456"}'
```

#### Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app

# Run specific test file
pytest tests/test_auth.py -v
```

---

## 🔧 Development Tools

### Useful Commands

```bash
# Check Python packages
pip list

# Update requirements.txt
pip freeze > requirements.txt

# Format code (if you have black installed)
black app/

# Lint code (if you have flake8 installed)
flake8 app/

# Type checking (if you have mypy installed)
mypy app/
```

### Debugging

1. **Check server logs** - The uvicorn server shows detailed logs
2. **Use Swagger UI** - http://localhost:8000/docs for interactive testing
3. **Database inspection** - Use psql or pgAdmin to inspect data
4. **Environment issues** - Check .env file and virtual environment

### Common Issues and Solutions

**Issue: `ModuleNotFoundError`**
```bash
# Solution: Ensure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**Issue: Database connection error**
```bash
# Solution: Check PostgreSQL is running and credentials are correct
brew services start postgresql@14  # macOS
sudo systemctl start postgresql    # Linux
```

**Issue: Port already in use**
```bash
# Solution: Use different port or kill existing process
python -m uvicorn app.main:app --reload --port 8001
# Or find and kill the process using port 8000
lsof -ti:8000 | xargs kill -9
```

**Issue: Migration errors**
```bash
# Solution: Reset migrations (CAUTION: Loses data)
alembic downgrade base
alembic upgrade head
```

---

## 📚 API Documentation

### Available Endpoints

**Authentication:**
- `POST /api/v1/auth/phone/send-otp` - Send OTP to phone
- `POST /api/v1/auth/phone/verify-otp` - Verify OTP and login
- `POST /api/v1/auth/google/login` - Google OAuth login
- `POST /api/v1/auth/complete-profile` - Complete user profile
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - Logout user
- `GET /api/v1/auth/me` - Get current user info

**User Management:**
- `GET /api/v1/users/profile` - Get user profile
- `PUT /api/v1/users/profile` - Update user profile
- `DELETE /api/v1/users/account` - Delete user account

**System:**
- `GET /api/v1/health/` - Health check
- `GET /` - API welcome message
- `GET /docs` - Swagger documentation
- `GET /redoc` - ReDoc documentation

### Authentication Flow

1. **Phone Auth:** Send OTP → Verify OTP → Complete Profile (if new user)
2. **Google Auth:** Verify Google token → Complete Profile (if new user)
3. **API Usage:** Use access token in Authorization header: `Bearer <token>`

---

## 🤝 Collaboration Guidelines

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ... code changes ...

# Commit changes
git add .
git commit -m "Add: brief description of changes"

# Push branch
git push origin feature/your-feature-name

# Create pull request on GitHub
```

### Code Standards
- Follow PEP 8 for Python code style
- Add docstrings to functions and classes
- Write tests for new features
- Update documentation for API changes

### Database Changes
1. Make model changes in `app/models/`
2. Create migration: `alembic revision --autogenerate -m "Description"`
3. Test migration: `alembic upgrade head`
4. Commit both model changes and migration files

### Adding New Endpoints
1. Add Pydantic schemas in `app/schemas/`
2. Add business logic in `app/services/`
3. Add endpoint in `app/api/endpoints/`
4. Add tests in `tests/`
5. Document in docstrings

---

## 🚨 Current Status & Limitations

### ✅ Completed Features
- FastAPI backend with Swagger documentation
- PostgreSQL database with user management
- Authentication endpoints (phone & Google)
- JWT token management
- Database migrations
- Basic testing setup
- Development environment

### 🔄 Demo Mode Features
- **Phone OTP**: Currently accepts "123456" as valid code
- **Firebase**: Needs proper Firebase project setup for production

### 🎯 Next Steps for Production
1. Set up Firebase project and credentials
2. Implement proper OTP service
3. Add comprehensive testing
4. Set up CI/CD pipeline
5. Add logging and monitoring
6. Security hardening

---

## 📞 Getting Help

### Documentation
- **Swagger UI**: http://localhost:8000/docs (when server is running)
- **Phase 1 Specs**: `/Documentations/phase1_backend_auth.md`
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **SQLAlchemy Docs**: https://docs.sqlalchemy.org/

### Debugging Steps
1. Check if virtual environment is activated
2. Verify PostgreSQL is running
3. Check .env configuration
4. Review server logs
5. Test endpoints in Swagger UI
6. Check database with psql

### Quick Health Check
```bash
# Verify everything is working
curl http://localhost:8000/api/v1/health/
# Should return: {"status": "healthy", ...}
```

---

**🎉 You're all set!** 

The backend is now ready for development. Visit http://localhost:8000/docs to explore the API!

---

*Last updated: July 19, 2025*
*Phase 1 - Authentication & User Management Complete*

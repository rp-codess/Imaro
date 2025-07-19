# Imaro Phase 1 - Backend Authentication API

> FastAPI backend with Firebase Phone/Google authentication and minimal user data collection

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Firebase project with Authentication enabled

### Installation

1. **Clone and setup the project:**
```bash
cd /Users/rohanpuri/Desktop/Imaro/backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Setup PostgreSQL database:**
```bash
# Create database
psql -U postgres -c "CREATE DATABASE imarodb;"
psql -U postgres -c "CREATE USER imaro_user WITH PASSWORD 'imaro_pass';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE imarodb TO imaro_user;"
psql -U postgres -d imarodb -c "GRANT ALL ON SCHEMA public TO imaro_user;"
```

3. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your Firebase credentials and database URL
```

4. **Setup Firebase:**
- Go to [Firebase Console](https://console.firebase.google.com)
- Create a new project or use existing
- Enable Authentication → Phone and Google sign-in
- Go to Project Settings → Service Accounts
- Generate and download service account key
- Save as `firebase-admin-sdk.json`

5. **Run migrations:**
```bash
alembic upgrade head
```

6. **Start the server:**
```bash
uvicorn app.main:app --reload --port 8000
```

## 📚 API Documentation

Once the server is running:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

## 🔐 Authentication Flow

### Phone Authentication
1. `POST /api/v1/auth/phone/send-otp` - Send OTP to phone
2. `POST /api/v1/auth/phone/verify-otp` - Verify OTP (use "123456" for demo)
3. `POST /api/v1/auth/complete-profile` - Complete profile if new user

### Google Authentication
1. `POST /api/v1/auth/google/login` - Verify Google ID token
2. `POST /api/v1/auth/complete-profile` - Complete profile if needed

## 📋 API Endpoints

### Authentication
- `POST /api/v1/auth/phone/send-otp` - Send phone OTP
- `POST /api/v1/auth/phone/verify-otp` - Verify phone OTP
- `POST /api/v1/auth/google/login` - Google authentication
- `POST /api/v1/auth/complete-profile` - Complete user profile
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - Logout user
- `GET /api/v1/auth/me` - Get current user info

### User Management
- `GET /api/v1/users/profile` - Get user profile
- `PUT /api/v1/users/profile` - Update user profile
- `DELETE /api/v1/users/account` - Delete user account

### System
- `GET /api/v1/health/` - Health check
- `GET /` - API welcome message

## 🧪 Testing

### Run Tests
```bash
pytest tests/ -v
```

### Test with curl
```bash
# Health check
curl http://localhost:8000/api/v1/health/

# Send OTP (demo)
curl -X POST "http://localhost:8000/api/v1/auth/phone/send-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890"}'

# Verify OTP (demo code: 123456)
curl -X POST "http://localhost:8000/api/v1/auth/phone/verify-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890", "otp_code": "123456"}'
```

## 🏗️ Project Structure

```
backend/
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── auth.py          # Authentication endpoints
│   │   │   ├── users.py         # User management endpoints
│   │   │   └── health.py        # Health check endpoint
│   │   └── router.py            # Main API router
│   ├── core/
│   │   ├── config.py            # App configuration
│   │   ├── database.py          # Database connection
│   │   └── security.py          # Security utilities
│   ├── models/
│   │   ├── base.py              # Base model
│   │   └── user.py              # User model
│   ├── schemas/
│   │   ├── auth.py              # Authentication schemas
│   │   └── user.py              # User schemas
│   ├── services/
│   │   ├── auth_service.py      # Authentication logic
│   │   ├── firebase_service.py  # Firebase integration
│   │   └── user_service.py      # User management
│   ├── utils/
│   │   ├── constants.py         # App constants
│   │   └── validators.py        # Validation utilities
│   ├── dependencies.py          # Dependency injection
│   └── main.py                  # FastAPI app
├── alembic/                     # Database migrations
├── tests/                       # Test files
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
└── README.md                    # This file
```

## 🗄️ Database Schema

### Users Table
- `id` (UUID) - Primary key
- `firebase_uid` (String) - Firebase user ID
- `auth_method` (String) - 'phone' or 'google'
- `phone_number` (String) - Phone number (for phone auth)
- `email` (String) - Email address (for Google auth)
- `first_name`, `last_name` (String) - User name
- `age` (Integer) - User age (13-120)
- `gender` (String) - Gender preference
- `country` (String) - 3-letter country code
- Profile completion and privacy flags
- Security and activity tracking fields
- Timestamps

## 🔧 Configuration

### Environment Variables (.env)
```bash
# Database
DATABASE_URL=postgresql://imaro_user:imaro_pass@localhost:5432/imarodb

# Firebase
FIREBASE_CREDENTIALS_PATH=firebase-admin-sdk.json
FIREBASE_PROJECT_ID=your-firebase-project-id

# JWT
SECRET_KEY=your-super-secret-jwt-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# App
DEBUG=True
ENVIRONMENT=development
APP_NAME=Imaro Phase 1 API
VERSION=1.0.0
```

## 🚨 Development Notes

### Demo Features
- Phone OTP: Use code "123456" for testing
- Firebase: Requires proper setup for production use
- Database: Uses PostgreSQL with proper constraints

### Security
- JWT tokens with 24-hour expiry
- Refresh tokens with 30-day expiry
- Firebase Admin SDK for authentication
- Input validation and sanitization

### Database
- PostgreSQL with UUID primary keys
- Proper indexing for performance
- Check constraints for data integrity
- Alembic migrations for schema versioning

## 🎯 Phase 1 Status

✅ **Completed Features:**
- FastAPI backend with proper structure
- PostgreSQL database with users table
- Firebase Authentication integration
- Phone OTP authentication (demo mode)
- Google OAuth authentication
- User profile management
- JWT token management
- Database migrations
- API documentation
- Basic testing

## 📞 Support

For issues and questions:
1. Check the API documentation at `/docs`
2. Review the health check at `/api/v1/health/`
3. Ensure PostgreSQL and Firebase are properly configured
4. Check application logs for detailed error messages

---

**🎉 Phase 1 Complete!** 

Ready for Phase 2: Credit System Implementation

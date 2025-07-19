# Phase 1: Backend Authentication System

> Setting up FastAPI backend with Firebase Phone/Google authentication and minimal user data collection

## 🎯 Phase 1 Scope

### **What We're Building**
- **FastAPI Backend** with authentication endpoints
- **Twilio SMS Authentication** with OTP verification
- **Firebase Google OAuth** integration and push notifications
- **Minimal User Profile** (first name, last name, age, gender, country)
- **PostgreSQL Database** with user tables
- **Basic API Documentation** with Swagger/OpenAPI

### **What We're NOT Building (Future Phases)**
- Frontend mobile app
- Credit system
- Product analysis features
- Admin panel
- Payment integration
- Image processing

---

## 🏗️ Technical Stack - Phase 1

- **Backend**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15+
- **SMS Service**: Twilio API
- **Authentication**: Firebase Admin SDK (Google OAuth only)
- **Push Notifications**: Firebase Cloud Messaging (FCM)
- **Environment**: Python virtual environment
- **Documentation**: Swagger UI (built-in with FastAPI)
- **Testing**: pytest (basic API tests only)

---

## 📁 Phase 1 Project Structure

```
imaro-phase1/
├── README.md                          # This documentation
├── .gitignore                         # Git ignore rules
├── .env.example                       # Environment template
│
├── backend/                           # FastAPI Application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI app entry point
│   │   ├── database.py                # Database connection
│   │   ├── dependencies.py            # Dependency injection
│   │   │
│   │   ├── api/                       # API Layer
│   │   │   ├── __init__.py
│   │   │   ├── router.py              # Main API router
│   │   │   └── endpoints/             # API endpoints
│   │   │       ├── __init__.py
│   │   │       ├── auth.py            # Authentication endpoints
│   │   │       ├── users.py           # User profile endpoints
│   │   │       └── health.py          # Health check endpoint
│   │   │
│   │   ├── models/                    # Database Models
│   │   │   ├── __init__.py
│   │   │   ├── base.py                # Base model class
│   │   │   └── user.py                # User model
│   │   │
│   │   ├── schemas/                   # Pydantic Schemas
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                # Authentication schemas
│   │   │   └── user.py                # User schemas
│   │   │
│   │   ├── services/                  # Business Logic
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py        # Authentication logic
│   │   │   ├── firebase_service.py    # Firebase integration
│   │   │   └── user_service.py        # User management
│   │   │
│   │   ├── core/                      # Core Configuration
│   │   │   ├── __init__.py
│   │   │   ├── config.py              # App configuration
│   │   │   ├── security.py            # Security utilities
│   │   │   └── database.py            # Database config
│   │   │
│   │   └── utils/                     # Utilities
│   │       ├── __init__.py
│   │       ├── constants.py           # App constants
│   │       └── validators.py          # Custom validators
│   │
│   ├── alembic/                       # Database Migrations
│   │   ├── versions/                  # Migration files
│   │   │   └── 001_create_users_table.py
│   │   ├── env.py                     # Alembic environment
│   │   └── script.py.mako             # Migration template
│   │
│   ├── tests/                         # Basic Tests
│   │   ├── __init__.py
│   │   ├── conftest.py                # Test configuration
│   │   └── test_auth.py               # Authentication tests
│   │
│   ├── requirements.txt               # Python dependencies
│   ├── .env.example                   # Environment template
│   ├── alembic.ini                    # Alembic configuration
│   └── Dockerfile                     # Docker configuration (optional)
│
└── docs/                              # Documentation
    ├── api-endpoints.md               # API documentation
    ├── database-schema.md             # Database design
    └── authentication-flow.md         # Auth flow documentation
```

---

## 🗄️ Phase 1 Database Schema

### **Users Table**
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Firebase Integration
    firebase_uid VARCHAR(128) UNIQUE NOT NULL,
    
    -- Authentication Method
    auth_method VARCHAR(20) NOT NULL CHECK (auth_method IN ('phone', 'google')),
    
    -- Basic Profile Information (Minimal Data)
    phone_number VARCHAR(20) UNIQUE, -- Only for phone auth
    email VARCHAR(255), -- Only for Google auth
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INTEGER CHECK (age >= 13 AND age <= 120),
    gender VARCHAR(20) CHECK (gender IN ('male', 'female', 'other', 'prefer_not_to_say')),
    country VARCHAR(3) NOT NULL, -- ISO 3166-1 alpha-3 (e.g., 'IND', 'USA')
    
    -- Account Status
    is_active BOOLEAN DEFAULT true,
    is_phone_verified BOOLEAN DEFAULT false,
    is_email_verified BOOLEAN DEFAULT false,
    profile_completed BOOLEAN DEFAULT false,
    
    -- Privacy & Terms
    privacy_policy_accepted BOOLEAN DEFAULT false,
    terms_accepted BOOLEAN DEFAULT false,
    privacy_policy_version VARCHAR(10),
    terms_version VARCHAR(10),
    
    -- Security & Activity
    last_login_at TIMESTAMPTZ,
    failed_login_attempts INTEGER DEFAULT 0,
    account_locked_until TIMESTAMPTZ,
    
    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT phone_required_for_phone_auth CHECK (
        (auth_method = 'phone' AND phone_number IS NOT NULL) OR 
        (auth_method = 'google')
    ),
    CONSTRAINT email_required_for_google_auth CHECK (
        (auth_method = 'google' AND email IS NOT NULL) OR 
        (auth_method = 'phone')
    )
);

-- Indexes
CREATE UNIQUE INDEX idx_users_firebase_uid ON users(firebase_uid);
CREATE UNIQUE INDEX idx_users_phone ON users(phone_number) WHERE phone_number IS NOT NULL;
CREATE INDEX idx_users_email ON users(email) WHERE email IS NOT NULL;
CREATE INDEX idx_users_active ON users(is_active, created_at);
CREATE INDEX idx_users_auth_method ON users(auth_method);
CREATE INDEX idx_users_country ON users(country);
```

---

## 🔐 Phase 1 Authentication Flow

### **Phone Authentication Flow**
```
1. POST /auth/phone/send-otp
   - Input: phone_number
   - Twilio sends OTP via SMS
   - Return: success/failure status

2. POST /auth/phone/verify-otp
   - Input: phone_number, otp_code
   - Twilio verifies OTP
   - If valid: Create/login user, return JWT token
   - If new user: profile_completed = false

3. POST /auth/complete-profile (if new user)
   - Input: first_name, last_name, age, gender, country
   - Update user profile
   - Set profile_completed = true
```

### **Google Authentication Flow**
```
1. POST /auth/google/login
   - Input: google_id_token (from frontend)
   - Firebase verifies Google token
   - Extract email, name from Google profile
   - Create/login user, return JWT token
   - If new user: profile_completed = false

2. POST /auth/complete-profile (if new user)
   - Input: first_name, last_name, age, gender, country
   - Update user profile
   - Set profile_completed = true
```

### **Token Management**
```
- JWT tokens with 24-hour expiry
- Refresh tokens with 30-day expiry
- Token refresh endpoint: POST /auth/refresh
```

---

## 📋 Phase 1 API Endpoints

### **Authentication Endpoints**
```
POST /api/v1/auth/phone/send-otp
POST /api/v1/auth/phone/verify-otp
POST /api/v1/auth/google/login
POST /api/v1/auth/complete-profile
POST /api/v1/auth/refresh
POST /api/v1/auth/logout
GET  /api/v1/auth/me
```

### **User Endpoints**
```
GET  /api/v1/users/profile
PUT  /api/v1/users/profile
DELETE /api/v1/users/account
```

### **System Endpoints**
```
GET  /api/v1/health
GET  /docs (Swagger UI)
GET  /redoc (ReDoc documentation)
```

---

## 🚀 Phase 1 Setup Instructions

### **Prerequisites**
- Python 3.11+
- PostgreSQL 15+
- Firebase project with Authentication enabled
- Git

### **1. Project Setup**
```bash
# Create project directory
mkdir imaro-phase1
cd imaro-phase1

# Create backend directory
mkdir backend
cd backend

# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Create requirements.txt
cat > requirements.txt << EOF
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
alembic==1.12.1
psycopg2-binary==2.9.9
pydantic==2.5.0
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
firebase-admin==6.4.0
twilio==8.10.0
redis==5.0.1
python-multipart==0.0.6
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2
python-dotenv==1.0.0
EOF

# Install dependencies
pip install -r requirements.txt
```

### **2. PostgreSQL Database Setup**
```bash
# Create database (adjust credentials as needed)
psql postgres
CREATE DATABASE ImaroDb;
CREATE USER imaro_user WITH PASSWORD 'imaro_pass';
GRANT ALL PRIVILEGES ON DATABASE ImaroDb TO imaro_user;
\c ImaroDb
GRANT ALL ON SCHEMA public TO imaro_user;
\q
```

### **3. Environment Configuration**
```bash
# Create .env file
cat > .env << EOF
# Database
DATABASE_URL=postgresql://imaro_user:imaro_pass@localhost:5432/imarodb

# Twilio Configuration
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_MESSAGING_SERVICE_SID=your-messaging-service-sid

# Firebase Configuration (Google OAuth & Push Notifications)
FIREBASE_CREDENTIALS_PATH=firebase-admin-sdk.json
FIREBASE_PROJECT_ID=your-firebase-project-id

# JWT
SECRET_KEY=your-super-secret-jwt-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# App
DEBUG=True
ENVIRONMENT=development
APP_NAME=Imaro Phase 1 API
VERSION=1.0.0
EOF
```

### **4. Twilio Setup**
```bash
# 1. Go to Twilio Console (https://console.twilio.com)
# 2. Create account or login
# 3. Get Account SID and Auth Token from dashboard
# 4. Create a Messaging Service:
#    - Go to Messaging > Services
#    - Create new service
#    - Add a sender (phone number or alphanumeric ID)
# 5. Update TWILIO_* variables in .env
```

### **5. Firebase Setup**
```bash
# 1. Go to Firebase Console (https://console.firebase.google.com)
# 2. Create new project or use existing
# 3. Enable Authentication
# 4. Enable Google sign-in method only (no phone auth needed)
# 5. Enable Cloud Messaging for push notifications
# 6. Go to Project Settings > Service Accounts
# 7. Generate new private key
# 8. Download JSON file and save as firebase-admin-sdk.json
# 9. Update FIREBASE_CREDENTIALS_PATH in .env
```

### **6. Initialize Alembic**
```bash
# Initialize Alembic
alembic init alembic

# Edit alembic.ini - update sqlalchemy.url
# sqlalchemy.url = postgresql://imaro_user:imaro_pass@localhost:5432/ImaroDb
```

### **6. Create Core Files**

#### **app/main.py**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.router import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Imaro Phase 1 API", "version": settings.VERSION}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### **7. Run Database Migrations**
```bash
# Create first migration
alembic revision --autogenerate -m "Create users table"

# Apply migrations
alembic upgrade head
```

### **8. Start Development Server**
```bash
# Start the server
uvicorn app.main:app --reload --port 8000

# API will be available at:
# http://localhost:8000
# Documentation: http://localhost:8000/docs
```

---

## 📝 Phase 1 File Templates

### **app/core/config.py**
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Imaro Phase 1 API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str
    
    # Firebase
    FIREBASE_CREDENTIALS_PATH: str
    FIREBASE_PROJECT_ID: str
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    # Environment
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### **app/models/user.py**
```python
from sqlalchemy import Column, String, Integer, Boolean, DateTime, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.models.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    firebase_uid = Column(String(128), unique=True, nullable=False, index=True)
    auth_method = Column(String(20), nullable=False)
    
    # Profile data
    phone_number = Column(String(20), unique=True, nullable=True)
    email = Column(String(255), nullable=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(20), nullable=True)
    country = Column(String(3), nullable=False)
    
    # Status
    is_active = Column(Boolean, default=True)
    is_phone_verified = Column(Boolean, default=False)
    is_email_verified = Column(Boolean, default=False)
    profile_completed = Column(Boolean, default=False)
    
    # Privacy
    privacy_policy_accepted = Column(Boolean, default=False)
    terms_accepted = Column(Boolean, default=False)
    privacy_policy_version = Column(String(10))
    terms_version = Column(String(10))
    
    # Security
    last_login_at = Column(DateTime(timezone=True))
    failed_login_attempts = Column(Integer, default=0)
    account_locked_until = Column(DateTime(timezone=True))
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Constraints
    __table_args__ = (
        CheckConstraint("auth_method IN ('phone', 'google')", name="valid_auth_method"),
        CheckConstraint("age >= 13 AND age <= 120", name="valid_age"),
        CheckConstraint("gender IN ('male', 'female', 'other', 'prefer_not_to_say')", name="valid_gender"),
    )
```

### **app/schemas/auth.py**
```python
from pydantic import BaseModel, validator
from typing import Optional
import re

class PhoneSendOTPRequest(BaseModel):
    phone_number: str
    
    @validator('phone_number')
    def validate_phone(cls, v):
        # Basic phone validation - adjust regex as needed
        if not re.match(r'^\+[1-9]\d{1,14}$', v):
            raise ValueError('Invalid phone number format')
        return v

class PhoneVerifyOTPRequest(BaseModel):
    phone_number: str
    otp_code: str

class GoogleLoginRequest(BaseModel):
    id_token: str

class CompleteProfileRequest(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    country: str
    privacy_policy_accepted: bool = True
    terms_accepted: bool = True
    
    @validator('age')
    def validate_age(cls, v):
        if v < 13 or v > 120:
            raise ValueError('Age must be between 13 and 120')
        return v
    
    @validator('gender')
    def validate_gender(cls, v):
        if v not in ['male', 'female', 'other', 'prefer_not_to_say']:
            raise ValueError('Invalid gender')
        return v
    
    @validator('country')
    def validate_country(cls, v):
        # Basic country code validation - you can expand this
        if len(v) != 3 or not v.isupper():
            raise ValueError('Country must be 3-letter ISO code')
        return v

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: str
    profile_completed: bool

class RefreshTokenRequest(BaseModel):
    refresh_token: str
```

---

## 🧪 Phase 1 Testing

### **Basic API Tests**
```bash
# Test health endpoint
curl http://localhost:8000/api/v1/health

# Test phone OTP (will fail without proper Firebase setup)
curl -X POST "http://localhost:8000/api/v1/auth/phone/send-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+919876543210"}'

# View API documentation
# http://localhost:8000/docs
```

### **Run Tests**
```bash
# Run basic tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app
```

---

## ✅ Phase 1 Deliverables

### **Completed Features**
- [x] FastAPI backend setup with proper structure
- [x] PostgreSQL database with users table
- [x] Firebase Authentication integration
- [x] Phone OTP authentication endpoints
- [x] Google OAuth authentication endpoints
- [x] User profile completion workflow
- [x] JWT token management
- [x] Database migrations with Alembic
- [x] API documentation with Swagger UI
- [x] Basic input validation
- [x] Environment configuration
- [x] Docker support (optional)

### **API Endpoints Ready**
- [x] `POST /api/v1/auth/phone/send-otp`
- [x] `POST /api/v1/auth/phone/verify-otp`
- [x] `POST /api/v1/auth/google/login`
- [x] `POST /api/v1/auth/complete-profile`
- [x] `POST /api/v1/auth/refresh`
- [x] `POST /api/v1/auth/logout`
- [x] `GET /api/v1/auth/me`
- [x] `GET /api/v1/users/profile`
- [x] `PUT /api/v1/users/profile`
- [x] `GET /api/v1/health`

### **Documentation Ready**
- [x] API documentation at `/docs`
- [x] Database schema documentation
- [x] Authentication flow documentation
- [x] Setup and deployment instructions

---

## 🚀 Next Phases Preview

### **Phase 2: Credit System**
- User credits table
- Credit transactions
- Purchase workflows
- Admin credit management

### **Phase 3: Product Analysis**
- Image upload endpoints
- Google Vision API integration
- OpenAI analysis integration
- Analysis results storage

### **Phase 4: Frontend Mobile App**
- React Native app
- Authentication screens
- Camera integration
- Analysis results display

### **Phase 5: Advanced Features**
- Product comparison
- User preferences
- Analytics and reporting
- Performance optimization

---

## 📞 Phase 1 Support

### **Common Issues**
1. **Firebase Connection**: Ensure credentials file path is correct
2. **Database Connection**: Check PostgreSQL is running and credentials
3. **Phone OTP**: Requires Firebase Phone Auth configuration
4. **Google OAuth**: Requires Google OAuth setup in Firebase

### **Development Tips**
- Use `/docs` endpoint for interactive API testing
- Check logs for Firebase authentication errors
- Use pgAdmin for database inspection
- Test with Postman or curl for API endpoints

**Phase 1 Goal**: Get authentication working perfectly before moving to next features!

---

**Built with ❤️ for Phase 1 Development**

*One step at a time, building robust foundations.*
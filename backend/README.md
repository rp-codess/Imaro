# Imaro Phase 1 - Backend Authentication API

> FastAPI backend with Twilio SMS authentication, Firebase Google OAuth, and user management

## 🚀 Quick Start

```bash
# 1. Navigate to backend
cd backend

# 2. Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env with your Twilio and Firebase credentials

# 4. Setup database
alembic upgrade head

# 5. Start server
python -m uvicorn app.main:app --reload --port 8000
```

## 📚 Documentation

- **Swagger UI**: http://localhost:8000/docs
- **Setup Guide**: `/Documentations/DEVELOPER_SETUP.md`
- **Phase 1 Specs**: `/Documentations/phase1_backend_auth.md`
- **Quick Reference**: `/Documentations/QUICK_REFERENCE.md`

## � Current Features

✅ **Authentication:**
- Twilio SMS OTP verification
- Firebase Google OAuth
- JWT token management

✅ **User Management:**
- Profile creation and updates
- Account management

✅ **Database:**
- PostgreSQL with Alembic migrations
- User table with proper constraints

✅ **API Documentation:**
- Swagger UI with interactive testing
- Comprehensive endpoint documentation

## 🧪 Test API

```bash
# Health check
curl http://localhost:8000/api/v1/health/

# Send OTP (demo mode: use code 123456)
curl -X POST "http://localhost:8000/api/v1/auth/phone/send-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890"}'
```

**📋 Next Steps:** Configure Twilio and Firebase credentials for production use.

For detailed setup instructions, see `/Documentations/DEVELOPER_SETUP.md`

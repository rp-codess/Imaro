# Imaro Backend - Quick Command Reference

> Essential commands for daily development

## 🚀 Daily Startup
```bash
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --port 8000
```

## 🗄️ Database Commands
```bash
# View tables
psql -U imaro_user -d imarodb -c "\dt"

# Check user count
psql -U imaro_user -d imarodb -c "SELECT COUNT(*) FROM users;"

# Create migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Reset database (CAUTION!)
alembic downgrade base && alembic upgrade head
```

## 🧪 Testing Commands
```bash
# Quick API test
curl http://localhost:8000/api/v1/health/

# Send demo OTP (Twilio SMS)
curl -X POST "http://localhost:8000/api/v1/auth/phone/send-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890"}'

# Verify demo OTP (use code: 123456)
curl -X POST "http://localhost:8000/api/v1/auth/phone/verify-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890", "otp_code": "123456"}'

# Run tests
pytest tests/ -v
```

## 📚 Documentation URLs
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/api/v1/health/

## 🔧 Environment
```bash
# Database URL
postgresql://imaro_user:imaro_pass@localhost:5432/imarodb

# Demo OTP Code
123456

# Server Port
8000
```

## 🚨 Troubleshooting
```bash
# Check if server is running
lsof -i :8000

# Restart PostgreSQL (macOS)
brew services restart postgresql@14

# Check venv activation
which python  # Should show venv path

# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

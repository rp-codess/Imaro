# Imaro Backend - Updated Setup Guide with Twilio & Firebase

> Complete setup guide with Twilio SMS and Firebase integration

## 📋 What Changed

### 🔄 **Phone Authentication**: Twilio SMS (instead of Firebase Phone Auth)
- More reliable SMS delivery
- Better international coverage  
- Easier to set up and manage
- Cost-effective for production

### 🔥 **Firebase**: Google OAuth + Push Notifications Only
- Google Sign-In authentication
- Push notifications for mobile app
- User profile management

---

## 🚀 Updated Quick Setup

### 1. Install New Dependencies
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt  # Now includes Twilio & Redis
```

### 2. Environment Configuration (.env)
```bash
# Database
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

# Application
DEBUG=True
ENVIRONMENT=development
APP_NAME=Imaro Phase 1 API
VERSION=1.0.0
```

---

## 📱 Twilio Setup (SMS/OTP)

### Step 1: Create Twilio Account
1. Go to [Twilio Console](https://console.twilio.com)
2. Sign up (free trial includes $15.50 credit)
3. Verify your phone number

### Step 2: Get Credentials
1. From Twilio Console Dashboard:
   - Copy **Account SID**
   - Copy **Auth Token**

### Step 3: Create Messaging Service
1. Go to **Messaging** → **Services** → **Create Messaging Service**
2. Choose "Notify my users" use case
3. Give it a name (e.g., "Imaro OTP Service")
4. Complete the setup wizard
5. Copy the **Messaging Service SID**

### Step 4: Add Phone Number (Optional for Production)
- For production: Buy a phone number from Twilio
- For development: Messaging Service works without buying a number

### Step 5: Update .env File
```bash
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_MESSAGING_SERVICE_SID=MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🔥 Firebase Setup (Google OAuth)

### Step 1: Create Firebase Project
1. Go to [Firebase Console](https://console.firebase.google.com)
2. Create new project or use existing
3. Enable Google Analytics (optional)

### Step 2: Enable Authentication
1. Go to **Authentication** → **Sign-in method**
2. Enable **Google** sign-in provider
3. Add your domain to authorized domains

### Step 3: Get Service Account Key
1. Go to **Project Settings** → **Service Accounts**
2. Click **Generate new private key**
3. Download the JSON file
4. Save as `firebase-admin-sdk.json` in backend directory

### Step 4: Update .env File
```bash
FIREBASE_CREDENTIALS_PATH=firebase-admin-sdk.json
FIREBASE_PROJECT_ID=your-project-id-here
```

---

## 🧪 Testing the New Setup

### Test Phone OTP (Demo Mode)
```bash
# Send OTP (will use mock service if Twilio not configured)
curl -X POST "http://localhost:8000/api/v1/auth/phone/send-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890"}'

# Response in demo mode:
{
  "success": true,
  "message": "Demo OTP sent to +1234567890. Use code: 123456"
}

# Verify OTP
curl -X POST "http://localhost:8000/api/v1/auth/phone/verify-otp" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890", "otp_code": "123456"}'
```

### Test Health Check
```bash
curl http://localhost:8000/api/v1/health/
```

---

## 🔧 Development Modes

### 1. **Demo Mode** (Default)
- **When**: Twilio credentials not configured
- **SMS**: Logged to console, no actual SMS sent
- **OTP**: Fixed code "123456"
- **Perfect for**: Local development and testing

### 2. **Production Mode**
- **When**: Valid Twilio credentials provided
- **SMS**: Real SMS sent via Twilio
- **OTP**: Random 6-digit codes
- **Perfect for**: Staging and production

---

## 📋 Updated API Endpoints

### Phone Authentication (Twilio)
- `POST /api/v1/auth/phone/send-otp` - Send OTP via Twilio SMS
- `POST /api/v1/auth/phone/verify-otp` - Verify OTP and authenticate

### Google Authentication (Firebase)
- `POST /api/v1/auth/google/login` - Verify Google ID token

### User Management
- `POST /api/v1/auth/complete-profile` - Complete user profile
- `GET /api/v1/auth/me` - Get current user info
- `GET /api/v1/users/profile` - Get user profile
- `PUT /api/v1/users/profile` - Update user profile

---

## 🔄 Migration from Old Setup

If you had the old Firebase phone auth setup:

1. **Update dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Update .env file** with Twilio credentials

3. **Restart server**:
   ```bash
   python -m uvicorn app.main:app --reload --port 8000
   ```

4. **Test new endpoints** in Swagger UI at http://localhost:8000/docs

---

## 🚨 Current Status

### ✅ **Working Features**
- **Twilio SMS**: Demo mode (123456) + Production mode
- **Firebase Google OAuth**: Ready for configuration
- **Database**: PostgreSQL with user management
- **API Documentation**: Swagger UI at `/docs`
- **Authentication**: JWT tokens with refresh
- **User Management**: Profile completion and updates

### 🔄 **Demo vs Production**

| Feature | Demo Mode | Production Mode |
|---------|-----------|-----------------|
| SMS OTP | Console log + fixed OTP (123456) | Real SMS via Twilio |
| Google Auth | Requires Firebase setup | Requires Firebase setup |
| Database | PostgreSQL (same) | PostgreSQL (same) |
| JWT Tokens | Working | Working |

---

## 💡 Benefits of New Architecture

### 🔧 **Twilio for SMS**
- ✅ Reliable SMS delivery worldwide
- ✅ Better developer experience
- ✅ Detailed delivery reports
- ✅ Cost-effective scaling
- ✅ Easy testing with demo mode

### 🔥 **Firebase for OAuth & Push**
- ✅ Seamless Google Sign-In
- ✅ Ready for push notifications
- ✅ Social login expansion ready
- ✅ User management tools

### 📱 **Ready for Mobile App**
- ✅ SMS OTP works on all devices
- ✅ Google Sign-In integration
- ✅ Push notification foundation
- ✅ Scalable authentication system

---

## 🚀 Quick Start Commands

```bash
# Start development
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --port 8000

# Test API
curl http://localhost:8000/api/v1/health/

# View documentation
open http://localhost:8000/docs
```

---

## 📞 Production Checklist

### Before Going Live:
- [ ] Set up real Twilio account with messaging service
- [ ] Configure Firebase project with Google OAuth
- [ ] Set up Redis for OTP storage (instead of in-memory)
- [ ] Update JWT secret key
- [ ] Configure CORS for your domain
- [ ] Set up SSL/TLS certificates
- [ ] Configure monitoring and logging

---

**🎉 Updated Architecture Complete!**

*Twilio + Firebase = Robust authentication system ready for production*

---

*Last updated: July 19, 2025*
*Phase 1 Complete - Enhanced with Twilio SMS*

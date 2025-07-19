### **1. Updated Users Table**
```sql# Imaro - Smart Product Analysis Mobile App

> AI-powered ingredient analysis for smarter product purchasing decisions

## 📱 Project Overview

**Imaro** is an intelligent mobile application that empowers users to make informed purchasing decisions by analyzing product ingredients and nutritional information through advanced AI. Users capture images of products, and the app provides health scores, personalized recommendations, and comparative analysis to help choose the healthiest options.

### ✨ Core Features
- **📸 Smart Image Capture**: AI-powered product label analysis
- **🤖 Intelligent Analysis**: Google Vision API + OpenAI for comprehensive ingredient evaluation
- **⚖️ Product Comparison**: Side-by-side health analysis of multiple products
- **💎 Health Scoring**: 1-10 rating system with detailed explanations
- **👤 Personalized Recommendations**: Tailored to dietary restrictions and health goals
- **🔐 Simple Authentication**: Phone number or Google login with minimal data collection
- **💰 Credit-Based System**: Pay ₹100 for 10 analysis requests + admin request management
- **🎛️ Admin Controls**: Dynamic request allocation and user credit management
- **📊 Request Tracking**: Real-time credit balance and usage analytics

---

## 🏗️ Technical Architecture

### **Tech Stack Overview**
- **Frontend**: React Native with TypeScript
- **Backend**: FastAPI (Python 3.11+) with async support
- **Database**: PostgreSQL 15+ with JSONB for flexible data
- **Cache**: Redis for session management and API response caching
- **Storage**: Azure Blob Storage for secure image storage
- **Authentication**: Firebase Auth (Google OAuth) + Phone Authentication
- **AI Services**: Google Vision API (OCR) + OpenAI GPT-4 (analysis)
- **Payment**: Razorpay integration for credit purchases

### **Credit-Based Pricing Model**
- **Base Package**: ₹100 = 10 analysis requests
- **Rate**: ₹10 per analysis request
- **Admin Flexibility**: Adjust request counts and pricing dynamically
- **Credit Management**: Real-time balance tracking and auto-deduction

---

## 📁 Complete Project Structure

```
imaro/
├── README.md                          # This documentation
├── .gitignore                         # Git ignore rules
├── docker-compose.yml                 # Backend containerization
├── .env.example                       # Environment template
│
├── frontend/                          # React Native Mobile Application
│   ├── src/
│   │   ├── components/                # Reusable UI Components
│   │   │   ├── common/                # Shared components
│   │   │   │   ├── Button/
│   │   │   │   │   ├── Button.tsx
│   │   │   │   │   ├── Button.styles.ts
│   │   │   │   │   └── index.ts
│   │   │   │   ├── LoadingSpinner/
│   │   │   │   ├── Modal/
│   │   │   │   ├── Toast/
│   │   │   │   ├── ErrorBoundary/
│   │   │   │   ├── Header/
│   │   │   │   └── TabBar/
│   │   │   ├── camera/                # Camera & Image components
│   │   │   │   ├── CameraView/
│   │   │   │   ├── ImagePreview/
│   │   │   │   ├── MultiImageCapture/
│   │   │   │   └── ImageCropper/
│   │   │   ├── product/               # Product display components
│   │   │   │   ├── ProductCard/
│   │   │   │   ├── ProductList/
│   │   │   │   ├── ProductComparison/
│   │   │   │   ├── IngredientAnalysis/
│   │   │   │   └── NutritionFacts/
│   │   │   ├── analysis/              # Analysis result components
│   │   │   │   ├── AnalysisResult/
│   │   │   │   ├── HealthScore/
│   │   │   │   ├── Recommendation/
│   │   │   │   └── ComparisonChart/
│   │   │   ├── auth/                  # Authentication components
│   │   │   │   ├── PhoneLogin/
│   │   │   │   ├── GoogleLogin/
│   │   │   │   ├── OTPVerification/
│   │   │   │   ├── ProfileSetup/
│   │   │   │   └── PrivacyConsent/
│   │   │   ├── credits/               # Credit management components
│   │   │   │   ├── CreditBalance/
│   │   │   │   ├── PurchaseCredits/
│   │   │   │   ├── CreditHistory/
│   │   │   │   ├── PaymentForm/
│   │   │   │   └── LowCreditAlert/
│   │   │   ├── admin/                 # Admin management components
│   │   │   │   ├── UserManagement/
│   │   │   │   ├── CreditAdjustment/
│   │   │   │   ├── PricingControl/
│   │   │   │   ├── UsageAnalytics/
│   │   │   │   └── AdminDashboard/
│   │   │   └── device/                # Device management
│   │   │       ├── DeviceInfo/
│   │   │       ├── SessionStatus/
│   │   │       └── SecurityAlert/
│   │   ├── screens/                   # Application Screens
│   │   │   ├── Home/
│   │   │   │   ├── HomeScreen.tsx
│   │   │   │   ├── HomeScreen.styles.ts
│   │   │   │   └── index.ts
│   │   │   ├── Camera/                # Product capture screen
│   │   │   ├── Analysis/              # Analysis results screen
│   │   │   ├── Comparison/            # Product comparison screen
│   │   │   ├── Profile/               # User profile management
│   │   │   ├── Auth/                  # Authentication screens
│   │   │   ├── Credits/               # Credit management screens
│   │   │   ├── Admin/                 # Admin panel screens
│   │   │   ├── Onboarding/            # First-time user experience
│   │   │   └── Settings/              # App configuration
│   │   ├── services/                  # Business Logic Services
│   │   │   ├── api/
│   │   │   │   ├── client.ts          # HTTP client configuration
│   │   │   │   ├── endpoints.ts       # API endpoint definitions
│   │   │   │   └── types.ts           # API type definitions
│   │   │   ├── auth/
│   │   │   │   ├── authService.ts     # Authentication logic
│   │   │   │   ├── firebaseConfig.ts  # Firebase configuration
│   │   │   │   ├── phoneAuth.ts       # Phone authentication
│   │   │   │   ├── googleAuth.ts      # Google OAuth integration
│   │   │   │   └── AuthProvider.tsx   # Auth context provider
│   │   │   ├── credits/
│   │   │   │   ├── creditService.ts   # Credit management logic
│   │   │   │   ├── paymentService.ts  # Payment processing
│   │   │   │   └── priceCalculator.ts # Dynamic pricing calculations
│   │   │   ├── admin/
│   │   │   │   ├── adminService.ts    # Admin operations
│   │   │   │   ├── userManagement.ts  # User management
│   │   │   │   └── analyticsService.ts # Admin analytics
│   │   │   ├── camera/
│   │   │   │   ├── cameraService.ts   # Camera operations
│   │   │   │   └── imageProcessor.ts  # Image processing utilities
│   │   │   ├── storage/
│   │   │   │   ├── localStorage.ts    # Local data storage
│   │   │   │   └── cache.ts           # Caching strategies
│   │   │   ├── analytics/
│   │   │   │   └── trackingService.ts # User behavior tracking
│   │   │   ├── notifications/
│   │   │   │   └── pushService.ts     # Push notification handling
│   │   │   └── device/
│   │   │       ├── deviceService.ts   # Device identification
│   │   │       └── fingerprint.ts     # Device fingerprinting
│   │   ├── store/                     # State Management (Redux)
│   │   │   ├── index.ts               # Store configuration
│   │   │   ├── slices/                # Redux slices
│   │   │   │   ├── authSlice.ts       # Authentication state
│   │   │   │   ├── cameraSlice.ts     # Camera state
│   │   │   │   ├── productSlice.ts    # Product data state
│   │   │   │   ├── analysisSlice.ts   # Analysis results state
│   │   │   │   ├── creditSlice.ts     # Credit management state
│   │   │   │   ├── adminSlice.ts      # Admin management state
│   │   │   │   └── deviceSlice.ts     # Device management state
│   │   │   ├── middleware/
│   │   │   │   └── logger.ts          # Redux logging middleware
│   │   │   └── selectors/
│   │   │       ├── authSelectors.ts   # Auth state selectors
│   │   │       ├── creditSelectors.ts # Credit state selectors
│   │   │       └── adminSelectors.ts  # Admin state selectors
│   │   ├── utils/                     # Utility Functions
│   │   │   ├── constants.ts           # App constants
│   │   │   ├── helpers.ts             # Helper functions
│   │   │   ├── validation.ts          # Form validation schemas
│   │   │   ├── animations.ts          # Animation utilities
│   │   │   ├── formatters.ts          # Data formatting
│   │   │   ├── priceFormatters.ts     # Price and credit formatting
│   │   │   └── storage.ts             # Storage utilities
│   │   ├── types/                     # TypeScript Definitions
│   │   │   ├── api.ts                 # API response types
│   │   │   ├── user.ts                # User data types
│   │   │   ├── product.ts             # Product data types
│   │   │   ├── analysis.ts            # Analysis result types
│   │   │   ├── auth.ts                # Authentication types
│   │   │   ├── credits.ts             # Credit system types
│   │   │   ├── admin.ts               # Admin management types
│   │   │   ├── device.ts              # Device types
│   │   │   └── common.ts              # Common/shared types
│   │   ├── assets/                    # Static Assets
│   │   │   ├── images/                # Image assets
│   │   │   ├── icons/                 # Icon assets
│   │   │   ├── animations/            # Lottie animations
│   │   │   └── fonts/                 # Custom fonts
│   │   ├── styles/                    # Styling
│   │   │   ├── themes/                # Theme definitions
│   │   │   ├── colors.ts              # Color palette
│   │   │   ├── typography.ts          # Typography system
│   │   │   └── components/            # Component-specific styles
│   │   ├── hooks/                     # Custom React Hooks
│   │   │   ├── auth/
│   │   │   │   ├── useAuth.ts         # Authentication hooks
│   │   │   │   ├── usePhoneAuth.ts    # Phone authentication hooks
│   │   │   │   ├── useGoogleAuth.ts   # Google OAuth hooks
│   │   │   │   └── useFirebase.ts     # Firebase integration hooks
│   │   │   ├── api/
│   │   │   │   ├── useApiCall.ts      # API calling hooks
│   │   │   │   └── useQuery.ts        # Data fetching hooks
│   │   │   ├── credits/
│   │   │   │   ├── useCredits.ts      # Credit management hooks
│   │   │   │   ├── usePayment.ts      # Payment processing hooks
│   │   │   │   └── usePricing.ts      # Dynamic pricing hooks
│   │   │   ├── admin/
│   │   │   │   ├── useAdminAuth.ts    # Admin authentication
│   │   │   │   ├── useUserManagement.ts # User management hooks
│   │   │   │   └── useAnalytics.ts    # Analytics hooks
│   │   │   ├── camera/
│   │   │   │   └── useCamera.ts       # Camera operation hooks
│   │   │   └── storage/
│   │   │       └── useStorage.ts      # Storage operation hooks
│   │   ├── navigation/                # App Navigation
│   │   │   ├── stacks/
│   │   │   │   ├── AuthStack.tsx      # Authentication flow
│   │   │   │   ├── MainStack.tsx      # Main app navigation
│   │   │   │   ├── AdminStack.tsx     # Admin panel navigation
│   │   │   │   └── OnboardingStack.tsx # Onboarding flow
│   │   │   ├── tabs/
│   │   │   │   └── MainTabs.tsx       # Bottom tab navigation
│   │   │   ├── types/
│   │   │   │   └── navigation.ts      # Navigation type definitions
│   │   │   └── AppNavigator.tsx       # Root navigator
│   │   ├── App.tsx                    # Root app component
│   │   └── index.ts                   # App entry point
│   ├── package.json                   # Dependencies & scripts
│   ├── tsconfig.json                  # TypeScript configuration
│   ├── metro.config.js                # Metro bundler configuration
│   ├── react-native.config.js         # React Native configuration
│   ├── .env.example                   # Environment variables template
│   ├── .eslintrc.js                   # ESLint configuration
│   ├── .prettierrc                    # Prettier configuration
│   ├── babel.config.js                # Babel configuration
│   ├── android/                       # Android-specific files
│   └── ios/                           # iOS-specific files
│
├── backend/                           # FastAPI Server Application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI app entry point
│   │   ├── database.py                # Database connection setup
│   │   ├── dependencies.py            # Dependency injection
│   │   │
│   │   ├── api/                       # REST API Layer
│   │   │   ├── __init__.py
│   │   │   ├── router.py              # Main API router
│   │   │   ├── deps.py                # API dependencies
│   │   │   └── endpoints/             # API endpoint modules
│   │   │       ├── __init__.py
│   │   │       ├── auth.py            # Authentication endpoints
│   │   │       ├── users.py           # User management endpoints
│   │   │       ├── products.py        # Product endpoints
│   │   │       ├── analysis.py        # Analysis endpoints
│   │   │       ├── images.py          # Image upload endpoints
│   │   │       ├── credits.py         # Credit management endpoints
│   │   │       ├── payments.py        # Payment processing endpoints
│   │   │       ├── admin.py           # Admin management endpoints
│   │   │       ├── devices.py         # Device management endpoints
│   │   │       └── comparisons.py     # Comparison endpoints
│   │   │
│   │   ├── models/                    # Database Models (SQLAlchemy)
│   │   │   ├── __init__.py
│   │   │   ├── base.py                # Base model class
│   │   │   ├── user.py                # User model
│   │   │   ├── active_session.py      # Session management model
│   │   │   ├── device_history.py      # Device tracking model
│   │   │   ├── user_credits.py        # Credit balance model
│   │   │   ├── credit_transactions.py # Credit transaction history
│   │   │   ├── pricing_config.py      # Dynamic pricing configuration
│   │   │   ├── admin_users.py         # Admin user management
│   │   │   ├── usage_tracking.py      # Usage tracking model
│   │   │   ├── product_analysis.py    # Product analysis model
│   │   │   ├── comparison.py          # Product comparison model
│   │   │   ├── security_events.py     # Security logging model
│   │   │   ├── payment_history.py     # Payment tracking model
│   │   │   └── ai_response_cache.py   # AI response caching model
│   │   │
│   │   ├── schemas/                   # Pydantic Schemas (API Models)
│   │   │   ├── __init__.py
│   │   │   ├── user.py                # User schemas
│   │   │   ├── auth.py                # Authentication schemas
│   │   │   ├── credits.py             # Credit system schemas
│   │   │   ├── admin.py               # Admin operation schemas
│   │   │   ├── product.py             # Product schemas
│   │   │   ├── analysis.py            # Analysis schemas
│   │   │   ├── device.py              # Device schemas
│   │   │   ├── image.py               # Image upload schemas
│   │   │   ├── payment.py             # Payment schemas
│   │   │   └── comparison.py          # Comparison schemas
│   │   │
│   │   ├── services/                  # Business Logic Layer
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py        # Authentication business logic
│   │   │   ├── user_service.py        # User management logic
│   │   │   ├── credit_service.py      # Credit management logic
│   │   │   ├── payment_service.py     # Payment processing logic
│   │   │   ├── admin_service.py       # Admin operations logic
│   │   │   ├── pricing_service.py     # Dynamic pricing logic
│   │   │   ├── device_service.py      # Device management logic
│   │   │   ├── session_service.py     # Session management
│   │   │   ├── product_analysis_service.py # Product analysis logic
│   │   │   ├── google_vision_service.py # Google Vision API integration
│   │   │   ├── openai_service.py      # OpenAI API integration
│   │   │   ├── azure_blob_service.py  # Azure storage integration
│   │   │   ├── usage_tracking_service.py # Usage monitoring
│   │   │   ├── recommendation_service.py # AI recommendations
│   │   │   └── security_service.py    # Security event handling
│   │   │
│   │   ├── repositories/              # Data Access Layer
│   │   │   ├── __init__.py
│   │   │   ├── base.py                # Base repository pattern
│   │   │   ├── user_repository.py     # User data access
│   │   │   ├── session_repository.py  # Session data access
│   │   │   ├── device_repository.py   # Device data access
│   │   │   ├── credit_repository.py   # Credit data access
│   │   │   ├── admin_repository.py    # Admin data access
│   │   │   ├── pricing_repository.py  # Pricing configuration data access
│   │   │   ├── analysis_repository.py # Analysis data access
│   │   │   ├── comparison_repository.py # Comparison data access
│   │   │   ├── usage_repository.py    # Usage data access
│   │   │   ├── payment_repository.py  # Payment data access
│   │   │   └── cache_repository.py    # Cache data access
│   │   │
│   │   ├── core/                      # Core Configuration
│   │   │   ├── __init__.py
│   │   │   ├── config.py              # Application configuration
│   │   │   ├── security.py            # Security utilities
│   │   │   ├── logging.py             # Logging configuration
│   │   │   ├── exceptions.py          # Custom exception classes
│   │   │   └── database.py            # Database connection management
│   │   │
│   │   ├── middleware/                # Request/Response Middleware
│   │   │   ├── __init__.py
│   │   │   ├── auth_middleware.py     # Authentication middleware
│   │   │   ├── single_device_middleware.py # Single device enforcement
│   │   │   ├── credit_check_middleware.py # Credit balance validation
│   │   │   ├── admin_auth_middleware.py # Admin authentication
│   │   │   ├── cors_middleware.py     # CORS handling
│   │   │   ├── logging_middleware.py  # Request logging
│   │   │   ├── rate_limit_middleware.py # Rate limiting
│   │   │   └── security_middleware.py # Security headers
│   │   │
│   │   └── utils/                     # Utility Functions
│   │       ├── __init__.py
│   │       ├── constants.py           # Application constants
│   │       ├── helpers.py             # Helper functions
│   │       ├── validators.py          # Custom validators
│   │       ├── formatters.py          # Data formatters
│   │       ├── credit_calculator.py   # Credit calculation utilities
│   │       ├── device_fingerprint.py  # Device identification
│   │       └── encryption.py          # Encryption utilities
│   │
│   ├── tests/                         # Test Suite
│   │   ├── __init__.py
│   │   ├── conftest.py                # Test configuration
│   │   ├── test_main.py               # Main app tests
│   │   ├── api/                       # API endpoint tests
│   │   │   ├── __init__.py
│   │   │   ├── test_auth.py           # Authentication tests
│   │   │   ├── test_users.py          # User management tests
│   │   │   ├── test_products.py       # Product tests
│   │   │   ├── test_analysis.py       # Analysis tests
│   │   │   ├── test_credits.py        # Credit system tests
│   │   │   ├── test_admin.py          # Admin operation tests
│   │   │   ├── test_payments.py       # Payment tests
│   │   │   └── test_devices.py        # Device tests
│   │   ├── services/                  # Service layer tests
│   │   │   ├── __init__.py
│   │   │   ├── test_auth_service.py   # Auth service tests
│   │   │   ├── test_device_service.py # Device service tests
│   │   │   ├── test_credit_service.py # Credit service tests
│   │   │   ├── test_admin_service.py  # Admin service tests
│   │   │   ├── test_azure_blob.py     # Azure integration tests
│   │   │   └── test_ai_services.py    # AI service tests
│   │   ├── unit/                      # Unit tests
│   │   └── integration/               # Integration tests
│   │
│   ├── alembic/                       # Database Migrations
│   │   ├── versions/                  # Migration files
│   │   │   ├── 001_create_users_table.py
│   │   │   ├── 002_create_sessions_table.py
│   │   │   ├── 003_create_user_credits_table.py
│   │   │   ├── 004_create_credit_transactions_table.py
│   │   │   ├── 005_create_pricing_config_table.py
│   │   │   ├── 006_create_admin_users_table.py
│   │   │   ├── 007_create_device_history_table.py
│   │   │   ├── 008_create_usage_tracking_table.py
│   │   │   ├── 009_create_product_analysis_table.py
│   │   │   ├── 010_create_comparisons_table.py
│   │   │   ├── 011_create_security_events_table.py
│   │   │   ├── 012_create_payment_history_table.py
│   │   │   └── 013_create_ai_cache_table.py
│   │   ├── env.py                     # Alembic environment
│   │   ├── script.py.mako             # Migration template
│   │   └── README                     # Migration documentation
│   │
│   ├── static/                        # Static Files
│   │   ├── images/                    # Static images
│   │   └── documents/                 # Documentation files
│   │
│   ├── logs/                          # Application Logs
│   │
│   ├── requirements.txt               # Python dependencies
│   ├── requirements-dev.txt           # Development dependencies
│   ├── .env.example                   # Environment variables template
│   ├── alembic.ini                    # Alembic configuration
│   ├── Dockerfile                     # Docker configuration
│   ├── docker-compose.yml             # Multi-service Docker setup
│   └── pyproject.toml                 # Python project configuration
│
├── docs/                              # Project Documentation
│   ├── api/
│   │   ├── endpoints.md               # API endpoint documentation
│   │   ├── authentication.md         # Auth flow documentation
│   │   ├── credit-system.md           # Credit system documentation
│   │   ├── admin-api.md               # Admin API documentation
│   │   └── payment-integration.md     # Payment flow documentation
│   ├── development/
│   │   ├── setup.md                   # Development setup guide
│   │   ├── contributing.md            # Contribution guidelines
│   │   ├── testing.md                 # Testing guide
│   │   ├── migrations.md              # Database migration guide
│   │   └── debugging.md               # Debugging guide
│   ├── deployment/
│   │   ├── docker.md                  # Docker deployment
│   │   ├── production.md              # Production deployment
│   │   ├── azure.md                   # Azure deployment
│   │   └── monitoring.md              # Monitoring setup
│   └── architecture/
│       ├── overview.md                # System architecture overview
│       ├── database-schema.md         # Database design documentation
│       ├── auth-flow.md               # Authentication flow
│       ├── credit-system.md           # Credit system architecture
│       ├── admin-system.md            # Admin system design
│       ├── single-device.md           # Single device strategy
│       ├── ai-integration.md          # AI services integration
│       └── security.md                # Security considerations
│
├── scripts/                           # Automation Scripts
│   ├── database/
│   │   ├── init_local_db.sql          # Local database initialization
│   │   ├── seed_data.sql              # Sample data for development
│   │   ├── seed_admin_data.sql        # Admin user setup
│   │   └── backup_restore.sh          # Backup/restore utilities
│   ├── deployment/
│   │   ├── build.sh                   # Build script
│   │   ├── deploy.sh                  # Deployment script
│   │   ├── rollback.sh                # Rollback script
│   │   └── health_check.sh            # Health check script
│   └── development/
│       ├── setup_dev.sh               # Development environment setup
│       ├── run_tests.sh               # Test execution script
│       ├── code_quality.sh            # Code quality checks
│       └── generate_docs.sh           # Documentation generation
│
└── .github/                           # GitHub Configuration
    ├── workflows/                     # GitHub Actions
    │   ├── ci.yml                     # Continuous Integration
    │   ├── deploy.yml                 # Deployment workflow
    │   └── security.yml               # Security scanning
    ├── ISSUE_TEMPLATE/                # Issue templates
    └── PULL_REQUEST_TEMPLATE.md       # PR template
```

---

## 🗄️ Updated Database Schema - Credit System

### **Core Tables Overview**
- **users**: User profiles and basic info (removed subscription fields)
- **user_credits**: Real-time credit balance management
- **credit_transactions**: Complete credit transaction history
- **pricing_config**: Admin-controlled pricing and request configurations
- **admin_users**: Admin authentication and permissions
- **active_sessions**: Single-device session management
- **device_history**: Complete device tracking
- **usage_tracking**: Credit-based usage monitoring
- **product_analyses**: AI analysis results
- **product_comparisons**: Multi-product comparisons
- **security_events**: Security audit logging
- **payment_history**: Financial transaction records
- **ai_response_cache**: Cost optimization caching

### **1. Updated Users Table**
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Firebase Integration
    firebase_uid VARCHAR(128) UNIQUE NOT NULL,
    
    -- Authentication Method
    auth_method VARCHAR(20) NOT NULL CHECK (auth_method IN ('phone', 'google')),
    
    -- Basic Profile Information (Minimal Data Collection)
    phone_number VARCHAR(20) UNIQUE, -- Only for phone auth users
    email VARCHAR(255), -- Only for Google auth users, may be null
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INTEGER CHECK (age >= 13 AND age <= 120),
    gender VARCHAR(10) CHECK (gender IN ('male', 'female', 'other', 'prefer_not_to_say')),
    country VARCHAR(3) NOT NULL, -- ISO 3166-1 alpha-3 country code
    
    -- User Preferences (JSONB for flexibility)
    dietary_restrictions JSONB DEFAULT '[]'::jsonb,
    health_goals JSONB DEFAULT '[]'::jsonb,
    notification_preferences JSONB DEFAULT '{
        "push": true,
        "low_credit_alert": true,
        "credit_purchase_success": true
    }'::jsonb,
    app_preferences JSONB DEFAULT '{
        "theme": "light",
        "language": "en",
        "units": "metric"
    }'::jsonb,
    
    -- Account Settings
    preferred_language VARCHAR(5) DEFAULT 'en',
    
    -- Account Status
    is_active BOOLEAN DEFAULT true,
    is_phone_verified BOOLEAN DEFAULT false,
    is_email_verified BOOLEAN DEFAULT false,
    
    -- Privacy & Terms
    privacy_policy_accepted BOOLEAN DEFAULT false,
    terms_accepted BOOLEAN DEFAULT false,
    privacy_policy_version VARCHAR(10),
    terms_version VARCHAR(10),
    
    -- Security & Activity
    last_login_at TIMESTAMPTZ,
    account_locked_until TIMESTAMPTZ,
    failed_login_attempts INTEGER DEFAULT 0,
    
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
CREATE INDEX idx_users_preferences ON users USING GIN (dietary_restrictions, health_goals);
```

### **2. User Credits Table**
```sql
CREATE TABLE user_credits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Credit Balance
    available_credits INTEGER DEFAULT 0 CHECK (available_credits >= 0),
    total_credits_purchased INTEGER DEFAULT 0,
    total_credits_used INTEGER DEFAULT 0,
    
    -- Credit Management
    last_purchase_amount DECIMAL(10,2),
    last_purchase_credits INTEGER,
    last_purchase_date TIMESTAMPTZ,
    
    -- Auto-purchase Settings (if enabled by user)
    auto_purchase_enabled BOOLEAN DEFAULT false,
    auto_purchase_threshold INTEGER DEFAULT 2,
    auto_purchase_amount INTEGER DEFAULT 10,
    
    -- Alert Settings
    low_credit_threshold INTEGER DEFAULT 5,
    last_low_credit_alert_sent TIMESTAMPTZ,
    
    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    -- Ensure one record per user
    CONSTRAINT unique_user_credits UNIQUE (user_id)
);

-- Indexes
CREATE UNIQUE INDEX idx_user_credits_user ON user_credits(user_id);
CREATE INDEX idx_user_credits_low_balance ON user_credits(available_credits) WHERE available_credits <= 5;
CREATE INDEX idx_user_credits_auto_purchase ON user_credits(auto_purchase_enabled, auto_purchase_threshold) WHERE auto_purchase_enabled = true;
```

### **3. Credit Transactions Table**
```sql
CREATE TABLE credit_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Transaction Details
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('purchase', 'usage', 'admin_adjustment', 'refund', 'bonus')),
    credit_amount INTEGER NOT NULL,
    
    -- For purchases: positive credits, For usage: negative credits
    balance_before INTEGER NOT NULL,
    balance_after INTEGER NOT NULL,
    
    -- Transaction Context
    description TEXT,
    reference_id UUID, -- Links to payment, analysis, or admin action
    reference_type VARCHAR(20), -- 'payment', 'analysis', 'admin_action', 'refund'
    
    -- Purchase Information (for purchase transactions)
    purchase_amount DECIMAL(10,2),
    currency VARCHAR(3) DEFAULT 'INR',
    payment_provider VARCHAR(20),
    external_transaction_id VARCHAR(100),
    
    -- Admin Information (for admin adjustments)
    admin_user_id UUID REFERENCES admin_users(id),
    admin_reason TEXT,
    
    -- Analysis Information (for usage transactions)
    analysis_id UUID REFERENCES product_analyses(id),
    
    -- Timestamps
    transaction_date TIMESTAMPTZ DEFAULT NOW(),
    processed_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_credit_transactions_user ON credit_transactions(user_id, transaction_date DESC);
CREATE INDEX idx_credit_transactions_type ON credit_transactions(transaction_type, transaction_date DESC);
CREATE INDEX idx_credit_transactions_reference ON credit_transactions(reference_type, reference_id);
CREATE INDEX idx_credit_transactions_admin ON credit_transactions(admin_user_id) WHERE admin_user_id IS NOT NULL;
```

### **4. Pricing Configuration Table**
```sql
CREATE TABLE pricing_config (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Pricing Settings
    config_name VARCHAR(100) NOT NULL UNIQUE,
    base_price_per_credit DECIMAL(10,2) NOT NULL DEFAULT 10.00,
    currency VARCHAR(3) DEFAULT 'INR',
    
    -- Credit Packages
    available_packages JSONB DEFAULT '[
        {"credits": 10, "price": 100, "bonus_credits": 0, "popular": true},
        {"credits": 25, "price": 240, "bonus_credits": 2, "popular": false},
        {"credits": 50, "price": 450, "bonus_credits": 5, "popular": false},
        {"credits": 100, "price": 850, "bonus_credits": 15, "popular": false}
    ]'::jsonb,
    
    -- Admin Controls
    min_purchase_credits INTEGER DEFAULT 5,
    max_purchase_credits INTEGER DEFAULT 500,
    default_new_user_credits INTEGER DEFAULT 3,
    
    -- Special Offers
    promotional_bonus_percentage DECIMAL(5,2) DEFAULT 0.00,
    promotional_active BOOLEAN DEFAULT false,
    promotional_start_date TIMESTAMPTZ,
    promotional_end_date TIMESTAMPTZ,
    
    -- System Settings
    is_active BOOLEAN DEFAULT true,
    applies_from TIMESTAMPTZ DEFAULT NOW(),
    
    -- Audit Information
    created_by UUID REFERENCES admin_users(id),
    last_modified_by UUID REFERENCES admin_users(id),
    
    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE UNIQUE INDEX idx_pricing_config_name ON pricing_config(config_name);
CREATE INDEX idx_pricing_config_active ON pricing_config(is_active, applies_from);
CREATE INDEX idx_pricing_config_promotional ON pricing_config(promotional_active, promotional_start_date, promotional_end_date);

-- Insert default pricing configuration
INSERT INTO pricing_config (config_name, base_price_per_credit, available_packages, created_at) 
VALUES ('default_pricing', 10.00, '[
    {"credits": 10, "price": 100, "bonus_credits": 0, "popular": true, "display_name": "Starter Pack"},
    {"credits": 25, "price": 240, "bonus_credits": 2, "popular": false, "display_name": "Value Pack"},
    {"credits": 50, "price": 450, "bonus_credits": 5, "popular": false, "display_name": "Power Pack"},
    {"credits": 100, "price": 850, "bonus_credits": 15, "popular": false, "display_name": "Premium Pack"}
]'::jsonb, NOW());
```

### **5. Admin Users Table**
```sql
CREATE TABLE admin_users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Admin Identity
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    
    -- Authentication
    password_hash VARCHAR(255) NOT NULL,
    mfa_secret VARCHAR(32), -- For two-factor authentication
    mfa_enabled BOOLEAN DEFAULT false,
    
    -- Permissions
    role VARCHAR(20) NOT NULL DEFAULT 'admin' CHECK (role IN ('super_admin', 'admin', 'moderator', 'viewer')),
    permissions JSONB DEFAULT '{
        "user_management": true,
        "credit_management": true,
        "pricing_control": true,
        "analytics_access": true,
        "system_settings": false,
        "admin_user_management": false
    }'::jsonb,
    
    -- Access Control
    is_active BOOLEAN DEFAULT true,
    last_login_at TIMESTAMPTZ,
    login_attempts INTEGER DEFAULT 0,
    account_locked_until TIMESTAMPTZ,
    
    -- Session Management
    current_session_token VARCHAR(255),
    session_expires_at TIMESTAMPTZ,
    
    -- Audit Trail
    created_by UUID REFERENCES admin_users(id),
    last_modified_by UUID REFERENCES admin_users(id),
    
    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE UNIQUE INDEX idx_admin_users_email ON admin_users(email);
CREATE UNIQUE INDEX idx_admin_users_username ON admin_users(username);
CREATE INDEX idx_admin_users_active ON admin_users(is_active, role);
CREATE INDEX idx_admin_users_permissions ON admin_users USING GIN (permissions);
```

### **6. Updated Usage Tracking Table**
```sql
CREATE TABLE usage_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    session_id UUID REFERENCES active_sessions(id),
    
    -- Usage Details
    request_type VARCHAR(30) NOT NULL DEFAULT 'analysis',
    usage_date DATE NOT NULL,
    request_sequence INTEGER NOT NULL,
    
    -- Credit Information
    credits_deducted INTEGER DEFAULT 1,
    credits_balance_before INTEGER NOT NULL,
    credits_balance_after INTEGER NOT NULL,
    
    -- Request Context
    request_metadata JSONB DEFAULT '{}'::jsonb,
    
    -- Success/Performance
    status VARCHAR(20) DEFAULT 'success' CHECK (status IN ('success', 'failed', 'insufficient_credits', 'timeout')),
    processing_time_ms INTEGER,
    error_code VARCHAR(50),
    
    -- Cost Tracking
    api_costs JSONB DEFAULT '{
        "google_vision": 0,
        "openai": 0,
        "total": 0
    }'::jsonb,
    
    -- Analysis Reference
    analysis_id UUID REFERENCES product_analyses(id),
    
    -- Timestamps
    request_timestamp TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);

-- Indexes
CREATE INDEX idx_usage_user_date ON usage_tracking(user_id, usage_date, request_sequence);
CREATE INDEX idx_usage_session ON usage_tracking(session_id, request_timestamp);
CREATE INDEX idx_usage_credits ON usage_tracking(credits_deducted, status);
CREATE UNIQUE INDEX idx_usage_user_date_seq ON usage_tracking(user_id, usage_date, request_sequence);
```

### **7. Updated Product Analysis Table**
```sql
CREATE TABLE product_analyses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    session_id UUID REFERENCES active_sessions(id),
    
    -- Credit Information
    credits_used INTEGER DEFAULT 1,
    
    -- Image Information
    image_url VARCHAR(500) NOT NULL,
    image_hash VARCHAR(64) UNIQUE,
    image_size_bytes INTEGER,
    
    -- AI Processing Results
    google_vision_results JSONB NOT NULL,
    openai_analysis JSONB NOT NULL,
    
    -- Extracted Product Information
    product_info JSONB DEFAULT '{
        "brand": null,
        "product_name": null,
        "category": null,
        "ingredients": [],
        "nutrition_facts": {},
        "allergens": []
    }'::jsonb,
    
    -- Health Analysis
    health_score DECIMAL(3,1) CHECK (health_score >= 0 AND health_score <= 10),
    recommendation_type VARCHAR(20) CHECK (recommendation_type IN ('excellent', 'good', 'fair', 'poor', 'avoid')),
    
    -- AI Analysis Details
    benefits JSONB DEFAULT '[]'::jsonb,
    concerns JSONB DEFAULT '[]'::jsonb,
    recommendations JSONB DEFAULT '[]'::jsonb,
    
    -- Analysis Metadata
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0 AND confidence_score <= 1),
    processing_time_ms INTEGER,
    
    -- User Interaction
    user_rating INTEGER CHECK (user_rating >= 1 AND user_rating <= 5),
    user_bookmark BOOLEAN DEFAULT false,
    
    -- Timestamps
    analyzed_at TIMESTAMPTZ DEFAULT NOW(),
    last_accessed_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_analyses_user ON product_analyses(user_id, analyzed_at DESC);
CREATE INDEX idx_analyses_credits ON product_analyses(credits_used, analyzed_at DESC);
CREATE INDEX idx_analyses_health_score ON product_analyses(health_score DESC);
CREATE INDEX idx_analyses_bookmarked ON product_analyses(user_id, user_bookmark) WHERE user_bookmark = true;
CREATE INDEX idx_analyses_product_info ON product_analyses USING GIN (product_info);
```

### **8. Updated Payment History Table**
```sql
CREATE TABLE payment_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id),
    credit_transaction_id UUID REFERENCES credit_transactions(id),
    
    -- Payment Details
    amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'INR',
    payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('pending', 'completed', 'failed', 'refunded')),
    
    -- Credit Information
    credits_purchased INTEGER NOT NULL,
    bonus_credits INTEGER DEFAULT 0,
    total_credits_received INTEGER GENERATED ALWAYS AS (credits_purchased + bonus_credits) STORED,
    
    -- Payment Provider Details
    payment_provider VARCHAR(20) NOT NULL,
    external_payment_id VARCHAR(100) UNIQUE,
    payment_method_type VARCHAR(20),
    
    -- Package Information
    package_name VARCHAR(50),
    package_details JSONB DEFAULT '{}'::jsonb,
    
    -- Promotional Information
    promotional_discount_percentage DECIMAL(5,2) DEFAULT 0.00,
    promotional_code VARCHAR(20),
    
    -- Payment Metadata
    payment_details JSONB DEFAULT '{}'::jsonb,
    
    -- Timestamps
    initiated_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_payment_user ON payment_history(user_id, completed_at DESC);
CREATE INDEX idx_payment_status ON payment_history(payment_status, initiated_at);
CREATE INDEX idx_payment_credits ON payment_history(credits_purchased, completed_at DESC);
CREATE UNIQUE INDEX idx_payment_external ON payment_history(external_payment_id);
```

---

## 💰 Credit System Architecture

### **Credit Management Flow**
```
1. User registers → Gets 3 free credits (configurable by admin)
2. User wants analysis → Check credit balance
3. If sufficient credits → Deduct 1 credit → Process analysis
4. If insufficient credits → Show purchase options
5. User purchases credits → Payment processed → Credits added
6. Admin can adjust credits → Audit trail maintained
```

### **Pricing Flexibility**
- **Base Rate**: ₹10 per credit (admin configurable)
- **Package Deals**: Bulk purchase bonuses (admin controlled)
- **Promotional Offers**: Temporary bonus percentages
- **New User Credits**: Default 3 free credits (admin adjustable)
- **Minimum/Maximum**: Purchase limits (admin controlled)

### **Admin Control Features**
- **Dynamic Pricing**: Adjust credit costs without code changes
- **Package Management**: Create/modify credit packages
- **User Credit Adjustment**: Add/remove credits with audit trail
- **Promotional Campaigns**: Time-limited bonus offers
- **Usage Analytics**: Detailed credit usage reports
- **Bulk Operations**: Mass credit adjustments for user groups

---

## 🔄 API Endpoints - Credit System

### **Credit Management Endpoints**
- `GET /api/v1/credits/balance` - Get user's current credit balance
- `GET /api/v1/credits/history` - Credit transaction history
- `GET /api/v1/credits/packages` - Available credit packages
- `POST /api/v1/credits/purchase` - Purchase credit package
- `POST /api/v1/credits/check-sufficient` - Check if user has enough credits

### **Admin Credit Endpoints**
- `GET /api/v1/admin/credits/users` - List all users with credit info
- `POST /api/v1/admin/credits/adjust` - Adjust user credits
- `GET /api/v1/admin/credits/analytics` - Credit usage analytics
- `PUT /api/v1/admin/pricing/config` - Update pricing configuration
- `GET /api/v1/admin/pricing/packages` - Manage credit packages

### **Payment Integration Endpoints**
- `POST /api/v1/payments/initiate` - Start payment process
- `POST /api/v1/payments/verify` - Verify payment completion
- `GET /api/v1/payments/history` - User payment history
- `POST /api/v1/payments/webhook` - Payment provider webhooks

### **Analysis Endpoints (Updated)**
- `POST /api/v1/analysis/upload` - Upload and analyze (requires 1 credit)
- `GET /api/v1/analysis/{id}` - Get analysis by ID (no credit required)
- `GET /api/v1/analysis/history` - User's analysis history (no credit required)
- `POST /api/v1/analysis/compare` - Compare products (requires 1 credit per comparison)

---

## 🎛️ Admin Panel Features

### **User Management**
- **User List**: Search, filter, and view all users
- **Credit Management**: View balances, adjust credits, transaction history
- **Account Actions**: Activate/deactivate users, reset passwords
- **Usage Analytics**: Individual user usage patterns

### **Credit System Control**
- **Pricing Configuration**: Adjust base credit price
- **Package Management**: Create/edit credit packages
- **Promotional Campaigns**: Set up time-limited bonuses
- **Bulk Credit Operations**: Mass credit adjustments
- **Financial Reports**: Revenue, credit sales, usage analytics

### **System Analytics**
- **Revenue Dashboard**: Daily/monthly revenue tracking
- **Usage Patterns**: Peak usage times, popular features
- **Credit Economics**: Cost per analysis, profit margins
- **User Behavior**: Purchase patterns, credit usage trends

### **Configuration Management**
- **Pricing Updates**: Real-time price adjustments
- **Feature Toggles**: Enable/disable features
- **API Limits**: Adjust system-wide limits
- **Promotional Settings**: Manage offers and discounts

---

## 🚀 Setup Commands (Updated)

### **Environment Configuration**

#### **Backend (.env) - Updated**
```env
# Database Configuration
DATABASE_URL=postgresql://imaro_user:imaro_pass@localhost:5432/imaro_db

# Redis Configuration
REDIS_URL=redis://localhost:6379

# Azure Storage
AZURE_STORAGE_ACCOUNT_NAME=your_storage_account
AZURE_STORAGE_ACCOUNT_KEY=your_storage_key
AZURE_STORAGE_CONTAINER_NAME=imaro-images

# AI APIs
GOOGLE_VISION_CREDENTIALS=path/to/google-credentials.json
OPENAI_API_KEY=your_openai_api_key

# Firebase Admin
FIREBASE_CREDENTIALS=path/to/firebase-admin-sdk.json

# Security
SECRET_KEY=your_secret_key_change_in_production
ALGORITHM=HS256
ADMIN_SECRET_KEY=your_admin_secret_key

# Payment Processing
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_secret
RAZORPAY_WEBHOOK_SECRET=your_webhook_secret

# Credit System Configuration
DEFAULT_NEW_USER_CREDITS=3
CREDIT_COST_RUPEES=10
MIN_PURCHASE_CREDITS=5
MAX_PURCHASE_CREDITS=500

# Admin Configuration
ADMIN_EMAIL=admin@imaro.app
ADMIN_PASSWORD=change_in_production
SUPER_ADMIN_EMAIL=superadmin@imaro.app

# Environment
ENVIRONMENT=development
DEBUG=true
```

### **Database Migration (Updated)**
```bash
cd backend
source venv/bin/activate

# Create new migration for credit system
alembic revision --autogenerate -m "implement credit system"

# Apply migrations
alembic upgrade head

# Seed admin user and default pricing
python scripts/seed_admin_data.py
```

### **Admin User Setup**
```bash
# Create initial admin user
python scripts/create_admin.py --email admin@imaro.app --password secure_password --role super_admin

# Verify admin setup
python scripts/verify_admin.py
```

---

## 🧪 Testing Credit System

### **Credit Flow Tests**
```bash
# Test credit purchase flow
pytest tests/api/test_credits.py::test_purchase_credits -v

# Test analysis with credits
pytest tests/api/test_analysis.py::test_analysis_with_sufficient_credits -v

# Test insufficient credits scenario
pytest tests/api/test_analysis.py::test_analysis_insufficient_credits -v

# Test admin credit adjustment
pytest tests/api/test_admin.py::test_admin_adjust_user_credits -v
```

### **Payment Integration Tests**
```bash
# Test Razorpay integration
pytest tests/integration/test_razorpay.py -v

# Test webhook handling
pytest tests/api/test_payments.py::test_webhook_credit_addition -v
```

---

## 📊 Monitoring Credit System

### **Key Metrics**
```sql
-- Daily revenue tracking
SELECT 
    DATE(completed_at) as date,
    COUNT(*) as transactions,
    SUM(amount) as revenue,
    SUM(credits_purchased) as credits_sold
FROM payment_history 
WHERE payment_status = 'completed' 
    AND completed_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY DATE(completed_at)
ORDER BY date DESC;

-- User credit distribution
SELECT 
    CASE 
        WHEN available_credits = 0 THEN '0 credits'
        WHEN available_credits BETWEEN 1 AND 5 THEN '1-5 credits'
        WHEN available_credits BETWEEN 6 AND 15 THEN '6-15 credits'
        WHEN available_credits BETWEEN 16 AND 50 THEN '16-50 credits'
        ELSE '50+ credits'
    END as credit_range,
    COUNT(*) as user_count
FROM user_credits
GROUP BY credit_range;

-- Credit usage patterns
SELECT 
    DATE(transaction_date) as date,
    SUM(CASE WHEN transaction_type = 'usage' THEN ABS(credit_amount) ELSE 0 END) as credits_used,
    SUM(CASE WHEN transaction_type = 'purchase' THEN credit_amount ELSE 0 END) as credits_purchased,
    COUNT(DISTINCT user_id) as active_users
FROM credit_transactions 
WHERE transaction_date >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY DATE(transaction_date)
ORDER BY date DESC;

-- Admin activity tracking
SELECT 
    au.username,
    COUNT(*) as adjustments,
    SUM(ct.credit_amount) as total_credits_adjusted
FROM credit_transactions ct
JOIN admin_users au ON ct.admin_user_id = au.id
WHERE ct.transaction_type = 'admin_adjustment'
    AND ct.transaction_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY au.username;
```

---

## 🔐 Security Considerations

### **Credit System Security**
- **Transaction Integrity**: All credit operations are atomic
- **Audit Trail**: Complete history of all credit transactions
- **Admin Authentication**: Multi-factor authentication for admin users
- **Payment Security**: PCI DSS compliant payment processing
- **Fraud Prevention**: Rate limiting on credit purchases
- **Balance Validation**: Real-time credit balance verification

### **Admin Security**
- **Role-based Access**: Granular permission system
- **Session Management**: Secure admin session handling
- **Activity Logging**: All admin actions logged with timestamps
- **IP Restrictions**: Optional IP-based access control
- **Password Policies**: Strong password requirements for admin users

---

## 💡 Business Model Benefits

### **Revenue Advantages**
- **Predictable Income**: Pay-per-use model with immediate revenue
- **Flexible Pricing**: Easy price adjustments based on demand
- **Upselling Opportunities**: Bulk packages with bonus credits
- **Lower Churn**: Users only pay when they use the service
- **Cash Flow**: Immediate payment upon credit purchase

### **User Experience Benefits**
- **Cost Control**: Users only pay for what they use
- **No Commitment**: No monthly subscription pressure
- **Transparent Pricing**: Clear cost per analysis
- **Flexible Usage**: Buy credits when needed
- **Budget-Friendly**: Start with small credit purchases

### **Operational Benefits**
- **Admin Control**: Dynamic pricing without code changes
- **Analytics**: Detailed usage and revenue tracking
- **Scalability**: Easy to adjust pricing for different markets
- **Promotional Flexibility**: Time-limited offers and bonuses
- **User Management**: Granular control over user credits

---

**Built with ❤️ by the Imaro Team**

*Making healthy choices easier, one credit at a time.*
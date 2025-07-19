# Application Constants

# User constraints
MIN_AGE = 13
MAX_AGE = 120
MIN_NAME_LENGTH = 1
MAX_NAME_LENGTH = 50

# Gender options
GENDER_OPTIONS = ["male", "female", "other", "prefer_not_to_say"]

# Authentication methods
AUTH_METHODS = ["phone", "google"]

# Token types
TOKEN_TYPE_ACCESS = "access"
TOKEN_TYPE_REFRESH = "refresh"

# Privacy and terms versions
CURRENT_PRIVACY_VERSION = "1.0"
CURRENT_TERMS_VERSION = "1.0"

# Response messages
MSG_OTP_SENT = "OTP sent successfully"
MSG_OTP_INVALID = "Invalid OTP code"
MSG_USER_CREATED = "User created successfully"
MSG_PROFILE_COMPLETED = "Profile completed successfully"
MSG_PROFILE_UPDATED = "Profile updated successfully"
MSG_ACCOUNT_DELETED = "Account deleted successfully"
MSG_ACCOUNT_DEACTIVATED = "Account deactivated successfully"
MSG_LOGGED_OUT = "Successfully logged out"

# Error messages
ERR_INVALID_PHONE = "Invalid phone number format. Use international format: +1234567890"
ERR_INVALID_AGE = f"Age must be between {MIN_AGE} and {MAX_AGE}"
ERR_INVALID_GENDER = f"Gender must be one of: {', '.join(GENDER_OPTIONS)}"
ERR_INVALID_COUNTRY = "Country must be 3-letter ISO code (e.g., USA, IND, GBR)"
ERR_INVALID_NAME = f"Name must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters"
ERR_INVALID_TOKEN = "Invalid or expired token"
ERR_USER_NOT_FOUND = "User not found"
ERR_PROFILE_ALREADY_COMPLETED = "Profile is already completed"
ERR_PROFILE_NOT_COMPLETED = "Profile must be completed to access this resource"
ERR_ACCOUNT_DEACTIVATED = "User account is deactivated"

import re
from typing import Optional

def validate_phone_number(phone: str) -> bool:
    """
    Validate phone number format
    
    Expects international format: +[country_code][number]
    Examples: +1234567890, +919876543210
    """
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone))

def validate_email(email: str) -> bool:
    """
    Validate email format
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_country_code(country: str) -> bool:
    """
    Validate 3-letter ISO country code
    """
    return len(country) == 3 and country.isupper() and country.isalpha()

def validate_age(age: int) -> bool:
    """
    Validate age range
    """
    return 13 <= age <= 120

def validate_gender(gender: str) -> bool:
    """
    Validate gender options
    """
    valid_genders = ["male", "female", "other", "prefer_not_to_say"]
    return gender in valid_genders

def validate_name(name: str) -> bool:
    """
    Validate name length and characters
    """
    if not name or not isinstance(name, str):
        return False
    
    name = name.strip()
    return 1 <= len(name) <= 50

def validate_otp_code(otp: str) -> bool:
    """
    Validate OTP code format (6 digits)
    """
    pattern = r'^\d{6}$'
    return bool(re.match(pattern, otp))

def sanitize_phone_number(phone: str) -> str:
    """
    Sanitize phone number by removing spaces and special characters
    """
    # Remove all non-digit characters except +
    cleaned = re.sub(r'[^\d+]', '', phone)
    
    # Ensure it starts with +
    if not cleaned.startswith('+'):
        cleaned = '+' + cleaned
    
    return cleaned

def format_name(name: str) -> str:
    """
    Format name by capitalizing first letter of each word
    """
    if not name:
        return ""
    
    return ' '.join(word.capitalize() for word in name.strip().split())

def mask_phone_number(phone: str) -> str:
    """
    Mask phone number for display purposes
    Example: +1234567890 -> +123****7890
    """
    if not phone or len(phone) < 8:
        return phone
    
    if phone.startswith('+'):
        country_code = phone[:4]  # +123
        ending = phone[-4:]       # 7890
        masked_middle = '*' * (len(phone) - 8)
        return f"{country_code}{masked_middle}{ending}"
    
    return phone

def mask_email(email: str) -> str:
    """
    Mask email for display purposes
    Example: user@example.com -> u***@example.com
    """
    if not email or '@' not in email:
        return email
    
    username, domain = email.split('@', 1)
    if len(username) <= 1:
        return email
    
    masked_username = username[0] + '*' * (len(username) - 1)
    return f"{masked_username}@{domain}"

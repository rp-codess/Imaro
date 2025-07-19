import pytest
from fastapi.testclient import TestClient

def test_health_check(client: TestClient):
    """Test health check endpoint"""
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data

def test_root_endpoint(client: TestClient):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data

def test_send_phone_otp(client: TestClient):
    """Test send phone OTP endpoint"""
    response = client.post(
        "/api/v1/auth/phone/send-otp",
        json={"phone_number": "+1234567890"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True

def test_send_phone_otp_invalid_format(client: TestClient):
    """Test send phone OTP with invalid phone number"""
    response = client.post(
        "/api/v1/auth/phone/send-otp",
        json={"phone_number": "invalid-phone"}
    )
    assert response.status_code == 422  # Validation error

def test_verify_phone_otp_demo(client: TestClient):
    """Test verify phone OTP with demo code"""
    response = client.post(
        "/api/v1/auth/phone/verify-otp",
        json={
            "phone_number": "+1234567890",
            "otp_code": "123456"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"

def test_verify_phone_otp_invalid_code(client: TestClient):
    """Test verify phone OTP with invalid code"""
    response = client.post(
        "/api/v1/auth/phone/verify-otp",
        json={
            "phone_number": "+1234567890",
            "otp_code": "000000"
        }
    )
    assert response.status_code == 400

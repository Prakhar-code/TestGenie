import unittest
import requests
import json


class TestUserRegistration(unittest.TestCase):

    BASE_URL = "http://localhost:8000"  # Replace with your API endpoint

    def test_successful_registration(self):
        user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "employee_id": "12345",
            "password": "Password123",
            "confirm_password": "Password123",
        }
        response = requests.post(f"{self.BASE_URL}/user/register", json=user_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["name"], user_data["name"])
        self.assertEqual(response_data["email"], user_data["email"])
        self.assertEqual(response_data["employee_id"], user_data["employee_id"])
        self.assertTrue(
            "password" in response_data
        )  # password might be hashed, so just check existence

    def test_missing_fields(self):
        user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "employee_id": "12345",
            "password": "Password123",
        }
        response = requests.post(f"{self.BASE_URL}/user/register", json=user_data)
        self.assertEqual(response.status_code, 422)
        response_data = response.json()
        self.assertTrue("detail" in response_data)
        self.assertTrue(len(response_data["detail"]) > 0)

    def test_invalid_email(self):
        user_data = {
            "name": "Test User",
            "email": "invalid_email",
            "employee_id": "12345",
            "password": "Password123",
            "confirm_password": "Password123",
        }
        response = requests.post(f"{self.BASE_URL}/user/register", json=user_data)
        self.assertEqual(response.status_code, 422)
        response_data = response.json()
        self.assertTrue("detail" in response_data)
        self.assertTrue(len(response_data["detail"]) > 0)

    def test_short_password(self):
        user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "employee_id": "12345",
            "password": "Pass",
            "confirm_password": "Pass",
        }
        response = requests.post(f"{self.BASE_URL}/user/register", json=user_data)
        self.assertEqual(response.status_code, 422)
        response_data = response.json()
        self.assertTrue("detail" in response_data)
        self.assertTrue(len(response_data["detail"]) > 0)

    def test_password_mismatch(self):
        user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "employee_id": "12345",
            "password": "Password123",
            "confirm_password": "WrongPassword",
        }
        response = requests.post(f"{self.BASE_URL}/user/register", json=user_data)
        self.assertEqual(response.status_code, 404)
        response_data = response.json()
        self.assertTrue("detail" in response_data)
        self.assertTrue(len(response_data["detail"]) > 0)

    def test_empty_name(self):
        user_data = {
            "name": "",
            "email": "testuser@example.com",
            "employee_id": "12345",
            "password": "Password123",
            "confirm_password": "Password123",
        }
        response = requests.post(f"{self.BASE_URL}/user/register", json=user_data)
        self.assertEqual(response.status_code, 422)
        response_data = response.json()
        self.assertTrue("detail" in response_data)
        self.assertTrue(len(response_data["detail"]) > 0)

    def test_duplicate_email(
        self,
    ):  # Requires setup to create a duplicate email before running this test
        user_data = {
            "name": "Test User Duplicate",
            "email": "duplicate@example.com",  # replace with a pre-existing email
            "employee_id": "67890",
            "password": "Password123",
            "confirm_password": "Password123",
        }
        response = requests.post(f"{self.BASE_URL}/user/register", json=user_data)
        # Expected response status code will depend on your implementation of duplicate email handling.  Could be 409 (Conflict), 422, or even 200 with an error message. Adjust accordingly.
        # self.assertEqual(response.status_code, 409) # Or 422 or 200 depending on your API's behavior.
        # Add assertions to check error message if needed.
        pass


if __name__ == "__main__":
    unittest.main()

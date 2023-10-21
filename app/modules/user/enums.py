from enum import Enum


class UserEnum(str, Enum):
    """
    Enum for messages sent by the server.
    """

    USER_NOT_FOUND = "User not found"
    INVALID_PASSWORD = "Invalid password"
    USER_NOT_UPDATED = "User not updated"
    EMAIL_ALREADY_EXIST = "Email already exists"
    ERROR_CREATE_USER = "Error when try create user"

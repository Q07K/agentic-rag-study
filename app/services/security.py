import secrets

from cryptography.fernet import Fernet


def generate_api_key(prefix: str = "kg_", nbytes: int = 32) -> str:
    """URL-safe한 API 키를 생성합니다.

    Parameters
    ----------
    prefix : str, optional
        키 앞에 붙일 접두사, by default "kg_"
    nbytes : int, optional
        키 생성에 사용할 랜덤 바이트 수, by default 32

    Returns
    -------
    str
        지정된 접두사가 포함된 생성된 API 키.
    """
    key = secrets.token_urlsafe(nbytes=nbytes)
    return f"{prefix}{key}"


def encrypt_value(value: str, key: bytes) -> str:
    f = Fernet(key)
    encrypted = f.encrypt(value.encode())
    return encrypted.decode()


def decrypt_value(token: str, key: bytes) -> str:
    f = Fernet(key)
    decrypted = f.decrypt(token.encode())
    return decrypted.decode()


if __name__ == "__main__":
    # 함수를 호출하여 새로운 키를 생성합니다.
    new_key = generate_api_key()
    print(f"생성된 API 키: {new_key}")
    print(f"키 길이 (접두사 포함): {len(new_key)}")

from argon2 import PasswordHasher

class passwordHashing:

    hasher = PasswordHasher(
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,
        salt_len=16
    )

def hashPassword(password:str):
    return passwordHashing.hasher.hash(password)

def checkHashedPassword(password:str , hashedPassword : str):
    return passwordHashing.hasher.verify(hashedPassword,password)

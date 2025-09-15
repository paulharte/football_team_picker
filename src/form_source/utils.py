import os


def load_env(path: str = ".env") -> dict[str, str]:
    """Lightweight .env parser without dependencies."""
    env_vars = {}
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found")
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            env_vars[key.strip()] = value.strip()
    return env_vars
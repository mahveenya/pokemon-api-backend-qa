def extract_id_from_url(url: str) -> int:
    return int(url.rstrip("/").split("/")[-1])

from __future__ import annotations

from pathlib import Path
from azure.storage.blob import BlobServiceClient


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        key, value = s.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def main() -> int:
    env_path = Path(r"C:\Users\javier.castaneda\botsquad\BPA_DataCentric\Parametros\Onnet\.env")
    env = load_env(env_path)

    account_url = env.get("AZURE_BLOB_ACCOUNT_URL")
    sas_token = env.get("AZURE_BLOB_SAS_TOKEN")
    container = env.get("AZURE_BLOB_CONTAINER") or "site-reporting"

    if not account_url or not sas_token:
        raise SystemExit("Missing AZURE_BLOB_ACCOUNT_URL or AZURE_BLOB_SAS_TOKEN in Onnet env")

    names = [
        "1070_TRANSACCIONES_ONNET.csv",
        "1070_TRANSACCIONES_ONNET_ticketes.csv",
        "VW_n8n_chat_histories_classfication.csv",
        "VW_n8n_chat_histories_textual_all.csv",
        "VW_n8n_chat_history_textual.csv",
        "VW_n8n_chat_history_textual_analisis_respuestas.csv",
        "VW_n8n_chat_history_textual_analisis_WordCloud_2.csv",
        "VW_n8n_chat_user_banned.csv",
    ]

    blob_service = BlobServiceClient(account_url=account_url, credential=sas_token)
    container_client = blob_service.get_container_client(container)

    print("blob,last_modified_utc")
    for name in names:
        props = container_client.get_blob_client(name).get_blob_properties()
        print(f"{name},{props.last_modified}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

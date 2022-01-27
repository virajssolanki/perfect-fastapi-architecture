aerich init -t app.main.aerich_config
aerich init-db
aerich upgrade
aerich migrate

uvicorn app.main:app --reload
aerich init -t app.main.aerich_config
aerich init-db
aerich upgrade

uvicorn app.main:app --reload
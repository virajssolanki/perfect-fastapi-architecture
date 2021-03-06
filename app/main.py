from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.starlette import register_tortoise

from app.api import api_router
# from app.core.middleware import httpsredirect
# from app.core.exception import APIException, on_api_exception
from app.core.config import get_app_settings

def get_application() -> FastAPI:
    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)


    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts, allow_credentials=True,
        allow_methods=["*"], allow_headers=["*"],
    )

    # application.add_middleware(
    #     httpsredirect.HTTPSRedirectMiddleware,
    # )

    # application.add_exception_handler(
    #     APIException, on_api_exception
    #     )

    application.include_router(api_router, prefix=settings.api_prefix)
    register_tortoise(
        application,
        config=settings.tortoise_config,
        generate_schemas=settings.generate_schemas,
    )
    return application


app = get_application()
aerich_config = get_app_settings().tortoise_config


# aerich init -t app.main.aerich_config
# aerich init-db
# aerich upgrade

# uvicorn app.main:app --reload
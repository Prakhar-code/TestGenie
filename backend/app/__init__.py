from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import generate_test_route, optimize_contract_route, ai_chatbot_route


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(generate_test_route.app)
    app.include_router(optimize_contract_route.app)
    app.include_router(ai_chatbot_route.app)

    return app

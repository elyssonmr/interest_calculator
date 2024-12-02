from fastapi import FastAPI

from web.routes import router

app = FastAPI(
    title='Simulador de Renda Fixa',
    description='API para simulação de investimentos em renda fixa',
)

app.include_router(router)

from api.controllers.market_controllers import router as MarketRouter
from api.controllers.rules_controller import router as RulesRouter

def init_routes(app):
    app.include_router(MarketRouter, prefix="/market-prices", tags=["Market"])
    return app

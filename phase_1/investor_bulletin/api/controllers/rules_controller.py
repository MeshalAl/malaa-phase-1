from fastapi import APIRouter
from resources.alerts.alert_service import create_new_alert

router = APIRouter()

@router.get('/')
def create_alert(name, threshold, symbol):
    return create_new_alert(name, threshold, symbol)

from fastapi import APIRouter
from resources.alerts.alert_service import create_new_alert

router = APIRouter()

@router.post('/alert-rules')
def create_alert_route(name, threshold, symbol):
    return create_new_alert(name, threshold, symbol)

@router.patch('/alert-rules/{id}')
def update_alert_route(id, name, threshold, symbol):
    return update_alert(id, name, threshold, symbol)

@router.delete('/alert-rules/{id}')
def delete_alert_route(id):
    return delete_alert(id)

@router.get('/alert-rules')
def get_alert_rules_route():
    return get_alert_rules()

@router.get('/')
def get_alerts_route():
    return get_alerts()

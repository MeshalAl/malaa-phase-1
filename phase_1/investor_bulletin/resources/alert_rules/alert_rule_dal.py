""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""

from resources.alert_rules.alert_rule_schema import AlertRuleCreate
from db.models import AlertRule

def create_alert_rule( rule: AlertRuleCreate, session ):
    new_rule = AlertRule(**rule.model_dump())
    session.add(new_rule)
    session.commit()

def get_alert_rules(session):
    return session.query(AlertRule).all()

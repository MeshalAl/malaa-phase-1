""" Alert Rule Model """
from db.models.model_base import Base
# use schema to construct the model
class AlertRule(Base):
    __tablename__ = "alert-rules"

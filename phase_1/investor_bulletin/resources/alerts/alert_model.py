""" Alert Model """

"""- [ ] **Setup your ORM models (RuleAlerts, Alerts) and connect them with the DB server**
alerts should have the following properties `name, threshold price, symbol`"""

from db.models.model_base import Base
class Alert(Base):
    __tablename__ = "alerts"
    name = Column(String(50), nullable=False)
    threshhold_price = Column(Float, nullable=False)
    symbol = Column(String(50), nullable=False)

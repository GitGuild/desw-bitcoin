from desw import CFG, ses, logger
from sqlalchemy_models import wallet as wm

hwb = wm.HWBalance(0, 0, 'BTC', 'bitcoin')
ses.add(hwb)
try:
    ses.commit()
except Exception as ie:
    ses.rollback()
    ses.flush()


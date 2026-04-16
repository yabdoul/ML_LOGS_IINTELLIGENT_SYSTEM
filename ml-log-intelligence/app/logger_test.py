from app.config import settings
from app.logger import get_logger

logger = get_logger(__name__)

print("DB:", settings.db_url)

logger.info("System started")
logger.error("Test error log")

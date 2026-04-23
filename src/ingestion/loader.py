import pandas as pd
from pathlib import Path

from core.logger import get_logger
from core.paths import RAW_DATA_DIR

logger = get_logger(__name__)


def load_raw_data(filename: str) -> pd.DataFrame:
    """
    Load raw dataset from RAW_DATA_DIR.

    Args:
        filename (str): Name of the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """

    file_path = RAW_DATA_DIR / filename

    if not file_path.exists():
        logger.error(f"Dataset not found at: {file_path}")
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    logger.info(f"Loading dataset from: {file_path}")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        logger.exception("Failed to read CSV file")
        raise

    if df.empty:
        logger.error("Loaded dataset is empty")
        raise ValueError("Dataset is empty")

    logger.info(f"Dataset loaded successfully | shape={df.shape}")

    return df

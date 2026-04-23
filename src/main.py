from ingestion.loader import load_data
from ingestion.validator import validate_schema
from ingestion.versioning import generate_dataset_id, compute_hash
from preprocessing.splitter import split_dataset
from preprocessing.stats import generate_dataset_report
from artifacts.writer import write_artifacts
from core.logger import get_logger

logger = get_logger(__name__)


def run_pipeline():
    logger.info("Starting ML data pipeline")

    try:
        logger.info("Loading raw dataset")
        df = load_data()

        logger.info("Validating dataset schema")
        validate_schema(df)

        logger.info("Generating dataset metadata")
        dataset_id = generate_dataset_id()
        data_hash = compute_hash(df)

        logger.info("Splitting dataset into train/val/test")
        train_df, val_df, test_df = split_dataset(df)

        logger.info("Generating dataset report")
        report = generate_dataset_report(
            df=df,
            train_df=train_df,
            val_df=val_df,
            test_df=test_df,
            dataset_id=dataset_id,
            data_hash=data_hash,
        )

        logger.info("Writing artifacts to disk")
        write_artifacts(
            train_df=train_df,
            val_df=val_df,
            test_df=test_df,
            report=report,
            dataset_id=dataset_id,
        )

        logger.info(f"Pipeline completed successfully | dataset_id={dataset_id}")

    except Exception as e:
        logger.exception(f"Pipeline failed: {str(e)}")
        raise


def main():
    run_pipeline()


if __name__ == "__main__":
    main()

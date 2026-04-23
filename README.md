# ML Detection System (Production-Style Pipeline)

A modular machine learning pipeline for detecting anomalies / fraud-like
behavior in structured tabular data.

This project focuses on building a **production-inspired ML system
architecture**, not just model training.

------------------------------------------------------------------------

## What this project demonstrates

This repository is designed to showcase:

-   End-to-end ML pipeline design (raw → validated → processed → output)
-   Data validation layer (schema enforcement before processing)
-   Modular engineering structure (not notebook-based workflows)
-   Reproducible pipeline execution
-   Logging + traceability for debugging and monitoring readiness

------------------------------------------------------------------------

## Problem Type

Currently implemented on a **credit card transaction dataset**,
simulating:

-   Fraud detection style classification problems
-   Real-world tabular ML pipelines
-   Data integrity + schema validation before modeling

------------------------------------------------------------------------

## System Architecture

    Raw Data
    ↓
    Data Loader (safe ingestion)
    ↓
    Schema Validator (data contract enforcement)
    ↓
    Preprocessing (splitting + feature preparation)
    ↓
    Artifacts + Reports + Logs

------------------------------------------------------------------------

## Project Structure

    src/
    ├── ingestion/        # Data loading + validation
    ├── preprocessing/    # Data splitting + transformations
    ├── core/             # Logging + paths utilities
    ├── main.py           # Pipeline entry point

    configs/
    ├── schema.json       # Data contract definition

    data/
    ├── raw/              # Input datasets
    ├── processed/        # Intermediate outputs
    ├── artifacts/        # Final outputs

    logs/
    reports/
    tests/

------------------------------------------------------------------------

## How to Run

``` bash
pip install -r requirements.txt
python src/main.py
```

------------------------------------------------------------------------

## Key Features

### 1. Data Validation Layer

Ensures dataset correctness before processing: - Required columns
check - Target column verification - Basic data sanity checks

------------------------------------------------------------------------

### 2. Modular Pipeline Design

Each stage is independent: - ingestion - validation - preprocessing

------------------------------------------------------------------------

### 3. Logging & Observability

-   Console + file logging
-   Structured log format for debugging pipeline runs

Logs are stored in:

    logs/pipeline.log

------------------------------------------------------------------------

## Example Use Case

Can be extended to: - Fraud detection systems - User behavior anomaly
detection - Risk scoring pipelines - Tabular ML classification tasks

------------------------------------------------------------------------

## Design Philosophy

-   Clarity over complexity
-   Reproducibility over experimentation noise
-   Debuggability over abstraction layers

------------------------------------------------------------------------

## Future Improvements

-   Model training module
-   MLflow experiment tracking
-   FastAPI inference service
-   CI/CD pipeline integration
-   Data drift monitoring

------------------------------------------------------------------------

## Author Notes

Built as part of a transition toward production ML engineering systems
design.
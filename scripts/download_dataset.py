from __future__ import annotations

import logging
import shutil
from pathlib import Path

import kagglehub


def _setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
    )


def _find_csv_file(download_path: Path) -> Path:
    if download_path.is_file() and download_path.suffix.lower() == ".csv":
        return download_path

    if download_path.is_dir():
        csv_files = sorted(download_path.rglob("*.csv"))
        if csv_files:
            return csv_files[0]

    raise FileNotFoundError(f"No CSV files found at {download_path}")


def download_dataset(output_dir: Path) -> Path:
    logging.info("Downloading dataset from Kaggle...")
    dataset_path = kagglehub.dataset_download("ruchi798/data-science-job-salaries")
    download_path = Path(dataset_path)

    logging.info("Download completed: %s", download_path)
    csv_path = _find_csv_file(download_path)

    output_dir.mkdir(parents=True, exist_ok=True)
    target_path = output_dir / csv_path.name
    shutil.copy2(csv_path, target_path)

    logging.info("Dataset saved to: %s", target_path)
    return target_path


def main() -> None:
    _setup_logging()
    raw_dir = Path("data") / "raw"
    download_dataset(raw_dir)


if __name__ == "__main__":
    main()

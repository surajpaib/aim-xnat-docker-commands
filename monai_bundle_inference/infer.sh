# Bundle script to run inference on custom data
python -m monai.bundle run inference \
  --meta_file configs/metadata.json \
  --config_file configs/inference.yaml \
  --logging_file configs/logging.conf \
  --datadir /app/data/input \
  --output_dir /app/data/output
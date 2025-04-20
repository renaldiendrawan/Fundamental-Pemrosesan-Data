import logging
from utils.extract import extract_product_data
from utils.transform import transform_product_data
from utils.load import load_to_csv, load_to_google_sheets, load_to_postgresql

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ganti dengan ID Sheet yang benar dari Google Sheets kamu
GOOGLE_SHEET_ID = 'your_google_sheet_id'

# Ganti dengan database URL PostgreSQL kamu
POSTGRESQL_URL = 'postgresql://username:password@localhost:5432/fashionstudio'

def main():
    logging.info("Mulai proses ETL...")

    # Extract
    raw_data = extract_product_data()
    if raw_data.empty:
        logging.warning("Data kosong. Proses dihentikan.")
        return

    # Transform
    clean_data = transform_product_data(raw_data)

    # Load
    load_to_csv(clean_data)
    load_to_google_sheets(clean_data, GOOGLE_SHEET_ID)
    load_to_postgresql(clean_data, POSTGRESQL_URL)

    logging.info("Proses ETL selesai.")

if __name__ == '__main__':
    main()

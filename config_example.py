"""
Example configuration pattern for the analytics system.
This file demonstrates the use of environment variables for secure configuration. Production values are excluded.
"""

import os

DB_HOST = os.getenv("DB_HOST", "REDACTED")
DB_NAME = os.getenv("DB_NAME", "REDACTED")
DB_USER = os.getenv("DB_USER", "REDACTED")


# These values never change, thus they can be used as constants.
EBAY_FEE_RATE = float(os.getenv("EBAY_FEE_RATE", "0.135"))
SALES_TAX_RATE = float(os.getenv("SALES_TAX_RATE", "0.08"))
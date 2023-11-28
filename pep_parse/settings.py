from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

PEP_SPIDER_ALLOWED_URL = 'peps.python.org'
"""Links from which parser can parse data.
In this project only one link is used so spider can parser data
from this link only.
"""

PEP_SPIDER_START_URL = 'https://peps.python.org/'
"""List of links from which the spider starts parsing data."""

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
"""Folder's name to save data after parsing."""

RESULTS_DIR = BASE_DIR / RESULTS
"""Path to saved after parsing data."""

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FILE_FORMAT = 'csv'
"""File extension for saved data after parsing."""

SUMMARY_NAME = 'status_summary'
"""Name of file for saved after parsing data."""

SUMMARY_TABLE_HEADER = ('Status', 'Quantity')
SUMMARY_TABLE_BOTTOM = 'Total'
"""Result table elements names."""

PEP_NAME = 'pep'
PEP_FILE_NAME = f'{PEP_NAME}_%(time)s.{FILE_FORMAT}'

FEEDS = {
    f'{RESULTS}/{PEP_FILE_NAME}': {
        'format': FILE_FORMAT,
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

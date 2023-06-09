# This pytest code defines test functions for the report_generator module.
# It loads test data into the API and tests the get_articles_by_category and get_average_words functions of the report_generator module.
# It also defines a fixture to remove the CSV files generated by the report_generator module after the tests have been run.
# The purpose of this code is to test the functionality and accuracy of the report_generator module in generating reports based on article data.

import pytest
import os
from datetime import datetime
from report_generator import get_all_articles, get_articles_by_category, get_average_words, categories

# Base URL of the API used in the main code
base_url = 'http://localhost:3000'

# Variable to store the articles returned by the API
articles = []

def setup_module(module):
    global articles
    # Load test data into the API and database testing environment.
    # This step will depend on how you set up your test environment
    # and how you can add test data to it.
    
    # Here, we assume that the test API is already configured and ready to use.
    articles = get_all_articles()

def test_get_articles_by_category():
    # Test the get_articles_by_category function with the author and articles obtained from the test API.
    articles_by_category = get_articles_by_category("Gabriela Oliveira", articles)
    expected_articles_by_category = [3, 1, 0, 1, 1, 2]
    assert articles_by_category == expected_articles_by_category

def test_get_average_words():
    # Test the get_average_words function with the author and articles obtained from the test API.
    average_words = get_average_words("Alexandre Souza", articles)
    expected_average_words = 360
    assert average_words == expected_average_words


@pytest.fixture(scope="module", autouse=True)
def cleanup(request):
    def remove_csv_files():
        # Remove the CSV files generated by the report_generator module after the tests have been run.
        file_name = f'relatório_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
        if os.path.exists(file_name):
            os.remove(file_name)

    request.addfinalizer(remove_csv_files)

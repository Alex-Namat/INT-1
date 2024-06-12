import os
import pytest
import logging
import time
from testcontainers.postgres import PostgresContainer

from db import table

LOGGER = logging.getLogger(__name__)

container = PostgresContainer("postgres:alpine")


@pytest.fixture(scope="module", autouse=True)
def setup(request: pytest.FixtureRequest):
    container.start()
    
    def remove_container():
        container.stop()

    request.addfinalizer(remove_container)
    os.environ["DB_CONN"] = container.get_connection_url()
    os.environ["DB_HOST"] = container.get_container_host_ip()    
    os.environ["DB_PORT"] = container.get_exposed_port(5432)
    os.environ["DB_USERNAME"] = container.username
    os.environ["DB_PASSWORD"] = container.password
    os.environ["DB_NAME"] = container.dbname
    table.create()

@pytest.fixture(scope="function", autouse=True)
def setup_data():
    table.delete()

def test_functional():
    table.generated_rows()
    no_idx_result = table.return_select_like()
    table.create_index()
    idx_result = table.return_select_like()
    table.drop_index()
    LOGGER.info(f"Data without index: {no_idx_result}")
    LOGGER.info(f"Data with index: {idx_result}")
    LOGGER.info(f"Rows: {len(idx_result)}")
    assert set(no_idx_result) == set(idx_result)

@pytest.mark.parametrize(
        "num_rows, pattern",
        [(100,'%An%'),(1000,'%An%'),(10000,'%An%'),(100000,'%An%')])
def test_perfomance(num_rows,pattern):
    table.generated_rows(num_rows)
    start = time.time()
    table.select_like(pattern)
    end = time.time() - start
    LOGGER.info(f"Without index: Total time for {num_rows} records {end} secs")
    table.create_index()
    start = time.time()
    table.select_like(pattern)  
    end = time.time() - start  
    table.drop_index()
    LOGGER.info(f"With index: Total time for {num_rows} records {end} secs")


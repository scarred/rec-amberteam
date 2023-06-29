import pytest
from pages.task_page import TaskPage


@pytest.fixture(scope='session')
def task_page(driver):
    return TaskPage(driver)


@pytest.mark.task3
def test_task3(task_page):
    # Start on the start page
    task_page.go_to_start_page()
    
    # Test steps for Task 3
    task_page.click_task_button(3)
    # Perform assertions and verifications
    
    task_page.t3_step_1()
    task_page.check_result()

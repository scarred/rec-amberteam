import pytest
from pages.task_page import TaskPage


@pytest.fixture(scope='session')
def task_page(driver):
    return TaskPage(driver)


@pytest.mark.task1
def test_task1(task_page):
    # Start on the start page
    task_page.go_to_start_page()
    
    # Test steps for Task 1
    task_page.click_task_button(1)
    # Perform assertions and verifications
    
    task_page.t1_step_1()
    task_page.t1_step_2()
    task_page.t1_step_3()
    task_page.check_result()

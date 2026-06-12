from time import sleep

import pytest

from pages.delete_page import DeletePage
from pages.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.order(7)
def test_delete_note_ui(setup_and_teardown):
    dp = DeletePage(setup_and_teardown)

    lp = LoginPage(setup_and_teardown)
    lp.login()
    sleep(2)

    dp.scroll()
    dp.click_delete()
    sleep(1)

    dp.click_confirm()
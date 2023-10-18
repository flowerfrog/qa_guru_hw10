from data.users import User
from pages.registration_page import RegistrationPage


def test_complete_practice_form():
    registration_page = RegistrationPage()

    # GIVEN
    user = User(
        first_name='test',
        last_name='user',
        email='test@user.com',
        gender='Female',
        phone_number='7999999999',
        month_of_birth='December',
        year_of_birth='2000',
        day_of_birth='25',
        subject='Maths',
        hobby='Reading',
        picture='image.jpg',
        current_address='Ростов-сити, Забугорная 3к1',
        state='NCR',
        city='Delhi'
    )

    registration_page.open()

    # WHEN
    registration_page.register(user)

    # THEN
    registration_page.user_should_registered(user)












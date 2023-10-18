from selene import browser, have, command
import os

from selene.support.conditions import be


def test_complete_practice_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('test')
    browser.element('#lastName').type('user')
    browser.element('#userEmail').type('test@user.com')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('79999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="11"]').click()
    browser.element('.react-datepicker__year-select').type('2000')
    browser.element('.react-datepicker__day.react-datepicker__day--025').click()
    browser.element('#subjectsInput').type('math').press_enter()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('//input[@type="file"]').type(os.path.abspath("resources/image.jpg"))
    browser.element('#currentAddress').type('Ростов-сити, Забугорная 3к1')
    browser.element('//*[@id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('//*[@id="react-select-4-input"]').type('Delhi').press_enter()
    browser.element('//footer').perform(command.js.remove)
    browser.all('#userForm > div').should(have.size(11))
    browser.element('#submit').click()
    browser.all('#todo-list>li').by(have.css_class('was-validated'))
    browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
        "test user",
        "test@user.com",
        "Female",
        "7999999999",
        "25 December,2000",
        "Maths",
        "Reading",
        "image.jpg",
        "Ростов-сити, Забугорная 3к1",
        "NCR Delhi"
    ))
    browser.element("#closeLargeModal").should(be.visible).click()












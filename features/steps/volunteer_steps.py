from behave import given, when, then
from volunteer_system import VolunteerRegistrationSystem

@given('a volunteer provides the name "{name}"')
def step_volunteer_name(context, name):
    context.system = VolunteerRegistrationSystem()
    context.name = name

@given('the volunteer provides the email "{email}"')
def step_volunteer_email(context, email):
    context.email = email


@given('the volunteer does not provide an email address')
def step_missing_email(context):
    context.email = ""

@when('the volunteer submits the registration form')
def step_submit_registration(context):
    context.result = context.system.register_volunteer(
        context.name,
        context.email
    )

@then('the system should display "{expected_message}"')
def step_check_message(context, expected_message):
    assert context.result == expected_message


@given('a volunteer with the email "{email}" is already registered')
def step_existing_volunteer(context, email):
    context.system = VolunteerRegistrationSystem()
    context.system.register_volunteer("Anna Smith", email)

@when('another volunteer submits the same email "{email}"')
def step_duplicate_email(context, email):
    context.result = context.system.register_volunteer(
        "Anna Smith",
        email
    )
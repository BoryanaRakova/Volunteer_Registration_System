from behave import given, when, then
from volunteer_system import VolunteerRegistrationSystem


@given('a volunteer provides the name "{name}"')
def step_volunteer_name(context, name):
    # Create a new volunteer registration system
    context.system = VolunteerRegistrationSystem()

    # Store the volunteer name
    context.name = name


@given('the volunteer provides the email "{email}"')
def step_volunteer_email(context, email):
    # Store the volunteer email
    context.email = email


@given('the volunteer does not provide an email address')
def step_missing_email(context):
    # Simulate a missing email address
    context.email = ""


@when('the volunteer submits the registration form')
def step_submit_registration(context):
    # Submit the registration request
    context.result = context.system.register_volunteer(
        context.name,
        context.email
    )


@then('the system should display "{expected_message}"')
def step_check_message(context, expected_message):
    # Verify the expected system response
    assert context.result == expected_message


@given('a volunteer with the email "{email}" is already registered')
def step_existing_volunteer(context, email):
    # Create a system with an existing volunteer
    context.system = VolunteerRegistrationSystem()
    context.system.register_volunteer("Anna Smith", email)


@when('another volunteer submits the same email "{email}"')
def step_duplicate_email(context, email):
    # Attempt to register using a duplicate email
    context.result = context.system.register_volunteer(
        "Anna Smith",
        email
    )


@when('the volunteer provides the invalid email "{email}"')
def step_invalid_email(context, email):
    # Store an invalid email address
    context.email = email
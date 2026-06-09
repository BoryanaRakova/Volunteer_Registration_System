class VolunteerRegistrationSystem:
    def __init__(self):
        # Store registered volunteers
        self.volunteers = []

    def register_volunteer(self, name, email):

        # Check that a name has been provided
        if not name:
            return "Error: Name is required"

        # Check that an email address has been provided
        if not email:
            return "Error: Email is required"

        # Validate the email format
        if "@" not in email:
            return "Error: Invalid email address"

        # Check for duplicate email registrations
        for volunteer in self.volunteers:
            if volunteer["email"] == email:
                return "Error: Volunteer already registered"

        # Save the volunteer details
        self.volunteers.append({
            "name": name,
            "email": email
        })

        # Return a success message
        return "Volunteer registered successfully"
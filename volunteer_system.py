class VolunteerRegistrationSystem:
    def __init__(self):
        self.volunteers = []

    def register_volunteer(self, name, email):
        if not name:
            return "Error: Name is required"

        if not email:
            return "Error: Email is required"

        if "@" not in email:
            return "Error: Invalid email address"

        for volunteer in self.volunteers:
            if volunteer["email"] == email:
                return "Error: Volunteer already registered"

        self.volunteers.append({
            "name": name,
            "email": email
        })

        return "Volunteer registered successfully"
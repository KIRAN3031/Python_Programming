class WorkshopAttendance:
    def __init__(self, day1, day2, day3):
        self.day1 = self.clean_and_deduplicate(day1)
        self.day2 = self.clean_and_deduplicate(day2)
        self.day3 = self.clean_and_deduplicate(day3)

    @staticmethod
    def clean_and_deduplicate(attendees):
        """Normalize emails to lowercase and remove duplicates."""
        return set(email.lower() for email in attendees)

    def total_unique_attendees(self):
        """Return the set of all unique attendees across all days."""
        return self.day1 | self.day2 | self.day3

    def attendees_all_three_days(self):
        """Return attendees who attended all three days."""
        return self.day1 & self.day2 & self.day3

    def attendees_exactly_one_day(self):
        """Return attendees who attended exactly one day."""
        all_three = self.attendees_all_three_days()
        return (self.day1 ^ self.day2 ^ self.day3) 

    def pairwise_overlaps(self):
        """Return dictionary with pairwise overlap sets."""
        return {
            'day1_day2': self.day1 & self.day2,
            'day2_day3': self.day2 & self.day3,
            'day1_day3': self.day1 & self.day3,
        }

    def generate_report(self):
        """Print the final report."""
        all_unique = self.total_unique_attendees()
        all_three = self.attendees_all_three_days()
        exactly_one = self.attendees_exactly_one_day()
        overlaps = self.pairwise_overlaps()

        print("Workshop Attendance Report")
        print("-"*40)
        print(f"Total unique attendees: {len(all_unique)}\n")

        print(f"Attendees who attended all three days ({len(all_three)}):")
        print(sorted(all_three))
        print()

        print(f"Attendees who attended exactly one day ({len(exactly_one)}):")
        print(sorted(exactly_one))
        print()

        print("Pairwise overlap counts:")
        for pair, attendees in overlaps.items():
            print(f"{pair.replace('_', ' & ').title()}: {len(attendees)} attendees")
        print()

        print("Pairwise overlap attendees:")
        for pair, attendees in overlaps.items():
            print(f"{pair.replace('_', ' & ').title()} ({len(attendees)}): {sorted(attendees)}")

day1 = ["alice@example.com", "Bob@Example.com", "carol@example.com", "alice@example.com"]
day2 = ["bob@example.com", "dave@example.com", "carol@example.com"]
day3 = ["ALICE@EXAMPLE.COM", "carol@example.com", "erin@example.com"]

workshop = WorkshopAttendance(day1, day2, day3)
print()
workshop.generate_report()

import frappe
from frappe.model.document import Document

class RideBooking(Document):
    def validate(self):
        # Initialize total_amount
        total_amount = 0

        # Ensure 'items' is a valid attribute
        if hasattr(self, 'items'):
            # Iterate through each item in the child table
            for item in self.items:
                # Calculate total_amount for each item
                item_total = item.distance * item.rate
                # Sum the total_amounts for all items
                total_amount += item_total

        # Set the total_amount in the parent document
        self.total_amount = total_amount

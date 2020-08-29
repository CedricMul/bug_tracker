from django import forms
from bug_app.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'time_and_date',
            'description',
            'user_field',
            'status',
            'assigned_to',
            'completed_by'
        ]

from django import forms


class CookiePageConsentForm(forms.Form):
    """Consent Form.

    Radio Select Form for setting analytics cookie consent in the cookies page.
    """

    ANALYTICS_CHOICES = [
        (True, "Yes"),
        (False, "No"),
    ]
    analytics_consent = forms.ChoiceField(
        choices=ANALYTICS_CHOICES,
        label="Do you want to accept analytics cookies?",
        widget=forms.RadioSelect(),
    )


class RegulationSearchForm(forms.Form):
    """Regulation Search Form.

    Regulation search form for searching
    for regulations by name or description.
    """

    query = forms.CharField(
        required=False,
        label="Enter the sector, business activity or topic you want to find regulations for.",  # noqa: E501
        help_text="For example, Construction, Health and Safety, or Food",
        widget=forms.TextInput(
            attrs={
                "class": "govuk-input",
                "id": "query",
                "name": "query",
                "type": "search",
                "placeholder": "Search for regulations",
            }
        ),
    )

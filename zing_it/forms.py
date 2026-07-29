"""Forms for the zing_it application."""

from __future__ import annotations

from typing import ClassVar

from django import forms

type Choices = list[tuple[str, str]]


class TestForm(forms.Form):
    """Demo form exercising the built-in field and widget types."""

    RADIO_CHOICES: ClassVar[Choices] = [
        ("signin", "Sign In"),
        ("signup", "Sign Up"),
        ("forgotpassword", "Forgot Password"),
    ]

    INTS_CHOICES: ClassVar[list[tuple[int, int]]] = [(x, x) for x in range(100)]

    YEARS: ClassVar[list[int]] = list(range(1980, 2031))

    CHECKBOX_CHOICES: ClassVar[Choices] = [
        ("terms", "Agree to terms and conditions"),
        ("privacy", "Agree to privacy policy"),
    ]

    date_field = forms.DateField(
        initial="2020-20-5",
        widget=forms.SelectDateWidget(years=YEARS),
    )
    text = forms.CharField(label="Feedback", min_length=7, widget=forms.Textarea)
    radio_choices = forms.CharField(widget=forms.RadioSelect(choices=RADIO_CHOICES))
    checkbox_choices = forms.CharField(
        widget=forms.CheckboxSelectMultiple(choices=CHECKBOX_CHOICES),
    )
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10, widget=forms.Select(choices=INTS_CHOICES))
    email = forms.EmailField()

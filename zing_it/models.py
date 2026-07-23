"""Models for the zing_it application.

This module defines the following models:
- Topic: represents a topic
- Webpage: represents a webpage associated with a topic
- AccessRecord: records access history for webpages
"""

from datetime import date

from django.db import models

# Create your models here.


class Topic(models.Model):
    """Model to represent a topic."""

    topic_name = models.CharField(max_length=254, unique=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.topic_name


class Webpage(models.Model):
    """Model to represent a webpage associated with a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.name


class AccessRecord(models.Model):
    """Model to record access history for webpages."""

    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return str(self.date)


class Company(models.Model):
    """Model to represent a company."""

    name = models.CharField(max_length=264, unique=True)
    number_of_employees = models.IntegerField(default=0)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.name


class Employee(models.Model):
    """Model to represent an employee."""

    employee_name = models.CharField(max_length=264, unique=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=date.today)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.employee_name


class Project(models.Model):
    """Model to represent a project."""

    project_name = models.CharField(max_length=264, unique=True)
    employee_name = models.ManyToManyField("Employee")

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.project_name

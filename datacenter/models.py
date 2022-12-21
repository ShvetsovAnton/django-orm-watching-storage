from django.db import models
import django.utils.timezone
import datetime


def get_duration(visit):
    entered = django.utils.timezone.localtime(visit.entered_at)
    leaved = django.utils.timezone.localtime(visit.leaved_at)
    duration = leaved - entered
    return duration


def format_duration(duration):
    seconds_in_hour = 3600
    seconds_in_minute = 60
    hours_in_day = 24
    total_second = duration.seconds
    days = duration.days
    hours = (days * hours_in_day) // seconds_in_hour
    minutes = (total_second % seconds_in_hour) // seconds_in_minute
    seconds = (total_second % seconds_in_minute)
    total_time_in = datetime.time(int(hours), int(minutes), int(seconds))
    return f'{total_time_in.strftime("%H:%M:%S")}'


def is_visit_long(visit, minutes=60):
    seconds_in_minute = 60
    total_second = get_duration(visit).total_seconds()
    how_long_inside = total_second // seconds_in_minute
    return how_long_inside > minutes


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

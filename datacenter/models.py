from django.db import models
import django.utils.timezone
import datetime


def get_duration(visit):
    entered = django.utils.timezone.localtime(visit.entered_at)
    leaved = django.utils.timezone.localtime(visit.leaved_at)
    duration = leaved - entered
    return duration.total_seconds()


def format_duration(duration):
    seconds_in_hour = 3600
    seconds_in_minute = 60
    seconds_in_day = 86400
    hours_in_day = 24
    days = duration // (hours_in_day * seconds_in_hour)
    hours = (duration - (days * seconds_in_day)) // seconds_in_hour
    minutes = (
                duration - (days * seconds_in_day + hours * seconds_in_hour)
              ) // seconds_in_minute
    seconds = (
            duration - (days * seconds_in_day + hours * seconds_in_hour +
                        minutes * seconds_in_minute)
    )
    total_time_in = datetime.time(int(hours), int(minutes), int(seconds))
    return f'{total_time_in.strftime("%H:%M:%S")}'


def is_visit_long(visit, minutes=60):
    seconds_in_minute = 60
    total_second = get_duration(visit)
    how_long_inside = total_second // seconds_in_minute
    if how_long_inside > minutes:
        return True
    return False


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

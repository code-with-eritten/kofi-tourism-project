import django_filters
from .models import Event
from datetime import datetime, timedelta


class EventFilter(django_filters.FilterSet):
    today = django_filters.BooleanFilter(method='filter_today')
    this_week = django_filters.BooleanFilter(method='filter_this_week')
    this_month = django_filters.BooleanFilter(method='filter_this_month')
    last_month = django_filters.BooleanFilter(method='filter_last_month')
    this_year = django_filters.BooleanFilter(method='filter_this_year')
    last_year = django_filters.BooleanFilter(method='filter_last_year')
    upcoming = django_filters.BooleanFilter(method='filter_upcoming')

    class Meta:
        model = Event
        fields = ['today', 'this_week', 'this_month', 'last_month', 'this_year', 'last_year', 'upcoming']

    def filter_today(self, queryset, name, value):
        if value:
            today = datetime.today().date()
            return queryset.filter(start_time__date=today)
        return queryset

    def filter_this_week(self, queryset, name, value):
        if value:
            start_of_week = datetime.today().date() - timedelta(days=datetime.today().weekday())
            end_of_week = start_of_week + timedelta(days=6)
            return queryset.filter(start_time__date__range=[start_of_week, end_of_week])
        return queryset

    def filter_this_month(self, queryset, name, value):
        if value:
            today = datetime.today()
            return queryset.filter(start_time__year=today.year, start_time__month=today.month)
        return queryset

    def filter_last_month(self, queryset, name, value):
        if value:
            today = datetime.today()
            first_of_this_month = today.replace(day=1)
            last_month = first_of_this_month - timedelta(days=1)
            return queryset.filter(start_time__year=last_month.year, start_time__month=last_month.month)
        return queryset

    def filter_this_year(self, queryset, name, value):
        if value:
            today = datetime.today()
            return queryset.filter(start_time__year=today.year)
        return queryset

    def filter_last_year(self, queryset, name, value):
        if value:
            last_year = datetime.today().year - 1
            return queryset.filter(start_time__year=last_year)
        return queryset

    def filter_upcoming(self, queryset, name, value):
        if value:
            today = datetime.now()
            return queryset.filter(start_time__gte=today)
        return queryset

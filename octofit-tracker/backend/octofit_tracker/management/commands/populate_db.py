from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='swim', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='run', duration=40, date=timezone.now().date())
        Activity.objects.create(user=users[4], type='cycle', duration=35, date=timezone.now().date())
        Activity.objects.create(user=users[5], type='swim', duration=50, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Pushups', description='Do 3 sets of 15 pushups')
        w2 = Workout.objects.create(name='Situps', description='Do 3 sets of 20 situps')
        w1.suggested_for.add(marvel, dc)
        w2.suggested_for.add(marvel, dc)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=120)
        Leaderboard.objects.create(team=dc, points=110)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))

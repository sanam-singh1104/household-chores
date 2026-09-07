from django.db import IntegrityError, transaction
from django.test import TestCase

from .models import Household, Roommate


class HouseholdModelTests(TestCase):
    def test_creates_with_valid_data(self):
        household = Household.objects.create(name="Maple Street")

        self.assertIsNotNone(household.pk)
        self.assertEqual(household.name, "Maple Street")

    def test_str_returns_name(self):
        household = Household.objects.create(name="Maple Street")

        self.assertEqual(str(household), "Maple Street")


class RoommateModelTests(TestCase):
    def test_creates_with_valid_data_and_links_to_household(self):
        household = Household.objects.create(name="Maple Street")
        roommate = Roommate.objects.create(name="Alex", household=household)

        self.assertIsNotNone(roommate.pk)
        self.assertEqual(roommate.name, "Alex")
        self.assertEqual(roommate.household, household)

    def test_str_returns_name(self):
        household = Household.objects.create(name="Maple Street")
        roommate = Roommate.objects.create(name="Alex", household=household)

        self.assertEqual(str(roommate), "Alex")

    def test_cannot_exist_without_a_household(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Roommate.objects.create(name="Alex", household=None)


class HouseholdRoommateRelationshipTests(TestCase):
    def test_household_roommates_returns_only_its_own_roommates(self):
        household_a = Household.objects.create(name="Maple Street")
        household_b = Household.objects.create(name="Oak Avenue")
        alex = Roommate.objects.create(name="Alex", household=household_a)
        jordan = Roommate.objects.create(name="Jordan", household=household_a)
        Roommate.objects.create(name="Sam", household=household_b)

        self.assertCountEqual(household_a.roommates.all(), [alex, jordan])

    def test_deleting_household_cascades_to_roommates(self):
        household = Household.objects.create(name="Maple Street")
        roommate = Roommate.objects.create(name="Alex", household=household)

        household.delete()

        self.assertFalse(Roommate.objects.filter(pk=roommate.pk).exists())

    def test_two_households_can_have_roommates_with_same_name(self):
        household_a = Household.objects.create(name="Maple Street")
        household_b = Household.objects.create(name="Oak Avenue")

        roommate_a = Roommate.objects.create(name="Alex", household=household_a)
        roommate_b = Roommate.objects.create(name="Alex", household=household_b)

        self.assertNotEqual(roommate_a.pk, roommate_b.pk)
        self.assertEqual(household_a.roommates.get().name, "Alex")
        self.assertEqual(household_b.roommates.get().name, "Alex")

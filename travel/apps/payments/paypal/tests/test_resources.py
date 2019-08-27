import json
import unittest

from django.test import TestCase, override_settings

from payments.paypal import resources


class PlanTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        pass
        # assert True == True
        # with open('payments/paypal/fixtures/plans/professional.json') as file:
        #     cls.data = json.loads(file.read())
        #
        # cls.plan = resources.Plan(cls.data)
        #
        # cls.plan.create()

    def setUp(self) -> None:
        self.plan = resources.Plan.find('P-4SG61272WE728141MLUUIK7A')

    @unittest.skip('Saltando la creación')
    def test_create(self):
        self.plan = resources.Plan(self.data)
        self.assertTrue(self.plan.create(), 'Plan creado con éxito')

    def test_list(self):
        plans = resources.Plan.all()
        self.assertIn(self.plan, plans)

    def test_find(self):
        plan = resources.Plan.find(self.plan.id)
        self.assertEqual(self.plan.id, plan.id)
        self.assertEqual(self.plan, plan)

    def test_deactivate(self):
        self.assertTrue(self.plan.active())
        self.assertEqual(self.plan.status, 'ACTIVE', 'Plan activo')
        self.assertTrue(self.plan.deactivate(), 'Plan desactivado con éxito')
        self.assertEqual(self.plan.status, 'INACTIVE', 'Plan inactivo')

    def test_activate(self):
        self.assertTrue(self.plan.deactivate())
        self.assertEqual(self.plan.status, 'INACTIVE', 'Plan inactivo')
        self.assertTrue(self.plan.active(), 'Plan activado con éxito')
        self.assertEqual(self.plan.status, 'ACTIVE', 'Plan activo')

    @unittest.skip('Saltando el cambio de precio')
    def test_update_price(self):
        pass


class SubscriptionTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def test_find(self):
        pass

    @unittest.skip
    def test_create(self):
        pass

    def test_activate(self):
        pass

    def test_cancel(self):
        pass

    def test_suspend(self):
        pass

    def test_transactions(self):
        pass

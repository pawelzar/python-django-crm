from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TransactionTestCase

from crm.forms import CompanyForm


class TestCompanyForm(TransactionTestCase):
    """Tests for company edition view."""

    def test_form_is_valid(self):
        """Test is_validate() method.

            Testing CompanyForm.is_valid() method
            with correct fields return valid form
        """
        form_data = dict(
            name='Example Company',
            city='City',
            street='Example Street 6',
            postal_code='11-111',
            number='586-22-50-789',
        )
        form = CompanyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid(self):
        """Test is_validate() method.

            Testing CompanyForm.is_valid() method
            with empty fields return invalid form
        """
        form_data = dict()
        form = CompanyForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_wrong_number_raise_exception(self):
        """Test clean_number() method.

            Testing Company.clean_number() method
            with too short number raise ValidationError exception
        """
        form_data = dict(
            name='Example Company',
            city='City',
            street='Example Street 6',
            postal_code='11-111',
            number='123',
        )
        form = CompanyForm(data=form_data)
        form.is_valid()
        self.assertRaises(ValidationError, form.clean_number)

    def test_wrong_postal_code_raise_exception(self):
        """Test clean_postal_code() method.

            Testing Company.clean_postal_code() method
            with wrong postal code raise ValidationError exception
        """
        form_data = dict(
            name='Example Company',
            city='City',
            street='Example Street 6',
            postal_code='111',
            number='123',
        )
        form = CompanyForm(data=form_data)
        form.is_valid()
        self.assertRaises(ValidationError, form.clean_postal_code)

from django.test import TestCase
from django.urls import reverse

from users.models import User
#
#
# class ProfileModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         user = User.objects.create(username='Testing', first_name='Richie', last_name='Meyer', email='richiemeyer@gmail.com')
#         Profile.objects.create(user=user, last_location="{\"journeyInfo\":[{\"timestamp\":1617194118000, \"lat1\":53.21801666666667, \"lon1\":-6.127745000000001, \"lat2\":53.219879999999996, \"lon2\":-6.1286000000000005, \"speed\":97, \"speedLimit\":0, \"road\":\"undefined\"},{\"timestamp\":1617194127000, \"lat1\":53.219879999999996, \"lon1\":-6.1286000000000005, \"lat2\":53.22178999999999, \"lon2\":-6.12893, \"speed\":85, \"speedLimit\":120, \"road\":\"M11\"},{\"timestamp\":1617194135000, \"lat1\":53.22178999999999, \"lon1\":-6.12893, \"lat2\":53.223731666666666, \"lon2\":-6.12895, \"speed\":97, \"speedLimit\":120, \"road\":\"M11\"},{\"timestamp\":1617194143000, \"lat1\":53.223731666666666, \"lon1\":-6.12895, \"lat2\":53.22569, \"lon2\":-6.129020000000001, \"speed\":98, \"speedLimit\":120, \"road\":\"M11\"},{\"timestamp\":1617194151000, \"lat1\":53.22569, \"lon1\":-6.129020000000001, \"lat2\":53.22754499999999, \"lon2\":-6.1297266666666665, \"speed\":95, \"speedLimit\":120, \"road\":\"M11\"},{\"timestamp\":1617194160000, \"lat1\":53.22754499999999, \"lon1\":-6.1297266666666665, \"lat2\":53.22933, \"lon2\":-6.13109, \"speed\":87, \"speedLimit\":120, \"road\":\"M11\"},{\"timestamp\":1617194170000, \"lat1\":53.22933, \"lon1\":-6.13109, \"lat2\":53.23076, \"lon2\":-6.132459999999999, \"speed\":66, \"speedLimit\":120, \"road\":\"M11\"},{\"timestamp\":1617194180000, \"lat1\":53.23076, \"lon1\":-6.132459999999999, \"lat2\":53.232395, \"lon2\":-6.132741666666667, \"speed\":66, \"speedLimit\":120, \"road\":\"M11\"}]}")
#
#     def test_journey_label(self):
#         journey = Profile.objects.get(id=1)
#         field_label = journey._meta.get_field('journey').verbose_name
#         self.assertEqual(field_label, 'journey')
#


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Testing', first_name='Richie', last_name='Meyer', email='richiemeyer@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('world-home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('world-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'world/home.html')


    # def test_view_url_accessible_by_name(self):
    #     response = self.client.get(reverse('authors'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('authors'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/author_list.html')

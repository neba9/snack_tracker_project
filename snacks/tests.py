from django.test import TestCase
from django.http import response 
# from django.test import SimpleTestCase
from django.urls import reverse

class ThingsTest(TestCase):

  def test_snack_list_page_status(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
 

  def test_snak_list_page_templet(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_list.html')

  def test_base_page_template(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'base.html')


  # def test_snack_detail_status(self):
  #   url = reverse('snack_detail', kwargs={'pk':1})
  #   response = self.client.get(url)
  #   self.assertEqual(response.status_code, 200)

  # def test_snack_detail_template(self):
  #   url = reverse('snack_detail',  kwargs={'pk':1})
  #   response = self.client.get(url)
  #   self.assertTemplateUsed(response, 'snack_detail.html')


# Create your tests here.

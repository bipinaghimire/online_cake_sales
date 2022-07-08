
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from customer.views import create, delete, edit,saveFn, update

# Create your tests here. 8 url test 8 CRUD test so total 16 tests are required

class TestUrls(SimpleTestCase):
    def test_create_url(self):
        url = reverse(create)
        print(url)
        self.assertEquals(resolve(url).func,create)
    # //finds url
    # reverse (url find) 
    # help to get function of that url
    # resolve
    # checks the function that came with resolve and compares with the one we entered
    # assertEquals

    def test_save_url(self):
        url = reverse(saveFn)
        # (or edit matra lekhera import garni)
        print(url)
        self.assertEquals(resolve(url).func,saveFn)

    def test_edit_url(self):
        url = reverse('customer_edit',args='1')
        # (or edit matra lekhera import garni)
        print(url)
        self.assertEquals(resolve(url).func,edit)

    def test_update_url(self):
        url = reverse(update, args='1')
        print(url)
        self.assertEquals(resolve(url).func,update)

    def test_delete_url(self):
        url = reverse(delete,args='1')
        print(url)
        self.assertEquals(resolve(url).func,delete)

    

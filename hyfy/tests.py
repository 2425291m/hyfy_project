
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.core.urlresolvers import reverse
import socket
import populate_hyfy


def login(self):
    self.browser.get(self.live_server_url + '/admin/')

    # Types username and password
    username_field = self.browser.find_element_by_name('username')
    username_field.send_keys('admin')

    password_field = self.browser.find_element_by_name('password')
    password_field.send_keys('admin')
    password_field.send_keys(Keys.RETURN)


class LiveServerTests(StaticLiveServerTestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        User.objects.create_superuser(username='admin', password='admin', email='admin@me.com')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options = chrome_options)
        self.browser.implicitly_wait(3)

    @classmethod
    def setUpClass(cls):
        cls.host = socket.gethostbyname(socket.gethostname())
        super(LiveServerTests, cls).setUpClass()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    # Test the index and about_us pages contain images
    def test_venues_display_correct_pictures(self):
        response = self.client.get(reverse('index'))
        self.assertIn('href="/static/CSS/homepage.css"', response.content.decode('ascii'))

        self.client.get(reverse('index'))
        response = self.client.get(reverse('about_us'))
        self.assertIn('img src="/static/images/', response.content.decode('ascii'))

    # Test the Navigation buttons on the base toolbar
    # Go from the index page to the about page and back again
    def test_navigate_from_HomePage_to_about_us(self):
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('index'))

        about_link = self.browser.find_element_by_partial_link_text("About Us")
        about_link.click()

        link_to_home_page = self.browser.find_element_by_link_text('Home')
        link_to_home_page.click()

        self.assertEqual(url + reverse('index'), self.browser.current_url)

    # Test to check if there is a template on the about us and index pages
    # Test if there are titles in the home page
    def test_template_usage(self):
        response = self.client.get(reverse('index'))
        self.assertIn('<title>', response.content.decode('ascii'))
        self.assertIn('</title>', response.content.decode('ascii'))
        self.assertTemplateUsed(response, 'hyfy/HomePage.html')

        response = self.client.get(reverse('about_us'))
        self.assertTemplateUsed(response, 'hyfy/about_us.html')

    # Test the appearance of the Logout link on the home page before and after user login
    # Test if logout link is returning the correct url after clicked
    def test_Logout_Link(self):
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')

        self.browser.get(url + reverse('index'))
        category_link = self.browser.find_elements_by_partial_link_text('Logout')
        self.assertNotEquals(len(category_link), 1)

        login(self)
        self.browser.get(url + reverse('index'))
        about_link = self.browser.find_element_by_partial_link_text("Logout")
        about_link.click()
        self.assertEqual(url + '/hyfy/', self.browser.current_url)

    # Test the appearance of the Account link on the homepage before and after login
    # Test that the link returns the correct url
    def test_Account_Link(self):
        # Access index page
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('index'))

        category_link = self.browser.find_elements_by_partial_link_text('Account')
        self.assertNotEquals(len(category_link), 1)
        login(self)

        self.browser.get(url + reverse('index'))
        about_link = self.browser.find_element_by_partial_link_text("Account")
        about_link.click()
        self.assertEqual(url + '/hyfy/account/admin/', self.browser.current_url)

    # Test to run populate_hyfy.py, then check the venue pages are accessible
    def test_venue_pages(self):
        populate_hyfy.populate()
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('index'))

        self.browser.get(url + '/hyfy/glasgow/')
        link_to_home_page = self.browser.find_element_by_link_text('Oran Mor')
        link_to_home_page.click()
        self.assertEqual(url + '/hyfy/glasgow/oran-mor/', self.browser.current_url)

        self.browser.get(url + '/hyfy/edinburgh/')
        link_to_home_page = self.browser.find_element_by_link_text('Cabaret Voltaire')
        link_to_home_page.click()
        self.assertEqual(url + '/hyfy/edinburgh/cabaret-voltaire/', self.browser.current_url)

        self.browser.get(url + '/hyfy/dundee/')
        link_to_home_page = self.browser.find_element_by_link_text('Beat Generator Live!')
        link_to_home_page.click()
        self.assertEqual(url + '/hyfy/dundee/beat-generator-live/', self.browser.current_url)





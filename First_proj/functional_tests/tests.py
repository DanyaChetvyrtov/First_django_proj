from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
from datetime import datetime
import pytz


class BasicInstallTest(LiveServerTestCase):

    def setUp(self):
        path_to_driver = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.browser = webdriver.Chrome(path_to_driver, options=options)
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='ooo-lya-lya'
            )

    # Quit browser after testing
    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Danil Semyonov website', self.browser.title)

    def test_home_page_header(self):
        browser = self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.TAG_NAME, 'h1') 

        self.assertIn('Danil Semenov', header.text)
        
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertTrue(header.location['x'] > 10)

    def test_home_page_blog(self):
        self.browser.get(self.live_server_url)
        article_list = self.browser.find_element(By.CLASS_NAME ,'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        aritcle_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(aritcle_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_title_text = article_title.text
        
        # Find link in article title
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        self.browser.get(article_link.get_attribute('href'))

        article_page_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        self.assertEqual(article_title_text, article_page_title.text)
        


# # test that Django page is open 
# path_to_driver = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)

# browser = webdriver.Chrome(path_to_driver, options=options)
# browser.get('http://127.0.0.1:8080')

# assert 'Congratulations' in browser.title

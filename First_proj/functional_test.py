from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        path_to_driver = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.browser = webdriver.Chrome(path_to_driver, options=options)

    # Quit browser after testing
    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get('http://127.0.0.1:8000')

        self.assertIn('My first site', self.browser.title)

    def test_home_page_header(self):
        browser = self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')

        self.assertIn('Danil Semenov', header.text)

    def test_home_page_blog(self):
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element(By.CLASS_NAME ,'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        aritcle_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(aritcle_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_title_text = article_title.text
        
        # Find link in article title
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        self.browser.get(article_link.get_attribute('href'))

        article_page_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        self.assertEqual(article_title_text, article_page_title.text)
        

if __name__ == '__main__':
    unittest.main()



# # test that Django page is open 
# path_to_driver = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)

# browser = webdriver.Chrome(path_to_driver, options=options)
# browser.get('http://127.0.0.1:8080')

# assert 'Congratulations' in browser.title

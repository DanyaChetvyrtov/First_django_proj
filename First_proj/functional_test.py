from selenium import webdriver
import unittest


class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        path_to_driver = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.browser = webdriver.Chrome(path_to_driver, options=options)

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get('http://127.0.0.1:8080')

        self.assertIn('My first site', self.browser.title)
        # self.fail('Finish the test!')

    def test_home_page_header(self):
        browser = self.browser.get('http://127.0.0.1:8080')
        header = browser.find_elements_by_tag_name('h1')[0]

        self.assertIn('My first site', header)
        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()








# # test that Django page is open 
# path_to_driver = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)

# browser = webdriver.Chrome(path_to_driver, options=options)
# browser.get('http://127.0.0.1:8080')

# assert 'Congratulations' in browser.title

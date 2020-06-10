from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import time
import fnmatch


def bot(mail, password, campaign, category, brand, color, size):
    # Changing all input to lower
    for i in range(0, len(category)):
        category[i] = category[i].lower()

    for i in range(0, len(brand)):
        brand[i] = brand[i].lower()

    for i in range(0, len(color)):
        color[i] = color[i].lower()

    for i in range(0, len(size)):
        size[i] = size[i].lower()
    # ############################

    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    driver.maximize_window()
    driver.get('https://www.zalando-lounge.pl/#/login')

    email_log = driver.find_element_by_id('form-email')
    pass_log = driver.find_element_by_id('form-password')
    submit_log = driver.find_element_by_css_selector('.sc-bxivhb.kMEQZP')

    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "uc-banner-text")))
    driver.find_element_by_id('uc-btn-accept-banner').click()

    email_log.send_keys(mail)
    pass_log.send_keys(password)

    submit_log.click()
    WebDriverWait(driver, 10).until(
        ec.title_contains('Ekskluzywna moda online'))

    driver.get('https://www.zalando-lounge.pl/campaigns/' + campaign)

    labels = driver.find_elements_by_class_name('tabs___link___UQInA')

    # KATEGORIE
    labels[0].click()
    try:
        filters_parent = driver.find_element_by_class_name('styles___categories-wrapper___3ZR1Q')
        for child in filters_parent.find_elements_by_xpath('./li'):
            if not fnmatch.fnmatch(child.find_element_by_xpath('./div/span').text.lower(), 'kobiet*'):
                for innerChild in child.find_elements_by_xpath('./ul/li'):
                    child_s = innerChild.find_element_by_xpath('./div/span')
                    if child_s.text.lower() in category:
                        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/*')))
                        time.sleep(0.1)
                        innerChild.click()
                        time.sleep(0.05)
    except NoSuchElementException:
        try:
            sex_filters = driver.find_elements_by_class_name('GlobalCategoriesSelectorstyles__GlobalCategorySelectorItem-ga6nuy-1.eGnAmb')
            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, 'sc-fzoLsD.jisZkH')))
            for sex in sex_filters:
                sex_span = sex.find_element_by_xpath('./span')
                if sex_span.text.lower() == "mężczyźni":
                    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/*')))
                    time.sleep(0.1)
                    sex.click()
                    time.sleep(0.05)

            filters = driver.find_elements_by_class_name('styles__Wrapper-sc-170uy6j-0.kwQkKn')
            for innerFilter in filters:
                if innerFilter.find_element_by_xpath('./span').text.lower() in category:
                    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/*')))
                    time.sleep(0.1)
                    innerFilter.click()
                    time.sleep(0.05)
        except NoSuchElementException:
            print("WYJĄTEK NIE WZIĘTY POD UWAGĘ PISZ DO MATIEGO X D")

    time.sleep(0.3)
    # ROZMIAR
    if size[0] != '':
        labels[1].click()
        filters_parent = driver.find_element_by_class_name('sizeSelectors___sizes___1FhVI')
        for child in filters_parent.find_elements_by_xpath('./button'):
            child_s = child.find_element_by_xpath('./li/div/span')
            if child_s.text.lower() in size:
                WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/*')))
                time.sleep(0.1)
                child.click()
        time.sleep(0.3)

    # BRAND
    if len(labels) > 6 and brand[0] != '':
        labels[2].click()
        filters_parent = driver.find_element_by_class_name('Brandstyles__BrandList-sc-17c5pap-1.kvMXQM')
        for child in filters_parent.find_elements_by_xpath('./li'):
            child_s = child.find_element_by_xpath('./span')
            if child_s.text.lower() in brand:
                WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/*')))
                time.sleep(0.1)
                child.click()
        time.sleep(0.3)

    # KOLOR
    if color[0] != '':
        if len(labels) == 7:
            labels[4].click()
        else:
            labels[3].click()
        try:
            filters_parent = driver.find_element_by_class_name('color___colors-wrapper___1CIsY')
            for child in filters_parent.find_elements_by_xpath('./button'):
                child_s = child.find_element_by_xpath('./li/div/span/span')
                if child_s.get_attribute('innerHTML').lower() in color:
                    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/*')))
                    time.sleep(0.1)
                    child.click()
        except ElementClickInterceptedException:
            print("Brak produktów w wybranym kolorze, wybierz inny kolor lub pozostaw puste")
            driver.close()
            quit()
        time.sleep(0.3)

    # OPEN TABS
    items = driver.find_elements_by_class_name('Articlestyles__ArticleWrapper-hib3gs-0.eFHNko')
    i = 1
    links = []
    for item in items:
        a = item.find_element_by_xpath('./a')
        links.append(a.get_attribute('href'))

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[i])

    for i in range(len(items)):
        driver.get(links[i])
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'ArticleSizestyles__ArticleSizeItemList-l3goqk-3.iHsGsG')))
        size_chart = driver.find_element_by_class_name('ArticleSizestyles__ArticleSizeItemList-l3goqk-3.iHsGsG')
        for sizeR in size_chart.find_elements_by_xpath('./div'):
            size_t = sizeR.find_element_by_xpath('./div/span')
            if size_t.text.lower() in size:
                sizeR.find_element_by_xpath('./div').click()
        driver.find_element_by_class_name('articleButton___add-to-cart___1Nngf.core___flipper___3yDf4').click()
        time.sleep(0.3)
        i += 1

    time.sleep(0.3)
    driver.switch_to.window(driver.window_handles[0])

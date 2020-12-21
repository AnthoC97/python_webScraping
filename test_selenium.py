# le webdriver gère le navigateur
#la class Keys permet d'utiliser les touches du clavier
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def ebay_example():
    driver = webdriver.Chrome("C:/Users/antho/chromedriver.exe")  # Optional argument, if not specified will search path.
    driver.get("http://www.ebay.fr/")
    # recuperation de la barre de recherche
    search_bar = driver.find_element_by_name("_nkw")
    # recherches des différents iphones
    search_bar.send_keys("iphone")
    search_bar.send_keys(Keys.ENTER)

    nb_page_to_check = 3
    i = 0
    while i < nb_page_to_check:
        # chaque offre est en quelque sorte une balise li de la classe s-item
        # on reccupere toutes ces balises li
        offers = driver.find_elements_by_xpath('//li[@class="s-item    "]')
        print("offer nb : ",len(offers))
        for offer in offers:
            title = offer.find_element_by_xpath('./div/div[2]/a/h3')
            print("title : ",title.text)
            # a corriger pour avoir l'image et le prix -----------------------------------------------------------------
            #     image = offer.find_element_by_css_selector("div.lvpicinner img.img").get_attribute("src")
            #     print("Image : ", image)
            #     price = offer.find_element_by_css_selector("li.lvprice span").text
            #     print("Prix : ", price)
            #     print("")
            # ----------------------------------------------------------------------------------------------------------
        next_page = driver.find_element_by_css_selector("nav.pagination a.pagination__next")
        next_page.click()
        i+=1
        sleep(10)

    # driver.get('http://www.google.com/');
    # sleep(5)  # Let the user actually see something!
    # search_box = driver.find_element_by_name('q')
    # search_box.send_keys('ChromeDriver')
    # search_box.submit()
    sleep(5)  # Let the user actually see something!
    driver.quit()


def cookie_validation_example():
    driver = webdriver.Chrome("C:/Users/antho/chromedriver.exe")
    driver.get("https://www.tutorialspoint.com/locating-child-nodes-of-webelements-in-selenium")
    cookie_button = driver.find_element_by_css_selector("button.sc-bwzfXH.jlyVur")
    sleep(5)
    cookie_button.click()
    sleep(5)
    driver.quit()


if __name__ == "__main__":
    ebay_example()
    # cookie_validation_example()


# https://www.tutorialspoint.com/locating-child-nodes-of-webelements-in-selenium
# //*div/div[2]/a/h3
# full xpath : /html/body/div[4]/div[5]/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/a/h3
# #srp-river-results > ul > li:nth-child(3) > div > div.s-item__info.clearfix > a > h3
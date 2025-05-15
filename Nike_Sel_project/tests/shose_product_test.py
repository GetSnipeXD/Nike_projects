from Nike_Sel_project.Base.Nike_Base import base_nike
from Nike_Sel_project.pages.Welcome_page.top_search_bar_categorys.categorys.New_Feature import New_feature
from Nike_Sel_project.pages.product_page.add_to_bag import add_to_bag
from Nike_Sel_project.pages.product_page.select_shose_size import selecting_shoes_size
from Nike_Sel_project.pages.shop_page.nav_to_products import nav_to_products

shoes_size=selecting_shoes_size()
adding_to_bag=add_to_bag()
product_nav=nav_to_products()
feature=New_feature()
base=base_nike()


driver=base.Base_start()
feature.nav_to_new_feature_page(driver)
product_nav.click_on_shoes_product(driver)
driver.implicitly_wait(10)
shoes_size.select_size_40(driver)
driver.implicitly_wait(10)
adding_to_bag.click_add_to_bag(driver)
base.Base_end(driver)





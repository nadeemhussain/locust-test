from locust import HttpUser, task
import random

class SolrTest(HttpUser):
    @task
    def load_test_index(self):
        id = random.random()
        titles = ["samsung", "iphone", "galaxy", "tv", "ipad", "ipod", "apple watch", "iphone 14", "iphone 13", "samsung s21", "samsung s22", "test title", "load testing"]
        title = random.choice(titles)
        products = list()
        for i in range(1,101):
            product =  {
            "sku": id,
            "sku_config": id,
            "sku_base": id,
            "offer_score": "7758",
            "is_fbn": random.randrange(0,1),
            "seller_rating": random.randrange(1,5),
            "cat":["17728",
            "31234",
            "16039",
            "34218",
            "43563",
            "20941",
            "34125",
            "34511",
            "34128",
            "34097",
            "43630",
            "43632",
            "43320",
            "16539",
            "17277"],
            "fk":[
                "8",
            "2628",
            "3015",
            "8204",
            "8205",
            "9393",
            "10065",
            "2006654",
            "2006663",
            "2008213",
            "2008424",
            "2011786",
            "2014311",
            "2014693",
            "2016645",
            "2017576",
            "2020333",
            "2021149"],
            "warehouse_codes":["W00011919A"],
            "listing_group_key":"N42382990A",
            "object_id": id,
            "rank_score":"95851434",
            "attr_brand":"ehome",
            "en_cat":["Kitchen & Dining",
            "Kitchen Accessories",
            "Aprons",
            "Kitchen Utensils & Gadgets",
            "Home",
            "Home & Kitchen",
            "Women's Fashion",
            "Kitchen & Table Linens"],
            "en_attr_material":"Cotton",
            "en_attr_serve_count":"1",
            "en_model":"HJL1838 HJL1838",
            "ar_cat":["أزياء االنساء",
            "المنزل",
            "المطبخ وأدوات الطعام",
            "إكسسوارات المطابخ",
            "مفروشات المطبخ والطاولات",
            "المنزل والمطبخ",
            "مستلزمات وأجهزة المطابخ",
            "المرايل"],
            "ar_attr_material":"قطن",
            "ar_attr_serve_count":"1",
            "en_title": title,
            "ar_title":"إيهوم مريلة مطبخ بطبعة، من قطعتين متعدد الألوان 38x47سم ",
            "en_brand":"EHOME",
            "en_colour_family":"Multicolour",
            "ar_brand":"إيهوم",
            "ar_colour_family":"متعدد الألوان"}
            products.append(product)
        
        
        self.client.post("update?commitWithin=1000&wt=json", json=products)
    
    # @task
    # def load_test_search(self):
    #     titles = ["samsung", "iphone", "galaxy", "tv", "ipad", "ipod", "apple watch", "iphone 14", "iphone 13", "samsung s21", "samsung s22", "test title", "load testing"]
    #     title = choice(titles)
    #     self.client.get(F"select?df=title&indent=true&q.op=OR&q={title}&useParams=")
        


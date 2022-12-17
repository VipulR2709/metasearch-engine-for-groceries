import pandas as pd
import numpy as np
import json
import os


def json_to_csv_traderjoes(path, list_of_jsons):

    print(list_of_jsons)
    
    list_of_dicts = []
    for file_ in list_of_jsons:
        #read json file
        # Opening JSON file
        prod_json = open(path + "//" +file_)
        print(file_)
        # returns JSON object as 
        # a dictionary
        data = (json.load(prod_json))["data"]["products"]
        
        dict_ = {}
        

        product_ids = []
        product_title = []
        product_url = []
        price_list = []
        ingredient_link = []
        packet_size_list = []
        packet_size_unit_list = []
        availability_list = []

        for product in data["items"]:

            id = product.get("sku")
            product_ids.append(id)
            
            title = product.get("item_title")
            product_title.append(title)

            url = product.get("url_key")
            product_url.append(url)

            # vendor_id = ",".join([x["id"] for x in product["item"]["product_vendors"]])
            # vendor_ids.append(vendor_id)

            price = product.get("retail_price")
            price_list.append(price)

            # rules = str(product["item"]["eligibility_rules"])
            # eligibility_rules.append(rules)

            # check if its out of stock in all stores
            # oos_in_all_stores = product["fulfillment"]["is_out_of_stock_in_all_store_locations"]
            # oos_all_store.append(oos_in_all_stores)

            #Shipping details
            # shipping_availability = product["fulfillment"]["shipping_options"]["availability_status"]
            # availability_shipping.append(shipping_availability)
            
            try:
                if len(product["ingredients"]) > 3:
                    ing = ",".join([x["ingredient"] for x in product["ingredients"]])
                    ingredient_link.append(ing)
                elif len(product["ingredients"]) > 0:
                    ing = product["ingredients"][0]["ingredient"]
                    ingredient_link.append(ing)
                else:
                    ingredient_link.append(np.nan)
            except:
                ingredient_link.append(np.nan)
            packet_size = product["sales_size"]
            packet_size_list.append(packet_size)

            packet_size_unit = product["sales_uom_description"]
            packet_size_unit_list.append(packet_size_unit)

            availability = product["availability"]
            availability_list.append(availability)

        dict_.update({
            "product_ids": product_ids,
            "product_title" : product_title,
            "product_url" : product_url,
            "price" : price_list,
            "ingredient_link" : ingredient_link,
            "packet_size_list": packet_size_list,
            "packet_size_unit_list": packet_size_unit_list,
            "availability_list" : availability_list
        })

        list_of_dicts.append(dict_)
    return list_of_dicts

def json_to_csv_star(path, list_of_jsons):

    print(list_of_jsons)
    
    list_of_dicts = []
    for file_ in list_of_jsons:
        #read json file
        # Opening JSON file
        prod_json = open(path + "//" +file_)
        print(file_)
        # returns JSON object as 
        # a dictionary
        data = (json.load(prod_json))["response"]
        
        dict_ = {}
        

        product_ids = []
        product_title = []
        # product_url = []
        price_list = []
        # packet_size_list = []
        packet_size_unit_list = []
        availability_list = []
        ratings_list = []
        prod_type_list = []

        pickup_eligibility_list= []
        delivery_eligibility_list = []
        inStore_eligibility_list= []
        pickup_availability_list= []
        delivery_availability_list= []
        inStore_availability_list= []
        
        for product in data["docs"]:
            # product = product_["productInfo"]

            id = product.get("pid")
            product_ids.append(id)
            
            title = product.get("name")
            product_title.append(title)

            # url = product.get("productURL")
            # product_url.append(url)

            prod_type = product.get("departmentName")
            prod_type_list.append(prod_type)

            # vendor_id = ",".join([x["id"] for x in product["item"]["product_vendors"]])
            # vendor_ids.append(vendor_id)

            price = product.get("price")
            price_list.append(price)

            # rules = str(product["item"]["eligibility_rules"])
            # eligibility_rules.append(rules)

            # check if its out of stock in all stores
            # oos_in_all_stores = product["fulfillment"]["is_out_of_stock_in_all_store_locations"]
            # oos_all_store.append(oos_in_all_stores)

            #Shipping details
            # shipping_availability = product["fulfillment"]["shipping_options"]["availability_status"]
            # availability_shipping.append(shipping_availability)
            
            # try:
            #     if len(product["ingredients"]) > 3:
            #         ing = ",".join([x["ingredient"] for x in product["ingredients"]])
            #         ingredient_link.append(ing)
            #     elif len(product["ingredients"]) > 0:
            #         ing = product["ingredients"][0]["ingredient"]
            #         ingredient_link.append(ing)
            #     else:
            #         ingredient_link.append(np.nan)
            # except:
            #     ingredient_link.append(np.nan)
            # packet_size = product.get("productSize")
            # packet_size_list.append(packet_size)

            packet_size_unit = product.get("unitOfMeasure")
            packet_size_unit_list.append(packet_size_unit)

            availability = product.get("inventoryAvailable")
            availability_list.append(availability)

            if(product.get("productReview")):
                rating = product.get("productReview").get("avgRating")
            else:
                rating = np.nan
            ratings_list.append(rating)

            pickup_eligibility = product.get("channelEligibility").get("pickUp")
            pickup_eligibility_list.append(pickup_eligibility)

            delivery_eligibility = product.get("channelEligibility").get("delivery")
            delivery_eligibility_list.append(delivery_eligibility)

            inStore_eligibility = product.get("channelEligibility").get("inStore")
            inStore_eligibility_list.append(inStore_eligibility)

            pickup_availability = product.get("channelInventory").get("pickUp")
            pickup_availability_list.append(pickup_availability)

            delivery_availability  = product.get("channelInventory").get("delivery")
            delivery_availability_list.append(delivery_availability)

            inStore_availability  = product.get("channelInventory").get("inStore")
            inStore_availability_list.append(inStore_availability)

        dict_.update({
            "product_ids": product_ids,
            "product_title" : product_title,
            # "product_url" : product_url,
            "price" : price_list,
            "prod_type_list": prod_type_list,
            # "packet_size_list": packet_size_list,
            "packet_size_unit_list": packet_size_unit_list,
            "availability_list" : availability_list,
            "pickup_eligibility_list": pickup_eligibility_list,
            "delivery_eligibility_list" : delivery_eligibility_list,
            "inStore_eligibility_list": inStore_eligibility_list,
            "pickup_availability_list": pickup_availability_list,
            "delivery_availability_list": delivery_availability_list,
            "inStore_availability_list": inStore_availability_list,
            "ratings_list" : ratings_list 
        })

        list_of_dicts.append(dict_)
    return list_of_dicts

def json_to_csv_target(path, list_of_jsons):

    print(list_of_jsons)
    
    list_of_dicts = []
    for file_ in list_of_jsons:
        #read json file
        # Opening JSON file
        prod_json = open(path + "//" +file_)
        print(file_)
        # returns JSON object as 
        # a dictionary
        data = (json.load(prod_json))["data"]
        
        dict_ = {}
        

        product_ids = []
        product_title = []
        product_url = []
        vendor_ids = []
        price_list = []
        eligibility_rules = []
        oos_all_store = []
        availability_shipping = []
        shipping_min_date = []
        shipping_max_date = []
        two_days_shipping_availability = []
        store_ids = []
        store_names = []
        pickup_availability = []
        pickup_date = []
        delivery_availability = []

        for product in data["product_summaries"]:

            id = product["tcin"]
            product_ids.append(id)
            
            title = product["item"]["product_description"]["title"]
            product_title.append(title)

            url = product["item"]["enrichment"]["buy_url"]
            product_url.append(url)

            vendor_id = ",".join([x["id"] for x in product["item"]["product_vendors"]])
            vendor_ids.append(vendor_id)

            price = product["price"].get("current_retail")
            price_list.append(price)

            rules = str(product["item"]["eligibility_rules"])
            eligibility_rules.append(rules)

            # check if its out of stock in all stores
            oos_in_all_stores = product["fulfillment"]["is_out_of_stock_in_all_store_locations"]
            oos_all_store.append(oos_in_all_stores)

            #Shipping details
            shipping_availability = product["fulfillment"]["shipping_options"]["availability_status"]
            availability_shipping.append(shipping_availability)

            if len(product["fulfillment"]["shipping_options"]["services"]) > 0:
                min_date = product["fulfillment"]["shipping_options"]["services"][0]["min_delivery_date"]
                shipping_min_date.append(min_date)

                max_date = product["fulfillment"]["shipping_options"]["services"][0]["max_delivery_date"]
                shipping_max_date.append(shipping_max_date)

                two_days_shipping = product["fulfillment"]["shipping_options"]["services"][0]["is_two_day_shipping"]
                two_days_shipping_availability.append(two_days_shipping)
            else:
                shipping_min_date.append(np.nan)
                shipping_max_date.append(np.nan)
                two_days_shipping_availability.append(np.nan)

            #Store Pickup details
            if len(product["fulfillment"]["store_options"]) > 0:
                pickup_store_id = product["fulfillment"]["store_options"][0]["location_id"]
                store_ids.append(pickup_store_id)

                pickup_store_name = product["fulfillment"]["store_options"][0]["store"]["location_name"] 
                store_names.append(pickup_store_name)

                pickup_avail = product["fulfillment"]["store_options"][0]["order_pickup"]["availability_status"]
                pickup_availability.append(pickup_avail)
            
                pickup_date_ = product["fulfillment"]["store_options"][0]["order_pickup"].get("pickup_date")
                pickup_date.append(pickup_date_)
            else:
                store_ids.append(np.nan)
                store_names.append(np.nan)
                pickup_availability.append(np.nan)
                pickup_date.append(np.nan)

            #Delivery details
            delivery_availability_ = product["fulfillment"]["scheduled_delivery"]["availability_status"]
            delivery_availability.append(delivery_availability_)

        dict_.update({
            "product_ids": product_ids,
            "product_title" : product_title,
            "product_url" : product_url,
            "vendor_ids" : vendor_ids,
            "price" : price_list,
            "eligibility_rules" : eligibility_rules,
            "oos_all_store" : oos_all_store,
            "availability_shipping" : availability_shipping,
            "shipping_min_date" : shipping_min_date,
            "shipping_max_date" : shipping_max_date,
            "two_days_shipping_availability" : two_days_shipping_availability,
            "store_ids" : store_ids,
            "store_names" : store_names,
            "pickup_availability" : pickup_availability,
            "pickup_date" : pickup_date,
            "delivery_availability" : delivery_availability
        })

        list_of_dicts.append(dict_)
    return list_of_dicts

def json_to_csv_walgreens(path, list_of_jsons):

    print(list_of_jsons)
    
    list_of_dicts = []
    for file_ in list_of_jsons:
        #read json file
        # Opening JSON file
        prod_json = open(path + "//" +file_)
        print(file_)
        # returns JSON object as 
        # a dictionary
        data = (json.load(prod_json))
        
        dict_ = {}
        

        product_ids = []
        product_title = []
        product_url = []
        price_list = []
        packet_size_list = []
        packet_size_unit_list = []
        availability_list = []
        ratings_list = []
        prod_type_list = []

        for product_ in data["productList"]:
            product = product_["productInfo"]

            id = product.get("dsSkuId")
            product_ids.append(id)
            
            title = product.get("productName")
            product_title.append(title)

            url = product.get("productURL")
            product_url.append(url)

            prod_type = product.get("productType")
            prod_type_list.append(prod_type)

            # vendor_id = ",".join([x["id"] for x in product["item"]["product_vendors"]])
            # vendor_ids.append(vendor_id)

            price = product.get("priceInfo").get("regularPrice")
            price_list.append(price)

            # rules = str(product["item"]["eligibility_rules"])
            # eligibility_rules.append(rules)

            # check if its out of stock in all stores
            # oos_in_all_stores = product["fulfillment"]["is_out_of_stock_in_all_store_locations"]
            # oos_all_store.append(oos_in_all_stores)

            #Shipping details
            # shipping_availability = product["fulfillment"]["shipping_options"]["availability_status"]
            # availability_shipping.append(shipping_availability)
            
            # try:
            #     if len(product["ingredients"]) > 3:
            #         ing = ",".join([x["ingredient"] for x in product["ingredients"]])
            #         ingredient_link.append(ing)
            #     elif len(product["ingredients"]) > 0:
            #         ing = product["ingredients"][0]["ingredient"]
            #         ingredient_link.append(ing)
            #     else:
            #         ingredient_link.append(np.nan)
            # except:
            #     ingredient_link.append(np.nan)
            packet_size = product.get("productSize")
            packet_size_list.append(packet_size)

            packet_size_unit = product.get("unitPriceSize")
            packet_size_unit_list.append(packet_size_unit)

            availability = product.get("storeInv")
            availability_list.append(availability)

            rating = product.get("averageRating")
            ratings_list.append(rating)

        dict_.update({
            "product_ids": product_ids,
            "product_title" : product_title,
            "product_url" : product_url,
            "price" : price_list,
            "prod_type_list": prod_type_list,
            "packet_size_list": packet_size_list,
            "packet_size_unit_list": packet_size_unit_list,
            "availability_list" : availability_list,
            "ratings_list": ratings_list
        })

        list_of_dicts.append(dict_)
    return list_of_dicts

def create_merge_dfs(list_of_dict):

    main_df = pd.DataFrame(list_of_dict[0], columns = list(list_of_dict[0].keys()))
    print("------------",len(list_of_dict))
    for dict_ in list_of_dict[1:]:
        df = pd.DataFrame(dict_, columns = list(dict_.keys()))
        
        main_df = main_df.append(df)

    return main_df

# Main function to call all the necessary conversion functions and exporting final datasets to csv
def main():
    
    # Mention a path to folder containing all the json files (Responses of store URLs)
    path = "Scripts\All Web Responses"
    
    # Checking all the jsons for store - Target
    target_dir_list = [filename for filename in os.listdir(path) if "target" in filename.lower()]
    data_dicts_target = json_to_csv_target(path, target_dir_list)
    target_merged_data = create_merge_dfs(data_dicts_target)
    target_merged_data.to_csv("Data\\Target_Products.csv")

    # Checking all the jsons for store - Star
    star_dir_list = [filename for filename in os.listdir(path) if "star" in filename.lower()]
    data_dicts_star = json_to_csv_star(path, star_dir_list)
    star_merged_data = create_merge_dfs(data_dicts_star)
    star_merged_data.to_csv("Data\\Star_Products.csv")

    # Checking all the jsons for store - TraderJoes
    traderjoes_dir_list = [filename for filename in os.listdir(path) if "trader" in filename.lower()]
    data_dicts_traderjoes = json_to_csv_traderjoes(path, traderjoes_dir_list)
    traderjoes_merged_data = create_merge_dfs(data_dicts_traderjoes)
    traderjoes_merged_data.to_csv("Data\\TraderJoes_Products.csv")

    # Checking all the jsons for store - Walgreens
    walgreens_dir_list = [filename for filename in os.listdir(path) if "walgreen" in filename.lower()]
    data_dicts_walgreens = json_to_csv_walgreens(path, walgreens_dir_list)
    walgreens_merged_data = create_merge_dfs(data_dicts_walgreens)
    walgreens_merged_data.to_csv("Data\\Walgreens_Products.csv")


if __name__ == "__main__":
    main()
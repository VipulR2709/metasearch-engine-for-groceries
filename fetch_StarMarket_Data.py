import pandas as pd
import numpy as np
import json
import os




def json_to_csv(path, list_of_jsons):

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

def create_merge_dfs(list_of_dict):

    main_df = pd.DataFrame(list_of_dict[0], columns = list(list_of_dict[0].keys()))
    print("------------",len(list_of_dict))
    for dict_ in list_of_dict[1:]:
        df = pd.DataFrame(dict_, columns = list(dict_.keys()))
        
        main_df = main_df.append(df)

    return main_df


def main():
    target_prod_json_list = []

    path = "D://MSIS//DMDD//Scraping//Star"
    dir_list = os.listdir(path)

    data_dicts = json_to_csv(path, dir_list)

    merged_data = create_merge_dfs(data_dicts)

    merged_data.to_csv("Star_Product.csv")


if __name__ == "__main__":
    main()
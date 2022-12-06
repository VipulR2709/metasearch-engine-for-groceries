import pandas as pd
import numpy as np
import json
import os


# data = product_summaries":[
#           {
#              "__typename":"ProductSummary",
#              "tcin":"13782536",
#              "item":{
#                 "relationship_type_code":"SA",
#                 "product_description":{
#                    "title":"General Mills Chocolate Chex Sweetened Rice Cereal - 10oz"
#                 },
#                 "enrichment":{
#                    "buy_url":"https://www.target.com/p/general-mills-chocolate-chex-sweetened-rice-cereal-10oz/-/A-13782536"
#                 },
#                 "fulfillment":{
                   
#                 },
#                 "merchandise_classification":{
#                    "class_id":0,
#                    "department_id":231
#                 },
#                 "product_vendors":[
#                    {
#                       "id":"2330590"
#                    }
#                 ],
#                 "eligibility_rules":{
                   
#                 }
#              },
#              "price":{
#                 "current_retail":3.99
#              },
#              "promotions":[
#                 {
#                    "ship_method":[
#                       "SCHEDULED_DELIVERY_PPO",
#                       "PickupInStore",
#                       "SCHEDULED_DELIVERY"
#                    ]
#                 }
#              ],
#              "fulfillment":{
#                 "product_id":"13782536",
#                 "is_out_of_stock_in_all_store_locations":false,
#                 "shipping_options":{
#                    "availability_status":"IN_STOCK",
#                    "loyalty_availability_status":"IN_STOCK",
#                    "services":[
#                       {
#                          "shipping_method_id":"STANDARD",
#                          "min_delivery_date":"2022-12-09",
#                          "max_delivery_date":"2022-12-09",
#                          "is_two_day_shipping":false,
#                          "is_base_shipping_method":true
#                       }
#                    ]
#                 },
#                 "store_options":[
#                    {
#                       "search_response_store_type":"PRIMARY",
#                       "location_id":"1898",
#                       "store":{
#                          "location_name":"Boston South Bay"
#                       },
#                       "order_pickup":{
#                          "availability_status":"IN_STOCK",
#                          "pickup_date":"2022-12-04",
#                          "guest_pick_sla":120,
#                          "location_locale":"America/New_York"
#                       },
#                       "in_store_only":{
#                          "availability_status":"IN_STOCK"
#                       }
#                    }
#                 ],
#                 "scheduled_delivery":{
#                    "availability_status":"IN_STOCK"
#                 }
#              }
#           }]

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

def create_merge_dfs(list_of_dict):

    main_df = pd.DataFrame(list_of_dict[0], columns = list(list_of_dict[0].keys()))
    print("------------",len(list_of_dict))
    for dict_ in list_of_dict[1:]:
        df = pd.DataFrame(dict_, columns = list(dict_.keys()))
        
        main_df = main_df.append(df)

    return main_df


def main():
    target_prod_json_list = []

    path = "D://MSIS//DMDD//Scraping//Target Products"
    dir_list = os.listdir(path)

    data_dicts = json_to_csv(path, dir_list)

    merged_data = create_merge_dfs(data_dicts)

    merged_data.to_csv("Target_Product.csv")


if __name__ == "__main__":
    main()
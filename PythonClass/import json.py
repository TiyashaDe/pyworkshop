import json
 def main():
     cities_file=open("cities.json")
     cities_data=json.load(cities_file)
     print(cities_data)
     
if __name__ =="__main__":
    main()
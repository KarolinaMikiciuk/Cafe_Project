import pandas
import csv

def update_file_value(category,column_name, entry_id,change_entry_to):  #column name and change_entry_to should be lists
    
    df = pandas.read_csv(f"{category}_list.csv") #read
    if category == "products":
        df.at[df.product_id == entry_id, column_name] = change_entry_to  #location is the row number starting at row 0
    elif category == "couriers":
        df.at[df.couriers_id == entry_id, column_name] = change_entry_to
    elif category == "orders":
        df.at[df.orders_id == entry_id, column_name] = change_entry_to  #location is the row number starting at row 0
        
    df.to_csv(f"{category}_list.csv", index = False)  #write
    

def show_file_contents(category):  #you can type the range in so you dont have to see all
    df = pandas.read_csv(f"{category}_list.csv")
    print(df)

def add_to_file(category,entry):    #works
    with open(f"{category}_list.csv","a+") as file:
        writer = csv.writer(file)
        row = []
        if type(entry) == dict:
            for key,value in entry.items():
                row.append(value)
            writer.writerow(row)
        elif type(entry) == list:
            for item in entry:
                row.append(item)
            writer.writerow(row)
        
def delete_entry(category,entry_id):
    df = pandas.read_csv(f'{category}_list.csv')
    df.drop(labels=[entry_id],axis=0,inplace=True)
    df.to_csv(f'{category}_list.csv', index=False)
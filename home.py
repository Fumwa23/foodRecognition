import utils.ai_tools as ai_tools
from datetime import datetime

def main():
    new_item("images/6_apples.jpg")
    
def new_item(image_path ):
    #declare the prompt
    prompt = "Return a dictionary based on the content in the image which contains: {\"type of food\": \"number of items\"}"
    
    #get the current time
    now = datetime.now()
    
    #get the current date in the format: day/month/year
    date = now.strftime("%d/%b/%y")
    
    #get the current time in the format: hour:minute
    time = now.strftime("%H:%M")
    
    #get the source of the food
    source = input("Enter source of food: ")
    
    # using the prompt and the image path, we can get the items and their quantity
    items_and_quantity = ai_tools.read_image(prompt=prompt, image_path=image_path)
    
    
    print(items_and_quantity)
    return items_and_quantity
    

if __name__ == "__main__":
    main()
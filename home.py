import ai_tools

def main():
    new_item()
    
def new_item(prompt, image_path, ):
    print("New item")
    item = input("Enter item: ")
    ai_tools.add_item(item)

if __name__ == "__main__":
    main()
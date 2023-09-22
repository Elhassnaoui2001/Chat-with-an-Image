from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
def get_image_caption(image_path):
    """
    Generates a short caption for the provided image....
    Args :
        image_path (str) : The path to the image file
        
    Returns :
    str: A string representing the caption for the image    
    """
    image = Image.open(image_path).convert("RGB")
    
    model_name = "Salesforce/blip-image-captioning-large"
    device = "cpu" #cuda
    
    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)
    
    inputs = processor(image , return_tensors='pt').to(device)
    output = model.generate(**inputs , max_new_tokens=20)
    
    caption = processor.decode(output[0], skip_special_tokens=True)
    
    return caption
    

def detect_objects(image_path):
    """Detects objects in the provided image ...."""
    pass

if __name__ == '__main__':
    image_path ='E:/photosIMG_20210326_122349.jpg'
    caption = get_image_caption(image_path)
    print(caption)
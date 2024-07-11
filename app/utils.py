from PIL import Image as PilImage
import io

def process_image(image_data):
    image = PilImage.open(io.BytesIO(image_data))
    image = image.resize((100, 100))
    output = io.BytesIO()
    image.save(output, format='JPEG')
    return output.getvalue()
    
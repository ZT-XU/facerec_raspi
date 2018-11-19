import face_recognition
from PIL import Image, ImageDraw

while True:
# Load an image with an unknown face
    try:
        unknown_image = face_recognition.load_image_file("frame.jpg")

        # Find all the faces and face encodings in the unknown image
        face_locations = face_recognition.face_locations(unknown_image)

        # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
        # See http://pillow.readthedocs.io/ for more about PIL/Pillow
        pil_image = Image.fromarray(unknown_image)
        # Create a Pillow ImageDraw Draw instance to draw with
        draw = ImageDraw.Draw(pil_image)

        # Loop through each face found in the unknown image
        for (top, right, bottom, left) in face_locations:

            # Draw a box around the face using the Pillow module
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0))



        # Remove the drawing library from memory as per the Pillow docs
        del draw

        # Display the resulting image
        pil_image.save("frame2.jpg")
        with open("proceed.txt","r") as f:
            b = f.read()
        if not eval(b):
            break
    except:
        pass
    #with open("proceed.txt","r") as f:
     #   b = f.read()
    #if not eval(b):
       # break
    # You can also save a copy of the new image to disk if you want by uncommenting this line
    # pil_image.save("image_with_boxes.jpg")
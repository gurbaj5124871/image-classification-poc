from PIL import Image
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # pretrained YOLOv8n model

print("Model initialised")
image_url = input("Please provide the image url to inference: ")

# Run batched inference on a list of images
results = model(
    [
        image_url
    ]
)  # return a list of Results objects


# print(results)

# Process results list
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save("results.jpg")  # save image

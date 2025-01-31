# Image classification

This is a POC to label the provided image url using the image classification model YOLO-V8

## Get started

1. Make sure you have poetry installed

```
pipx install poetry
```

2. Install dependencies

```
poetry install
```

3. Run the script using below command:

```
poetry run python3 yolov8/__main__.py
```

## Example Result

Example Image used:

![Image of a sheep](https://media.istockphoto.com/id/645788690/photo/funny-sheep-portrait-of-sheep-showing-tongue.jpg?s=612x612&w=0&k=20&c=QeL2ZWDvP1rrEtPw_zl4BTHxKILn1IRxDKs_YKSdrbo=)

Result:

![Inferenced image of a sheep](results.jpg)

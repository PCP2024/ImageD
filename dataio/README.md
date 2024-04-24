# ImageLoader Class Usage Guide

Written by Anastasia Simonoff for ImageD; PCP, 2024.

## Introduction
The `ImageLoader` class is a utility class designed to simplify the process of loading images in your application.

## Installation
To use the `ImageLoader` class, simply import it into the folder that you need.

```python
from ..dataio.imageLoader import ImageLoader
```

## Usage

### Loading an Image

To load an image, create an instance of `ImageLoader` and call the `load_image` method with the path to your image file. It will return a PIL Image object.

```python
loader = ImageLoader()
image = loader.load_image('path/to/your/image.png')
```

### Displaying an Image

To display an image, you can use the `show_image` method. This will open a new window displaying the image.

```python
loader.show_image(image)
```

### Handling Errors

If the image cannot be loaded, the `load_image` method will throw an `ImageLoadException`. You should catch this exception and handle it appropriately in your code.

```python
try:
    image = loader.load_image('path/to/your/image.png')
except ImageLoadException:
    print('Failed to load image.')
```

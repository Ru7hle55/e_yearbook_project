from django.core.exceptions import ValidationError

def validate_image_size(image):
    # Maximum allowed file size in bytes (5MB)
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError('The image file exceeds the maximum allowed size of 5MB.')

import base64, uuid
from django.core.files.base import ContentFile


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_report_image(string_img):
    unnecessary_titles, string_image = string_img.split(';base64, ')
    decoded_img = base64.b64decode(string_image)
    img_name = str(uuid.uuid4())[:10] + ".png"
    image = ContentFile(decoded_img, img_name)
    return image


from celery import shared_task
from .models import ImageUpload
from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings

@shared_task
def process_image_task(image_id):
    try:
        print("Running task")
        image_obj = ImageUpload.objects.get(id=image_id)
        image_obj.status = 'processing'
        image_obj.save()

        input_path = image_obj.original_image.path
        output_path = os.path.join(settings.MEDIA_ROOT, 'processed', f'processed_{os.path.basename(input_path)}')
        os.makedirs(os.path.join(settings.MEDIA_ROOT, 'processed'), exist_ok=True)

        with Image.open(input_path) as img:
            img = img.resize((300, 300))
            img.save(output_path)

        rel_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
        image_obj.processed_image.name = rel_path
        image_obj.status = 'done'
        image_obj.save()
    except Exception:
        image_obj.status = 'failed'
        image_obj.save()

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from PIL import Image
import numpy as np
from .utils import classify_emotion
from io import BytesIO
from django.core.files.base import ContentFile

BACKEND_CHOICES = (
    ('opencv', 'Open Computer Vision'),
    ('mtcnn', 'Multi-task Cascaded Convolutional Neural Networks'),
    ('dlib', 'Dlib'),
    ('ssd', 'Single Shot Detector')
)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    detector = models.CharField(max_length=50, choices=BACKEND_CHOICES, default='mtcnn')
    image = models.ImageField(default='default.jpg', blank=False, upload_to='face_pictures', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    emotion = models.TextField(default='Failed')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        pil_img = Image.open(self.image)
        cv_img = np.array(pil_img)
        predictions = classify_emotion(cv_img, self.detector)
        self.emotion = predictions[1]

        img_pil = Image.fromarray(predictions[0])

        buffer = BytesIO()
        img_pil.save(buffer, format='jpeg')
        image_png = buffer.getvalue()
        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

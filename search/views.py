import numpy as np
import speech_recognition as sr
import tensorflow as tf
from PIL import Image
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from mobile.models import Mobile
from book.serializers import BookSerializer
from mobile.serializers import MobileSerializer


# Create your views here.
class SearchBookAPI(APIView):
    def get(self, request):
        searched = request.GET.get('searched')
        if searched:
            books = Book.objects.filter(name__icontains=searched).order_by('name')
        else:
            books = Book.objects.none()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchMobileAPI(APIView):
    def get(self, request):
        searched = request.GET.get('searched')
        if searched:
            mobiles = Mobile.objects.filter(name__icontains=searched).order_by('name')
        else:
            mobiles = Mobile.objects.none()

        serializer = MobileSerializer(mobiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


model = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))


def extract_features(image):
    preprocessed_image = preprocess_image(image)
    features = model.predict(preprocessed_image)
    features = features.flatten()
    return features


def preprocess_image(image):
    image = image.resize((224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.vgg16.preprocess_input(image)
    return image


def search_by_image(request):
    uploaded_image = request.FILES['image']
    searched_image = Image.open(uploaded_image)

    image_features = extract_features(searched_image)

    all_books = Book.objects.all()

    threshold = 50

    books = []
    for book in all_books:
        book_image = Image.open(book.image)
        book_features = extract_features(book_image)
        distance = np.linalg.norm(image_features - book_features)
        if distance < threshold:
            books.append(book)

    context = {'books': books}

    return render(request, 'search.html', {'context': context})


def search_by_voice(request):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    searched = recognizer.recognize_google(audio)
    books = Book.objects.filter(name__icontains=searched).order_by('name')

    context = {
        'books': books
    }
    return render(request, 'search.html', {'context': context, 'searched': searched})

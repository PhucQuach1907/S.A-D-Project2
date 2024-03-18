import numpy as np
import speech_recognition as sr
import tensorflow as tf
from PIL import Image
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookSerializer
from clothes.models import Clothes
from clothes.serializers import ClothesSerializer
from mobile.models import Mobile
from mobile.serializers import MobileSerializer


# Create your views here.
class SearchAPI(APIView):
    def get(self, request):
        searched = request.GET.get('searched')
        type = request.GET.get('type')
        if searched and type == '1':
            products = Book.objects.filter(name__icontains=searched).order_by('name')
        elif searched and type == '2':
            products = Mobile.objects.filter(name__icontains=searched).order_by('name')
        elif searched and type == '3':
            products = Clothes.objects.filter(name__icontains=searched).order_by('name')
        else:
            products = Book.objects.none()

        if type == '1':
            serializer = BookSerializer(products, many=True)
        elif type == '2':
            serializer = MobileSerializer(products, many=True)
        elif type == '3':
            serializer = ClothesSerializer(products, many=True)
        else:
            serializer = BookSerializer(products, many=True)
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


class SearchImageAPI(APIView):
    def post(self, request):
        type = request.data.get('type')
        if 'image' not in request.FILES:
            return Response({"error": "No image uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        uploaded_image = request.FILES['image']

        try:
            searched_image = Image.open(uploaded_image)
        except Exception as e:
            return Response({"error": f"Error opening image: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        image_features = extract_features(searched_image)

        threshold = 50

        if type == '1':
            all_books = Book.objects.all()
            matched_books = []
            for book in all_books:
                try:
                    book_image = Image.open(book.image)
                    book_features = extract_features(book_image)
                    distance = np.linalg.norm(image_features - book_features)
                    if distance < threshold:
                        matched_books.append(book)
                except Exception as e:
                    print(f"Error processing image for book {book.id}: {str(e)}")

            serializer = BookSerializer(matched_books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif type == '2':
            all_mobiles = Mobile.objects.all()
            matched_mobiles = []
            for mobile in all_mobiles:
                try:
                    mobile_image = Image.open(mobile.image)
                    mobile_features = extract_features(mobile_image)
                    distance = np.linalg.norm(image_features - mobile_features)
                    if distance < threshold:
                        matched_mobiles.append(mobile)
                except Exception as e:
                    print(f"Error processing image for mobile {mobile.id}: {str(e)}")

            serializer = MobileSerializer(matched_mobiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif type == '3':
            all_clothes = Clothes.objects.all()
            matched_clothes = []
            for cloth in all_clothes:
                try:
                    cloth_image = Image.open(cloth.image)
                    cloth_features = extract_features(cloth_image)
                    distance = np.linalg.norm(image_features - cloth_features)
                    if distance < threshold:
                        matched_clothes.append(cloth)
                except Exception as e:
                    print(f"Error processing image for mobile {cloth.id}: {str(e)}")

            serializer = ClothesSerializer(matched_clothes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            products = Book.objects.none()
            serializer = BookSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


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


class SearchByVoiceAPI(APIView):
    def post(self, request):
        recognizer = sr.Recognizer()

        try:
            audio_file = request.FILES['audio']
        except KeyError:
            return Response({"error": "No audio file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        try:
            searched = recognizer.recognize_google(audio_data)
            books = Book.objects.filter(name__icontains=searched).order_by('name')
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except sr.UnknownValueError:
            return Response({"error": "Unable to recognize audio"}, status=status.HTTP_400_BAD_REQUEST)

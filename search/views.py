import numpy as np
import speech_recognition as sr
import tensorflow as tf
from PIL import Image
from django.shortcuts import render

from book.models import Book


# Create your views here.
def search(request):
    searched = request.GET.get('searched')
    if searched:
        books = Book.objects.filter(name__icontains=searched).order_by('name')
    else:
        books = Book.objects.all().order_by('name')

    context = {
        'books': books
    }
    return render(request, 'search_results.html', {'context': context, 'searched': searched})


model = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))


def extract_features(image):
    # Tiền xử lý ảnh và trích xuất đặc trưng bằng cách sử dụng mô hình đã được đào tạo
    preprocessed_image = preprocess_image(image)
    features = model.predict(preprocessed_image)
    # Chuyển đổi ma trận đặc trưng thành mảng 1 chiều
    features = features.flatten()
    return features


def preprocess_image(image):
    # Chuyển đổi ảnh thành định dạng phù hợp cho mô hình
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

    return render(request, 'search_results.html', {'context': context})


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
    return render(request, 'search_results.html', {'context': context, 'searched': searched})

function displayCloth(cloth, clothesList) {
    const clothContainer = document.createElement('div');
    clothContainer.className = 'book_container';

    const clothImageDiv = document.createElement('div');
    if (cloth.image) {
        const clothImage = document.createElement('img');
        clothImage.src = cloth.image;
        clothImage.alt = 'Cloth Image';
        clothImage.style.width = '300px';
        clothImage.style.height = '400px';
        clothImage.style.margin = '10px';
        clothImage.style.border = '1px solid';
        clothImageDiv.appendChild(clothImage);
    }

    const clothInfoDiv = document.createElement('div');
    const nameParagraph = document.createElement('p');
    nameParagraph.className = 'book_content';
    nameParagraph.textContent = 'Name: ' + cloth.name;
    const brandParagraph = document.createElement('p');
    brandParagraph.className = 'book_content';
    brandParagraph.textContent = 'Brand: ' + cloth.brand_name;
    const statusParagraph = document.createElement('p');
    statusParagraph.className = 'book_content';
    statusParagraph.textContent = cloth.quantity >= 1 ? 'Status: In stock' : 'Status: Out of stock';
    const priceParagraph = document.createElement('p');
    priceParagraph.className = 'book_content';
    priceParagraph.textContent = 'Price: ' + formatPrice(cloth.price);

    const form = document.createElement('form');
    form.className = 'book_button';
    form.method = 'POST';
    form.action = 'clothes/add-to-cart/' + cloth.id + '/';
    const csrfInput = document.createElement('input');
    csrfInput.type = 'hidden';
    csrfInput.name = 'csrfmiddlewaretoken';
    csrfInput.value = getCookie('csrftoken');
    const addButton = document.createElement('button');
    addButton.id = 'book_button';
    addButton.type = 'submit';
    addButton.textContent = 'Add To Cart';

    form.appendChild(csrfInput);
    form.appendChild(addButton);

    clothInfoDiv.appendChild(nameParagraph);
    clothInfoDiv.appendChild(brandParagraph);
    clothInfoDiv.appendChild(statusParagraph);
    clothInfoDiv.appendChild(priceParagraph);
    clothInfoDiv.appendChild(form);

    clothContainer.appendChild(clothImageDiv);
    clothContainer.appendChild(clothInfoDiv);

    clothesList.appendChild(clothContainer);
}

function displayClothes() {
    fetch('http://127.0.0.1:8000/api/clothes/')
        .then(response => response.json())
        .then(data => {
            const clothesList = document.getElementById('clothes-list');
            clothesList.innerHTML = '';

            data.results.forEach(cloth => {
                displayCloth(cloth, clothesList);
            })

        })
        .catch(error => console.error('Error fetching books:', error));
}

function displaySearchedClothes(data) {
    const clothesList = document.getElementById('clothes-list');
    clothesList.innerHTML = '';

    data.forEach(cloth => {
        displayBook(cloth, clothesList);
    })
}

function handleSearchCloth(event) {
    event.preventDefault();

    const searchInput = document.getElementById('search-by-word-input');
    const searched = searchInput.value.trim();
    const type = 3;
    if (searched) {
        fetch(`http://127.0.0.1:8000/api/search?searched=${searched}&type=${type}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                displaySearchedClothes(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    } else {
        displayClothes();
    }
}

function handleSearchImageCloth(event) {
    const input = document.getElementById('image');
    const file = input.files[0];
    if (!file) {
        alert("Please select an image.");
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    const type = 3;
    formData.append('type', type);

    fetch(`http://127.0.0.1:8000/api/search-image/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            displaySearchedClothes(data);
        })
        .catch(error => console.error('Error:', error));
}

function displayMobile(mobile, mobileList) {
    const mobileContainer = document.createElement('div');
    mobileContainer.className = 'book_container';

    const mobileImageDiv = document.createElement('div');
    if (mobile.image) {
        const mobileImage = document.createElement('img');
        mobileImage.src = mobile.image;
        mobileImage.alt = 'Mobile Image';
        mobileImage.style.width = '300px';
        mobileImage.style.height = '400px';
        mobileImage.style.margin = '10px';
        mobileImage.style.border = '1px solid';
        mobileImageDiv.appendChild(mobileImage);
    }

    const mobileInfoDiv = document.createElement('div');
    const nameParagraph = document.createElement('p');
    nameParagraph.className = 'book_content';
    nameParagraph.textContent = 'Name: ' + mobile.name;
    const producerParagraph = document.createElement('p');
    producerParagraph.className = 'book_content';
    producerParagraph.textContent = 'Producer: ' + mobile.producer;
    const statusParagraph = document.createElement('p');
    statusParagraph.className = 'book_content';
    statusParagraph.textContent = mobile.quantity >= 1 ? 'Status: In stock' : 'Status: Out of stock';
    const priceParagraph = document.createElement('p');
    priceParagraph.className = 'book_content';
    priceParagraph.textContent = 'Price: ' + formatPrice(mobile.price);

    const form = document.createElement('form');
    form.className = 'book_button';
    form.method = 'POST';
    form.action = 'mobiles/' + mobile.id + '/';
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

    mobileInfoDiv.appendChild(nameParagraph);
    mobileInfoDiv.appendChild(producerParagraph);
    mobileInfoDiv.appendChild(statusParagraph);
    mobileInfoDiv.appendChild(priceParagraph);
    mobileInfoDiv.appendChild(form);

    mobileContainer.appendChild(mobileImageDiv);
    mobileContainer.appendChild(mobileInfoDiv);

    mobileList.appendChild(mobileContainer);
}

function displayMobiles() {
    fetch('http://127.0.0.1:8000/api/mobiles/')
        .then(response => response.json())
        .then(data => {
            const mobileList = document.getElementById('mobile-list');
            mobileList.innerHTML = '';

            data.results.forEach(mobile => {
                displayMobile(mobile, mobileList);
            });
        })
        .catch(error => console.error('Error fetching mobiles:', error));
}

function displaySearchedMobiles(data) {
    const mobileList = document.getElementById('mobile-list');
    mobileList.innerHTML = '';

    data.forEach(mobile => {
        displayMobile(mobile, mobileList);
    })
}

function handleSearchMobile(event) {
    event.preventDefault();

    const searchInput = document.getElementById('search-by-word-input');
    const searched = searchInput.value.trim();
    if (searched) {
        fetch(`http://127.0.0.1:8000/api/search-mobile/?searched=${searched}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                displaySearchedMobiles(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    } else {
        displayMobiles();
    }
}
function displayBook(book, bookList) {
    const bookContainer = document.createElement('div');
    bookContainer.className = 'book_container';

    const bookImageDiv = document.createElement('div');
    if (book.image) {
        const bookImage = document.createElement('img');
        bookImage.src = book.image;
        bookImage.alt = 'Book Image';
        bookImage.style.width = '300px';
        bookImage.style.height = '400px';
        bookImage.style.margin = '10px';
        bookImage.style.border = '1px solid';
        bookImageDiv.appendChild(bookImage);
    }

    const bookInfoDiv = document.createElement('div');
    const nameParagraph = document.createElement('p');
    nameParagraph.className = 'book_content';
    nameParagraph.textContent = 'Name: ' + book.name;
    const authorParagraph = document.createElement('p');
    authorParagraph.className = 'book_content';
    authorParagraph.textContent = 'Author: ' + book.author;
    const publisherParagraph = document.createElement('p');
    publisherParagraph.className = 'book_content';
    publisherParagraph.textContent = 'Publisher: ' + book.publisher;
    const statusParagraph = document.createElement('p');
    statusParagraph.className = 'book_content';
    statusParagraph.textContent = book.quantity >= 1 ? 'Status: In stock' : 'Status: Out of stock';
    const priceParagraph = document.createElement('p');
    priceParagraph.className = 'book_content';
    priceParagraph.textContent = 'Price: ' + formatPrice(book.price);

    const form = document.createElement('form');
    form.className = 'book_button';
    form.method = 'POST';
    form.action = 'books/' + book.id + '/';
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

    bookInfoDiv.appendChild(nameParagraph);
    bookInfoDiv.appendChild(authorParagraph);
    bookInfoDiv.appendChild(publisherParagraph);
    bookInfoDiv.appendChild(statusParagraph);
    bookInfoDiv.appendChild(priceParagraph);
    bookInfoDiv.appendChild(form);

    bookContainer.appendChild(bookImageDiv);
    bookContainer.appendChild(bookInfoDiv);

    bookList.appendChild(bookContainer);
}

function displayBooks() {
    fetch('http://127.0.0.1:8000/api/books/')
        .then(response => response.json())
        .then(data => {
            const bookList = document.getElementById('book-list');
            bookList.innerHTML = '';

            data.results.forEach(book => {
                displayBook(book, bookList);
            })

        })
        .catch(error => console.error('Error fetching books:', error));
}

function displaySearchedBooks(data) {
    const bookList = document.getElementById('book-list');
    bookList.innerHTML = '';

    data.forEach(book => {
        displayBook(book, bookList);
    })
}

function handleSearchBook(event) {
    event.preventDefault();

    const searchInput = document.getElementById('search-by-word-input');
    const searched = searchInput.value.trim();
    if (searched) {
        fetch(`http://127.0.0.1:8000/api/search-book/?searched=${searched}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                displaySearchedBooks(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    } else {
        displayBooks();
    }
}

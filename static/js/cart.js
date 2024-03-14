function getImage(image) {
    const Image = document.createElement('img');
    Image.src = image;
    Image.alt = 'Product Image';
    Image.style.width = '300px';
    Image.style.height = '400px';
    Image.style.margin = '10px';
    Image.style.border = '1px solid';
    return Image;
}

function removeCartItem(id) {
    fetch(`http://127.0.0.1:8000/cart/remove/${id}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                console.error('Failed to remove item from cart');
            }
        })
        .catch(error => console.error('Error removing item from cart:', error));
}

function displayCartItems() {
    fetch('http://127.0.0.1:8000/api/cart-items/')
        .then(response => response.json())
        .then(data => {
            const cartItems = document.getElementById('cart-items');
            cartItems.innerHTML = '';
            let total = 0;

            data.results.forEach(item => {
                const cartItemDiv = document.createElement('div');
                cartItemDiv.className = 'cart-item';
                const ImageDiv = document.createElement('div');
                const cartItemInfoDiv = document.createElement('div');

                const nameParagraph = document.createElement('p');
                const authorParagraph = document.createElement('p');
                const publisherParagraph = document.createElement('p')
                const producerParagraph = document.createElement('p');
                const quantityParagraph = document.createElement('p');
                quantityParagraph.textContent = 'Quantity: ' + item.quantity;
                const subtotalParagraph = document.createElement('p');
                subtotalParagraph.textContent = 'Subtotal: ' + formatPrice(item.subtotal);
                const removeButton = document.createElement('button');
                removeButton.id = 'book_button';
                removeButton.textContent = 'Remove';
                removeButton.addEventListener('click', function () {
                    removeCartItem(item.id);
                });

                if (item.type === 'book') {
                    fetch(`http://127.0.0.1:8000/api/books/${item.product_id}/`)
                        .then(response => response.json())
                        .then(bookData => {
                            if (bookData) {
                                if (bookData.image) {
                                    ImageDiv.appendChild(getImage(bookData.image));
                                }

                                nameParagraph.textContent = 'Name: ' + bookData.name;
                                authorParagraph.textContent = 'Author: ' + bookData.author;
                                publisherParagraph.textContent = 'Publisher: ' + bookData.publisher;
                            }
                        })
                        .catch(error => console.error('Error fetching book data:', error));
                }

                if (item.type === 'mobile') {
                    fetch(`http://127.0.0.1:8000/api/mobiles/${item.product_id}/`)
                        .then(response => response.json())
                        .then(mobileData => {
                            if (mobileData) {
                                if (mobileData.image) {
                                    ImageDiv.appendChild(getImage(mobileData.image));
                                }

                                nameParagraph.textContent = 'Name: ' + mobileData.name;
                                producerParagraph.textContent = 'Producer: ' + mobileData.producer;
                            }
                        })
                        .catch(error => console.error('Error fetching mobile data:', error));
                }

                cartItemInfoDiv.appendChild(nameParagraph);
                if (authorParagraph) cartItemInfoDiv.appendChild(authorParagraph);
                if (publisherParagraph) cartItemInfoDiv.appendChild(publisherParagraph);
                if (producerParagraph) cartItemInfoDiv.appendChild(producerParagraph);
                cartItemInfoDiv.appendChild(quantityParagraph);
                cartItemInfoDiv.appendChild(subtotalParagraph);
                cartItemInfoDiv.appendChild(removeButton);

                cartItemDiv.appendChild(ImageDiv);
                cartItemDiv.appendChild(cartItemInfoDiv);

                total += item.subtotal;
                cartItems.appendChild(cartItemDiv);
            });

            document.getElementById('total').textContent = formatPrice(total);
        })
        .catch(error => console.error('Error fetching cart items:', error));
}

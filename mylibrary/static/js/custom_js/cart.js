var updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var product_id = this.dataset.product
        var action = this.dataset.action

        console.log("Product id: ", product_id, " Action: ", action);
        user = current_user;

        if (user === "AnonymousUser") {
            console.log("Anonymous user, not authenticated");
        } else {
            updateUserOrder(product_id, action)
        }

    })

}

function updateUserOrder(productId, action) {
    var url = '/rental/update/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })

    })
        .then((response) => {
            return response.json()
        })

        .then((data) => {
            if (action == 'add') {
                window.FlashMessage.success('This is a successs flash message !');
                alert(data)
            }
            else {
                location.reload()
            }
        })

    console.log('Updated!!! for product: ', productId, "action is: ", action);
}
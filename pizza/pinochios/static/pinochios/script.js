// This is to get through django's CSRF authentication on EVERY post request to server
function parse_cookies() {
    var cookies = {};
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(function (c) {
            var m = c.trim().match(/(\w+)=(.*)/);
            if(m !== undefined) {
                cookies[m[1]] = decodeURIComponent(m[2]);
            }
        });
    }
    return cookies;
}
cookies = parse_cookies()


document.addEventListener('DOMContentLoaded', () => {

    function writeToLog(text, type) {
        document.querySelector('#log').innerHTML = `<div class='alert alert-${type} role='alert'>${text}</div>`
        console.log(`<div class='alert alert-${type}>${text}</div>`)
    }

    function addToCart(name, type, price1, price2) {

        // Updates how many items are in the cart for the user
        const cart = document.querySelector('#shoppingCartAmount').innerHTML;
        var new_cart = parseInt(cart) + 1;

        const shoppingCart = document.querySelector('#shoppingCartAmount')
        shoppingCart.innerHTML = new_cart


        // This triggers the animation for the shopping cart
        shoppingCart.style.animationPlayState = "running"
        shoppingCart.addEventListener('animationiteration', () => {
            shoppingCart.style.animationPlayState = "paused"
        })

        // Get the users ID
        const firstChild = document.body.firstElementChild
        
        // Open new request
        const request = new XMLHttpRequest();

        // Set method, route, and django CSRF token
        request.open('POST', 'add_to_shopping_cart')
        request.setRequestHeader('X-CSRFToken', cookies['csrftoken'])

        // Make new form data
        const data = new FormData();

        // Add all the data
        data.append('user_id', firstChild.nextElementSibling.value)
        data.append('name', name)
        data.append('type', type)
        data.append('price1', price1)
        if (price2) { data.append('price2', price2) }
        // Send data

        request.send(data)
    }




    if (window.location.pathname === "/") {
        // Since pizzas and other menu items work differently they're grouped seperately
        document.querySelectorAll('.addPizzaMenuItem').forEach(function(button) {
            button.onclick = () => {
                // Gets all the different information for the addtoCart function
                const div = button.parentNode

                const small_price = div.nextElementSibling

                const large_price = small_price.nextElementSibling

                const name = large_price.nextElementSibling

                const type = name.nextElementSibling


                addToCart(name.value, type.value, small_price.value, large_price.value)
                
            }
        })
        // This is for anything that isn't a pizza
        document.querySelectorAll('.addMenuItem').forEach(function(button) {
            button.onclick = () => {
                // Get all the different information for the addToCart function
                const div = button.parentNode

                const price = div.nextElementSibling

                const name = price.nextElementSibling

                const type = name.nextElementSibling


                addToCart(name.value, type.value, price.value)
            }
        })
    }



    if (window.location.pathname === "/register") {

        // Checks to make sure both the passwords are the same
        document.querySelector('#registerSubmit').onsubmit = () => {
            const password = document.querySelector('#registerPassword').value;
            const repassword = document.querySelector('#registerRePassword').value;

            if (password !== repassword) {
                alert('Passwords don\' match')
                return false;
            }
        }


        // When user types new username
        document.querySelector('#registerUsername').addEventListener('keyup', () => {

            // Initialize variables
            const request = new XMLHttpRequest();
            const username = document.querySelector('#registerUsername').value;

            // Set route and method
            request.open('POST', '/validate_username');

            // This is for django's CSRF authentication
            request.setRequestHeader('X-CSRFToken', cookies['csrftoken'])

            // When the server returns a response
            request.onload = () => {
                // Get the response JSON
                const data = JSON.parse(request.responseText);

                const button = document.querySelector('#registerSubmitButton');
            
                // If the username is already taken display it to user
                if (data.is_taken) {
                    writeToLog('username already taken', 'danger');
                    button.disabled = true;
                }
                // If it 
                else {
                    writeToLog('username is not already taken', 'success')
                    button.disabled = false;
                }
            }
            // Make data to be sent to server
            const data = new FormData();
            data.append('username', username)

            // Send the data
            request.send(data)
        })
    }
    
})
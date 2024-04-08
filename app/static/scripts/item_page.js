function subtotal_update()
{
    var cart_subtotal_value = document.getElementById("cart-subtotal-value");
    var cart_button = document.getElementById("add-to-cart-form")

    var quantity = document.getElementById("quantity-select");

    var cost = 0;
    
    temp_num = Number(cart_subtotal_value.getAttribute("item_price")) * quantity.value;
    cost = Math.round(temp_num * 100)/100
    
    cost = Math.round(cost * 100)/100;

    cart_subtotal_value.textContent = "$"+cost.toFixed(2);


    var id = Number(cart_button.getAttribute("item_id"))

    count = quantity.value
    if (count == 1)
    {
        cart_button.action = "/shop/add_to_cart/"+id;
    }
    else
    {
        cart_button.action = "/shop/add_to_cart/"+id+"/"+quantity.value;
    }
    
}

window.onload = subtotal_update()

function lower_quantity()
{
    var quantity = document.getElementById("quantity-select");

    count = quantity.value
    if (count == 1)
    {
        alert("Can't decrease quantity anymore")
    }
    else
    {
        count--
        quantity.value = count;
        subtotal_update()
    }
}

function increase_quantity()
{
    var quantity = document.getElementById("quantity-select");

    count = quantity.value
    if (count == 10)
    {
        alert("Can't increase quantity above 10")
    }
    else
    {
        count++
        quantity.value = count;
        subtotal_update()
    }
}
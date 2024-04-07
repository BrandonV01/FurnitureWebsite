function price_update()
{
    item_total_value = document.getElementById("item-total-value");
    shipping_tax_value = document.getElementById("shipping-tax-value");
    shipping_total_value = document.getElementById("shipping-total-value");
    tax_value = document.getElementById("tax-value");
    order_total_value = document.getElementById("order-total-value");
    bottom_order_total_value = document.getElementById("bottom-order-total-value");

    var list = document.getElementsByClassName("item-price");
    var list2 = document.getElementsByClassName("quantity_dropdown");
    var deliver_options = document.getElementsByClassName("delivery-radio");

    var cost = 0;
    for (var i = 0; i < list.length; i++) 
    {
        temp_num = Number(list[i].getAttribute("value")) * Number(list2[i].value)
        cost += Math.round(temp_num * 100)/100
    }
    

    cost = Math.round(cost * 100)/100;

    item_total_value.textContent = "$"+cost.toFixed(2);

    var delivery_tax = 0;
    for (var i = 0; i < deliver_options.length; i++)
    {
        if (deliver_options[i].checked) 
        {
            if (deliver_options[i].value == "3_day")
            {
                delivery_tax += 14.99
            }
            else if (deliver_options[i].value == "1_week")
            {
                delivery_tax += 9.99
            }
            else if (deliver_options[i].value == "2_week")
            {
                delivery_tax += 4.99
            }
        }
    }

    delivery_tax = Math.round(delivery_tax * 100)/100;

    shipping_tax_value.textContent = "$"+delivery_tax.toFixed(2);

    cost += delivery_tax;

    shipping_total_value.textContent = "$"+cost.toFixed(2);

    tax = Math.round((cost * .08)* 100)/100;

    tax_value.textContent = "$"+tax.toFixed(2);

    cost += tax;

    order_total_value.textContent = "$"+cost.toFixed(2);
    bottom_order_total_value.textContent = "Order Total: $"+cost.toFixed(2);
}

window.onload = function() {
    var myArray = JSON.parse(sessionStorage.getItem('cart_list'));
    for (var i = 0; i < myArray.length; i++)
    {
        var div = document.getElementById('item-list');

        var img = `<img src="/static/images/items/`+ myArray[i][1] +`" width="90">`;
        
        var dropdown = `<div id="myDropdown`+myArray[i][4]+`" class="dropdown-content"><button onclick="update_dropdown('`+myArray[i][4]+`', 1)">1</button><button onclick="update_dropdown('`+myArray[i][4]+`', 2)">2</button><button onclick="update_dropdown('`+myArray[i][4]+`', 3)">3</button><button onclick="update_dropdown('`+myArray[i][4]+`', 4)">4</button><button onclick="update_dropdown('`+myArray[i][4]+`', 5)">5</button><button onclick="update_dropdown('`+myArray[i][4]+`', 6)">6</button><button onclick="update_dropdown('`+myArray[i][4]+`', 7)">7</button><button onclick="update_dropdown('`+myArray[i][4]+`', 8)">8</button><button onclick="update_dropdown('`+myArray[i][4]+`', 9)">9</button><button onclick="update_dropdown('`+myArray[i][4]+`', 10)">10</button><button onclick="update_dropdown('`+myArray[i][4]+`', 0)">Delete</button></div>`
        
        var quantity = `<button onclick="cart_dropdown('`+myArray[i][4]+`')" class="dropbtn quantity_dropdown" id="`+myArray[i][4]+`dropdown" value="`+myArray[i][3]+`">QTY: `+myArray[i][3]+`<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots-vertical" viewBox="0 0 16 16"><path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0"/></svg></button>`;
        var info_block = `<div class="delivery-info"><p>`+myArray[i][0]+`</p><p class="item-price" value="`+myArray[i][2]+`">$`+myArray[i][2]+`</p><div class="dropdown">`+quantity+dropdown+`</div></div>`;
        var deliver_options = `<div class="delivery-options"><p>Choose your delivery option:</p><input type="radio" class="delivery-radio" onchange="price_update();" id="3_day" name="delivery_option`+myArray[i][4]+`" value="3_day" checked><label for="html">3 Day</label><br><input type="radio" class="delivery-radio" onchange="price_update();" id="1_week" name="delivery_option`+myArray[i][4]+`" value="1_week"><label for="css">1 Week</label><br><input type="radio" class="delivery-radio" onchange="price_update();" id="2_week" name="delivery_option`+myArray[i][4]+`" value="2_week"><label for="javascript">2 Week:</label></div>`;
        var item_info = `<div class="item-info" style="padding-left:96px"> <div style="width: 96px; margin-left: -96px; float: left;">`+img+`</div> <div class="info-block">`+info_block+deliver_options+`</div> </div>`;

        div.innerHTML += `<div class="item-row" id="`+myArray[i][4]+`_item-row" item_id="`+myArray[i][4]+`">`+ item_info +`</div>`;
    }

    price_update()
}

function cart_dropdown(id)
{
    element = document.getElementById("myDropdown"+id);
    element.classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
        }
    }
} 

function update_dropdown(id, quantity)
{
    if (quantity == 0)
    {
        var div = document.getElementById(id+"_item-row");
        div.remove();
    }
    else {
        var button = document.getElementById(id+"dropdown");
        button.innerHTML = `QTY: `+quantity+` <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots-vertical" viewBox="0 0 16 16"><path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0"></path></svg>`;
        button.value = quantity;
    }
    

    price_update()
}

function order_complete()
{
    var list = document.getElementsByClassName("item-row");

    var testArray = new Array(list.length);
    for (var i = 0; i < list.length; i++) 
    {
        testArray[i] = Number(list[i].getAttribute("item_id"));
    }

    window.location = '/cart/order?array='+testArray;

}
function price_update()
{
    order_subtotal = document.getElementById("subtotal-value");
    order_total = document.getElementById("total-value");

    var list = document.getElementsByClassName("check");
    var list2 = document.getElementsByClassName("quantity_dropdown");

    var total=0;
    for (var i = 0; i < list.length; i++) 
    {
        if (list[i].checked) 
        {
            temp_num = Number(list[i].getAttribute("value")) * Number(list2[i].value)
            total += Math.round(temp_num * 100)/100
        }
    }
    

    cost = Math.round(total * 100)/100;
    order_subtotal.textContent = "$"+cost.toFixed(2);
    order_total.textContent = "$"+cost.toFixed(2);
}

window.onload = price_update();

document.body.onclick = function(e){
    e=window.event? event.srcElement: e.target;
    if(e.className && e.className.indexOf('check')!=-1)price_update();
}

function uncheck_boxes()
{
    var list = document.getElementsByClassName("check");

    for (var i = 0; i < list.length; i++) 
    {
        if (list[i].checked) 
        {
            list[i].checked = ""
        }
    }

    price_update();
}

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function cart_dropdown(id) {
    element = document.getElementById("myDropdown"+id);
    element.classList.toggle("show");
}

function go_checkout() {
    var list = document.getElementsByClassName("check");

    var arraylength = 0;
    for (var i = 0; i < list.length; i++) 
    {
        if (list[i].checked) 
        {
            arraylength++
        }
    }

    var testArray = new Array(arraylength);
    for (var i = 0; i < list.length; i++) 
    {
        if (list[i].checked) 
        {
            var name = list[i].getAttribute("item_name")
            var img = list[i].getAttribute("item_img");
            var price = Number(list[i].getAttribute("value"));
            var amount = Number(list[i].getAttribute("item_amount"));
            var id = Number(list[i].getAttribute("item_id"));
            testArray[i] = new Array(name, img, price, amount, id);
        }
    }

    sessionStorage.setItem('cart_list', JSON.stringify(testArray));
    window.location = '/cart/checkout';
}
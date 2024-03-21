function updateList(target_dropdown, origin_dropdown, subtag_arr){
    let l = document.getElementById(target_dropdown);
    l.innerHTML = "";
    if (origin_dropdown == "first_option")
    {
        l.innerHTML = "<option value='first_option'>--SELECT CATEGORY--</option>"
    }
    else
    {
        for (let i = 0; i < subtag_arr.length; i++)
        {
            if (subtag_arr[i][1] == origin_dropdown)
            {
                l.innerHTML += "<option value='"+subtag_arr[i][0]+"'>"+subtag_arr[i][0]+"</option>";
            }
        }
    }
}

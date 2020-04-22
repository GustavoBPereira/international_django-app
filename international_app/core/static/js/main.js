document.querySelector('#js-filled').innerHTML = 'Texto renderizado pelo JS'



function fill_subtitle() {
    let sub = document.querySelector("#to-be-filled-by-js")
    sub.innerHTML = "JS preenchendo um campo"
    sub.className = "from-js"
}
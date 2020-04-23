document.querySelector('#js-filled').innerHTML = gettext('Texto renderizado pelo JS')



function fill_subtitle() {
    let sub = document.querySelector("#to-be-filled-by-js")
    sub.innerHTML = gettext("texto do JS")
}
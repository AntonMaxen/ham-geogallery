export {create_alert, fade_out_element}

let create_alert = (category, message) => {
    let spacer = document.querySelector('#top-bar .spacer');
    let infoboxes = spacer.querySelectorAll('.info');
    if (infoboxes.length > 0) {
        infoboxes.forEach(box => box.parentNode.removeChild(box));
    }
    let new_infobox = document.createElement('div');
    new_infobox.className = `info ${category}`;
    new_infobox.innerText = `${message}`;
    spacer.appendChild(new_infobox);
    return new_infobox;
}

let fade_out_element = (el) => {
    let effect = setInterval(function() {
        if (!el.style.opacity) {
            el.style.opacity = 1;
        }
        if (el.style.opacity > 0) {
            el.style.opacity -= 0.025;
        } else {
            clearInterval(effect);
        }
    }, 50);

}
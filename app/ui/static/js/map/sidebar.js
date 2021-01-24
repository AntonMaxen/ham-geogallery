import * as api from "./api.js";
import {truncate_text} from "./utils.js";

export {load_sidebar_data};

let sidebar_cleanup = () => {
    let containers = document.querySelectorAll('.sidebar-container');

    containers.forEach(container => {
       container.parentNode.removeChild(container)
    });
}

let load_image_container = async (loc) => {
    let images = await api.get_images_by_location_id(loc.Id);
    let sidebar = document.querySelector('#sidebar');

    let sidebar_container = create_sidebar_container(sidebar);
    let sidebar_header = create_sidebar_header(sidebar_container);
    let img_header_text = document.createElement('h4');
    img_header_text.innerText = `Images`;
    sidebar_header.appendChild(img_header_text);

    let img_div = document.createElement('div')
    img_div.setAttribute('id', 'sidebar-image-group');
    sidebar_container.appendChild(img_div);

    images.forEach(image => {
        let image_element = document.createElement('img');
        image_element.setAttribute('class', 'sidebar-image')
        image_element.setAttribute('src', `http://localhost:5000/api/static/image/${image.FileName}`);
        img_div.appendChild(image_element);
    });
}

let load_review_container = async (loc) => {
    let sidebar = document.querySelector('#sidebar');
    let reviews = await api.get_reviews_by_location_id(loc.Id);
    console.log(reviews)
    let sidebar_container = create_sidebar_container(sidebar);
    let sidebar_header = create_sidebar_header(sidebar_container);
    let header_text = document.createElement('h4');
    header_text.innerText = `Reviews`;
    sidebar_header.appendChild(header_text);

    let review_container = document.createElement('div');
    review_container.setAttribute('class', 'sidebar-review-group');
    sidebar_container.appendChild(review_container);

    reviews.forEach(review => {
       let review_div = document.createElement('div');
       review_div.setAttribute('class', 'sidebar-review');
       let title = document.createElement('h5');
       title.innerText = review.Title;
       let review_text = document.createElement('p');
       review_text.innerText = truncate_text(review.ReviewText, 80);
       review_div.appendChild(title);
       review_div.appendChild(review_text);
       let bottom_bar = document.createElement('div');
       bottom_bar.setAttribute('class', 'sidebar-container-bottombar');
       let likes = document.createElement('span');
       likes.innerText = `Likes 10`;
       likes.addEventListener('click', () => {
           let split_string = likes.innerText.split(' ');
           let new_value = parseInt(split_string[1]) + 1;
           likes.innerText = split_string[0] + ' ' + new_value;

       });
       let rating = document.createElement('span');
       // rating.setAttribute('class','text-left');
       rating.innerText = review.Score + '/10';

       let review_date = document.createElement('span');
       //review_date.setAttribute('class', 'text-right');
       review_date.innerText = review.DateCreated;
       bottom_bar.appendChild(likes);
       bottom_bar.appendChild(rating);
       bottom_bar.appendChild(review_date);
       review_div.appendChild(bottom_bar);

       review_container.appendChild(review_div);
    });
}

let create_sidebar_container = (sidebar) => {
    let sidebar_container = document.createElement('div');
    sidebar_container.setAttribute('class', 'sidebar-container');
    sidebar.appendChild(sidebar_container);
    return sidebar_container;
}

let create_sidebar_header = (sidebar_container) => {
    let sidebar_header = document.createElement('div');
    sidebar_header.setAttribute('class', 'sidebar-container-header');
    sidebar_container.appendChild(sidebar_header);
    return sidebar_header;
}


let load_sidebar_data = async (loc) => {
    sidebar_cleanup();
    let sidebar = document.querySelector('#sidebar');
    let sidebar_container = create_sidebar_container(sidebar);
    let sidebar_header = create_sidebar_header(sidebar_container);
    let header_text = document.createElement('h4');
    header_text.innerText = `${loc.Place}`;
    sidebar_header.appendChild(header_text);
    await load_image_container(loc);
    await load_review_container(loc);

}
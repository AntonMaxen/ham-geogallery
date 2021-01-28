import * as api from "./api.js";
import {truncate_text} from "./utils.js";

export {load_sidebar_data, load_sidebar_new_location_data};

let sidebar_cleanup = () => {
    let containers = document.querySelectorAll('.sidebar-container');

    containers.forEach(container => {
       container.parentNode.removeChild(container)
    });
}



let create_image = async (image) => {
    let image_container = document.createElement('div');
    image_container.setAttribute('class', 'sidebar-image-container');

    let image_element = document.createElement('img');
    image_element.setAttribute('class', 'sidebar-image');
    image_element.setAttribute('src', `http://localhost:5000/api/static/image/${image.FileName}`);

    let image_text = document.createElement('div');
    image_text.setAttribute('class', 'image-text');
    let picture_likes = await api.get_amount_likes_by_picture_id(image.Id);
    image_text.innerText = `${picture_likes.likes}`;

    image_container.addEventListener('mouseover', show_element);
    image_container.addEventListener('mouseleave', hide_element);

    image_container.appendChild(image_element);
    image_container.appendChild(image_text);
    return image_container;
}

let create_review = async (review) => {
    let review_container = document.createElement('div');
    review_container.setAttribute('class', 'sidebar-review');
    let title = document.createElement('h5');
    title.innerText = review.Title;
    let review_text = document.createElement('p');
    review_text.innerText = truncate_text(review.ReviewText, 80);
    review_container.appendChild(title);
    review_container.appendChild(review_text);
    let bottom_bar = document.createElement('div');
    bottom_bar.setAttribute('class', 'sidebar-container-bottombar');
    let likes = document.createElement('span');
    let review_likes = await api.get_amount_likes_by_review_id(review.Id);
    likes.innerHTML = `<i class="fas fa-angle-up"> ${review_likes.likes}</i>`;
    
    
    likes.addEventListener('click', () => {
       let value = likes.innerText;
       let new_value = parseInt(value) + 1;
       likes.innerHTML = `<i class="fas fa-angle-up"> ${new_value}</i>`;

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
    review_container.appendChild(bottom_bar);
    return review_container;
}

async function asyncForEach(array, callback) {
    for (let index = 0; index < array.length; index++) {
        await callback(array[index], index, array);
    }
}


let create_sidebar_container = (sidebar, order=0) => {
    let sidebar_container = document.createElement('div');
    sidebar_container.setAttribute('class', 'sidebar-container');
    sidebar.insertBefore(sidebar_container, sidebar.childNodes[order]);
    return sidebar_container;
}


let create_sidebar_header = (sidebar_container) => {
    let sidebar_header = document.createElement('div');
    sidebar_header.setAttribute('class', 'sidebar-container-header');
    sidebar_container.appendChild(sidebar_header);
    return sidebar_header;
}

let create_form_container = (sidebar_container) => {
    let form_container = document.createElement('div');
    form_container.setAttribute('class', 'form-container');
    sidebar_container.appendChild(form_container);
    return form_container;
}


function show_element(e) {
    let text_element = this.querySelector('.image-text');
    text_element.style.opacity = 1;
}


function hide_element(e) {
    let text_element = this.querySelector('.image-text');
    text_element.style.opacity = 0;
}

let load_image_container = async (loc, amount) => {
    console.log(amount)
    let images = await api.get_images_by_location_id(loc.Id, amount);
    let sidebar = document.querySelector('#sidebar');

    let sidebar_container = create_sidebar_container(sidebar, 1);
    let sidebar_header = create_sidebar_header(sidebar_container);
    let img_header_text = document.createElement('h4');
    img_header_text.innerText = `Images`;
    sidebar_header.appendChild(img_header_text);

    let img_div = document.createElement('div')
    img_div.setAttribute('class', 'sidebar-image-group');
    sidebar_container.appendChild(img_div);

    let sidebar_footer = create_sidebar_header(sidebar_container);
    let sidebar_footer_text = document.createElement('h4');
    sidebar_footer_text.innerText = 'Load More';
    sidebar_footer.appendChild(sidebar_footer_text);

    await asyncForEach(images,async (image) => {
        let image_container = await create_image(image);
        img_div.appendChild(image_container);
    });

    sidebar_footer.addEventListener('click', async function() {
        let amount_images = document.querySelectorAll('.sidebar-image-container').length;
        let db_images = await api.get_all_images_by_location_id(loc.Id);

        if (db_images.length > amount_images) {
            let container = this.parentNode.querySelector('.sidebar-image-group');
            for (let i = amount_images; i < amount_images + 3 && i < db_images.length; i++) {
                let image = await create_image(db_images[i]);
                container.appendChild(image);
            }
            if (container.childNodes.length == db_images.length) {
                this.firstChild.innerText = `${db_images.length} Rows Loaded`;
            }
        }
    });
}

let load_review_container = async (loc, amount) => {
    let sidebar = document.querySelector('#sidebar');
    let reviews = await api.get_reviews_by_location_id(loc.Id, amount);
    console.log(reviews)
    let sidebar_container = create_sidebar_container(sidebar, 2);
    let sidebar_header = create_sidebar_header(sidebar_container);
    let header_text = document.createElement('h4');
    header_text.innerText = `Reviews`;
    sidebar_header.appendChild(header_text);

    let review_div = document.createElement('div');
    review_div.setAttribute('class', 'sidebar-review-group');
    sidebar_container.appendChild(review_div);

    await asyncForEach(reviews, async (review) => {
        let review_container = await create_review(review)
        review_div.appendChild(review_container);
    });

    let sidebar_footer = create_sidebar_header(sidebar_container);
    let sidebar_footer_text = document.createElement('h4');
    sidebar_footer_text.innerText = 'Load More';
    sidebar_footer.appendChild(sidebar_footer_text);

    sidebar_footer.addEventListener('click', async function() {
        let amount_reviews = document.querySelectorAll('.sidebar-review').length;
        let db_reviews = await api.get_all_reviews_by_location_id(loc.Id);
        let container = this.parentNode.querySelector('.sidebar-review-group');
        console.log(db_reviews.length)

        if (db_reviews.length > amount_reviews) {
            for (let i = amount_reviews; i < amount_reviews + 1 && i < db_reviews.length; i++) {
                let review = await create_review(db_reviews[i]);
                container.appendChild(review);
                this.parentNode.parentNode.scrollBy({
                    top: review.offsetHeight + 10,
                    left: 0,
                    behavior: 'auto'
                });
            }
            if (container.childNodes.length == db_reviews.length) {
                this.firstChild.innerText = `${db_reviews.length} Rows Loaded`;
            }
        }
    });
}


let load_sidebar_new_location_data = async(lat_lng) => {
    let lat = lat_lng.lat();
    let lng = lat_lng.lng();
    console.log(lat, lng)
    let location_information = await api.get_location_info_by_latlng(lat, lng)
    console.log(location_information)

}

let load_sidebar_infobox = async(loc) => {
    let sidebar = document.querySelector('#sidebar');

    let sidebar_container = create_sidebar_container(sidebar, 0);
    let sidebar_header = create_sidebar_header(sidebar_container);
    let header_text = document.createElement('h4');
    header_text.innerText = `${loc.Place}`;
    sidebar_header.appendChild(header_text);

    let button_container = document.createElement('div');
    button_container.setAttribute('class', 'button-container');
    let button_one = document.createElement('button');
    button_one.setAttribute('class', 'info-button');
    button_one.innerText = 'Add Image';
    button_one.addEventListener('click', async function() {
        let form_containers = document.querySelectorAll('.form-container');
        form_containers.forEach(c => c.parentNode.removeChild(c));

        let form_container = create_form_container(sidebar_container);
        form_container.innerHTML = (
            '<h5>Add Image</h5>' +
            '<form action="#" enctype="multipart/form-data">' +
            '<input type="text" name="image_name" placeholder="Image Name">' +
            '<label for="image-browse">Choose file</label>' +
            '<input type="file" id="image-browse" name="image" accept="image/png, image/jpeg">' +
            '<button>Submit</button>' +
            '</form>'
        );


        let input = document.querySelector('input[type="file"]');
        input.addEventListener('change', function() {
            let textbox = document.querySelector('label[for="image-browse"]');
            let file_list = input.files;
            if (file_list.length > 0) {
                let current_file = file_list[0];
                if (["image/png", "image/jpeg"].includes(current_file.type)) {
                    textbox.innerText = `${current_file.name}`;
                    console.log(URL.createObjectURL(current_file))
                } else {
                    textbox.innerText = `Filename ${current_file.name} is not a valid filetype.`;
                }
            }
            else {
                textbox.innerText = 'No files Selected';
            }
        });

       let form = form_container.querySelector('form');
       form.addEventListener('submit', function(e){
           e.preventDefault();
           let image_name = this.querySelector('input[type="text"]').value;
           let files = this.querySelector('input[type="file"]').files;
           let form_data = new FormData();

           if (files.length > 0 && image_name.length) {
               console.log(files[0])
               form_data.append('user_id', 1)
               form_data.append('location_id', loc.Id)
               form_data.append('image', files[0]);
               form_data.append('image_name', image_name);

               fetch('http://localhost:5000/api/add/image', {
                   method: 'POST',
                   body: form_data
               }).then(response => {
                  console.log(response)
               });
           }
           console.log(files);
           console.log(image_name);

       });

    });

    let button_two = document.createElement('button');
    button_two.setAttribute('class', 'info-button');
    button_two.innerText = 'Add Review';

    button_container.appendChild(button_one);
    button_container.appendChild(button_two);
    sidebar_container.appendChild(button_container);
}


let load_sidebar_data = async (loc, amount_pictures=3, amount_reviews=3) => {
    sidebar_cleanup();
    let sidebar = document.querySelector('#sidebar');

    await load_sidebar_infobox(loc);
    await load_image_container(loc, amount_pictures);
    await load_review_container(loc, amount_reviews);

    let sidebar_container_footer = create_sidebar_container(sidebar, 4);
    let sidebar_footer = create_sidebar_header(sidebar_container_footer);
    let footer_text = document.createElement('h4');
    footer_text.innerText = `Back To Top ^`
    sidebar_footer.appendChild(footer_text);
    sidebar_footer.addEventListener('click', function(){
        sidebar.scrollTo({
            top:0,
            left:0,
            behavior: 'smooth'
        })
    });
}

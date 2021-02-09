import * as api from "./api.js";
import {truncate_text} from "./utils.js";
import {load_location, center_map_on_marker} from "./map.js";

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


let create_sidebar_container = (sidebar, name='noclass', order=0) => {
    let sidebar_container = document.createElement('div');
    sidebar_container.setAttribute('class', 'sidebar-container');
    sidebar_container.classList.add(name);
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

    let sidebar_container = create_sidebar_container(sidebar, 'imagebox', 1);
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
        let all_images = document.querySelectorAll('.sidebar-image-container');
        let amount_images = all_images.length;
        let db_images = await api.get_all_images_by_location_id(loc.Id);

        if (db_images.length > amount_images) {
            let amount = 3 - (amount_images % 3);
            if (amount == 3) {
                let scroll_height = all_images[0].offsetHeight;
                this.parentNode.parentNode.scrollBy({
                    top: scroll_height + 10,
                    left: 0,
                    behavior: 'smooth'
                });
            }
            let container = this.parentNode.querySelector('.sidebar-image-group');
            for (let i = amount_images; i < amount_images + amount && i < db_images.length; i++) {
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
    let sidebar_container = create_sidebar_container(sidebar, 'reviewbox', 2);
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


let load_sidebar_new_location_data = async(lat_lng, map) => {
    console.log(lat_lng.lat(), lat_lng.lng());
    let lat = lat_lng.lat();
    let lng = lat_lng.lng();
    console.log(lat, lng);
    // let location_information = await api.get_location_info_by_latlng(lat, lng)
    sidebar_cleanup();
    let sidebar = document.querySelector('#sidebar');
    let sidebar_container = create_sidebar_container(sidebar, 'newbox', 0);
    let sidebar_header = create_sidebar_header(sidebar_container);
    let header_text = document.createElement('h4');
    header_text.innerText = `Selected Location`;
    let header_extra_box = document.createElement('div');
    header_extra_box.setAttribute('class', 'header-extra-info');
    let header_lat_text = document.createElement('h6');
    header_lat_text.innerText = `Lat: ${Number(lat.toFixed(4))}`;
    let header_lng_text = document.createElement('h6');
    header_lng_text.innerText = `Lng: ${Number(lng.toFixed(4))}`;
    sidebar_header.appendChild(header_text);
    header_extra_box.appendChild(header_lat_text);
    header_extra_box.appendChild(header_lng_text);
    sidebar_header.appendChild(header_extra_box);

    if (user != null) {
        let button_container = document.createElement('div');
        button_container.setAttribute('class', 'button-container');

        let button_one = await load_new_location_button_container(map, lat, lng);

        button_container.appendChild(button_one);
        sidebar_container.appendChild(button_container);
    }

}


let remove_form = sidebar_container => {
    let form_containers = sidebar_container.querySelectorAll('.form-container');
    let footer_containers = sidebar_container.querySelectorAll('.form-footer')
    form_containers.forEach(c => c.parentNode.removeChild(c));
    footer_containers.forEach(f => f.parentNode.removeChild(f));
}

let load_sidebar_infobox = async (loc) => {
    let sidebar = document.querySelector('#sidebar');
    let sidebar_container = create_sidebar_container(sidebar, 'infobox', 0);
    let sidebar_header = create_sidebar_header(sidebar_container);
    sidebar_header.addEventListener('click', function(){
        location.replace(`http://localhost:5000/place/${loc.Place}`)
    });
    let header_text = document.createElement('h4');
    header_text.innerText = `${loc.Place}`;
    sidebar_header.appendChild(header_text);
    if (user != null) {
        let button_container = document.createElement('div');
        button_container.setAttribute('class', 'button-container');

        let button_one = await load_image_button_container(loc);
        let button_two = await load_review_button_container(loc);

        button_container.appendChild(button_one);
        button_container.appendChild(button_two);
        sidebar_container.appendChild(button_container);
    }
}

let load_image_button_container = async (loc) => {
    let button_one = document.createElement('button');
    button_one.setAttribute('class', 'info-button');
    button_one.innerText = 'Add Image';

    button_one.addEventListener('click', async function() {
        let sidebar_container = document.querySelector('.infobox');
        remove_form(sidebar_container);

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

        let form_footer = create_sidebar_header(sidebar_container);
        form_footer.classList.add('form-footer');
        let footer_text = document.createElement('h4');
        footer_text.innerText = 'Close';
        form_footer.appendChild(footer_text);
        form_footer.addEventListener('click', function (){
            let sidebar_container = document.querySelector('.infobox');
            remove_form(sidebar_container);
        });


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
            let sidebar_container = document.querySelector('.infobox');
            let image_name = this.querySelector('input[type="text"]').value;
            let files = this.querySelector('input[type="file"]').files;
            let form_data = new FormData();

            if (files.length > 0 && image_name.length) {
                console.log(files[0])
                form_data.append('user_id', user.Id)
                form_data.append('location_id', loc.Id)
                form_data.append('image', files[0]);
                form_data.append('image_name', image_name);

                fetch('http://localhost:5000/api/add/image', {
                    method: 'POST',
                    body: form_data
                }).then(async response => {
                    if (response.status == 200) {
                        let image_box = document.querySelector('.imagebox');
                        let images = image_box.querySelectorAll('.sidebar-image-container');
                        image_box.parentNode.removeChild(image_box);
                        await load_image_container(loc, images.length + 1);
                        remove_form(sidebar_container)
                    }
                });
            }
            console.log(files);
            console.log(image_name);

        });

    });

    return button_one;
}


let load_review_button_container = async (loc) => {
    let button_two = document.createElement('button');
    button_two.setAttribute('class', 'info-button');
    button_two.innerText = 'Add Review';

    button_two.addEventListener('click', async function(){
        let sidebar_container = document.querySelector('.infobox');
        remove_form(sidebar_container);

        let form_container = create_form_container(sidebar_container);
        form_container.innerHTML = (
            '<h5>Add Review</h5>' +
            '<form action="#" enctype="multipart/form-data">' +
            '<input type="text" name="title" placeholder="Title"/>' +
            '<textarea name="review_text" placeholder="Review Text"></textarea>' +
            '<input type="text" name="show_score" placeholder="Score" readonly/>' +
            '<input type="range" name="score" min="0" max="9.9" value="5" step="0.1"/>' +
            '<button>Submit</button>' +
            '</form>'
        );


        let form_footer = create_sidebar_header(sidebar_container);
        form_footer.classList.add('form-footer');
        let footer_text = document.createElement('h4');
        footer_text.innerText = 'Close';
        form_footer.appendChild(footer_text);
        form_footer.addEventListener('click', function (){
            let sidebar_container = document.querySelector('.infobox');
            remove_form(sidebar_container);
        });

        let slider = sidebar_container.querySelector('input[type="range"]');
        let show_score = sidebar_container.querySelector('input[name="show_score"]');
        show_score.value = slider.value;

        slider.addEventListener('change', function(){
            let sidebar_container = document.querySelector('.infobox');
            let show_score = sidebar_container.querySelector('input[name="show_score"]');
            show_score.value = this.value;
        });

        slider.addEventListener('input', function(){
            let sidebar_container = document.querySelector('.infobox');
            let show_score = sidebar_container.querySelector('input[name="show_score"]');
            show_score.value = this.value;
        });

        let form = form_container.querySelector('form');
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            let title = this.querySelector('input[name="title"]').value;
            let review_text = this.querySelector('textarea[name="review_text"]').value;
            let score = this.querySelector('input[name="score"]').value;
            let form_data = new FormData()
            form_data.append('title', title);
            form_data.append('review_text', review_text);
            form_data.append('score', score);
            form_data.append('user_id', user.Id);
            form_data.append('location_id', loc.Id);

            if (title != '' && review_text != '') {
                fetch('http://localhost:5000/api/add/review', {
                    method: 'POST',
                    body: form_data
                }).then(async response => {
                    let sidebar_container = document.querySelector('.infobox');
                    let review_box = document.querySelector('.reviewbox');
                    let reviews = review_box.querySelectorAll('.sidebar-review');
                    review_box.parentNode.removeChild(review_box);
                    await load_review_container(loc, reviews.length + 1);
                    remove_form(sidebar_container);
                });
            }
        });
    });
    return button_two;
}

let load_new_location_button_container = async (map, lat, lng) => {
    let button_one = document.createElement('button');
    button_one.setAttribute('class', 'info-button');
    button_one.innerText = 'Add Location';

    button_one.addEventListener('click', async function() {
        let sidebar_container = document.querySelector('.newbox');
        remove_form(sidebar_container);

        let form_container = create_form_container(sidebar_container);
        let hidden_place = `<input type="hidden" name="place" value="${'5'}"/>`;
        let shown_place = '<input type="text" name="place" placeholder="City/Town"/>';


        let category_select = document.createElement('select');
        let categories = await api.get_categories(10);
        setAttributes(category_select, {
            'name': 'category',
            'id': 'category-select'
        });

        category_select.innerHTML = '<option selected disabled>Category</option>';

        categories.forEach(category => {
            let option = document.createElement('option');
            setAttributes(option, {
                'value': category.Name,
                'data-category-id': category.Id
            });
            option.innerText = category.Name;
            category_select.appendChild(option);
        });

        form_container.innerHTML = (
            '<h5>Add Location</h5>' +
            '<form action="#" enctype="multipart/form-data">' +
            (false ? hidden_place: shown_place) +
            '<input type="text" name="name" placeholder="Name for your place"/>' +
            category_select.outerHTML +
            '<button>Submit</button>' +
            '</form>'
        );

        let form_footer = create_sidebar_header(sidebar_container);
        form_footer.classList.add('form-footer');
        let footer_text = document.createElement('h4');
        footer_text.innerText = 'Close';
        form_footer.appendChild(footer_text);
        form_footer.addEventListener('click', function (){
            let sidebar_container = document.querySelector('.newbox');
            remove_form(sidebar_container);
        });

        let form = form_container.querySelector('form');
        form.addEventListener('submit', async function(e){
            e.preventDefault();
            let sidebar_container = document.querySelector('.newbox');
            let place = this.querySelector('input[name="place"]').value;
            let name = this.querySelector('input[name="name"]').value;
            let category = this.querySelector('#category-select');
            let form_data = new FormData();

            if (place != '' && name != '' && category.value != 'Category') {
                let category_id = category.options[category.selectedIndex].getAttribute("data-category-id");
                form_data.append('place', place);
                form_data.append('longitude', lng);
                form_data.append('latitude', lat);
                form_data.append('name', name);
                form_data.append('user_id', user.Id);
                form_data.append('category_id', category_id);

                let response = await fetch('http://localhost:5000/api/add/location', {
                    method: 'POST',
                    body: form_data
                });

                let location = await response.json();
                let created_location = load_location(map, location);
                center_map_on_marker(map, created_location.marker);
                sidebar_cleanup();
                load_sidebar_data(location, 9, 3);
            }
        });
    });

    return button_one;
}

let load_sidebar_data = async (loc, amount_pictures=3, amount_reviews=3) => {
    sidebar_cleanup();
    let sidebar = document.querySelector('#sidebar');

    await load_sidebar_infobox(loc);
    await load_image_container(loc, amount_pictures);
    await load_review_container(loc, amount_reviews);

    let sidebar_container_footer = create_sidebar_container(sidebar, 'footerbox', 4);
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

let setAttributes = (el, attrs) => {
    for(let key in attrs) {
        el.setAttribute(key, attrs[key]);
    }
}

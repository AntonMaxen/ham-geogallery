export {
    get_images_by_location_id,
    get_reviews_by_location_id,
    get_amount_likes_by_picture_id,
    get_amount_likes_by_review_id,
    get_all_images_by_location_id,
    get_all_reviews_by_location_id,
    get_location_info_by_latlng
}


let get_images_by_location_id = async (loc_id, amount) => {
    let response = await fetch(`http://localhost:5000/api/resource/location/${loc_id}/picture?amount=${amount}`);
    let images = await response.json();
    return images;
}

let get_reviews_by_location_id = async (loc_id, amount) => {
    let response = await fetch(`http://localhost:5000/api/resource/location/${loc_id}/review?amount=${amount}`);
    let reviews = await response.json();
    return reviews;
}

let get_all_images_by_location_id = async (loc_id) => {
    let response = await fetch(`http://localhost:5000/api/resource/location/${loc_id}/picture/all`);
    let images = await response.json();
    return images;
}

let get_all_reviews_by_location_id = async (loc_id) => {
    let response = await fetch(`http://localhost:5000/api/resource/location/${loc_id}/review/all`);
    let reviews = await response.json();
    return reviews;
}


let get_amount_likes_by_picture_id = async (picture_id) => {
    let response = await fetch(`http://localhost:5000/api/resource/picture/${picture_id}/like/count`);
    let likes = await response.json();
    return likes;
}

let get_amount_likes_by_review_id = async (review_id) => {
    let response = await fetch(`http://localhost:5000/api/resource/review/${review_id}/like/count`);
    let likes = await response.json();
    return likes;
}

let get_location_info_by_latlng = async (lat, lng) => {
    let response = await fetch(`http://localhost:5000/api/external/geocoding/reverse?latlng=${lat},${lng}`);
    let geoinfo = await response.json();
    return geoinfo;
}
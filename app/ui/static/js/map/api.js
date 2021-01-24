export {get_images_by_location_id, get_reviews_by_location_id, get_amount_likes_by_picture_id}


let get_images_by_location_id = async (loc_id) => {
    let response = await fetch(`http://localhost:5000/api/resource/location/${loc_id}/picture/all`);
    let images = await response.json();
    return images;
}

let get_reviews_by_location_id = async (loc_id) => {
    let response = await fetch(`http://localhost:5000/api/resource/location/${loc_id}/review/all`);
    let reviews = await response.json();
    return reviews;
}

let get_amount_likes_by_picture_id = async (picture_id) => {
    let response = await fetch(`http://localhost:5000/api/resource/picture/${picture_id}/like/count`);
    let likes = await response.json();
    return likes;
}
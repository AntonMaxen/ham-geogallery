let api_key = 'AIzaSyDmfIZTORaan7mk7CLAlKAnXS4t0csT9E0';
let script = document.createElement('script');
script.src = `https://maps.googleapis.com/maps/api/js?key=${api_key}&callback=initMap&libraries=&v=weekly`;
script.defer = true;

window.initMap = async () => {
    const map = await create_map()
    let home = map.getCenter()
    place_current_location_marker(map, home)
    let location_objects = load_locations(map, locations);
    let focused_location = init_center_map(map, location_objects)


}

let create_map = async () => {
    let center_lat_lng = new google.maps.LatLng(0, 0);
    let position = await current_position()
    if (position) {
        center_lat_lng = new google.maps.LatLng(
            position.coords.latitude,
            position.coords.longitude
        );
    }
    return new google.maps.Map(document.getElementById("map"), {
        zoom: 11,
        center: center_lat_lng
    });
}

let current_position = async () => {
    return new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(resolve, reject);
    });
}

let init_center_map = (map, location_objects) => {
    let center_position = null;
    if (location_id !== null && get_location_obj(location_objects, location_id)) {
        let focused_location = get_location_obj(location_objects, location_id);
        center_position = center_map_on_marker(map, focused_location.marker);
    }
    return center_position;
}

let place_current_location_marker = (map, latlng) => {
    return new google.maps.Marker({
        position: latlng,
        map: map,
        title: 'Current Location',
        icon: '../static/images/Templatic-map-icons/residential-places.png'
    });
}

let get_location_obj = (location_objects, location_id) => {
    return location_objects.find(element => element.location.Id === location_id);
}

let center_map_on_geopos = async (map) => {
    let current_pos = await current_position();
    let latlng = new google.maps.LatLng(current_pos.coords.latitude, current_pos.coords.longitude);
    map.setCenter(latlng);
    return latlng;
}

let center_map_on_marker = (map, marker) => {
    let position = marker.getPosition();
    map.setCenter(position);
    return position;
}


let load_locations = (map, locations) => {
    let location_objects = [];
    locations.forEach(l => {
        let location_object = {}
        let title_text = `Place: ${l.Place}\n`+
            `Name: ${l.Name}\n` +
            `Longitude: ${l.Longitude}\n` +
            `Latitude: ${l.Latitude}\n`;

        location_object.marker = new google.maps.Marker({
            position: {lat: l.Latitude, lng: l.Longitude},
            map,
            title: title_text
        });
        location_object.location = l;
        location_objects.push(location_object);
    });

    return location_objects;
}


let get_random_item = arr => {
    let random_index = Math.floor(Math.random() * arr.length);
    return arr[random_index];
}

document.head.appendChild(script);
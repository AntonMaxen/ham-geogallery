let api_key = 'AIzaSyDmfIZTORaan7mk7CLAlKAnXS4t0csT9E0';
let script = document.createElement('script');
script.src = `https://maps.googleapis.com/maps/api/js?key=${api_key}&callback=initMap&libraries=&v=weekly`;
script.defer = true;


window.initMap = () => {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 11,
    center: {lat: 62.323907, lng: -150.109291}
  });
}

document.head.appendChild(script);
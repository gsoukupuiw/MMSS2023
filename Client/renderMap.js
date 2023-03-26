import { getPoints } from './getPoints.js';
let coords;
let map;

const renderingMap = () =>
{
    navigator.geolocation.getCurrentPosition(locateUser, fail);
}

const locateUser = (position) =>
{
    const { latitude, longitude } = position.coords;
    //user coordinates
    coords = [latitude, longitude];
    console.log(coords);
    if(!map)
    {
        map = L.map('map').setView(coords, 13);
    }
    else
    {
        map.setView(coords, 13)
    }
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    //creating markers
    getPoints.forEach(point =>
        {
            L.marker([point[0], point[1]]).addTo(map)
            .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
            .openPopup();
        }
    );

    // locateUser();
}



const fail = () =>
{
    alert('Could not get your position');
}





export {locateUser, renderingMap};
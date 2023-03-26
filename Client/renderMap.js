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
        map = L.map('map').setView(coords, 30);
    }
    else
    {
        map.setView(coords, 20)
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
        L.circle([point[0], point[1]],
            {
                radius: 30,
                stroke: false,
                color: 'blue',
                fillColor: 'lightblue',
                fillOpacity: 0.5
            })
            .addTo(map);
    });

    // locateUser();
}



const fail = () =>
{
    alert('Could not get your position');
}





export {locateUser, renderingMap};
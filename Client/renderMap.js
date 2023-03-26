import { getPoints } from './getPoints.js';
let userCoords;
let map;
let userMarker;


const locateUser = (position) =>
{
    const { latitude, longitude } = position.coords;
    //user coordinates
    userCoords = [latitude, longitude];
    console.log(userCoords);
    if(!map)
    {
        map = L.map('map').setView(userCoords, 30);
    }
    else
    {
        map.setView(userCoords, 20)
    }
    userMarker = L.marker(userCoords).addTo(map);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    //creating markers
    getPoints.forEach(point =>
    {
        const circle = L.circle([point[0], point[1]],
            {
                radius: 30,
                stroke: false,
                color: 'blue',
                fillOpacity: 0.5
            })
            .addTo(map);

        const distanceToCenter = userMarker.getLatLng().distanceTo(circle.getLatLng());

        const gradientScale = chroma.scale(['#00ffff', '#ff0000']).domain([0, circle.getRadius()]);

        if (distanceToCenter <= circle.getRadius()) {
            circle.setStyle({color: 'green', fillColor: '#0f3'});
        } else {
            const colorValue = gradientScale(distanceToCenter).hex();
            circle.setStyle({fillColor: colorValue});
        }
    });
}

const fail = () =>
{
    alert('Could not get your position');
}


export {locateUser, fail};
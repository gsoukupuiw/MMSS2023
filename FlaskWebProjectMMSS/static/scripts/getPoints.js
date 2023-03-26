'use strict'

let geoCaches = [];
let newGeoCache = [];
const test = async () => {
    const script = await fetch('/data');
    const data = await script.json();

    data.features.forEach((feature, i) => {
        let longitude, latitude;
        const url = feature.properties.url;
        if (feature.geometry.type === 'Point') {
            [longitude, latitude] = feature.geometry.coordinates;
        }
        geoCaches[i] = [latitude, longitude, url];
    })
    geoCaches.forEach(point => {
        if (!newGeoCache.includes(point)) {
            newGeoCache.push(point);
        }
    })
}
test();
console.log(newGeoCache);
export { newGeoCache as getPoints };
'use strict'

// const fetchPoints = async() =>
// {
//     // const data = await fetch(''); //datalocation
//     // const dataObjects = await data.json();
//     const script = await fetch('./tempGeoJson.json');
//     const data = await script.json();
    
//     return data.points;
// }

const script = await fetch('./tempGeoJson.json');
const data = await script.json();

let getPoints = [];

const dataValues = Object.values(data.points);
dataValues.forEach((point, i) => getPoints[i] = [point['latitude'], point['longitude']]);


export {getPoints};
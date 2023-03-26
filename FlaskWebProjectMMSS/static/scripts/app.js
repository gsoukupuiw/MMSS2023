'use strict'
import {locateUser, fail} from './renderMap.js';


const btn = document.getElementById('#submit');
let phoneNumber;

if (navigator.geolocation)
{
    navigator.geolocation.watchPosition(locateUser, fail)
}

const postNumber = () => {
    phoneNumber = document.getElementById('#phone').value;
}

btn.addEventListener(postNumber);

export { phoneNumber };
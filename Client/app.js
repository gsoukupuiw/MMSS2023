'use strict'

import {locateUser, renderingMap} from './renderMap.js';


if (navigator.geolocation)
{
    renderingMap();
}

setInterval(renderingMap, 10000);
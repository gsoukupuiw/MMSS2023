'use strict'

import {locateUser, fail} from './renderMap.js';


if (navigator.geolocation)
{
    navigator.geolocation.watchPosition(locateUser, fail)
}
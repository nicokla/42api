// import axios from 'axios'
var axios = require('./node_modules/axios')
require('dotenv').config();

// https://api.intra.42.fr/apidoc/guides/specification
// https://api.intra.42.fr/apidoc/guides/getting_started
// https://api.intra.42.fr/apidoc/guides/web_application_flow
// https://api.intra.42.fr/apidoc#users


(async()=>{

let uid = process.env.UID42
let secret = process.env.SECRET42
let payload = {
  'grant_type': 'client_credentials',
  'client_id': uid,
  'client_secret': secret
}

let response = await axios({
  method: 'post',
  url: 'https://api.intra.42.fr/oauth/token',
  data: payload
})
let token = response.data.access_token
console.log(token)

var baseUrl = 'https://api.intra.42.fr/v2/'
//  users, campus, 
async function getFromApi(path){
  let response2 = await axios({
    method: 'get',
    url: `baseUrl${path}` ,
    headers: {'Authorization': `Bearer ${token}`}
  })
  return response2.data
}
let answer = getFromApi('campus')

})()






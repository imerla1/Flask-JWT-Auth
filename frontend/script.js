let url = "http://127.0.0.1:5000/login";
test_data = {
  username: "george",
  password: "1234",
};
headers = { "Content-Type": "application/json" };
submitBtn = document.getElementById("btn-submit")
alertInfo = document.getElementById("alert-info")
infoText = document.getElementById("info-text")
username = document.getElementById("username")
password = document.getElementById("password")


// submitBtn.submitBtn.addEventListener()

function makePostRequest(url, data, headers) {
  fetch(url,{
    method: "POST",
    headers: headers,
    body: JSON.stringify(data)
  }).then((res)=>{
    if (res.ok) {
      // provided data is valid
      return res.json()
    }
    else {
      // provided data is invalid
      alertInfo.className = "alert alert-danger"
      infoText.innerText = "Invalid Useranme Or Password"
    }
  }).then((data)=>{
    access_token = data.access_token
    alertInfo.className = "alert alert-success"
    infoText.innerText = `accessToken: ${access_token}`

  })
}

submitBtn.addEventListener("click", ()=>{
  data = {
    "username": username.value,
    "password": password.value
  }
  makePostRequest(url, data, headers)
})
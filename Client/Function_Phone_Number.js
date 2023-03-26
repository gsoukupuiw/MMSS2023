function login() {
    const phoneNumber = document.getElementById("phone").value;

    console.log("Phone Number: " + phoneNumber);

    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({phone: phoneNumber})
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Do something with the response data
    })
    .catch(error => {
      console.error(error);
      // Handle any errors
    });
  }
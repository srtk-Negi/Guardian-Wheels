"use strict";
const submitBtn = document.querySelector("btn1");

submitBtn.addEventListener("click", function (e) {
  e.preventDefault();

  const make = document.querySelector("make").value;
  const name = document.querySelector("model").value;
  const carColor = document.querySelector("carColor").value;
  const licencePlate = document.querySelector("licencePlate").value;

  const formData = {
    make: make,
    name: name,
    carColor: carColor,
    licencePlate: licencePlate,
  };

  console.log(formData);

  // const jsonData = JSON.stringify(formData);

  // fetch("http://127.0.0.1:8000/formdata", {
  //   method: "POST",
  //   body: jsonData,
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  // })
  //   .then((response) => response.json())
  //   .then((data) => {
  //     document.getElementById("result").innerHTML =
  //       "Data sent to the backend: " + JSON.stringify(data);
  //   })
  //   .catch((error) => {
  //     document.getElementById("result").innerHTML = "Error: " + error;
  //   });
});

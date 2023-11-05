import random from "./random.js";

const form = document.getElementById("userForm");

form.addEventListener("submit", async function (event) {
  event.preventDefault();
  const messageDiv = document.getElementById("messageDiv");

  const car_make = document.getElementById("make").value;
  const car_model = document.getElementById("model").value;
  const car_color = document.getElementById("color").value;
  const license_plate_num = document.getElementById("license").value;
  const num = random(1, 1000);
  userData = {
    form_id: num,
    user_id: num,
    car_make: parseInt(car_make, 10),
    car_model: car_model,
    car_color: car_color,
    license_plate_num: license_plate_num,
  };

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  };

  try {
    const response = await fetch(
      "http://127.0.0.1:8000/forms/create",
      requestOptions
    );

    if (response.ok) {
      messageDiv.innerHTML = "Data submitted successfully.";
    } else {
      messageDiv.innerHTML = "Error submitting data.";
    }
  } catch (error) {
    messageDiv.innerHTML = "Error: " + error.message;
  }
});
